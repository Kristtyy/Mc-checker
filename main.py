import requests, random
Token = input("Enter Bearer Token: ")
username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=4))
while True:
    headers = {
        'authority': 'api.minecraftservices.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,nl-NL;q=0.8,nl;q=0.7',
        'authorization': '{Token}',
        'origin': 'https://www.minecraft.net',
        'referer': 'https://www.minecraft.net/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get(f'https://api.minecraftservices.com/minecraft/profile/name/{username}/available', headers=headers)
        if response.json()['status'] == "AVAILABLE":
            print(f"{username} Available")
    except:
        print(response.json())