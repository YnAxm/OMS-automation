# import json
# import requests
# headers = {'Content-Type': 'application/json;charset=utf-8'}
# api_url = "https://oapi.dingtalk.com/robot/send?access_token=46312a78a8f728f2bae5caf6dd330afd08f5c0b75ae3cfd2c2678dae58e7111c"
# ##从钉钉机器人设置中拷贝
# def msg(text):
#     json_text = {
#         "msgtype": "text",
#         "at": {
#             "atMobiles": [
#                 ""
#             ],
#             "isAtAll": False
#         },
#         "text": {
#             "content": text
#         }
#     }
#     print(requests.post(api_url, json.dumps(json_text), headers=headers).content)
# data = ('E:\\OMS-automation\\report\\report')
# msg("自动化测试报告已生成，文件地址"+data+"。")
# # print(data)