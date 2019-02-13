film=input("ВВедите название фильма(Пятница, Чемпионы, Пернатая банда) ")
if film=="Пятница":
    date=input("ВВедите дату(сегодня или завтра) ")
    if date=="сегодня":
        time=int(input("ВВедите время сеанса(12, 16, 20) "))
        score=int(input("ВВедите к-во билетов "))
        if time==12:
            if score<20:
                print(250*score)
            else:
                print(250*score*0.8)
        if time==16:
            if score<20:
                print(350*score)
            else:
                print(350*score*0.8)
        if time==20:
            if score<20:
                print(450*score)
            else:
                print(450*score*0.8)     
    if date=="завтра":
        time=int(input("ВВедите время сеанса(12, 16, 20) "))
        score=int(input("ВВедите к-во билетов "))
        if score<20:
                print(250*score*0.95)
        else:
                print(250*score*0.8*0.95)
        if time==16:
            if score<20:
                print(350*score*0.95)
            else:
                print(350*score*0.8*0.95)
        if time==20:
            if score<20:
                print(450*score*0.95)
            else:
                print(450*score*0.8*0.95)  


if film=="Чемпионы":
    date=input("ВВедите дату(сегодня или завтра) ")
    if date=="сегодня":
        time=int(input("ВВедите время сеанса(10, 13, 16) "))
        score=int(input("ВВедите к-во билетов "))
        if time==10:
            if score<20:
                print(250*score)
            else:
                print(250*score*0.8)
        if time==13:
            if score<20:
                print(350*score)
            else:
                print(350*score*0.8)
        if time==16:
            if score<20:
                print(350*score)
            else:
                print(350*score*0.8)     
    if date=="завтра":
        time=int(input("ВВедите время сеанса(10, 13, 16) "))
        score=int(input("ВВедите к-во билетов "))
        if time==10:
            if score<20:
                print(250*score*0.95)
            else:
                print(250*score*0.8*0.95)
        if time==13:
            if score<20:
                print(350*score*0.95)
            else:
                print(350*score*0.8*0.95)
        if time==16:
            if score<20:
                print(350*score*0.95)
            else:
                print(350*score*0.8*0.95)  



if film=="Пернатая банда":
    date=input("ВВедите дату(сегодня или завтра) ")
    if date=="сегодня":
        time=int(input("ВВедите время сеанса(10, 14, 18) "))
        score=int(input("ВВедите к-во билетов "))
        if time==10:
            if score<20:
                print(350*score)
            else:
                print(250*score*0.8)
        if time==14:
            if score<20:
                print(450*score)
            else:
                print(350*score*0.8)
        if time==18:
            if score<20:
                print(450*score)
            else:
                print(450*score*0.8)     
    if date=="завтра":
        time=int(input("ВВедите время сеанса(10, 14, 18) "))
        score=int(input("ВВедите к-во билетов "))
        if time==10:
            if score<20:
                print(350*score*0.95)
            else:
                print(250*score*0.8*0.95)
        if time==14:
            if score<20:
                print(450*score*0.95)
            else:
                print(350*score*0.8*0.95)
        if time==18:
            if score<20:
                print(450*score*0.95)
            else:
                print(450*score*0.8*0.95)  



















































    
