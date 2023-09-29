from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep, time
from colorama import Fore,Style, init as color_ama
color_ama(autoreset=True)
import json, re, sys, os, random

banner = Style.BRIGHT+Fore.YELLOW +  """

   ____               _   
  / ___| ___ __ _ ___| |_ 
 | |  _ / __/ _` / __| __|
 | |_| | (_| (_| \__ \ |_ 
  \____|\___\__,_|___/\__|
                          
  Creator : MK KHAIRIL || Youtube : MK KHAIRIL
  Support : Cocentz404 || Youtube : Cocentz404"""

putih = Style.BRIGHT+Fore.WHITE
hijau = Style.BRIGHT+Fore.GREEN
merah = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
reset = Fore.RESET
biru = Style.BRIGHT+Fore.BLUE


os.system('clear') 
print(banner)
print("\n")
print(f'{hijau}[+] Indonesia/English')
import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.2)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik("[+] Ini Adalah Program Ilegal\n[+] Semua Resiko Harap Ditanggung Pengguna..!!\n[+] This Is An Illegal Program\n[+] All Risks Borne by Users...!\n")
if not os.path.exists('session'):
    os.makedirs('session')
if len(sys.argv) < 2:
    print( Fore.RED + '\n\nUsage : python main.py +62' + Fore.RESET)
    sys.exit(1)
api_id = 1148490
api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
phone_number = sys.argv[1]
client = TelegramClient('session/' + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input(Fore.WHITE + 'Enter Yout Code Code : '))
    except SessionPasswordNeededError:
        passw = input(Fore.RESET + 'Your 2fa Password : ')
        me = client.start(phone_number, passw)
saia = client.get_me()
print('[*]Account:',saia.first_name)
print('[*]Phone:',saia.phone,'\n')
channel_username = 't.me/+AX-FvO4A7gswMTI1'
channel_entity = client.get_entity('t.me/+AX-FvO4A7gswMTI1')
print('Memulai Bot Gcast..!')


while True:
  try:
    
    client.send_message(entity=channel_entity, message='ahhh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='enakkk bngett sayanggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Channel Private ada konten baru nihhh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5);
    client.send_message(entity=channel_entity, message='Ahhhhh enak banget sayangggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(4)
    client.send_message(entity=channel_entity, message='Lagii sayangg crotin ke muka aku')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(1)
    client.send_message(entity=channel_entity, message='Ughhh gede banget kntolll kamuu')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(2);
    client.send_message(entity=channel_entity, message='ahhhhh mppss')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Btw channel private ada konten baru nihh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Ahhhh sayanggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5);
    client.send_message(entity=channel_entity, message='Ahhhhhhh enak banget sayangggg,cepetin dong sayang')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(4)
    client.send_message(entity=channel_entity, message='Mentokin sayangg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(1)
    client.send_message(entity=channel_entity, message='Uhhhh enakkkk bnget sumpahhhh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(900);
    client.send_message(entity=channel_entity, message='aahhhh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='enakkk bngett sayanggg, mentokin dong')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Channel Private ada konten baru nihhh,yukk join')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5);
    client.send_message(entity=channel_entity, message='Ahhhhh enak banget sayangggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(4)
    client.send_message(entity=channel_entity, message='Lagii dong sayangg crotin ke muka aku')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(1)
    client.send_message(entity=channel_entity, message='Ughhh gede banget kntolll kamuu,aku jilatt yaa')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(2);
    client.send_message(entity=channel_entity, message='ahhhhh mppss,terasa bngett')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Btw channel private ada konten baru nihh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Ahhhh sayanggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5);
    client.send_message(entity=channel_entity, message='yukk joinn channel private aku sengg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(4)
    client.send_message(entity=channel_entity, message='prot prot prot')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(1)
    client.send_message(entity=channel_entity, message='ahhh becekkk bngettt')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(900);
    client.send_message(entity=channel_entity, message='basah bngett aku di channel private')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='busett gede bngettt ahh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Channel Private ada konten baru nihhh,yukk join')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5);
    client.send_message(entity=channel_entity, message='Ahhhhh enak banget sayangggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(4)
    client.send_message(entity=channel_entity, message='crott sini ke mulutt sayanggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(1)
    client.send_message(entity=channel_entity, message='Ughhh gede banget kntolll kamuu,aku jilatt yaa')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(2);
    client.send_message(entity=channel_entity, message='ahhhhh mppss,terasa bngett kontol kamu')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Btw channel private ada konten baru nihh')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5)
    client.send_message(entity=channel_entity, message='Ahhhh sayanggg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(5);
    client.send_message(entity=channel_entity, message='yukk joinn channel private aku sengg')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(4)
    client.send_message(entity=channel_entity, message='prot prot prot')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(1)
    client.send_message(entity=channel_entity, message='ahhh becekkk bngettt')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(900);
    
  except:
    print(f'{hijau} Gcast gagal.! {putih} gcast by : khairil')
    sleep(5)

sys.exit()
client.disconnect()
