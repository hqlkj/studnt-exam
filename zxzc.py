import tkinter
import pymysql
from tkinter import *
import  random
import tkinter.filedialog
import  tkinter.messagebox
from tkinter import scrolledtext

conn=pymysql.connect(host="localhost",port=3306,
                user="root",password="admin123456",
                database="xtsj",charset="utf8")
cur=conn.cursor()

sql = "select ti_gan,ti_a,ti_b,ti_c,ti_d,ti_da from tiku"
cur.execute(sql)
namelist = cur.fetchall()

answerlist = []
count = 1
list2 = []
score = 0
countf = 0


def testwin():

    global list1  # 存放出过的题目
    global answerlist
    global list2  # 存放错题

    list2 = []  # 存放错题
    score = 0  # 记录分数
    list5=[]

    window = Tk()
    window.title("欢迎使用kk系统！")  # title()  定义这个窗口的标题
    window.geometry("1100x600")  # geometry()  定义窗口的大小
    label = Label(window, font=("隶书", 18), justify=LEFT)
    label.place(x=100, y=50, width=900, height=400)
    var1 = StringVar()
    list1 = set()  # 存放出过的题目
    while len(list1) < 10:
        p = random.choice(namelist)
        q = "\n".join(p)
        list1.add(q)
    list1 = list(list1)
    for i in list1:
        d = list(i).pop()
        answerlist.append(d)
        a=i[:-1]
        list5.append(a)

    num = 0
    label.config(text=list5[num])
    print(list1[num])

    def zuoti():
        nonlocal num
        global score
        if num < len(list5):
            standardnanswer = answerlist[num]  # 获取当前题目的标准答案
            zijianswer = var1.get()
            if zijianswer == standardnanswer:
                print("答题成功", num)
                score += 10
                num += 1
                print(num)
                if num == len(list5):
                    label.config(text="您已完成本轮测试，请点击“完成”来退出本次测试。\n")
                    return None
                label.config(text=list5[num])

            else:
                print("答题错误", num)
                list2.append(list5[num] + "\n\n正确答案是%s\t" % answerlist[num] + "\n\n\n\n")  # 将错题加入list2
                num += 1
                if num == len(list5):
                    label.config(text="您已完成本轮测试，请点击“完成”来退出本次测试。\n")
                    return None
                label.config(text=list5[num])
        # else:
        #     answerlist.clear()

    fra = Frame(window, width=50, height=50)
    fra.place(x=300, y=400)
    frb = Frame(window, width=50, height=50)
    frb.place(x=400, y=400)
    frc = Frame(window, width=50, height=50)
    frc.place(x=500, y=400)
    frd = Frame(window, width=50, height=50)
    frd.place(x=600, y=400)
    radio1 = Radiobutton(fra, text="A", font=("楷体", 20), variable=var1, value="A", command=zuoti)
    radio1.pack()
    radio2 = Radiobutton(frb, text="B", font=("楷体", 20), variable=var1, value="B", command=zuoti)
    radio2.pack()
    radio3 = Radiobutton(frc, text="C", font=("楷体", 20), variable=var1, value="C", command=zuoti)
    radio3.pack()
    radio4 = Radiobutton(frd, text="D", font=("楷体", 20), variable=var1, value="D", command=zuoti)
    radio4.pack()

    def exit():
        window.destroy()
        cuotiwin()

    button1 = Button(window, text="完成", font=("隶书", 18), command=exit)
    button1.place(x=750, y=400, width=100, height=40)
    # button1 = Button(window, text="下一题", font=("隶书", 20), command=zhucewin)
    # button1.place(x=225, y=260, width=150, height=60)
    window.mainloop()

def welwin():
    window = Tk()
    window.title("欢迎来到KK系统！")  # title()  定义这个窗口的标题
    window.geometry("600x400")  # geometry()  定义窗口的大小

    label1 = Label(window, text="你好,欢迎使用KK系统！", font=("隶书", 24))
    label1.place(x=50, y=50, width=500, height=100)

    def aa():
        window.destroy()
        testwin()

    def tex6():
        window.destroy()
        stuwere()

    button1 = Button(window, text="开始做题", font=("隶书", 20), command=aa)
    button1.place(x=225, y=180, width=150, height=60)
    quit = Frame(window)
    quit.place(x=225, y=260, width=150, height=60)
    button2 = Button(quit, text="退    出", font=("隶书", 20), command=tex6)
    button2.place(x=0, y=0, width=150, height=60)
    window.mainloop()


def caidanwin():
    global score
    window = Tk()
    window.title("欢迎使用KK系统！")  # title()  定义这个窗口的标题
    window.geometry("600x400")  # geometry()  定义窗口的大小

    label1 = Label(window, text="欢迎使用KK系统！", font=("隶书", 26))
    label1.place(x=50, y=50, width=500, height=50)

    # button1 = Button(window, text="", font=("隶书", 20), command=cuotiwin)
    # button1.place(x=225, y=160, width=150, height=60)

    def exit1():
        cuotiwin()
        window.destroy()

    def exit():
        welwin()
        window.destroy()

    def exit2():
        window.destroy()
        stuwere()



    button1 = Button(window, text="查看错题", font=("隶书", 20), command=exit1)
    button1.place(x=225, y=160, width=150, height=60)
    button1 = Button(window, text="继续做题", font=("隶书", 20), command=exit)
    button1.place(x=225, y=240, width=150, height=60)
    quit = Frame(window)
    quit.place(x=225, y=320, width=150, height=60)
    button2 = Button(quit, text="退    出", font=("隶书", 20), command=exit2)
    button2.place(x=0, y=0, width=150, height=60)

def cuotiwin():

    global score
    global list2
    a = 0
    var1 = StringVar
    window = Tk()
    window.title("错题APP！")  # title()  定义这个窗口的标题
    window.geometry("1000x500")  # geometry()  定义窗口的大小

    scr = scrolledtext.ScrolledText(window, width=70, height=13, font=("隶书", 18))
    scr.place(x=50, y=50)


    def exit():
        caidanwin()
        window.destroy()
        global score
        global list2
        score = 0
        list2 = []

    button2 = Button(window, text="返     回", font=("隶书", 20), command=exit)
    button2.place(x=700, y=420, width=150, height=60)

    window.mainloop()




def stuwere():
    # 学生登录后界面

    tk = tkinter.Tk()
    tk.title("学生系统APP！")
    tk.geometry("600x600+400+0")


    def exit3():
        tk.destroy()
        welwin()



    def exit8():
        tk.destroy()
        stulog()

    stubar = tkinter.Button(tk, text="在线自测", command=exit3, width=100, bg="gray", font=("楷体", 32))
    stubar.place(x=150, y=50, width=300, height=80)
    stuher = tkinter.Button(tk, text="切换账户", command=exit8, width=100, bg="gray", font=("楷体", 32))
    stuher.place(x=150, y=150, width=300, height=80)

    tk.mainloop()





def stulog():
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

    label = tkinter.Label(tb, textvariable=var1 , width=100, font=("楷体", 25))
    label.place(x=50, y=50, width=500, height=100)

    tb.mainloop()

stulog()
