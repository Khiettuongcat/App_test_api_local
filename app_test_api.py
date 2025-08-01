import json
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import *
import os

from src.module.all_from     import from_msg_e
from src.module.fix_file import fix_file_log_send
from  src.module.test_apis import TestAPIs
from  src.module.note_file_log import Note

# open json methods
def open_Json():
    # get data methods 
    with open('src/data/data_methods.json', 'r', encoding='utf-8') as file_methods:
        data_ = json.load(file_methods)
        tiltes = data_["title"]
        method = data_['methods']
        data_types = data_['data_type']
        content_types = data_['content_type']
    return tiltes, method, data_types, content_types

# btn clean
def clean():
    Input_url.delete("0", tk.END)
    txt_input.delete("1.0", tk.END)
    txt_output.delete("1.0", tk.END)

#  check
def check():
    method  = combo_box.get()
    input_usl = Input_url.get()

    data_row = txt_input.get("1.0", "end-1c")
    output_data = txt_output

    data_types = combo_box_data.get()
    conetent_type = cp_box.get()

    try:
        if data_row == "seelog" or data_row == "log" or  data_row == "l":
            os.startfile(parth_file)
        else:
            if method != "" and input_usl != "":
                if method == "GET":
                    status, data = TestAPIs.APIsGet(input_usl)
                    Note(methods=method, url=input_usl,status_code=status,headers=conetent_type, body=data_row)
                    if status == 200:
                        data2 = data
                        output_data.insert(END, f'{data}')
                        if data2 == data:
                            output_data.delete('1.0', tk.END)
                            output_data.insert(END, f'{data}')
                    else:
                        from_msg_e(status=status)
                elif method == "POST":
                    if data_types == "Json":
                        status, data_post = TestAPIs.APIsPost_Json(url=input_usl, data=data_row)
                        Note(methods=method, url=input_usl, status_code=status, headers=conetent_type, body=data_row
                        )
                        if status == 201:
                            data2 = data_post
                            output_data.insert(END, f'{json.loads(data_post)}')
                            if data2 == data_post:
                                output_data.delete('1.0', tk.END)
                                output_data.insert(END, f'{data_post}')
                        else:
                            from_msg_e(status)
                    elif data_types == "Text":
                        status, data = TestAPIs.APIsPost_Text(input_usl, data_row, conetent_type)
                        Note(methods=method, url=input_usl, status_code=status, headers=conetent_type, body=data_row
                        )

                        if status == 200 or status == 201:
                            data2 = data
                            output_data.insert(END, f'{data}')
                            if data2 == data:
                                output_data.delete('1.0', tk.END)
                                output_data.insert(END, f'{data}')
                        else:
                            from_msg_e(status)
                elif method == "PUT":
                    status, data = TestAPIs.APIsPUT(input_usl, data_row)
                    Note(methods=method, url=input_usl,status_code=status,headers=conetent_type, body=data_row)
                    if status == 200:
                        data2 = data
                        output_data.insert(END, f'{data}')
                        if data2 == data:
                            output_data.delete('1.0', tk.END)
                            output_data.insert(END, f'{data}')
                    else:
                        from_msg_e(status)

                elif method == "DELETE":
                    status, data = TestAPIs.APIsDelete(input_usl)
                    Note(methods=method, url=input_usl,status_code=status,headers=conetent_type, body=data_row)
                    if status == 200:
                        data2 = data
                        output_data.insert(END, f'{data}')
                        if data2 == data:
                            output_data.delete('1.0', tk.END)
                            output_data.insert(END, f'{data}')
                    else:
                        from_msg_e(status)
            else:
                if method == "":
                    messagebox.showinfo('mesage Test APIS', 'cannot data method')
                elif input_usl == "":
                    messagebox.showinfo('mesage Test APIS', "Cannot link test")
                else:
                    messagebox.showerror('mesage Test APIS', "about methods and link api test cannot")
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
    except Exception as e: # Catch any other unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    finally:
        # This code will always execute, regardless of errors
        print("Calculation attempt finished.")


