import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import sys

def resource_path(relative_path):
  base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
  return os.path.join(base_path, relative_path)

def calculate():
  result1.delete(0, len(result1.get()))
  result2.delete(0, len(result2.get()))
  result3.delete(0, len(result3.get()))
  result4.delete(0, len(result4.get()))
  #전폭기
  if len(ent1_a.get()) == 0:
    first_a1 = 0
    ent1_a.insert(0, 0)
  else:
    first_a1 = float(ent1_a.get())
  if len(ent2_a.get()) == 0:
    first_a2 = 0
    ent2_a.insert(0, 0)
  else:
    first_a2 = float(ent2_a.get())
  if len(ent3_a.get()) == 0:
    first_a3 = 0
    ent3_a.insert(0, 0)
  else:
    first_a3 = float(ent3_a.get())
  if len(ent4_a.get()) == 0:
    first_a4 = 0
    ent4_a.insert(0, 0)
  else:
    first_a4 = float(ent4_a.get())
  if len(ent5_a.get()) == 0:
    first_a5 = 0
    ent5_a.insert(0, 0)
  else:
    first_a5 = float(ent5_a.get())
  #전폭기 계산
  res1 = (first_a2 - first_a1)*1.276264237
  res2 = (first_a3 - first_a1)*1.276264237
  res3 = (first_a4 - first_a1)*1.276264237
  res4 = (first_a5 - first_a1)*1.276264237

  result1.insert(0, res1)
  result2.insert(0, res2)
  result3.insert(0, res3)
  result4.insert(0, res4)


def retry():
  ent1_a.delete(0, len(ent1_a.get()))
  ent2_a.delete(0, len(ent2_a.get()))
  ent3_a.delete(0, len(ent3_a.get()))
  ent4_a.delete(0, len(ent4_a.get()))
  ent5_a.delete(0, len(ent5_a.get()))
  result1.delete(0, len(result1.get()))
  result2.delete(0, len(result2.get()))
  result3.delete(0, len(result3.get()))
  result4.delete(0, len(result4.get()))

root = Tk()
root.title("실험실 NH4 계산용")
root.geometry('750x250')
root.resizable(width = False, height = False)
try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())

lb_text1 = ttk.Label(root, text = "NH4 계산기",  foreground= 'yellow green', font = 'helvetica 16 bold')
lb_text2 = ttk.Label(root, text = "")
lb_text3 = ttk.Label(root, text = "")
lb_text1.grid(row=0, column = 0)
lb_text2.grid(row=4)
lb_text3.grid(row=8)
# 입력창 위에 글자
lb0_a = ttk.Label(root, text = '')
lb1_a = ttk.Label(root, text = 'blk적정량')
lb2_a = ttk.Label(root, text = '방류수 적정량')
lb3_a = ttk.Label(root, text = '막분리 적정량')
lb4_a = ttk.Label(root, text = '전폭기 적정량')
lb5_a = ttk.Label(root, text = '유입량 적정량')
lb6_a = ttk.Label(root, text = 'a(mL) = 시료적정량\nb(mL) = 증류수\nf(역가) = 0.9111617312\nN(노르말농도) = 0.005\nV(ml) = 50')
lb0_a.grid(row=2, column = 0)
lb1_a.grid(row=3, column = 0)
lb2_a.grid(row=3, column = 1)
lb3_a.grid(row=3, column = 2)
lb4_a.grid(row=3, column = 3)
lb5_a.grid(row=3, column = 4)
lb6_a.grid(row=9, column = 2)


ent1_a = ttk.Entry(root)
ent2_a = ttk.Entry(root)
ent3_a = ttk.Entry(root)
ent4_a = ttk.Entry(root)
ent5_a = ttk.Entry(root)
ent1_a.grid(row=4, column=0)
ent2_a.grid(row=4, column=1)
ent3_a.grid(row=4, column=2)
ent4_a.grid(row=4, column=3)
ent5_a.grid(row=4, column=4)


lbra1 = ttk.Label(root, text = '')
lbra2 = ttk.Label(root, text = '결과값')
image_path = resource_path("exll.png")

photo = PhotoImage(file= image_path)
photo = photo.subsample(4)
lbra3 = Label(root, image=photo)
lbra3.place(x = 20, y = 140)

lbra1.grid(row=7, column=0)
lbra2.grid(row=8, column=0)


result1 = ttk.Entry(root)
result2 = ttk.Entry(root)
result3 = ttk.Entry(root)
result4 = ttk.Entry(root)

result1.grid(row=8, column=1)
result2.grid(row=8, column=2)
result3.grid(row=8, column=3)
result4.grid(row=8, column=4)

b1 = Button(root, text = "계산하기", command=calculate)
b2 = Button(root, text = "다시하기", command=retry)
b1.place(x = 280, y = 210)
b2.place(x = 400, y = 210)

root.mainloop()