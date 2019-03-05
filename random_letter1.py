import random
L=['самовар','самосвал','самокат']
i=0
j=random.randint(0, len(L)-1)
print(j, len(L[j]))
k=random.randint(0, len(L[j]))
while i < len(L[1]):
    b=L[j][k-1]
    c=L[j][:k-1]+'?'+L[j][k:]
    print(c)
    ans=str(input("Введите букву: "))
    if ans == b:
        print('Gracias')
        break
    else:
        print('Try again')

