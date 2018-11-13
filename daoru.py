import pymysql
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import xlrd

conn=pymysql.connect(host="localhost",port=3306,
                     user="root",password="admin123456",
                     database="xtsj",charset="utf8")
cur=conn.cursor()

def fileupload():
    filename=tkinter.filedialog.askopenfilename(title="请选择要导入的文件",
                                                filetypes=[('Excle Files', '*.xls')])
    file=xlrd.open_workbook(filename)
    sheet1=file.sheet_by_index(0)
    for index in range(0,sheet1.nrows):
        row=sheet1.row(index)
        sql="insert into tiku values (null,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,(str(row[0].value),str(row[1].value),str(row[2].value),
                         str(row[3].value),str(row[4].value),str(row[5].value),
                         str(row[6].value)))
        conn.commit()
    tkinter.messagebox.showinfo("恭喜","导入成功")

app=tkinter.Tk()
app.config(height=260)
app.config(width=360)


b=tkinter.Button(app,text="导入文件",command=fileupload)
b.place(x=40,y=40,height=80,width=100)
tkinter.mainloop()