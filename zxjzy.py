import tkinter
from  tkinter import *
import tkinter.messagebox
import pymysql
app=tkinter.Tk()
app.title("大学生创新")
app.geometry("600x600")

conn=pymysql.connect(host="localhost",port=3306,
                     user="root",password="admin123456",
                     database="xtsj",charset="utf8")
cur=conn.cursor()
def Rname():
    sql="select stu_name from student where stu_id=%s"
    row=cur.execute(sql,(identry,))
    if row==0:
        print("账号或者密码有误")
    else:
        stu_id, = cur.fetchone()
        if identry != stu_id:
            print("账号或者密码有误")
        else:
            print("登录成功")

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

b=tkinter.Button(app,text="登录",command=Rname,bg="gray",font=("楷体",25))
b.place(x=200,y=400,height=50,width=200)


def zxzc():
    stubar=tkinter.Button(app, text="在线自测",command=kszc, width=100, font=("楷体", 32))
    stubar.place(x=150, y=100, width=300, height=80)
    stuher=tkinter.Button(app, text="在线考试",command=ksks, width=100, font=("楷体", 32))
    stuher.place(x=150, y=300, width=300, height=80)


list1=[]
list2=[]
def kszc():
    i = 1
    m = 0
    count = 0
    def check():
        global i
        global count
        global m
        sql = "select ti_gan from tiku"
        row = cur.execute(sql)
        if row == count:
            var1.set("题目已经做完了")
            tkinter.messagebox.showerror("错误", "题目已经出完了")
            return
        else:
            sql = "select * from tiku order  by rand() limit %s"
            cur.execute(sql, (i))
            add = cur.fetchone()
            print(add)
            if add[2] not in list2:
                list2.append(add[2])
                list1.append(add[1])
                m += 1
                print(list1)
                print(list2)
                var1.set(add[2] + "\n" + add[3] + "\n" + add[4] + "\n" + add[5] + "\n" + add[6])
                count += 1
                i += 1
            else:
                check()
def get():
    commm=var3.get()
    var2.set("您的选择是："+commm)
def xxx(m):
    cnnn=var3.get()
    if str(cnnn)==list1[m-1]:
        var2.set("回答正确")
    else:
        var2.set("回答错误")
var1 = StringVar()
var1.set("点击下一题考试")
var2=StringVar()
var3=StringVar()
var3.set("a")
label=tkinter.Label(app,textvariable=var1,bg="#44ffff",font= ("Arial", 12))
label.place(x=0,y=0,height=300,width=700)
label=tkinter.Label(app,textvariable=var2,bg="red",font= ("Arial", 12))
label.place(x=700,y=0,height=300,width=200)
button1=tkinter.Radiobutton(app,text="A",value="A",variable=var3,bg="white",command=get)
button1.place(x=400,y=400,height=30,width=100)
button2=tkinter.Radiobutton(app,text="B",value="B",variable=var3,bg="white",command=get)
button2.place(x=400,y=450,height=30,width=100)
button3=tkinter.Radiobutton(app,text="C",value="C",variable=var3,bg="white",command=get)
button3.place(x=400,y=500,height=30,width=100)
button4=tkinter.Radiobutton(app,text="D",value="D",variable=var3,bg="white",command=get)
button4.place(x=400,y=550,height=30,width=100)
button5=tkinter.Button(app,text="下一题",bg="white",command=zxzc)
button5.place(x=0,y=330,height=60,width=150)#随机选题
button6=tkinter.Button(app,text="判断对错",bg="white",command=lambda :xxx(m))
button6.place(x=0,y=420,height=60,width=150)

def ksks():
    pass
app.mainloop()