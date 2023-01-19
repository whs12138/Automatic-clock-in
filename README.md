# Automatic-clock-in
自动体温打卡（python+OCR+requests）

使用环境以及工具：
 - 开发工具PyCharm
 - Python版本 <= 3.8
 - 第三方库 
    - requests （网络请求） 
    - ddddocr （OCR验证码识别）
 使用方法：
  1. 创建一个py工程，放入3个py文件
  2. `pip install requests` 
     `pip install ddddocr`
  3. 在`config.py`文件中, 填上用户名、密码
  ```
   # 登录请求参数
        self.post_params = {
            'username': '*************',  # 用户名
            'password': '***********',  # 密码
            'uuid': '',  # uuid
            'code': ''  # 验证码
        }
  ```
  4. 运行`main.py`文件
  
  B站配套操作视频：[自动打卡运行教程](https://space.bilibili.com/477564364)
  
  后续在B站更新：
    - 怎么用PC浏览器打开只允许在微信移动端打开的网页
    - JS逆向，从零分析打卡网站的技术选型、操作流程，进行网站的JS解析
    - 使用Python,获取验证码、uuid -> 登录 -> 得到token -> 提交体温信息
    - 在Linux(阿里云 CentOS)上部署程序，设置定时任务
    
  
