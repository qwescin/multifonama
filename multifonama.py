# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import requests
import xml.etree.ElementTree as ET
import base64
import os

URL = 'https://sm.megafon.ru/sm/client/routing'
URL_SW = 'https://sm.megafon.ru/sm/client/routing/set'


root = Tk()
root.geometry('250x250+800+300')
root.title("MULTIFONAMA")
root.resizable(False, False)

# icon = """"""         #here app favicon in base64
#icondata= base64.b64decode(icon)           # if u want use favicon, uncomments this block 
#tempFile= "icon.ico"
#iconfile= open(tempFile,"wb")
#iconfile.write(icondata)
#iconfile.close()
#root.wm_iconbitmap(tempFile)
#os.remove(tempFile)


def Check():
    
    login = phone_entry.get()+'@multifon.ru'
    password = password_entry.get()
    data = {'login': login, 'password': password }
    req = requests.get(URL, params=data)                          #если будет ругатссо на ssl, то добавить , verify=False (актуально для py2exe)
    
    tree = ET.fromstring(req.content)
    code = tree.findall('result')
    description = code[0].find('description').text
    result = code[0].find('code').text
    if result == '200':
        route = tree.findall('routing')
        route_type = route[0].text
        if route_type == '0':
            text = u'Телефон'
        elif route_type == '1':
            text = u'МультиФон (SIP)'
        elif route_type == '2':
            text = u'телефон и МультиФон'
            
    elif result == '101':
        text = u'Неверный пароль'
        
    elif result == '404':
        text = u'Номер не найден'
    else:
        text = u'Что-то пошло не так!'
    
    tkMessageBox.showinfo('AZAZA', text)
    
def Switch():
    login = phone_entry.get()+'@multifon.ru'
    password = password_entry.get()
    route_rb = choice.get()
    
    if route_rb == 0:
        tkMessageBox.showinfo(u'ВАРНИНГ!!!', u'Выбери режим маршрутизации!')
        return
    elif route_rb == 1:
        route = '0'
    elif route_rb == 2:
        route = '1'
    elif route_rb == 3:
        route = '2'
    else:
        tkMessageBox.showinfo(u'ВАРНИНГ!!!', u'Что-то пошло не так!')
    
    data = {'login': login, 'password': password, 'routing': route }
    req = requests.get(URL_SW, params=data)
    tree = ET.fromstring(req.content)
    code = tree.findall('result')
    description = code[0].find('description').text
    result = code[0].find('code').text
    
    if result == '200':
        text = u'Переключено'
            
    elif result == '101':
        text = u'Неверный пароль'
        
    elif result == '404':
        text = u'Номер не найден'
    else:
        text = u'Что-то пошло не так!'
    
    tkMessageBox.showinfo('AZAZA', text)
    
    
def Nofreez_check():                                         #указать этот эвент в кнопке, если не охота наблюдать фризы её
    root.after(100, Check)

btn_check = Button(root,                                     #кнопка проверки
             text=u"Проверить",     
             width=11,height=1,    
             bg="white",fg="black", command=Check) 
             
btn_switch = Button(root,                                    #кнопка переключения
             text=u"Переключить",     
             width=11,height=1,    
             bg="white",fg="black", command=Switch) 
             
phone_entry = Entry(root, width=14, borderwidth=2)                          #номер телефона
password_entry = Entry(root, width=14, borderwidth=2 )                       #пароль

label_phone = Label(root, text=u'Номер телефона')                            #лейблы
label_password = Label(root, text=u'Пароль')

choice = IntVar()
rbut_phone = Radiobutton(root, text=u'Телефон', variable=choice, value=1)                #радиобаттоны
rbut_sip = Radiobutton(root, text=u'Мультифон (SIP)', variable=choice, value=2)
rbut_phone_sip = Radiobutton(root, text=u'Телефон и SIP', variable=choice, value=3)

                   
btn_check.place(x=2, y=3)
btn_switch.place(x=2, y=40)
phone_entry.place(x=2, y=80)
label_phone.place(x=100, y=80)
password_entry.place(x=2, y=120)
label_password.place(x=100, y=120)
rbut_phone.place(x=2, y=160)
rbut_sip.place(x=2, y=180)
rbut_phone_sip.place(x=2, y=200)
root.mainloop()
