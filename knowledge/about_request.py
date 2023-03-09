import requests

url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
send_head = {'phone':'15070720246'}

a = requests.post(url,data="",json=send_head)
print(a.json())
