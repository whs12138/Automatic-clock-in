import random
import datetime


class Config:
    def __init__(self):
        # 基础URL
        self.baseURL = "https://ysxy.easyway.wang/peace-app/"
        # 登录请求参数
        self.post_params = {
            'username': '******',  # 用户名
            'password': '****',  # 密码
            'uuid': '',  # uuid
            'code': ''  # 验证码
        }
        # 随机生成体温 36.3~36.7
        self.temperature = 36 + random.randint(3, 7) * 0.1
        # 请求用到的数据
        self.utils = {
            'img_path': '',  # 图片名称
            'token': '',
            'cookie':  """user={%22zhanghao%22:%22""" + self.post_params['username'] + """%22%2C%22mima%22:%22""" + self.post_params['password'] + """%22%2C%22checked1%22:true%2C%22checked2%22:true};jiankangs={%22tiwen%22:%22"""+  str(self.temperature) + """"%22%2C%22yichang%22:1%2C%22quezhen%22:1%2C%22jingwai%22:1%2C%22renshi%22:1%2C%22jiankang%22:0%2C%22sixclass%22:1}""",
            'insert_params': {
                "address": "济南市",
                "addressDetail": "山东财经大学燕山学院(莱芜校区)",
                "healthStatus": 0,
                "recordTime": str(datetime.date.today()),
                "temperature": str(self.temperature),
                "temperatureImg": "",
                "remark": "",
                "recordType": 2,
                "familyCondition": "",
                "familyStatus": 1,
                "topicOne": 1,
                "topicThree": 1,
                "topicTwo": 1,
                "abnormal": 1,
                "flag": 0
            }
}
