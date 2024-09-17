One of my very early projects. It is a server/computer monitoring program, wich calls 
a few common comands (e.g wich processes are running, wich network ports are open, how many users are loged in, etc) on the server and sends it over the network to an other computer.

it has two parts:

backEndScript.py:
  Calls the commands and sends it over the 
  network to an other computer wich runs the frontEndScript.py

frondEndScript.py:
  recieves the data comming from the backEndScript.py
  and processes the data for dsiplaying it to a UI 
