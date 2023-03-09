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
        name = topic.get('name')
        if (Usertopic == name):
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
    try:
        m2 = et.Element("topic")
        m2.set('name', Usertopic)

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
    except:
        text = "Something went wrong while adding new note"
        return text


def notebookTopic(Usertopic):
    bookContent = []

    tree = et.parse('notebook.xml')
    root = tree.getroot()

    for topic in root.findall('topic'):
        name = topic.get('name')
        if (name == Usertopic):
            for info in topic.findall('note'):
                text = name+"\n"+info.get('name').strip()+"\n"+info.find(
                    'text').text.strip()+"\n"+info.find('timestamp').text.strip()
                bookContent.append(text)
            return bookContent
    text = "Something went wrong while searching note"
    bookContent.append(text)
    return bookContent


server.register_function(noteInput, 'noteInput')
server.register_function(notebookTopic, 'notebookTopic')

if __name__ == "__main__":
    try:
        print("Serving...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
