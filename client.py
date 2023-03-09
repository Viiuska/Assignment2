# Viia Mäntymäki

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:3000")

if __name__ == "__main__":
    userInput = -1

    while (userInput != "0"):
        print("\nNotebook menu:")
        print("1: Add new note")
        print("2: Print the contents of the notebook on the given topic")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        if userInput == "1":
            topic = input("Give a topic: ")
            note = input("Give a note: ")
            text = input("Enter text: ")
            print(proxy.noteInput(topic, text, note))
        if userInput == "2":
            topic = input("Give a topic: ")
            content = proxy.notebookTopic(topic)
            print(*content, sep="\n")
        if userInput == "0":
            print("Ending software...")
