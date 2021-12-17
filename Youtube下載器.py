import tkinter as tk
from typing import Text
from pytube import YouTube

#--主視窗--#
window = tk.Tk()
window.geometry("640x480")
window.title("Youtube下載器")

input_fm = tk.Frame(window, bg='red',width=640,height=120)  #建立Frame
input_fm.pack() #設定排版方法

#--Label--#
lb = tk.Label(input_fm, text = "請輸入Youtube影片網址", bg = 'red', fg= "white",font=("標楷體", 12))
lb.place(rely = 0.25 ,relx=0.5, anchor="center")

#--Entry--#
yt_url = tk.StringVar()
entry = tk.Entry(input_fm,textvariable=yt_url,width=50)
entry.place(rely = 0.5 ,relx = 0.5 ,anchor="center")

#--Button--#
def click_func():
    print("已按")
btn = tk.Button(input_fm,text="下載影片",command = click_func, bg = "#FFD700", fg="Black",font=("標楷體",10))
btn.place(rely=0.5,relx=0.85,anchor="center")


#--下方顯示下載清單區域--#
dload_fm = tk.Frame(window, width=640, height=480-120)
dload_fm.pack()

#--Label--#
lb = tk.Label(dload_fm, text = "下載狀態", fg = 'black',font=("標楷體", 10))
lb.place(rely = 0.25 ,relx=0.5, anchor="center")

#--Listbox--#
listbox = tk.Listbox(dload_fm,width=65,height=15)
listbox.place(relx=0.5,rely=0.5,anchor="center")

#--Scrollbar--#
sbar = tk.Scrollbar(dload_fm)
sbar.place(rely=0.5 , relx=0.87 , anchor="center", relheight= 0.7)

#--List與Scrollbar的連結--#
listbox.config(yscrollcommand= sbar.set)
sbar.config(command= listbox.yview)

#--啟動主視窗--#
window.mainloop()