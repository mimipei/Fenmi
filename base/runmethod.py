import requests
import json


class runMethod:
    '封装get/post请求'

    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def runmain(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.pos_tmain(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
