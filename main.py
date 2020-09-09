import time
import json
import requests
import random
import datetime

#sectets字段录入
deptId = eval(input())
text = input()
emergencyNum = input()
phoneNum = input()
userName = input()
stuNum = input()
userId = input()
dormNum = input()
homeTown = input()
personNum = input()
homeAddress = input()
local = input()



area = {'address':homeAddress,'text':local,'code':""}
areaStr = json.dumps(area, ensure_ascii=False)


sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

jsons =  {
    "businessType": "epmpics",
    "method": "submitUpInfoSchool",
    "jsonData": {
        "deptStr": {
            "deptid": deptId,
            "text": text
        },
        "areaStr": areaStr,
        "reportdate": round(time.time()*1000),
        "customerid": "43",
        "deptid": deptId,
        "source": "app",
        "templateid": "clockSign3",
        "stuNo": stuNum,
        "username": userName,
        "userid": userId,
        "updatainfo": [
         {
	"propertyname":"temperature:,
	"value":"36.5"
         },
         {
	"propertyname":"symptom",
	"value":"无症状"
         }
        ],
        "customerAppTypeRuleId":148,
        "clockState":0
    }
}                       
#提交打卡
response = requests.post(sign_url, json=jsons)
utcTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
cstTime = utcTime.strftime("%H:%M:%S")
print(response.text)
#结果判定
if response.json()["msg"] == '成功':
        msg = "打卡成功-" + cstTime
else:
        msg = "打卡异常-" + cstTime
print(msg)
#微信通知
sckey = input()
title = msg
result = json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False)
content = f"""
```
{result}
```
### 😀[收藏](https://github.com/YooKing/HAUT_autoCheck)此项目
"""
data = {
"text":title,
"desp":content
}
req = requests.post(sckey,data = data)
