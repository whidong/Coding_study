import tkinter as tk
from tkinter import ttk
from tkinter import *

def calculate():
  ent_rass.delete(0, len(ent_rass.get()))
  ent_ravss.delete(0, len(ent_ravss.get()))
  ent_rmss.delete(0, len(ent_rmss.get()))
  ent_rmvss.delete(0, len(ent_rmvss.get()))
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
    dry_a1 = 0
    ent4_a.insert(0, 0)
  else:
    dry_a1 = float(ent4_a.get())
  if len(ent5_a.get()) == 0:
    dry_a2 = 0
    ent5_a.insert(0, 0)
  else:
    dry_a2 = float(ent5_a.get())
  if len(ent6_a.get()) == 0:
    dry_a3 = 0
    ent6_a.insert(0, 0)
  else:
    dry_a3 = float(ent6_a.get())
  if len(ent7_a.get()) == 0:
    burn_a1 = 0
    ent7_a.insert(0, 0)
  else:
    burn_a1 = float(ent7_a.get())
  if len(ent8_a.get()) == 0:
    burn_a2 = 0
    ent8_a.insert(0, 0)
  else:
    burn_a2 = float(ent8_a.get())
  if len(ent9_a.get()) == 0:
    burn_a3 = 0
    ent9_a.insert(0, 0)
  else:
    burn_a3 = float(ent9_a.get())
  #막분리
  if len(ent1_m.get()) == 0:
    first_m1 = 0
    ent1_m.insert(0, 0)
  else:
    first_m1 = float(ent1_m.get())
  if len(ent2_m.get()) == 0:
    first_m2 = 0
    ent2_m.insert(0, 0)
  else:
    first_m2 = float(ent2_m.get())
  if len(ent3_m.get()) == 0:
    first_m3 = 0
    ent3_m.insert(0, 0)
  else:
    first_m3 = float(ent3_m.get())
  if len(ent4_m.get()) == 0:
    dry_m1 = 0
    ent4_m.insert(0, 0)
  else:
    dry_m1 = float(ent4_m.get())
  if len(ent5_m.get()) == 0:
    dry_m2 = 0
    ent5_m.insert(0, 0)
  else:
    dry_m2 = float(ent5_m.get())
  if len(ent6_m.get()) == 0:
    dry_m3 = 0
    ent6_m.insert(0, 0)
  else:
    dry_m3 = float(ent6_m.get())
  if len(ent7_m.get()) == 0:
    burn_m1 = 0
    ent7_m.insert(0, 0)
  else:
    burn_m1 = float(ent7_m.get())
  if len(ent8_m.get()) == 0:
    burn_m2 = 0
    ent8_m.insert(0, 0)
  else:
    burn_m2 = float(ent8_m.get())
  if len(ent9_m.get()) == 0:
    burn_m3 = 0
    ent9_m.insert(0, 0)
  else:
    burn_m3 = float(ent9_m.get())
  if len(inject_vi.get()) == 0:
    inject_w = 10
    inject_vi.insert(0, 10)
  else:
    inject_w = float(inject_vi.get())
  #전폭기 계산
  ssa1 = (dry_a1-first_a1)/inject_w*(10**6)
  ssa2 = (dry_a2-first_a2)/inject_w*(10**6)
  ssa3 = (dry_a3-first_a3)/inject_w*(10**6)
  vssa1 = (dry_a1-burn_a1)/inject_w*(10**6)
  vssa2 = (dry_a2-burn_a2)/inject_w*(10**6)
  vssa3 = (dry_a3-burn_a3)/inject_w*(10**6)
  #막분리 계산
  ssm1 = (dry_m1-first_m1)/inject_w*(10**6)
  ssm2 = (dry_m2-first_m2)/inject_w*(10**6)
  ssm3 = (dry_m3-first_m3)/inject_w*(10**6)
  vssm1 = (dry_m1-burn_m1)/inject_w*(10**6)
  vssm2 = (dry_m2-burn_m2)/inject_w*(10**6)
  vssm3 = (dry_m3-burn_m3)/inject_w*(10**6)

  a_ss_average1 = (ssa1+ssa2+ssa3)/3
  a_vss_average1 = (vssa1+vssa2+vssa3)/3
  m_ss_average2 = (ssm1+ssm2+ssm3)/3
  m_vss_average2 = (vssm1+vssm2+vssm3)/3
  ent_rass.insert(0, a_ss_average1)
  ent_ravss.insert(0, a_vss_average1)
  ent_rmss.insert(0, m_ss_average2)
  ent_rmvss.insert(0, m_vss_average2)


