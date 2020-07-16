from tkinter import *
import tkinter as tk
import requests
import json

root=Tk()
root.title('wheather report')
root.configure(background='red')
root.geometry('300x200')


def search():
    a=entry.get()
    api_req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+a+'&APPID=da739875a20418560256900f213720d8')
    api = json.loads(api_req.content)

    x = api['main']['temp']-273
    y = api['main']['humidity']

    humidity = Label(root,text='humidity : '+str(api['main']['humidity']))
    temp = Label(root,text='temperature : '+str(api['main']['temp']-273))
    place = Label(root,text='place : '+(api['name']))
    humidity.grid(row=3,column=0,padx=10,pady=10)
    temp.grid(row=2,column=0,padx=10,pady=10)
    place.grid(row=1,column=0,padx=10,pady=10)

var=StringVar

entry = Entry(root,text=var)
entry.grid(row=0,column=0,padx=20,pady=20)

search = Button(text='search',bg='snow',fg='black',activebackground='yellow',command=search)
search.grid(row=0,column=1,padx=20,pady=20)

root.mainloop()
