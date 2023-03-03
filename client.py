import xmlrpc.client
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:3000")

if __name__ == "__main__":
    # print(proxy.list_directory(r"C:\Users\viia_\Downloads\DS_kurssi\Assignment2"))
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
            print(proxy.notebookTopic(topic))
        if userInput == "0":
            print("Ending software...")
