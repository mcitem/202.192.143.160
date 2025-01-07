import requests
import json
import urllib

login_url = "https://202.192.143.160:9443/gw/api/v1/auth/login"
login_hea = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "content-type": "application/json;charset=UTF-8"
}


def loginbody(username):
    return {"username": username, "password": "U2Vuc2VTdHVkeTEyMw=="}


def login(username):
    res = requests.post(login_url, json=loginbody(
        username), headers=login_hea, verify=False)
    print("loginstatus", res.status_code)
    res = res.json()
    return res["data"]['token'], res["data"]['refreshToken']


def get_h(username):
    token, refreshToken = login(username)
    return {
        "Origin": "https://202.192.143.160:9443",
        "Content-Type": "application/json; charset=UTF-8",
        "Cookie": f"language=zh_CHS; userId={username}; roles=[%22ROLE_STUDENT%22]; token={urllib.parse.quote(refreshToken)}",
        "X-Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    }


def getlist():
    with open("exp.json", "r", encoding="utf-8") as f:
        fs = f.read()
        fs = json.loads(fs)
    return fs["data"]


h = get_h(202311294304)
for i in getlist():
    eid = i["id"]
    # body00 = {"experimentId": eid}
    body = {"experimentId": eid,
            "isFinished": False,
            "currentStep": 0,
            "expContext": "",
            "lastopertime": "2099-99-99T99:99:99.999+9999",
            "excSuccess": False
            }
    # res0 = requests.post("https://202.192.143.160:9443/api/v1/student/student_experiment",
    #                      json=body00, headers=header, verify=False)
    # print(res0.status_code)
    res = requests.put("https://202.192.143.160:9443/api/v1/student/student_experiment/context",
                       json=body, headers=h, verify=False)

    print(res.status_code)
