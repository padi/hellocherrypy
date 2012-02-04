import cherrypy

class Page:
    title = 'Untitled Page'

    def header(self):
        return '''
            <html>
            <head>
                <title>%s</title>
            </head>
            <body>
            <h2>%s</h2>
        ''' % (self.title, self.title)

    def footer(self):
        return '''
            </body>
            </html>
        '''

class HomePage(Page):
    title = 'Tutorial 5'

    def __init__(self):
        self.another = AnotherPage()

    def index(self):
        return self.header() + '''
            <p>
            Isn't this exciting? There's
            <a href="./another/">another page</a>, too!
            </p>
        ''' + self.footer()
    index.exposed = True

class AnotherPage(Page):
    title = 'Another Page'

    def index(self):
        return self.header() + '''
            <p>
            And this is the amazing second page!
            </p>
        ''' + self.footer()
    index.exposed = True

cherrypy.quickstart(HomePage())