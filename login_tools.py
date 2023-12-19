import requests
import jwt
from loguru import logger
from flask import current_app


def get_host():
    return current_app.config['pandora_domain'] + '/' + current_app.config['proxy_api_prefix']


# 本类用于封装登录相关操作，包括登录、获取session_token、获取access_token、获取用户信息等

# 使用用户名和密码登录 /api/auth/login
def login(username, password):
    host = get_host()
    payload = f'username={username}&password={password}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", host + "/api/auth/login", headers=headers, data=payload)
    if response.status_code != 200:
        raise Exception(response.json())
    logger.info("登录结果：{}", response.json())
    return response.json()


# 使用session_token获取access_token /api/auth/session
def get_access_token(session_token):
    host = get_host()
    payload = f'session_token={session_token}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", host + "/api/auth/session", headers=headers, data=payload)
    logger.info("获取access_token结果：{},{}", response.json(), response.status_code)
    if response.status_code != 200:
        raise Exception("获取access_token失败")
    return response.json()


def fresh_setup():
    host = get_host()
    response = requests.request("POST", host + "/api/setup/reload")
    logger.info("重载：{}", response.json())
    if response.status_code != 200:
        raise Exception("重载失败")
    return response.json()


def get_email_by_jwt(token):
    # 解析token
    return jwt.decode(token, algorithms=['HS256'], options={"verify_signature": False})
