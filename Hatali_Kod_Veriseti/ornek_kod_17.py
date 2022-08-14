def faktoriyeAl(sayi):
    s=1
    if (sayi==0 or sayi==1):
        s=1
    elif sayi>1:
        for i in range(1, sayi+1, 1):
            s*=i
    else: s=-1
 sonuc = faktoriyeAl(5)
     
