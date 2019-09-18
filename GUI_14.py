"""
登录窗口
待解决的问题是：为什么用户名和密码一样才能成功，修改代码
"""
import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='/home/zjy/图片/welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name:').place(x=80, y=150)
tk.Label(window, text='Password:').place(x=80, y=190)

# entry
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
var_usr_pwd = tk.StringVar()
var_usr_pwd.set('')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name).place(x=160, y=150)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*').place(x=160, y=190)

# login and sign up button
def urs_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong!')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                                            'You have not sign up yet. Sign up.')
        if is_sign_up:
            urs_sign_up()

def urs_sign_up():
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')
    # user information
    tk.Label(window_sign_up, text='User name:').place(x=45, y=60)
    tk.Label(window_sign_up, text='Password:').place(x=50, y=80)
    tk.Label(window_sign_up, text='Confirm Password:').place(x=00, y=100)
    # entry
    var_usr_name = tk.StringVar()
    var_usr_name.set('example@python.com')
    var_usr_pwd = tk.StringVar()
    var_usr_pwd.set('')
    var_usr_pwd_2 = tk.StringVar()
    var_usr_pwd_2.set('')

    def sign_info():

        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if var_usr_pwd_2.get() != var_usr_pwd.get():
            tk.messagebox.showerror('Error', 'password is different')
        elif var_usr_name.get() in exist_usr_info:
            tk.messagebox.showerror("Erro", 'The user has already signed up!')
        else:
            exist_usr_info[var_usr_name.get()]=var_usr_pwd_2.get()
            tk.messagebox.showinfo("welcome", 'Success!')
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            window_sign_up.destroy()
    entry_usr_name = tk.Entry(window_sign_up, textvariable=var_usr_name).place(x=120, y=60)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=var_usr_pwd, show='*').place(x=120, y=80)
    entry_usr_pwd_2 = tk.Entry(window_sign_up, textvariable=var_usr_pwd_2, show='*').place(x=120, y=100)
    btn_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_info).place(x=120, y=150)


btn_login = tk.Button(window, text='Login', command=urs_login).place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=urs_sign_up).place(x=270, y=230)





window.mainloop()

