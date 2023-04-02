import os
import time
import requests
from multiprocessing.dummy import Pool,Lock
from bs4 import BeautifulSoup
import sys,ctypes
import time
import subprocess
from random import choice
from colorama import Fore
from colorama import Style
from colorama import init





#made by cracki ♥


################################################################ DONT TOUCH U FUCKING IDIOT ###############################################################




init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
b = """\033[41;1m



   ____    ____        _        ____   _  __                
U /"___|U |  _"\ u U  /"\  u U /"___| |"|/ /       ___      
\| | u   \| |_) |/  \/ _ \/  \| | u   | ' /       |_"_|     
 | |/__   |  _ <    / ___ \   | |/__U/| . \\u      | |      
  \____|  |_| \_\  /_/   \_\   \____| |_|\_\     U/| |\u    
 _// \\   //   \\_  \\    >>  _// \\,-,>> \\,-.-,_|___|_,-. 
(__)(__) (__)  (__)(__)  (__)(__)(__)\.)   (_/ \_)-' '-(_/ \033[0m  
																	
					ShellFinder V3.0
					For premium stuff 
					Telegram : @itcracki
					Channel : https://t.me/crackioff




"""







def Folder(directory):
  if not os.path.exists(directory):
  	os.makedirs(directory)
Folder("THERESULT")

def clear():
	try:
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
	except:
		pass


Bad = 0
Good = 0
pro = 0
mailer = 0
password = 0



clear()
print("""\033[41;1m

   ____    ____        _        ____   _  __                
U /"___|U |  _"\ u U  /"\  u U /"___| |"|/ /       ___      
\| | u   \| |_) |/  \/ _ \/  \| | u   | ' /       |_"_|     
 | |/__   |  _ <    / ___ \   | |/__U/| . \\u      | |      
  \____|  |_| \_\  /_/   \_\   \____| |_|\_\     U/| |\u    
 _// \\   //   \\_  \\    >>  _// \\,-,>> \\,-.-,_|___|_,-. 
(__)(__) (__)  (__)(__)  (__)(__)(__)\.)   (_/ \_)-' '-(_/ \033[0m  
																	
					ShellFinder V3.0
					For premium stuff 
					Telegram : @itcracki
					Channel : https://t.me/crackioff



""")

urli = 'https://pastebin.com/raw/SM8uEui8'


try:

	url1 = requests.get(urli).text
except Exception:
	print(' CHECK YOUR INTERNET')
	time.sleep(5)
	quit()
lis = []


lis.append(url1.rsplit('\n'))
listaaa = lis[0]



							



file_name = input("\033[46m Give me your urls list ============> \033[0m")
op = open(file_name,'r').read().splitlines()
sitelist = [list.strip() for list in op]    

def finder(i) :
	global Bad,Good,pro,password,mailer
	head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	try :
				r = requests.session()
				for path in listaaa :
					url = ('http://'+i+'/'+path)
				
					req_first = r.get(url, headers=head)
					if ">public_html" in req_first.text :
						
						sitelist.remove(i)
						Good = Good + 1
						print("\033[42;1m -- Shell Found -- \033[0m "+url)
						with open("THERESULT/shell.txt","a") as file :
							file.write(url+"\n")
							file.close()
					elif "<span>Upload file:" in req_first.text :
						
						sitelist.remove(i)
						Good = Good + 1
						print("\033[42;1m -- Shell Found -- \033[0m "+url)
						with open("THERESULT/random.txt","a") as gn :
							gn.write(url+"\n")
							gn.close()
					elif 'type="submit" id="_upl" value="Upload">' in req_first.text :
						
						sitelist.remove(i)
						Good = Good + 1
						print("\033[42;1m -- Shell Found -- \033[0m "+url)
						
						with open("THERESULT/Config.txt","a") as fox :
							Good = Good + 1
							fox.write(url+"\n")
							fox.close()
					elif 'Leaf PHPMailer' in req_first.text or '>alexusMailer 2.0<' in req_first.text :
						
						sitelist.remove(i)
						mailer = mailer + 1
						print("\033[42;1m -- Mailer Found -- \033[0m "+url)
						with open('THERESULT/Mailer.txt','a') as mailers :
							mailers.write(url+'\n')
							mailers.close()
					elif 'method=post>Password:' in req_first.text or '<input type=password name=pass' in req_first.text :
						
						sitelist.remove(i)
						password = password + 1
						print("\033[42;1m -- Shell with PASS Found -- \033[0m "+url)
						with open('THERESULT/passwod.txt','a') as pa :
							pa.write(url+'\n')
							pa.close()
					elif 'name="uploader" id="uploader">' in req_first.text:
						
						sitelist.remove(i)
						good = good +1
						print("\033[42;1m -- VULN Found-- \033[0m "+url)
						with open('THERESULT/result.txt','a') as fo :
							fo.write(url+'\n')
							fo.close()
					else :
						
						Bad = Bad + 1
						print("\033[41;1m -- BAD -- \033[0m "+url)
						pass
					
	except :
		pass
	if os.name == 'nt':
		ctypes.windll.kernel32.SetConsoleTitleW(' Cracki Shell Finder  | Shell- {} | BAAD- {} | Mailer- {}| Password-{}'.format(Good, Bad, mailer, password))
	else :
		sys.stdout.write('HrackeDz Shell Finder  | Shell- {} | BAAD- {} | Mailer- {}| Password-{}'.format(Good, Bad, mailer, password))

def start():
	
	
	
		mp = Pool(150)
		mp.map(finder, sitelist)
		mp.close()
		mp.join()

start()