import math as mt
r=input("digite el valor de la distancia r:")
r=float(r)
angulo=input("digite el valor del angulo:")
angulo=float(angulo)
a=(mt.pi*angulo)/180
z=input("digite el valor de z:")
z=float(z)
print("valor de la coordenada x es:")
x=r*(mt.cos(a))
print(x)
print("valor de la coordenada y es:")
y=r*(mt.sin(a))
print(y)
print("valor de la coordenada z es:")
print(z)
