import requests

url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
send_data = {'phone':'15070720246'}

a = requests.post(url,data=send_data)
print(a.json())

url1 = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/login"
send_data = {"phone":"15070720246","verifyCode":"999999"}
b = requests.post(url1,data=send_data)
get_token = b.json()["data"]["token"]
print(b.json()["data"]["token"])

url2 = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/user/getUserInfo"
send_header = {"token": get_token}
print(send_header)
b = requests.post(url2,headers=send_header)
print(type(b.json()["code"]))