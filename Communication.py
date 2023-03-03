# https://www.youtube.com/watch?v=_8xXrFWcWao

from xmlrpc.server import SimpleXMLRPCServer
from xml.dom import minidom
import os
import xml.etree.ElementTree as et
import datetime

server = SimpleXMLRPCServer(("localhost", 3000), logRequests=True)


def noteInput(Usertopic, Usertext, Usernote):
    # https://docs.python.org/3/library/xml.etree.elementtree.html#modifying-an-xml-file

    tree = et.parse('notebook.xml')
    root = tree.getroot()
    text = "Topic added"
    time = datetime.datetime.today()
    time = datetime.datetime.strftime(time, "%m/%d/%Y - %H:%M:%S")

    for topic in root.findall('topic'):
        if (Usertopic == topic.get('name')):
            newNote = et.Element("note")
            newNote.set('name', Usernote)

            newText = et.Element("text")
            newText.text = str(Usertext)
            newNote.append(newText)

            newTime = et.Element("timestamp")
            newTime.text = str(time)
            newNote.append(newTime)

            topic.append(newNote)
            tree.write("notebook.xml")

            text = "Added new text"
            return text
        else:
            m2 = et.Element("topic")
            m2.set('name', str(Usertopic))

            c1 = et.Element("note")
            c1.set("name", str(Usernote))
            m2.append(c1)

            c2 = et.Element("text")
            c2.text = str(Usertext)
            c1.append(c2)

            c3 = et.Element("timestamp")
            c3.text = str(time)
            c1.append(c3)

            root.append(m2)

            tree.write('notebook.xml')

            return text


def notebookTopic(Usertopic):
    tree = et.parse('notebook.xml')
    root = tree.getroot()
    bookContent = []
    for topic in root.findall('topic'):
        if (Usertopic == topic.get('name')):
            # https://www.guru99.com/manipulating-xml-with-python.html
            for note in topic:
                bookContent.append(note.get('name'))
                for subelem in note:
                    bookContent.append(subelem.text.strip())
        return bookContent

    text = "Something went wrong"
    return text


server.register_function(noteInput, 'noteInput')
server.register_function(notebookTopic, 'notebookTopic')

if __name__ == "__main__":
    try:
        print("Serving...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
