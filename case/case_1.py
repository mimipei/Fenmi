
import requests
import re
def TappingToken():
    data = {
        "username": "17673058430",
        "password": "123456",
        "device_type": "android"
    }
    url = "http://test.51fenmi.com/api/user/public/login"
    response = requests.post(url, data)
    return_result = response.json()
    login_token = re.findall(r"'token':..(.+)....beService'", str(return_result))
    return login_token
