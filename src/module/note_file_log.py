import json
import os
from datetime import datetime

def openfile(data_new): # me use AI code openfile note
    get_name_parth = os.path.expanduser('~')
    parth_file_history = r"{}\AppData\Roaming\data_Test_APIs\Log\history.json".format(get_name_parth)

    if not  os.path.exists(parth_file_history):
        with open(parth_file_history, 'w', encoding='utf-8') as fj:
            json.dump([], fj, indent=4)

    # Đọc dữ liệu cũ
    try:
        with open(parth_file_history, 'r', encoding='utf-8') as file_r:
            db_json = json.load(file_r)
            if not isinstance(db_json, list):
                db_json = []
    except json.JSONDecodeError:
        db_json = []

    db_json.append(data_new)

    with open(parth_file_history,'w', encoding='utf-8') as file_w:
        json.dump(db_json, file_w,indent=4, ensure_ascii=False)

def from_date(data_time,methods,url,headers,status_code,body):
    data_note = {
        "timestamp": str(data_time),
        "method": str(methods),
        "url": str(url),
        "response": {
            "status_code": status_code,
            "headers": {
                "Content-Type": str(headers)
            },
        "data" : {
            "body" : str(body)
             }
        }
    }
    return data_note
def Note(methods, url, status_code, headers, body):
    data_time = datetime.now()
    db_note = from_date(data_time, methods,url,headers,status_code,body)
    openfile(db_note)
