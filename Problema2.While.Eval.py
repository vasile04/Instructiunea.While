# p=lunile in care temperatura e mai mare de 0 grade sum_neg=suma temperaturilor negative; i=nr de luni din an
# n=lunile in care temperatura e mai mica de 0 grade sum_poz=suma temperaturilor pozitive
i=0
p=0
n=0
sum_neg=0
sum_poz=0
while i<12:
    temp=eval(input('Introdu temperatura din luna respectiva:'))
    if temp>=0:
        p+=1
        sum_poz+=temp
    if temp<=0:
        n+=1
        sum_neg+=n
    i=i+1

if p>0:
    media_poz=float(sum_poz/ p)
    print(f'Media pozitiva este: {round(media_poz, 2)}')

if n>0:
    media_neg=float(sum_neg /2)
    print(f'Media negativa este: {round(media_neg, 2)}')