import cherrypy

class WelcomePage:
    def index(self):
        return '''
            <form action="greetUser" method="GET">
            What is your name?
            <input type="text" name="name" />
            <input type="submit" />
            </form>'''
    index.exposed = True
    
    def greetUser(self, name = None):
        if name:
            return "Hey %s, what's up?" % name
        else:
            return 'Enter your name <a href="./">here</a>.'
    greetUser.exposed = True
cherrypy.quickstart(WelcomePage())