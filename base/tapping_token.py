import requests
import xlrd
import re


def tapping_token():
    data = xlrd.open_workbook('D:/PycharmProjects/Fenmi/dataconfig/user.xlsx')
    tables = data.sheet_by_index(0)
    username = tables.cell(1, 0).value
    password = tables.cell(1, 1).value
    data = {
        "username": username,
        "password": password,
        "device_type": "android"
    }
    url = "http://test.51fenmi.com/api/user/public/login"
    response = requests.post(url, data)
    return_result = response.json()
    login_token = re.findall(r"'token':..(.+)....beService'",
                             str(return_result))
    return login_token[0]