if __name__ == "__main__":
    title,methods, data_type, content_type = open_Json()
    get_name_parth = os.path.expanduser('~')
    parth_file_history = r"{}\AppData\Roaming\data_Test_APIs\Log\history.json".format(get_name_parth)
    parth_file = r"{}\AppData\Roaming\data_Test_APIs\Log".format(get_name_parth)

    if os.path.isfile(parth_file_history):
        try:
            # main
            main = tk.Tk()

            main.geometry("1200x800")
            main.title(title)
            photo = PhotoImage(file='src/img/api.png')
            main.iconphoto(True, photo)

            # combobox methos
            combo_box = ttk.Combobox(main, state="readonly", values=methods)
            combo_box.set("GET")

            # input
            Input_url = Entry(main)

            # button sand
            btn = ttk.Button(main, text='Send', command=check)

            # clean btn
            btn_clean = ttk.Button(main, text='Clean', command=clean)

            # combobox data type
            from_post = tk.Label(main, text='form post')
            combo_box_data = ttk.Combobox(main, state="readonly", values=data_type)
            combo_box_data.set("Json")
            # type content
            tilte_ct = tk.Label(main, text='Content Type')
            cp_box = ttk.Combobox(main, state='readonly', values=content_type)
            cp_box.set("application/json")

            # input date test
            txt_input = tk.Text(main)
            # txt output
            txt_output = tk.Text(main)

            # css
            combo_box.place(x=225, y=30, width=100, height=40)
            Input_url.place(x=350, y=30, width=500, height=40)
            btn.place(x=870, y=30, width=75, height=40)

            from_post.place(x=1075, y=50)
            btn_clean.place(x=950, y=30, width=70, height=40)
            combo_box_data.place(x=1059, y=75, width=100, height=30)

            tilte_ct.place(x=815, y=78)
            cp_box.place(x=900, y=75, width=150, height=30)

            txt_input.place(x=35, y=110, width=1125, height=350)
            txt_output.place(x=35, y=475, width=1125, height=300)

            main.resizable(False, False)  # discibale
            # loop taoj window
            main.mainloop()

        except ValueError as Ve:
            print(Ve)
        except NameError as Ne:
            print(Ne)
        except SystemError as Se:
            print(Se)
    else:
        fix_file_log_send()
        if os.path.isfile(parth_file_history):
            try:
                # main
                main = tk.Tk()

                main.geometry("1200x800")
                main.title(title)
                photo = PhotoImage(file='src/img/api.png')
                main.iconphoto(True, photo)

                # combobox methos
                combo_box = ttk.Combobox(main, state="readonly", values=methods)
                combo_box.set("GET")

                # input
                Input_url = Entry(main)

                # button sand
                btn = ttk.Button(main, text='Send', command=check)

                # clean btn
                btn_clean = ttk.Button(main, text='Clean', command=clean)

                # combobox data type
                from_post = tk.Label(main, text='form post')
                combo_box_data = ttk.Combobox(main, state="readonly", values=data_type)
                combo_box_data.set("Json")
                # type content
                tilte_ct = tk.Label(main, text='Content Type')
                cp_box = ttk.Combobox(main, state='readonly', values=content_type)
                cp_box.set("application/json")

                # input date test
                txt_input = tk.Text(main)
                # txt output
                txt_output = tk.Text(main)

                # css
                combo_box.place(x=225, y=30, width=100, height=40)
                Input_url.place(x=350, y=30, width=500, height=40)
                btn.place(x=870, y=30, width=75, height=40)

                from_post.place(x=1075, y=50)
                btn_clean.place(x=950, y=30, width=70, height=40)
                combo_box_data.place(x=1059, y=75, width=100, height=30)

                tilte_ct.place(x=815, y=78)
                cp_box.place(x=900, y=75, width=150, height=30)

                txt_input.place(x=35, y=110, width=1125, height=350)
                txt_output.place(x=35, y=475, width=1125, height=300)

                main.resizable(False, False)  # discibale
                # loop taoj window
                main.mainloop()

            except ValueError as Ve:
                print(Ve)
            except NameError as Ne:
                print(Ne)
            except SystemError as Se:
                print(Se)