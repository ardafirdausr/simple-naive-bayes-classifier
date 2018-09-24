import socket

website = input("masukan nama website : ")
ip = socket.gethostbyname(website)
print('***************************************************')
print('alamat IP : ', ip)
print ('**************************************************')