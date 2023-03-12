# Makers_2023
A basic mullti client chat room server created using socket programming in python.

To run the project, download both the server.py and client.py

First run the server.py file, it will show the message, 
  "Server is running"
  
Then run the client.py file. It will show the client a prompt: 
  "Enter ur name"
After they have entered their name, the client will get connected to server and all connected clients will get message:
  " 'The name' has joined the chat room"
And the connected client will get the msg:
   "you are now connected!"
At the server side it will show:
  "connection is established with (client ip addr, client port no)
  "The name of this client is <The name>"
  
The client.py can be run multiple times for many clients to join the chatroom
  
Then they can start chatting and the msg sent by one person is visible to everyone else as:
  " 'The name': 'The msg sent' "
  
If the connection with server is lost or the server closes down the following msg will display:
  "error!"
  
  
![Screenshot 2023-03-12 234401](https://user-images.githubusercontent.com/117470303/224564133-a59a1e6e-7b60-4424-8c81-8165bdcb704a.png)
