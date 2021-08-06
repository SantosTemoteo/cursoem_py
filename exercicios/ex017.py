from math import sqrt
catop = float(input('Cateto Oposto: '))
catadj = float(input('Cateto Adjacente: '))
hip = (catop**2)+(catadj**2) # **(1/2)
print('Hipotenusa = {:.2f}'.format(sqrt(hip)))