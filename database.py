import pymysql


conn=pymysql.connect(host="localhost",port=3306,user="root",
                     password="admin123456",database="xtsj",charset="utf8")
cur=conn.cursor()
try:
    sql="create table student(" \
        "stu_id int(20) primary key," \
        "stu_name varchar(30)," \
        "stu_sex char(20)," \
        "stu_age char(20)," \
        "stu_dpt char(20))";

    sql="create table teacher(" \
        "tea_id int(20) primary key," \
        "tea_name varchar(30),"\
        "tea_dpt char(20))";
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
except:
    conn.rollback()
    conn.close()
'''


'''
conn=pymysql.connect(host="localhost",port=3306,user="root",
                     password="admin123456",database="xtsj",charset="utf8")
cur=conn.cursor()
try:
    sql="create table teacher(" \
        "tea_id int(20) primary key," \
        "tea_name varchar(30),"\
        "tea_dpt char(20))";
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
except:
    conn.rollback()
    conn.close()
'''


'''
conn=pymysql.connect(host="localhost",port=3306,user="root",
                     password="admin123456",database="xtsj",charset="utf8")
cur=conn.cursor()
try:
    sql="insert into student values('10001','蔡明伟','男',17,'y1003')," \
        "('10002','李小莲','女',15,'y1002')," \
        "('10003','哈德','男',19,'y1004')," \
        "('10004','可欣','女',18,'y1003')," \
        "('10005','大鹏','男',20,'y1003')," \
        "('10006','小翠','女',16,'y1002')," \
        "('10007','李浩','男',19,'y1001')," \
        "('10008','魏雨','女',18,'y1002')," \
        "('10009','黄媛','女',19,'y1004')," \
        "('10010','石白','男',22,'y1001')," \
        "('10011','元芳','女',19,'y1001')," \
        "('10012','马克','男',20,'y1004')";

    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
except:
    conn.rollback()
    conn.close()
'''


'''
conn=pymysql.connect(host="localhost",port=3306,user="root",
                     password="admin123456",database="xtsj",charset="utf8")
cur=conn.cursor()
try:
    sql="insert into teacher values('9001','张老师','y1002')," \
        "('9002','轩老师','y1001')," \
        "('9003','李老师','y1004')," \
        "('9004','毛老师','y1003')";

    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
except:
    conn.rollback()
    conn.close()
