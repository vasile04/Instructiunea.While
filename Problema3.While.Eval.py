x=0
suma=0
while x%2==0 or (x%2!=0) and (x%3!=0):
    if x%2==0:
        suma+=x

    x=eval(input('Introdu numarul:'))

print('Suma numerelor pare este:', suma)