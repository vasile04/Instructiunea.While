s=0
p=1
nr=1
n=eval(input("n= "))
while nr<=n:
    s+=nr
    p*=nr
    nr+=1
    
print("Suma= ",s)
print("Produs= ",p)
print("Media aritmetica= ",s/n)
