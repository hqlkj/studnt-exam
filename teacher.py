

from tkinter import *
import pymysql
import tkinter

conn=pymysql.connect(host="localhost",port=3306,
                user="root",password="admin123456",
                database="xtsj",charset="utf8")
cur=conn.cursor()
'''

import socket
import threading
import pymysql

server=socket.socket()
server.bind(('192.168.0.106',8888))
server.listen(100)

conn=pymysql.connect(host="localhost",port=3306,user="root",password="admin123456",database="xtsj",charset="utf8")
cur=conn.cursor()
iplist=[]


def run(s,addr):
    while True:
        data=s.recv(1024).decode("utf-8")
        print(data)
        id,name=data.split(" ")
        sql="select stu_name from student where stu_id=%s"
        row=cur.execute(sql,(id))
        if row==0:
            s.send("notmath".encode("utf-8"))
        else:
            if cur.fetchone()[0]!=name:
                s.send("notmath".encode("utf-8"))
            else:
                if addr[0] in iplist:
                    s.send("repeat".encode("utf-8"))
                else:
                    iplist.append(addr[0])
                    sql2="update student set score=score+5 where stu_id=%s"
                    cur.execute(sql2,(id))
                    conn.commit()
                    s.send("success".encode("utf-8"))

while True:
    s,addr=server.accept()
    threading.Thread(target=run,args=(s,addr,)).start()

server.close()
'''


def checkname():
    pass

def operation():
    pass

def otstu():
    pass

def tealog():
    pass
def teawere():
    id = identry.get()
    name = nameentry.get()

    sql = "select tea_name from teacher where tea_id=%s"
    row = cur.execute(sql, (id,))
    if row == 0:
        var.set("您输入的id或者姓名有误！")
    else:
        password2, = cur.fetchone()
        if name != password2:
            var.set("您输入的id或者姓名有误！")
        else:
            tk = tkinter.Tk()
            tk.title("欢迎使用KK系统！")
            tk.geometry("600x600")

            def exi1():
                tk.destroy()
                checkname()

            def exi2():
                tk.destroy()
                operation()

            def exi3():
                tk.destroy()
                otstu()


            def exi4():
                tk.destroy()
                tealog()

            stubar = tkinter.Button(tk, text="教师点名", command=exi1, width=100, bg="gray", font=("楷体", 32))
            stubar.place(x=150, y=100, width=300, height=80)
            stuher = tkinter.Button(tk, text="在线收作业", command=exi2, width=100, bg="gray", font=("楷体", 32))
            stuher.place(x=150, y=200, width=300, height=80)
            stuher = tkinter.Button(tk, text="开始考试", command=exi3, width=100, bg="gray", font=("楷体", 32))
            stuher.place(x=150, y=300, width=300, height=80)
            stuher = tkinter.Button(tk, text="切换账号", command=exi4, width=100, bg="gray", font=("楷体", 32))
            stuher.place(x=150, y=400, width=300, height=80)

            tk.mainloop()


def denglu():
    tk = tkinter.Tk()
    tk.title("欢迎使用KK系统！")
    tk.geometry("600x600+400+0")

    global identry
    global nameentry
    global var
    var = StringVar()
    var.set(" 教师端登录系统 ")

    idlabel = tkinter.Label(tk, text="工号:", width=40, font=("楷体", 25))
    idlabel.place(x=100, y=170, width=100, height=50)
    identry = tkinter.Entry(tk, width=100, font=("楷体", 25))
    identry.place(x=200, y=170, width=270, height=40)

    namelabel = tkinter.Label(tk, text="姓名:", width=40, font=("楷体", 25))
    namelabel.place(x=100, y=250, width=100, height=50)
    nameentry = tkinter.Entry(tk, width=100, font=("楷体", 25))
    nameentry.place(x=200, y=250, width=270, height=40)



    b = tkinter.Button(tk, text="登录", command=teawere,  font=("楷体", 25))
    b.place(x=200, y=400, height=50, width=200)

    label = tkinter.Label(tk, textvariable= var , width=100, font=("楷体", 25))
    label.place(x=50, y=50, width=500, height=100)

    tk.mainloop()

denglu()