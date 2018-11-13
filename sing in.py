import socket
import threading
import pymysql
server=socket.socket()
server.bind(('192.168.0.106',8888))
server.listen(100)


conn=pymysql.connect(host="localhost",port=3306,user="root",password="admin123456",database="xtsj",charset="utf8")
cur=conn.cursor()
iplist=[]



def charuser():
    key=input("1.注册    2.登录")
    if key=="1":
        zhuce()
    if key=="2":
        denglu()
    if key!="1"and key!="2":
        print("请输入正确的选项!")
        charuser()

def zhuce():
    pass

def denglu():
    userid=input("请输入学号:")
    username=input("请输入姓名:")
    sql="select userid from student where username=%s"
    row=cur.execute(sql,(username,))
    if row==0:
        print("学号或者姓名有误！")
    else:
        password2,=cur.fetchone()
        if userid!=password2:
            print("学号或者姓名有误！")
        else:
            print("登陆成功！")
            while True:
                key1=input("")
                if key1=="1":
                    run(conn,cur)



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
                    sql2="update checktable set score=score+5 where stu_id=%s"
                    cur.execute(sql2,(id))
                    conn.commit()
                    s.send("success".encode("utf-8"))

while True:
    s,addr=server.accept()
    threading.Thread(target=run,args=(s,addr,)).start()

server.close()