def retry():
  ent1_a.delete(0, len(ent1_a.get()))
  ent2_a.delete(0, len(ent2_a.get()))
  ent3_a.delete(0, len(ent3_a.get()))
  ent4_a.delete(0, len(ent4_a.get()))
  ent5_a.delete(0, len(ent5_a.get()))
  ent6_a.delete(0, len(ent6_a.get()))
  ent7_a.delete(0, len(ent7_a.get()))
  ent8_a.delete(0, len(ent8_a.get()))
  ent9_a.delete(0, len(ent9_a.get()))

  ent1_m.delete(0, len(ent1_m.get()))
  ent2_m.delete(0, len(ent2_m.get()))
  ent3_m.delete(0, len(ent3_m.get()))
  ent4_m.delete(0, len(ent4_m.get()))
  ent5_m.delete(0, len(ent5_m.get()))
  ent6_m.delete(0, len(ent6_m.get()))
  ent7_m.delete(0, len(ent7_m.get()))
  ent8_m.delete(0, len(ent8_m.get()))
  ent9_m.delete(0, len(ent9_m.get()))

  inject_vi.delete(0, len(inject_vi.get()))

  ent_rass.delete(0, len(ent_rass.get()))
  ent_ravss.delete(0, len(ent_ravss.get()))
  ent_rmss.delete(0, len(ent_rmss.get()))
  ent_rmvss.delete(0, len(ent_rmvss.get()))

root = Tk()
root.title("SS VSS 평균값계산기")
root.geometry('600x500')
root.resizable(width = False, height = False)

lb_text1 = ttk.Label(root, text = "SS VSS 계산기",  foreground= 'cyan', font = 'helvetica 16 bold')
lb_text2 = ttk.Label(root, text = "")
lb_text3 = ttk.Label(root, text = "")
lb_text1.grid(row=0, column = 0)
lb_text2.grid(row=4)
lb_text3.grid(row=8)

lb1_a = ttk.Label(root, text = '처음무지개_전폭기1번')
lb2_a = ttk.Label(root, text = '처음무지개_전폭기2번')
lb3_a = ttk.Label(root, text = '처음무지개_전폭기3번')
lb4_a = ttk.Label(root, text = '건조무지개_전폭기1번')
lb5_a = ttk.Label(root, text = '건조무지개_전폭기2번')
lb6_a = ttk.Label(root, text = '건조무지개_전폭기3번')
lb7_a = ttk.Label(root, text = '태운무지개_전폭기1번')
lb8_a = ttk.Label(root, text = '태운무지개_전폭기2번')
lb9_a = ttk.Label(root, text = '태운무지개_전폭기3번')

lb1_a.grid(row=1, column = 0)
lb2_a.grid(row=2, column = 0)
lb3_a.grid(row=3, column = 0)
lb4_a.grid(row=5, column = 0)
lb5_a.grid(row=6, column = 0)
lb6_a.grid(row=7, column = 0)
lb7_a.grid(row=9, column = 0)
lb8_a.grid(row=10, column = 0)
lb9_a.grid(row=11, column = 0)


