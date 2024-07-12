# Project NiceShot
# Base Setting Module
# Created : 2024.07.12 By Mint
# Last Modified :

# 파파고 API 키 값, 네이버 클라우드 플랫폼을 참고하세요.
client_id = ""
client_secret = ""

# 파파고 기능 활성화 여부를 따집니다. (1 = Enable, 0 = Disable)
papago_enabled = 0

def setup():
    global lang
    if papago_enabled == 1:
        if not client_id:
            print("client_id 값이 비어있습니다. settings.py 파일을 확인해주세요.")
            exit()
        elif not client_secret:
            print("client_secret 값이 비어있습니다. settings.py 파일을 확인해주세요.")
            exit()
    elif papago_enabled == 0:
            lang = input("인식할 언어를 입력하세요[ko-kr, ja-jp, .. etc] : ")
            if not lang:
                lang = "ja-jp"
                print(f"입력값이 없어 {lang}(으)로 설정되었습니다.")
            else:
                print(f"설정된 언어 : {lang}")
                lang = lang
    else:
        lang = input("인식할 언어를 입력하세요[ko-kr, ja-jp, .. etc] : ")
        if not lang:
            lang = "ja-jp"
            print(f"입력값이 없어 {lang}(으)로 설정되었습니다.")
        else:
            print(f"설정된 언어 : {lang}")
            lang = lang