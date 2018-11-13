import tkinter
from sjtw import rname

app=tkinter.Tk()
app.title("点名APP")
app.config(height=300)
app.config(width=600)


b=tkinter.Button(app,text="随机点名",font=("楷体", 30),command=rname)
b.place(x=50,y=50,height=100,width=500)

app.mainloop()