"""
در این برنامه میخواهیم نمودار سینوسی مدار الکتریکی را نمایش دهیم
"""
import numpy as n
import matplotlib.pyplot as p 
#دریافت ورودی از کاربر
damane = float(input("enter a damane: "))
zavie = float(input("entaer zavie just degrees: "))
frequnce = float(input("enter frequnce : "))

#تبدیل درجه به رادیان
zavie = n.radians(zavie)

#متغییر زمان
start_t = 0
stop_t = 2*n.pi
T_step = 1000 
time_all = n.linspace(start_t, stop_t, T_step) #روی نمودار بخش x

#محاسبات فورمولی
y = damane*n.sin(frequnce*time_all+zavie)

#رسم نمودار
p.plot(time_all,y)
p.xlabel("Time")
p.ylabel("formola")
p.title("nemodar")
p.show()