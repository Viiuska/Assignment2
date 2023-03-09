# Assignment2
### CT30A3401 Distributed Systems

This program is simple notebook distriputed system using RPC. I have created a client and a server that communicate through Rometo Procedire Calls. Server side saves user's input in an xml file. If notebook topic already exists, it will append it and if not, it will create a new topic.

Setting up the system I am using xmlrpc.client
![image](https://user-images.githubusercontent.com/87257685/224013982-85d51645-ba12-49f0-bf85-cd18141c18b3.png)

The server accept the client request using SimpleXMLRPCServer (line 3 and 9)
![image](https://user-images.githubusercontent.com/87257685/224014144-143bc55c-1867-454b-a5c4-2fa91c9f5ef4.png)

### How to run  
Open at least two terminals.  
First terminal set up the server up  "python .\Communication.py"  
Then set up the second terminal up "python .\client.py". You can open up more of these.
