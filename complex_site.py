import cherrypy

class HomePage:
    def index(self):
        return '''
            <p>Hi, this is the home page! Check out the other
            fun stuff on this site:</p>

            <ul>
                <li><a href="/joke/">A silly joke</a></li>
                <li><a href="/links/">Usefeul Links</a></li>
            </ul>'''
    index.exposed = True

root = HomePage()
cherrypy.quickstart(root)