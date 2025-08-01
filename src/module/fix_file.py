import os
from tkinter import messagebox

def fix_file_log_send():
    get_name_parth = os.path.expanduser('~')
    parth_open = r"{}\AppData\Roaming".format(get_name_parth)
    parth = r"{}\AppData\Roaming\data_Test_APIs".format(get_name_parth)
    parth_log = r"{}\AppData\Roaming\data_Test_APIs\Log".format(get_name_parth)
    parth_file_history = r"{}\AppData\Roaming\data_Test_APIs\Log\history.json".format(get_name_parth)

    if not os.path.exists(parth):
        os.mkdir(parth)
        if os.path.isdir(parth):
            os.mkdir(parth_log)
            if os.path.isdir(parth_log):
                with open(parth_file_history, 'a'):
                    os.utime(parth_file_history, None)
        else:
            value = messagebox.showerror("messege Test APIs",'Cannot create folder, you want check folder not')
            if value == "ok":
                os.startfile(parth_open)
    else:
        if not os.path.exists(parth_log):
            os.mkdir(parth_log)
        else:
            with open(parth_file_history,'a'):
                os.utime(parth_file_history, None)