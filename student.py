import tkinter
import pymysql
from tkinter import *
import tkinter.filedialog
import  tkinter.messagebox


conn=pymysql.connect(host="localhost",port=3306,
                user="root",password="admin123456",
                database="xtsj",charset="utf8")
cur=conn.cursor()


'''

import socket
import tkinter
import tkinter.messagebox
app=tkinter.Tk()
app.title("学生登录界面！")
app.geometry("600x600")


stulabel=tkinter.Label(app,text="欢迎进入学生登录系统！",width=100,font=("楷体",32))
stulabel.place(x=50,y=50,width=500,height=100)


idlabel=tkinter.Label(app,text="学号:",width=40,font=("宋体",25))
idlabel.place(x=100,y=170,width=100,height=50)
identry=tkinter.Entry(app,width=100,font=("宋体",25))
identry.place(x=200,y=170,width=270,height=40)

namelabel=tkinter.Label(app,text="姓名:",width=40,font=("宋体",25))
namelabel.place(x=100,y=250,width=100,height=50)
nameentry=tkinter.Entry(app,width=100,font=("宋体",25))
nameentry.place(x=200,y=250,width=270,height=40)

s=socket.socket()
s.connect(('192.168.0.106',8888))

def check():
    id=identry.get()
    name=nameentry.get()
    print(id+name)
    s.send((id+" "+name).encode("utf-8"))
    mess=s.recv(1024).decode("utf-8")
    if mess=="notmath":
        tkinter.messagebox.showerror("失败","学号或者姓名输入错误")
    elif mess=="repeat":
        tkinter.messagebox.showerror("失败","不允许重复签到")
    elif mess=="success":
        tkinter.messagebox.showinfo("恭喜","登录成功")
b=tkinter.Button(app,text="登录",command=check,font=("楷体",30))
b.place(x=200,y=400,width=200,height=70)


app.mainloop()

'''



def welwin():
    pass

def examination():
    pass

def qiandao():
    pass

def handwork():
    pass
def stuwere():
    tk = tkinter.Tk()
    tk.title("学生系统APP！")
    tk.geometry("600x600+400+0")

    def exit3():
        tk.destroy()
        welwin()

    def exit4():
        tk.destroy()
        examination()

    def exit5():
        tk.destroy()
        qiandao()

    def exit6():
        tk.destroy()
        handwork()

    def exit8():
        tk.destroy()
        stulog()

    stubar = tkinter.Button(tk, text="在线自测", command=exit3, width=100, bg="gray", font=("楷体", 32))
    stubar.place(x=150, y=50, width=300, height=80)
    stuher = tkinter.Button(tk, text="在线考试", command=exit4, width=100, bg="gray", font=("楷体", 32))
    stuher.place(x=150, y=150, width=300, height=80)
    stuher = tkinter.Button(tk, text="在线签到", command=exit5, width=100, bg="gray", font=("楷体", 32))
    stuher.place(x=150, y=250, width=300, height=80)
    stuher = tkinter.Button(tk, text="在线交作业", command=exit6, width=100, bg="gray", font=("楷体", 32))
    stuher.place(x=150, y=350, width=300, height=80)
    stuher = tkinter.Button(tk, text="切换账户", command=exit8, width=100, bg="gray", font=("楷体", 32))
    stuher.place(x=150, y=450, width=300, height=80)

    tk.mainloop()

def stulog():
    # 学生登录界面
    tb = tkinter.Toplevel()
    tb.title("学生登录APP！")
    tb.geometry("600x600+400+0")

    global identry
    global nameentry
    global var1
    var1 = StringVar()
    var1.set(" 欢迎！ ")

    idlabel = tkinter.Label(tb, text="学号:", width=40, font=("楷体", 25))
    idlabel.place(x=100, y=170, width=100, height=50)
    identry = tkinter.Entry(tb, width=100, font=("楷体", 25))
    identry.place(x=200, y=170, width=270, height=40)

    namelabel = tkinter.Label(tb, text="姓名:", width=40, font=("楷体", 25))
    namelabel.place(x=100, y=250, width=100, height=50)
    nameentry = tkinter.Entry(tb, width=100, font=("楷体", 25))
    nameentry.place(x=200, y=250, width=270, height=40)

    def exit():
        id = identry.get()
        name = nameentry.get()

        sql = "select stu_name from student where stu_id=%s"
        row = cur.execute(sql, (id,))
        if row == 0:
            var1.set("您输入的id或者姓名有误！")
        else:
            password2, = cur.fetchone()
            if name != password2:
                var1.set("您输入的id或者姓名有误！")
            else:
                tb.destroy()
                stuwere()


    b = tkinter.Button(tb, text="登录", command=exit, bg="gray", font=("楷体", 25))
    b.place(x=200, y=400, height=50, width=200)

    label = tkinter.Label(tb, textvariable=var1, width=100, font=("楷体", 25))
    label.place(x=50, y=50, width=500, height=100)

    tb.mainloop()
stulog()