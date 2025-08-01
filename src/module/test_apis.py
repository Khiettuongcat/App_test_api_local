import requests
import json

class TestAPIs:
    @staticmethod
    def APIsGet(url):
        url_rq = requests.get(url)
        return url_rq.status_code, url_rq.text
    @staticmethod
    def APIsPost_Json(url, data):
        post_ = requests.post(url, json=json.loads(data))
        return post_.status_code, post_.text
    @staticmethod
    def APIsPost_Text(url, text, ct):
        headers = {
            "Content-Type": f"{ct}"
        }
        post_test = requests.post(url, data=str(text),headers=headers)
        return post_test.status_code, post_test.text
    @staticmethod
    def APIsPUT(url, data):
        rq = requests.put(url, json.dumps(data))
        return  rq.status_code, rq.text
    @staticmethod
    def APIsDelete(url):
        rq = requests.delete(url)
        return rq.status_code, rq.text