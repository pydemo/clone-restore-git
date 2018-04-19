"""
    
    Git-Clone-All is a clonning tool that clones all public github repositories of a User or organization with a single command.

    Author: SpeedCuber (@yogendrasinghx)
 
    Special Thanks to @tirthapriya12 ;)


"""


from bs4 import BeautifulSoup
#import urllib2
from urllib.request import urlopen
import re
import os
import socket
import sys
e=sys.exit


# Console colors
G = '\033[32m'  # green
Y = '\033[33m'  #Yellow
B = '\033[34m'  # blue
C = '\033[36m'  # cyan
GR ='\033[37m'  # gray
R = '\033[31m'  # red



"""
Display ASCII art to make it cool ;)
"""
print (B +" _____ _ _          _____ _                          ___  _ _ ")
print (B +"|  __ (_) |        /  __ \ |                        / _ \| | |")
print (B +"| |  \/_| |_ ______| /  \/ | ___  _ __   ___ ______/ /_\ \ | |")
print (B +"| | __| | __|______| |   | |/ _ \| '_ \ / _ \______|  _  | | |")
print (B +"| |_\ \ | |_       | \__/\ | (_) | | | |  __/      | | | | | |")
print (B +" \____/_|\__|       \____/_|\___/|_| |_|\___|      \_| |_/_|_|\n")
print (C +"                                                    Ver.1.0\n")
print (C +"                                         Author: SpeedCuber\n")
                                                              


#Check internet connection

def internet_on():
  try:
  	print (Y+"\r[.]Checking Internet Connection...\r")
  	host = socket.gethostbyname("www.google.com")
  	s = socket.create_connection((host, 80), 2)
  	return True
  except:
     pass
  return False

if internet_on():
	print (G+"[OK] Connected\n")
	#username= raw_input(Y+'Enter Github Username : '+GR)
	username='KarmArt'
	if not os.path.exists(username):
		os.makedirs(username)
	os.chdir(username)

	#Count number of pages for repositories
	uurl="https://github.com/"+username+"?tab=repositories"
	print(uurl)
	#e(0)
	html_page = urlopen(uurl)
	soup = BeautifulSoup(html_page,"lxml")
	for child in soup.find(class_=re.compile("Counter")):
		count=int(child)
	print (G+"\n\n[+]"+str(count) + " Repositories Found!!\n")
	nop=int(count/30)+1; #Number of pages
	#print nop


	#Dump git URL and execute git clone command
	for i in range(nop):
		#print "https://github.com/"+username+"?page="+str(i+1)+"&tab=repositories"
		html_page = urlopen("https://github.com/"+username+"?page="+str(i+1)+"&tab=repositories")
		soup = BeautifulSoup(html_page,"lxml")
		for link in soup.findAll(itemprop="name codeRepository"):
			repo=link.get('href')
			print(os.path.join(username,repo.split(r'/')[2]))
			print (os.path.isdir('c:\\Python35-64\\'+username+'\\'+repo.split(r'/')[2]))
			#e(0)
			if not 'PROCESSING' in repo.upper() and not os.path.isdir('c:\\Python35-64\\'+username+'\\'+repo.split(r'/')[2]):
				catch="git clone https://github.com"+link.get('href')+".git"
				#print "git clone https://github.com"+link.get('href')+".git"
				print (B+"\n=================================================================="+GR+"\n")
				os.system(catch)
				print('\x1b[6;30;42m' + '\nSuccess!' + '\x1b[0m')  	
			else:
				print("passing on %s" % repo)
else:
	print (R+"\nINTERNET IS NOT WORKING :( \n\n")
