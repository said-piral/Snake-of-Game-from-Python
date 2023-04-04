#!/usr/bin/env python
# coding: utf-8

# In[7]:


import turtle
import time
import random

wn = turtle.Screen()  # ekranı oluştur
wn.title("Yılan Oyunu")
wn.bgcolor("green")
wn.setup(width=600, height=600)

# yılan kafası
kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("black")
kafa.penup()
kafa.goto(0, 0)
kafa.direction = "stop"

# yılan yemeği
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.goto(0, 100)

yilan_parcalari = [kafa]
skor = 0
en_yuksek_skor = 0

skor_yazisi = turtle.Turtle()
skor_yazisi.speed(0)
skor_yazisi.color("white")
skor_yazisi.penup()
skor_yazisi.hideturtle()
skor_yazisi.goto(0, 260)
skor_yazisi.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

# Yılanın hareket etmesi
def yukari():
    if kafa.direction != "asagi":
        kafa.direction = "yukari"
def asagi():
    if kafa.direction != "yukari":
        kafa.direction = "asagi"
def sola():
    if kafa.direction != "sag":
        kafa.direction = "sola"
def saga():
    if kafa.direction != "sola":
        kafa.direction = "sag"

def hareket_et():
    if kafa.direction == "yukari":
        y = kafa.ycor()
        kafa.sety(y + 20)

    if kafa.direction == "asagi":
        y = kafa.ycor()
        kafa.sety(y - 20)

    if kafa.direction == "sola":
        x = kafa.xcor()
        kafa.setx(x - 20)

    if kafa.direction == "sag":
        x = kafa.xcor()
        kafa.setx(x + 20)

    # Yılanın vücudu takip eder
    for index in range(len(yilan_parcalari)-1, 0, -1):
        x = yilan_parcalari[index-1].xcor()
        y = yilan_parcalari[index-1].ycor()
        yilan_parcalari[index].goto(x, y)

    if len(yilan_parcalari) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        yilan_parcalari[0].goto(x, y)

    skor_yazisi.clear()
    skor_yazisi.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

# Tuşlara bağlanma
wn.listen()
wn.onkeypress(yukari, "Up")
wn.onkeypress(asagi, "Down")
wn.onkeypress(sola, "Left")
wn.onkeypress(saga, "Right")


# Ana oyun döngüsü
while True:
    wn.update()

    # Yılanın sınırları aşması durumu
    if yilan_parcalari[0].xcor() == yemek.xcor() and yilan_parcalari[0].ycor() == yemek.ycor():
        yemek_x = random.randint(-290, 290)
        yemek_y = random.randint(-290, 290)
        yemek.goto(yemek_x, yemek_y)
        yeni_parca = turtle.Turtle()
        yeni_parca.speed(0)
        yeni_parca.shape("square")
        yeni_parca.color("grey")
        yeni_parca.penup()
        yilan_parcalari.append(yeni_parca)
    
    hareket_et() # yılanı hareket ettir

    # Yılanın sınırları aşması durumu
if yilan_parcalari[0].xcor() == yemek.xcor() and yilan_parcalari[0].ycor() == yemek.ycor():
    yemek_x = random.randint(-290, 290)
    yemek_y = random.randint(-290, 290)
    yemek.goto(yemek_x, yemek_y)
    yeni_parca = turtle.Turtle()
    yeni_parca.speed(0)
    yeni_parca.shape("square")
    yeni_parca.color("grey")
    yeni_parca.penup()
    yilan_parcalari.append(yeni_parca)
if yilan_parcalari[0].xcor() == yemek.xcor() and yilan_parcalari[0].ycor() == yemek.ycor():
    yemek_x = random.randint(-290, 290)
    yemek_y = random.randint(-290, 290)
    yemek.goto(yemek_x, yemek_y)
    yeni_parca = turtle.Turtle()
    yeni_parca.speed(0)
    yeni_parca.shape("square")
    yeni_parca.color("grey")
    yeni_parca.penup()
    yilan_parcalari.append(yeni_parca)


# In[ ]:




