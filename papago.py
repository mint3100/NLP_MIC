import urllib.request, requests
import settings

client_id = settings.client_id
client_secret = settings.client_secret

# Project MintBot
# Papago Translate Module
# Created : 2023.11.17 By Mint
# Last Modified : 2024.07.10
# ChangeLog : 네이버 오픈 API 종료에 대응했습니다.

def translate(text, source, target):
    data = {'text' : text,'source' : source,'target': target}
    header = {"X-NCP-APIGW-API-KEY-ID":client_id, "X-NCP-APIGW-API-KEY":client_secret}
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    response = requests.post(url, headers=header, data= data)
    t_data = response.json()
    global trans_res
    trans_res = t_data['message']['result']['translatedText']
    return trans_res

print(client_id)