lb1_m = ttk.Label(root, text = '처음무지개_막분리1번')
lb2_m = ttk.Label(root, text = '처음무지개_막분리2번')
lb3_m = ttk.Label(root, text = '처음무지개_막분리3번')
lb4_m = ttk.Label(root, text = '건조무지개_막분리1번')
lb5_m = ttk.Label(root, text = '건조무지개_막분리2번')
lb6_m = ttk.Label(root, text = '건조무지개_막분리3번')
lb7_m = ttk.Label(root, text = '태운무지개_막분리1번')
lb8_m = ttk.Label(root, text = '태운무지개_막분리2번')
lb9_m = ttk.Label(root, text = '태운무지개_막분리3번')
lb1_m.grid(row=1, column = 2)
lb2_m.grid(row=2, column = 2)
lb3_m.grid(row=3, column = 2)
lb4_m.grid(row=5, column = 2)
lb5_m.grid(row=6, column = 2)
lb6_m.grid(row=7, column = 2)
lb7_m.grid(row=9, column = 2)
lb8_m.grid(row=10, column = 2)
lb9_m.grid(row=11, column = 2)

ent1_a = ttk.Entry(root)
ent2_a = ttk.Entry(root)
ent3_a = ttk.Entry(root)
ent4_a = ttk.Entry(root)
ent5_a = ttk.Entry(root)
ent6_a = ttk.Entry(root)
ent7_a = ttk.Entry(root)
ent8_a = ttk.Entry(root)
ent9_a = ttk.Entry(root)
ent1_a.grid(row=1, column=1)
ent2_a.grid(row=2, column=1)
ent3_a.grid(row=3, column=1)
ent4_a.grid(row=5, column=1)
ent5_a.grid(row=6, column=1)
ent6_a.grid(row=7, column=1)
ent7_a.grid(row=9, column=1)
ent8_a.grid(row=10, column=1)
ent9_a.grid(row=11, column=1)

ent1_m = ttk.Entry(root)
ent2_m = ttk.Entry(root)
ent3_m = ttk.Entry(root)
ent4_m = ttk.Entry(root)
ent5_m = ttk.Entry(root)
ent6_m = ttk.Entry(root)
ent7_m = ttk.Entry(root)
ent8_m = ttk.Entry(root)
ent9_m = ttk.Entry(root)
ent1_m.grid(row=1, column=3)
ent2_m.grid(row=2, column=3)
ent3_m.grid(row=3, column=3)
ent4_m.grid(row=5, column=3)
ent5_m.grid(row=6, column=3)
ent6_m.grid(row=7, column=3)
ent7_m.grid(row=9, column=3)
ent8_m.grid(row=10, column=3)
ent9_m.grid(row=11, column=3)

lbra1 = ttk.Label(root, text = '전폭기ss :')
lbra2 = ttk.Label(root, text = '전폭기vss :')
lbrm1 = ttk.Label(root, text = '막분리ss :')
lbrm2 = ttk.Label(root, text = '막분리vss :')
lbra1.place(x=5, y=320)
lbra2.place(x=5, y=370)
lbrm1.place(x=250, y=320)
lbrm2.place(x=250, y=370)

ent_rass =  ttk.Entry(root)
ent_ravss = ttk.Entry(root)
ent_rmss = ttk.Entry(root)
ent_rmvss = ttk.Entry(root)
ent_rass.place(x=65, y=320)
ent_ravss.place(x=65, y=370)
ent_rmss.place(x=315, y=320)
ent_rmvss.place(x=315, y=370)

text_a = ttk.Label(root, text = '{(건조무지개-처음무지개)/주입량}x10^6 mg/L')
text_a.place(x=20, y=280)
inject_v = ttk.Label(root, text = '주입량 :')
inject_v.place(x=300, y=280)
inject_ml = ttk.Label(root, text = 'ml')
inject_ml.place(x=500, y=280)
inject_vi = ttk.Entry(root)
inject_vi.place(x=350, y=280)

scales1 =  ttk.Label(root, text = 'mg/L')
scales2 = ttk.Label(root, text = 'mg/L')
scales3 = ttk.Label(root, text = 'mg/L')
scales4 = ttk.Label(root, text = 'mg/L')
scales1.place(x=215, y=320)
scales2.place(x=215, y=370)
scales3.place(x=460, y=320)
scales4.place(x=460, y=370)

b1 = Button(root, text = "계산하기", command=calculate)
b2 = Button(root, text = "다시하기", command=retry)
b1.place(x = 100, y = 420)
b2.place(x = 300, y = 420)

root.mainloop()