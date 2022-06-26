from email import message
from mimetypes import init
from os import system
import time
import httpx
import re
import json
import random
from unicodedata import name
from random import randint as r
from faker import Faker
from threading import Thread
import colorama
import json
from json import load
import requests
from colorama import Fore, Style
from os import system

#GOT FUCK Regenxy#9696


class Email:

    def key():
        cookies = {
            'version': 'eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D',
            '__gads': 'ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg',
            'XSRF-TOKEN': 'eyJpdiI6Ikw5bm5EVS9wZXRCbm1pcU9JSkxPTUE9PSIsInZhbHVlIjoiaHpJSk9ZQXdGTHFmcDRaZXQrTHIvVVgvSlJvbVZ3dFpWeGpLVmZLQ01HNlZ6WWFjTEYvdWh2dXNrdGsrMklmNEEwbUFBenVENi9UWXJzMWZFaUdYYWlDWW9DT1p4bngxUHRvWldhOHdlY3dMU3JhbWtUZGtrRVZjT05jNXd3Vm4iLCJtYWMiOiI2NTM3YTYxYzU3NTU4OTQ5MjFlMGFiYjQzNjY0NzU0MTRmZGYxMzRmYmM3NDVlODUxZjI0NWUxNGI1NGZhMDE1In0%3D',
            'sonjj_session': 'eyJpdiI6ImZRRUQybVI1eUZxVUI3dnVmY2dhT3c9PSIsInZhbHVlIjoiYmVBcHVCbE0vVU1GZE1ySEl4YXV0eGxvRWhNNDVLZTlCdVFhL3haTEFDNUdoVUNIYVVWZjgwWTE5dzBtb0VBS3M3RndUbTZVMjVUS2dlY3BuOFRSWHhTaTJ2cFM2OE5pQzB3a0JkbjJXZUhNZFo0VEM0ZTdTaHNGbS8yejlpS1EiLCJtYWMiOiJkNWUwMWM3YzdhYjk0MzQ1Mjc3ZThjY2RlZTQzZmJjZjI1YjVhZGI4OWQ3ZjllNDJhOWI1YjllYmJiNTRmNDEwIn0%3D',
        }

        headers = {
            'authority': 'smailpro.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'version=eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D; __gads=ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg; XSRF-TOKEN=eyJpdiI6Ikw5bm5EVS9wZXRCbm1pcU9JSkxPTUE9PSIsInZhbHVlIjoiaHpJSk9ZQXdGTHFmcDRaZXQrTHIvVVgvSlJvbVZ3dFpWeGpLVmZLQ01HNlZ6WWFjTEYvdWh2dXNrdGsrMklmNEEwbUFBenVENi9UWXJzMWZFaUdYYWlDWW9DT1p4bngxUHRvWldhOHdlY3dMU3JhbWtUZGtrRVZjT05jNXd3Vm4iLCJtYWMiOiI2NTM3YTYxYzU3NTU4OTQ5MjFlMGFiYjQzNjY0NzU0MTRmZGYxMzRmYmM3NDVlODUxZjI0NWUxNGI1NGZhMDE1In0%3D; sonjj_session=eyJpdiI6ImZRRUQybVI1eUZxVUI3dnVmY2dhT3c9PSIsInZhbHVlIjoiYmVBcHVCbE0vVU1GZE1ySEl4YXV0eGxvRWhNNDVLZTlCdVFhL3haTEFDNUdoVUNIYVVWZjgwWTE5dzBtb0VBS3M3RndUbTZVMjVUS2dlY3BuOFRSWHhTaTJ2cFM2OE5pQzB3a0JkbjJXZUhNZFo0VEM0ZTdTaHNGbS8yejlpS1EiLCJtYWMiOiJkNWUwMWM3YzdhYjk0MzQ1Mjc3ZThjY2RlZTQzZmJjZjI1YjVhZGI4OWQ3ZjllNDJhOWI1YjllYmJiNTRmNDEwIn0%3D',
            'origin': 'https://smailpro.com',
            'referer': 'https://smailpro.com/advanced',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
            'x-xsrf-token': 'eyJpdiI6Ikw5bm5EVS9wZXRCbm1pcU9JSkxPTUE9PSIsInZhbHVlIjoiaHpJSk9ZQXdGTHFmcDRaZXQrTHIvVVgvSlJvbVZ3dFpWeGpLVmZLQ01HNlZ6WWFjTEYvdWh2dXNrdGsrMklmNEEwbUFBenVENi9UWXJzMWZFaUdYYWlDWW9DT1p4bngxUHRvWldhOHdlY3dMU3JhbWtUZGtrRVZjT05jNXd3Vm4iLCJtYWMiOiI2NTM3YTYxYzU3NTU4OTQ5MjFlMGFiYjQzNjY0NzU0MTRmZGYxMzRmYmM3NDVlODUxZjI0NWUxNGI1NGZhMDE1In0=',
        }

        json_data = {
            'domain': 'gmail.com',
            'username': 'random',
            'server': 'server-1',
            'type': 'alias',
        }

        response = requests.post('https://smailpro.com/app/key',
                                 headers=headers, cookies=cookies, json=json_data).json()
        return response["items"]

    def mail():
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://smailpro.com',
            'Referer': 'https://smailpro.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-rapidapi-ua': 'RapidAPI-Playground',
        }

        params = {
            'key': Email.key(),
            'rapidapi-key': 'f871a22852mshc3ccc49e34af1e8p126682jsn734696f1f081',
            'domain': 'gmail.com',
            'username': 'random',
            'server': 'server-1',
            'type': 'alias',
        }

        response = requests.get(
            'https://public-sonjj.p.rapidapi.com/email/gm/get', headers=headers, params=params).json()
        return response['items']['email']

    def key2(mailx):
        cookies = {
            'version': 'eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D',
            '__gads': 'ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg',
            'XSRF-TOKEN': 'eyJpdiI6IjZINmRlVFp2SWhkV1Y5eFBIMXJzVUE9PSIsInZhbHVlIjoiaDZKenJGTzN5Y1M2V1hueDh5eHkxMjRuRUkvU3JPeWlzSjB5WnJJaUNrMnhWU0Z2Zk5DN3B4aE90MkdaM2pYcllXMHdrb3hhU01PWWkxWnFnMG5pNTFrMjJsemw3V0dSV2FHTTE1NDlnNnd3cDByMlVZOW5FanJIckp0Y0xiRW0iLCJtYWMiOiJlYTIzYzAwM2IyZThhNTQ5ZTdlZWUxYjExMjkwZjBlYjc4YWQ0MmYzZTFlNDliMWE0ZGY4M2RjNWRkMWU4NDU0In0%3D',
            'sonjj_session': 'eyJpdiI6Ik4raURLRFpxN2NxQW40Yzk0RHNDc0E9PSIsInZhbHVlIjoiNWx2Y3I2eXROUkwyUkRUc2ZOQmYzV01VWGFBeVFFdERvd1k5NjRtOVdwTFdFNWxPVU9NRVZ0UVJjZWpzZTRzWjcxUVVLTDdYWGZ5cnlyeUY4bm14U0d4YXdoQU5kZlA1b3pIbkxEbTd5RVVEc1FqRWhHUXpPYzd5Mk1pUHlFMTMiLCJtYWMiOiJjODQ1OGJlYTBkN2U1YmFmMjI5ZjQ0MjM2NzZiZjQ3N2MxYzUxODkzMjg4YWVlZjk2N2M5ZTk1OTI4NmVmYzY2In0%3D',
        }

        headers = {
            'authority': 'smailpro.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'version=eyJpdiI6IktkbVJ6K1hib1hQd3dSa0ZsVW8wSGc9PSIsInZhbHVlIjoicWtLcC9MQ0V6N01wUnRaZHBQUnRIU0dSbXozT3pzWWE2b0IzeE14VWZhQXphWnBtVERzb2pWc3dES3pQaUE3aSIsIm1hYyI6IjAxOTVhOTc1NWQ0YWFlMzVlYjdkNDY1Yzg2MzM5ZWEwNDA0NjFlY2UwYWZhN2QzZDM0OWZhYjBlNmNhNzUzNmIifQ%3D%3D; __gads=ID=126c59b47c8c697e-222effbbc8d100b6:T=1649306792:RT=1649306792:S=ALNI_MZUpgRJ9G9w-YvySdgwKAh_vU4hKg; XSRF-TOKEN=eyJpdiI6IjZINmRlVFp2SWhkV1Y5eFBIMXJzVUE9PSIsInZhbHVlIjoiaDZKenJGTzN5Y1M2V1hueDh5eHkxMjRuRUkvU3JPeWlzSjB5WnJJaUNrMnhWU0Z2Zk5DN3B4aE90MkdaM2pYcllXMHdrb3hhU01PWWkxWnFnMG5pNTFrMjJsemw3V0dSV2FHTTE1NDlnNnd3cDByMlVZOW5FanJIckp0Y0xiRW0iLCJtYWMiOiJlYTIzYzAwM2IyZThhNTQ5ZTdlZWUxYjExMjkwZjBlYjc4YWQ0MmYzZTFlNDliMWE0ZGY4M2RjNWRkMWU4NDU0In0%3D; sonjj_session=eyJpdiI6Ik4raURLRFpxN2NxQW40Yzk0RHNDc0E9PSIsInZhbHVlIjoiNWx2Y3I2eXROUkwyUkRUc2ZOQmYzV01VWGFBeVFFdERvd1k5NjRtOVdwTFdFNWxPVU9NRVZ0UVJjZWpzZTRzWjcxUVVLTDdYWGZ5cnlyeUY4bm14U0d4YXdoQU5kZlA1b3pIbkxEbTd5RVVEc1FqRWhHUXpPYzd5Mk1pUHlFMTMiLCJtYWMiOiJjODQ1OGJlYTBkN2U1YmFmMjI5ZjQ0MjM2NzZiZjQ3N2MxYzUxODkzMjg4YWVlZjk2N2M5ZTk1OTI4NmVmYzY2In0%3D',
            'origin': 'https://smailpro.com',
            'referer': 'https://smailpro.com/advanced',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
            'x-xsrf-token': 'eyJpdiI6IjZINmRlVFp2SWhkV1Y5eFBIMXJzVUE9PSIsInZhbHVlIjoiaDZKenJGTzN5Y1M2V1hueDh5eHkxMjRuRUkvU3JPeWlzSjB5WnJJaUNrMnhWU0Z2Zk5DN3B4aE90MkdaM2pYcllXMHdrb3hhU01PWWkxWnFnMG5pNTFrMjJsemw3V0dSV2FHTTE1NDlnNnd3cDByMlVZOW5FanJIckp0Y0xiRW0iLCJtYWMiOiJlYTIzYzAwM2IyZThhNTQ5ZTdlZWUxYjExMjkwZjBlYjc4YWQ0MmYzZTFlNDliMWE0ZGY4M2RjNWRkMWU4NDU0In0=',
        }

        json_data = {
            'email': mailx,
            'timestamp': 1650628073,
        }

        response = requests.post('https://smailpro.com/app/key',
                                 cookies=cookies, headers=headers, json=json_data).json()
        return response['items']

    def check_mail(mailx):

        xkey = Email.key2(mailx)

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://smailpro.com',
            'Referer': 'https://smailpro.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-rapidapi-ua': 'RapidAPI-Playground',
        }
       
        while True:
            try:

                response = requests.get(
                    f'https://public-sonjj.p.rapidapi.com/email/gm/check?key={xkey}&rapidapi-key=f871a22852mshc3ccc49e34af1e8p126682jsn734696f1f081&email={mailx}&timestamp=1650628073', headers=headers).json()
                if response['items'] == []:
                    None
                else:
                    print(response)
            except:
                return False


def urmom():
    system(' ')
    system("mode 50,30")
    print(f''' 
            {Fore.LIGHTBLUE_EX}â•”â•â•—â•”â•â•—â•”â•—â•”{Fore.BLUE}â•”â•â•—â•”â•¦â•—â•”â•â•—â•¦â•¦  {Fore.LIGHTBLACK_EX} G
            {Fore.LIGHTBLUE_EX}â•‘ â•¦â•‘â•£ â•‘â•‘â•‘{Fore.BLUE}â•‘â•£ â•‘â•‘â•‘â• â•â•£â•‘â•‘  {Fore.LIGHTBLACK_EX} E
            {Fore.LIGHTBLUE_EX}â•šâ•â•â•šâ•â•â•â•šâ•{Fore.BLUE}â•šâ•â•â•© â•©â•© â•©â•©â•©â•â•{Fore.LIGHTBLACK_EX} L

''')
    a = input(f"    {Fore.LIGHTBLACK_EX}[!]{Fore.LIGHTCYAN_EX} how much email u want to gen : ")
    print('\n\n')
    for i in range(int(a)):
        print("            " + Email.mail())
        input("            if u done press enter : ")
        Email.check_mail(Email.mail())
        print("            verify")

urmom()