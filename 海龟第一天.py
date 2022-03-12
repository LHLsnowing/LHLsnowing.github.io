# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:31:17 2021

@author: Mr.Liu
"""

import turtle as t
t.screensize(2960,1600)
t.speed(10)
t.pensize(5)
t.shape("turtle")
t.color("yellow","red") #画笔色 画笔填充色
t.begin_fill()
i=1
t.setheading(120)   #转角度
while i<10:
    t.pensize(i)
    t.fd(200)
    t.rt(144)
    i+=1
t.end_fill()
t.penup()
t.goto(-150,-150)
t.color("violet")
t.write("中国红！",font=("Arial",40,'normal'))



t.done()
    