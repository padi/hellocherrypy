import os
localDir = os.path.dirname(__file__)
curpath = os.path.normpath(os.path.join(os.getcwd(), localDir))

import cherrypy

class HTTPErrorDemo(object):

    # Set a custom response for 403 errors
    _cp_config = {'error_page.403' : os.path.join(curpath, "custom_error.html")}

    def index(self):
        # display some links that will result in errors
        tracebacks = cherrypy.request.show_tracebacks
        if tracebacks:
            trace = 'off'
        else:
            trace = 'on'

        return """
        <html><body>
            <p>Toggle tracebacks <a href="toggleTracebacks">%s</a></p>
            <p><a href="/doesNotExist">Click me; I'm a broken link!</a></p>
            <p>These errors are explicitly raised by the application:</p>
            <ul>
                <li><a href="/error?code=400">400</a></li>
                <li><a href="/error?code=401">401</a></li>
                <li><a href="/error?code=402">402</a></li>
                <li><a href="/error?code=500">500</a></li>
            </ul>
            <p><a href="/messageArg">You can also set the response body
            when you raise an error.</a></p>
        </body></html>
        """ % trace
    index.exposed = True

    def toggleTracebacks(self):
        # simple function to toggle tracebacks on and off
        tracebacks = cherrypy.request.show_tracebacks
        cherrypy.config.update({'request.show_tracebacks': not tracebacks})

        # redirect back to the index
        raise cherrypy.HTTPRedirect('/')
    toggleTracebacks.exposed = True

    def error(self, code):
        # raise an error based on the get query
        raise cherrypy.HTTPError(status = code)
    error.exposed = True

    def messageArg(self):
        message = ("If you construct and HTTPError with a 'message' "
                    "argument, it will be placed on the error page "
                    "(underneath the status line by default).")
        raise cherrypy.HTTPError(500, message=message)
    messageArg.exposed = True

cherrypy.quickstart(HTTPErrorDemo())