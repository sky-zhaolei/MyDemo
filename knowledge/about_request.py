import requests

url = "https://api.dstcar.com/sso/sendVerifCode"
send_head = "'phone':'15070720246'"

a = requests.post(url,data="",json=send_head)
print(a.json())
