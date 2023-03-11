"""
基于项目定制化封装
1、鉴权:token
2、项目通用请求头设置
3、请求体格式处理
"""
import requests


def handle_header(token=None):
    """
    判断是否有token参数，如果有，则请求时携带token
    :param token:
    :return:
    """
    headers = {}
    if token:
        headers["token"] = token
    return headers


def send_requests(method,url,data=None,token=None):
    # 设置token请求头
    headers = handle_header(token)
    # 根据请求类型，调用请求方法
    method = method.upper()
    if method == "GET":
        resp = requests.get(url,params=data,headers=headers)
    elif method == "POST":
        resp = requests.post(url,json=data,headers=headers)
    else:
        resp = "当前仅支持post/get请求方式"
        print(resp)

    return resp


if __name__ == '__main__':
    p = send_requests(method="sss",url="iji",data="jjj",token="jij")
    url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
    send_data = {'phone': '15070720246'}
    a = send_requests(method="post",url=url, data=send_data)
    print(a.json())

    url1 = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/login"
    send_data = {"phone": "15070720246", "verifyCode": "999999"}
    b = send_requests(method="post",url=url1, data=send_data)
    token = b.json()["data"]["token"]
    print(b.json()["data"]["token"])

    url2 = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/user/getUserInfo"
    b = send_requests(method="post",url=url2, data=send_data,token=token)
    print(b.json())


