'''
Bonus Tutorial: Using SQLObject

This is a silyy little contacts manager application intended to
demonstrate how to use SQLObject from within a CherryPy2 project. It also shows how to use inline Cheetah templates.
SQLObject is an Object/Relational Mapper that allows you to access data stored in an RDBMS in a pythonic fashion. You create dataobjects
as Python classes and let SQLObject take care of all the nasty details.

After starting this application for the first time, you will need to
access the /reset URI in order to create the database table and some
sample data. Accessing /reset again will drop and re-create the table, so you may want to be careful. :)

This application isn't supposed to be fool-proof, it's not even supposed
to be very GOOD. Play around with it some, browse the source code, smile.

:)
'''

import cherrypy
from Cheetah.Template import Template
from sqlobject import *

# configure your database connection here
__connection__ = 'mysql://root:@localhost/test'

# this is our (only) data class.
class Contact(SQLObject):
    lastName  = StringCol(length = 50, notNone = True)
    firstName = StringCol(length = 50, notNone = True)
    phone     = StringCol(length = 30, notNone = True, default = '')
    email     = StringCol(length = 30, notNone = True, default = '')
    url       = StringCol(length = 100, notNone = True, default = '')

class ContactManager:
    def index(self):
        # Let's display a list of all stored contacts.
        contacts = Contact.select()

        template = Template('''
            <h2>All Contacts</h2>

            #for $contact in $contacts
                <a href="mailto:$contact.email">$contact.lastName, $contact.firstName</a>
                [<a href="./edit?id=$contact.id">Edit</a>]
                [<a href="./delete?id=$contact.id">Delete</a>]
                <br/>
            #end for

            <p>[<a href="./edit">Add new contacts</a>]</p>
        ''', [locals(), globals()])

        return template.respond()
    
    index.exposed = True

    def edit(self, id=0):
        # we really want id as an integer. Since GET/POST parameters
        # are always passed as strings, let's convert it.
        id = int(id)

        if id > 0:
            # if an id is specified, we're editing an existing contact.
            contact = Contact.get(id)
            title = "Edit Contact"
        else:
            # if no id is specified, we're entering a new contact.
            contact = None
            title = "New Contact"

        # In the following template code, please note that we use
        # Cheetah's $getVar() construct for the form values. We have
        # to do this because contact may be set to None (see above).
        template = Template('''
            <h2>$title</h2>

            <form action="./store" method="POST">
                <input type="hidden" name="id" value="$id" />
                Last Name: <input name="lastName" value="$getVar('contact.lastName', '')" /><br/>
                First Name: <input name="firstName" value="$getVar('contact.firstName', '')" /><br/>
                Phone: <input name="phone" value="$getVar('contact.phone', '')" /><br/>
                Email: <input name="email" value="$getVar('contact.email', '')" /><br/>
                URL: <input name="url" value="$getVar('contact.url', '')" /><br/>
                <input type="submit" value="Store" />
            </form>
        ''', [locals(), globals()])

        return template.respond()
    
    edit.exposed = True

    def reset(self):
        # Drop existing table
        Contact.dropTable(True)

        # Create new table
        Contact.createTable()

        # Create some sample data
        Contact(
            firstName = 'Hendrik',
            lastName = 'Mans',
            email = 'hendrik@mans.de',
            phone = '234241',
            url = 'http://www.mornography.de')

        return "reset completed!"

    reset.exposed = True

print("If you're running this application for the first time, please go to http://localhost:8080/reset once in order to create the database!")
cherrypy.quickstart(ContactManager())