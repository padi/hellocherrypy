import cherrypy

class HelloWorld:
    def index(self):
        return 'We have an <a href="showMessage">important message</a> for you!'
    index.exposed = True
    
    def showMessage(self):
        return 'Hello world! <a href=\"anotherMessage\">another message</a> for you!'
    showMessage.exposed = True

    def anotherMessage(self):
        return "This is another message"
    anotherMessage.exposed = True
cherrypy.quickstart(HelloWorld())