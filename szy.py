import pymysql
from multiprocessing import Pool
import os
import tkinter.messagebox


conn=pymysql.connect(host="localhost",port=3306,
                     user="root",password="admin123456",
                     database="xtsj",charset="utf8")

cur=conn.cursor()

def fileupload(name):
    pathfrom = r"D:\kkt" + "\\" + name
    pathto = r"D:\老师收作业文件" + "\\" + name
    filefrom = open(pathfrom, "rb")
    fileto = open(pathto, "wb")
    fileto.write(filefrom.read())
    fileto.close()
    filefrom.close()
'''
    filename=tkinter.filedialog.askopenfilename(title="jkt",
                                                filetypes=[('Excle Files', '*.xls')])
    file=xlrd.open_workbook(filename)
    sheet1=file.sheet_by_index(0)
    for index in range(0,sheet1.nrows):
        row=sheet1.row(index)

        sql="insert into testdb values (null,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,(str(row[0].value),str(row[1].value),str(row[2].value),
                         str(row[3].value),str(row[4].value),str(row[5].value)))
        conn.commit()
    tkinter.messagebox.showinfo("恭喜","导入成功")
'''

app=tkinter.Tk()
app.config(height=260)
app.config(width=360)

b=tkinter.Button(app,text="导入文件",command=fileupload)
b.place(x=40,y=40,height=80,width=100)
tkinter.mainloop()
if __name__=="__main__":
    pool=Pool()
    namelist=os.listdir(r"D:\kkt")
    for name in namelist:
        pool.apply_async(func=fileupload,args=(name,))
    pool.close()
    pool.join()
