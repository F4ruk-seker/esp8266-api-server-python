import firebase_admin
from firebase_admin import credentials
import datetime

import requests
import json
from firebase_admin import auth
from firebase_admin import firestore
import os

cred = credentials.Certificate(os.getenv("Admin_sdk_google"))
app = firebase_admin.initialize_app(cred)



class Database:
    def __init__(self):
        "test"
        self.db = firestore.client()

    def updateEspData(self,ID:str,value:str) -> bool:
        data = self.getEspData(ID)
        if data:
            self.db.collection('esp').document(ID).update({'sensor':value})
            return True
        return False
    def update_alert_time_out(self,ID:str):
        date = datetime.datetime.now() + datetime.timedelta(minutes=1)
        self.db.collection('esp').document(ID).update({'delay': date.timestamp()})
    def getEspData(self,ID):
        return self.db.collection('esp').document(ID).get().to_dict()

def notification(title,detail):
    notification_api = os.getenv("notification_api")
    notification_target = os.getenv("notification_test_target")
    api_host = os.getenv("notification_api_host")
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+notification_api
    }
    payload = {
        "to": notification_target,
        "priority" : "high",
        "notification" : {
            "body" : detail,
            "title" :title,
        },
    }
    response = requests.post(api_host, data=json.dumps(payload), headers=headers)
    return response.status_code == 200
