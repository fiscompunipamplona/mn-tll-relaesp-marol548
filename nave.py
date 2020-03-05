import math as mt
x= float(input("ingrese el valor de la distancia en años luz:"))
v= float(input("ingrese el valor de la velocidad de la nave en fraccion de c(m/s):"))
x1=x*9.461e+15
t=x1/v
print("tiempo desde la tierra en segundos t:",t ) # s
c=3e8 # m/s
gamma=mt.sqrt(1-v**2)
print("el valor de gamma es..",gamma)
t1= gamma*(t-(v*x)/c)
print("el valor del tiempo desde la nave es..",t1)
