import cherrypy

class UsersPage:

    def index(self):
        return '''
            <a href="./remi">Remi Delon</a><br/>
            <a href="./hendrik">Hendrik Mans</a><br/>
            <a href="./lorenzo">Lorenzo Lamas</a><br/>
        '''
    index.exposed = True

    def default(self, user):
        # In a real application, we would probably do some database lookups here
        # instead of the silly if/elif/else construct.
        if user == 'remi':
            out = "Remi Delon, CherryPy lead developer"
        elif user == 'hendrik':
            out = "Hendrik Mans, CherryPy co-developer & crazy german"
        elif user == 'lorenzo':
            out = "Lorenzo Lamas, famous actor and singer!"
        else:
            out = "Unknown user :-("

        return '%s (<a href="./">back</a>)' % out
    default.exposed = True

cherrypy.quickstart(UsersPage())