while True:
    try:
        x=input('Bir sayı girin:')
        if not x:
            break
        y=1/floa(x)
    except ValueError:
        print('geçersiz')
        continue
    except ZeroDivisionError:
        print("Sıfıra bölme")
        continue
    print(y)