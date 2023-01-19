from config import Config
import requests
import json
import ddddocr
import base64
import time


class App:
    def __init__(self):
        self.con = Config()
        self.get_info()
        self.login()
        self.insert_temperature()

    def base64_to_image(self, base):
        """
        base64转图片
        :param base: 验证码的base64编码
        :return: null
        """
        self.con.utils['img_path'] = str(time.time()) + ".jpg"
        imgdata = base64.b64decode(base)
        file = open(self.con.utils['img_path'], 'wb')
        file.write(imgdata)
        file.close()

    def get_info(self):
        """
        获取验证码和uuid
        :return: null
        """
        res = requests.get(self.con.baseURL + "captchaImage")
        data = json.loads(res.text)
        self.con.post_params['uuid'] = data['uuid']
        self.base64_to_image(data['img'])
        self.get_code_by_ocr()

    def get_code_by_ocr(self):
        """
        调用OCR
        :return: null
        """
        ocr = ddddocr.DdddOcr()  # 实例化
        with open(self.con.utils['img_path'], 'rb') as f:  # 打开图片
            img_bytes = f.read()  # 读取图片
        res = ocr.classification(img_bytes)  # 识别
        self.con.post_params['code'] = res

    #
    def login(self):
        """
        登录获取token
        :return: null
        """
        res = requests.post(self.con.baseURL + "login?username=" + self.con.post_params['username'] + "&password=" + self.con.post_params['password'] + "&code=" +
                            self.con.post_params['code'] + "&uuid=" + self.con.post_params['uuid'])
        data = json.loads(res.text)
        if data['code'] == 200:
            self.con.utils['token'] = data['token']

    def insert_temperature(self):
        """
        插入体温数据
        :return: null
        """
        headers = {
            'Authorization': self.con.utils['token'],
            'Cookie': self.con.utils['cookie'],
            'Content-Type': 'application/json'
        }

        res = requests.post(url=self.con.baseURL + "insertHealthRecord", data=json.dumps(self.con.utils['insert_params']), json=json,
                            headers=headers)
        print(res.text)
        print(self.con.temperature)
