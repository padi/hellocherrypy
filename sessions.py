import cherrypy

class HitCounter:

    _cp_config = {'tools.sessions.on': True}

    def index(self):
        count = cherrypy.session.get('count', 0) + 1

        cherrypy.session['count'] = count

        return '''
            During your current session, you've viewed this
            page %s times! Your life is a patio of fun!
        ''' % count
    index.exposed = True

cherrypy.quickstart(HitCounter())