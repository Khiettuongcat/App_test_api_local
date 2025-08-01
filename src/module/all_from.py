from tkinter import messagebox

# from_output_error
def from_msg_e(status):
    if status == 400:
        messagebox.showerror('message', 'HTTP 400 Bad Request troubleshooting')
    elif status == 404:
        messagebox.showerror('message', 'HTTP 401 Unauthorized authentication')
    elif status == 500:
        messagebox.showerror('msg', 'error data input')