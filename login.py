

def login_check(username=None, password=None):
    if username != None and password != None:
        if username == 'py27' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或者密码不正确"}
    else:
        return {"code": 1, "msg": "参数不能为空"}


if __name__ == '__main__':
    res = login_check()
    print(res)
