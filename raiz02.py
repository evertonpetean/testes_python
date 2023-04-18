import math
print('Equação do 2 grau da forma: ax^2+bx+c')
a=int(input('coeficiente a: '))
if a==0:
    print('Se a =0, não é equação de segundo grau.')
else:
    b=int(input('coeficiente b: '))
    c=int(input('coeficiente c: '))
    delta=b*b-(4*a*c)
    if delta<0:
        print('nao existem soluçoes reais!')
    elif delta==0:
        raiz=-b/(2*a)
        print('delta=0, a equação tem uma unica solução! x=',raiz)
    else:
        raiz1=(-b+math.sqrt(delta))/(2*a)
        raiz2=(-b+math.sqrt(delta))/(2*a)
        print('X1:',raiz1, 'e X2 :',raiz2)
        

        
