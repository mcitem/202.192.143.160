
import json
import urllib
import urllib.parse
import requests
# 被复制端
username0 = "202311294460"
# 粘贴端
username1 = "202311294304"

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


def get_cont(h, eid):

    url = "https://202.192.143.160:9443/api/v1/student/student_experiment?isScored=false&experimentId="
    res = requests.get(url+eid, headers=h, verify=False)
    print("getcont", res.status_code)
    print(res.json())
    res = res.json()
    return res["data"]['stuExp']["expContext"]


def make_c(eid, ctx):
    body = {"experimentId": eid,
            "isFinished": True,
            "currentStep": 1,
            "expContext": ctx,
            "lastopertime": "2099-99-99T99:99:99.999+9999",
            "excSuccess": True
            }
    return body


def copy_to():
    list = getlist()
    h0 = get_h(username0)
    h1 = get_h(username1)
    count = 0
    for i in list:

        # body00 = {"experimentId": eid}
        # res0 = requests.post("https://202.192.143.160:9443/api/v1/student/student_experiment",
        #                      json=body00, headers=h1, verify=False)
        # print(res0.status_code)
        count += 1
        eid = i["id"]
        ctx = get_cont(h0, eid)
        body = make_c(eid, ctx)
        res = requests.put("https://202.192.143.160:9443/api/v1/student/student_experiment/context",
                           json=body, headers=h1, verify=False)
        print(res.status_code)

        if (count >= 20):
            print("done")
            break


def copy_from_save():
    list = getlist()
    h1 = get_h(username1)
    count = 0
    for i in list:

        # body00 = {"experimentId": eid}
        # res0 = requests.post("https://202.192.143.160:9443/api/v1/student/student_experiment",
        #                      json=body00, headers=h1, verify=False)
        # print(res0.status_code)
        eid = i["id"]
        with open(f"save/{eid}.json", "r", encoding="utf-8") as f:
            ctx = f.read()
        body = make_c(eid, ctx)
        res = requests.put("https://202.192.143.160:9443/api/v1/student/student_experiment/context",
                           json=body, headers=h1, verify=False)
        print(res.status_code)


def save_h0():
    list = getlist()
    h0 = get_h(username0)
    count = 0
    for i in list:

        # body00 = {"experimentId": eid}
        # res0 = requests.post("https://202.192.143.160:9443/api/v1/student/student_experiment",
        #                      json=body00, headers=h1, verify=False)
        # print(res0.status_code)
        count += 1
        eid = i["id"]
        ctx = get_cont(h0, eid)
        with open(f"save/{eid}.json", "w", encoding="utf-8") as f:
            f.write(ctx)
        # body = make_c(eid, ctx)


# save_h0()
