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

class JokePage:
    def index(self):
        return '''
        <p>"In Python, how do you create a string of random
        characters?" -- "Read a Perl file"</p>
        <p>[<a href="../">Return</a>]</p>'''
    index.exposed = True

class LinksPage:
    def __init__(self):
        self.extra = ExtraLinksPage()

    def index(self):
        return '''
            <p>Here are some useful links:</p>

            <ul>
                <li><a href="http://www.cherrypy.org">The CherryPy Homepage</a></li>
                <li><a href="http://www.python.org">The Python Homepage</a></li>
            </ul>

            <p>You can check out some extra useful
            links <a href="./extra/">here</a>.</p>

            <p>[<a href="../">Return</a>]</p>
        '''
    index.exposed = True

class ExtraLinksPage:
    def index(self):
        return '''
            <p>Here are some extra useful links:</p>

            <ul>
                <li><a href="http://def.icio.us">del.icio.us</a></li>
                <li><a href="http://www.mornography.de">Hendrik's weblog</a></li>
            </ul>

            <p>[<a href="../">Return to links page</a>]</p>'''
    index.exposed = True

root = HomePage()
root.joke = JokePage()
root.links = LinksPage()

cherrypy.quickstart(root)