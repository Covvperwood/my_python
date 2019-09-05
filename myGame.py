##class Cat:
##    def bark(self):
##        print("Meow", self.color)
##
##myCat=Cat()
##myCat.weight=20
##myCat.color="mixed"
##myCat.name="Matroskin"
##
##
##myCat.bark()
##class Cat:
##    pass
##my_сat1 = Cat()
##my_сat1.set_name("Котик")
##my_сat1.gaming()
##my_сat1.meow()
##my_сat1.eating()

##class Car:  
##    def start(self):
##        # переменная внутри метода:
##        message = "Двигатель заведен" 
##        return message
##    def webasta(self):
##        # переменная внутри метода:
##        message2 = "Двигатель прогрет"
##        return message2
##    def __init__(self):
##        self.maxspeed = 200
## 
##
##
##car = Car()  
### print(car.message)
### AttributeError: 'Car' object has no attribute 'message'
### не можем обратиться к переменной внутри метода
##
##print(car.start()) # Car.start(car)
##print(car.webasta())
##print(car.maxspeed)

from random import *

class Killer:
    def start(self):
        message="ready to kill"
        return message
    def kill(self, target):
        onechance=randrange(3)
        if onechance == 0: #good shoot
            target.hp = 0
        if onechance == 1: #middle shoot
            target.hp = (target.hp)/2
        #else bad shoot
    def __init__(self):
        self.placed=(5,5)
        self.weapon="sniper riffle"
        self.power=8
        self.hp=100
        self.money=1000
    def escape(self):
        onechance=randrange(2)
        if onechance == 0:
            self.placed=(10,10)
        else: self.placed=(0,0)
    def changeweapon(self, new):
        self.weapon = new
    def growup(self):
        self.power+=1
    def increasehp(self, num):
        self.hp+=num
    def increasemoney(self, num):
        self.money+=num    
        
        
            
class Jurii:
    def __init__(self):
        self.hp = 100


class Guard1:
    def __init__(self):
        self.hp = 100

class Guard2:
    def __init__(self):
        self.hp = 100

class Guard3:
    def __init__(self):
        self.hp = 100

class Guard4:
    def __init__(self):
        self.hp = 100        

        
print("PART I: GOT HIM")    

guard1=Guard1()
guard2=Guard2()
guard3=Guard3()
guard4=Guard4()

killer=Killer()
jurii=Jurii()
killer.kill(jurii)

input("press 1 to shoot\n")
if jurii.hp == 0:
    print("jurii died")
print(jurii.hp, "hp of Jurii")

input("press 1 to escape\n")
killer.escape()
if killer.placed==(10,10):
    print(killer.placed, "killer in home")
if killer.placed==(0,0):
    print(killer.placed, "killer in prison")
    killer.power-=3

##if (jurii.hp != 0 and killer.placed != (0,0)):
##    print("Choose weapon \n", "1 is pistol with silencer \n", "2 is grenade launcher \n", "3 is radio bomb")
##    a=input("Your choice: ")
##    if a=="1":
##        killer.changeweapon("pistol with silencer")
##    if a=="2":
##        killer.changeweapon("grenade launcher")
##    if a=="3":
##        killer.changeweapon("radio bomb")

       
if killer.placed == (0,0):
    print("Chose your way: \n", "1 Try to escape from prison \n", "2 Call your layer")
    b=input("Your choice ")
    if b=="1":
        if killer.power<9:
            print("You need to grow up your power for escape press any key to do it")              
            print("If you want to grow up power press g, until value of power rise 9 \n")
            while killer.power < 9:
                if input("press G: ") == "g":
                    killer.growup()    
        killer.increasehp(50)
    if b == "2":
        if jurii.hp >= 100:
            killer.placed==(10,10)
            print("your layer help you to get out, be afraid of jurii's killers")
        if 50 <= jurii.hp < 100:
            print("killer had been killed on the prison's exit")
            killer.increasehp(-100)
        if 0 <= jurii.hp < 50:
            print("no one layer can help you because you killed a man, go to gym")
            print("press ""g"" to grow up power")
            while killer.power < 9:
                if input("press G: ") == "g":
                    killer.growup()
            killer.increasehp(50)

if killer.hp<=0:
    print("GAME OVER")
else:
     print("Choose weapon \n", "1 is pistol with silencer \n", "2 is grenade launcher \n", "3 is radio bomb")
     a=input("Your choice: ")
     if a=="1":
         killer.changeweapon("pistol with silencer")
     if a=="2":
         killer.changeweapon("grenade launcher")
     if a=="3":
         killer.changeweapon("radio bomb")
     print("Do you want to buy bulletproof vest.It increase your hp on 50, now you have:", killer.hp, " and cost 300$", "now you have:", killer.money, "\n 1 - Yes \n 2 - No")
     a3=input("your choice: ")
     if a3=="1":
         killer.increasehp(50)
         killer.increasemoney(-300)
                     
print("killer's weapom is",killer.weapon, "\nkiller's hp is", killer.hp, "\nkiller's money is", killer.money, "\n\n\n\n")        
            
print("PART II: DEVIL'S DOGS ON A TAIL")

print("phone ring")
input("press any key to pick up phone\n")
print("-hi, jurii's mans is looking for you, kill them all")
print("-who are you?")
print("...\n\n")

print("you heard steps on the stair")
a3=input("0 - go to bed \n1 - take ak-47\n")
if a3=="0":
    print("you had been killed in a dream")
    killer.hp=0
else:
    guard1.hp=randrange(5)
    guard2.hp=randrange(10)
    guard3.hp=randrange(15)
    guard4.hp=randrange(20)
print("you killed first and second guards")
if guard1.hp==0:
    print("and third too")
elif guard1.hp<10:
    print("third on the edge of a life")

if guard2.hp==0:
    print("number 4 died")
elif guard2.hp<10:
    print("number 4 on the edge of a life")

if guard3.hp==0:
    print("number 5 died")
elif guard3.hp<10:
    print("number 5 on the edge of a life")    

if guard4.hp==0:
    print("number 6 died")
elif guard4.hp<10:
    print("number 6 on the edge of a life\n")    

print("press 1 to shoot by your weapon immediately\npress 2 to check died guard's pulse\npress 3 to change your weapon")
c=input("Choose\n")

if (c=="1" and killer.weapon=="pistol with silencer"):
    print("You finished a lot of them due to your pistol, but one of them survived and shoot in your back")
    killer.increasehp(-80)
elif (c=="1" and killer.weapon=="grenade launcher"):
    print("You died, because you was crazy, no one will shot in room by grenade launcher ")
    killer.hp=0
elif (c=="1" and killer.weapon=="radio bomb"):
    print("You are seriously? You detonate radio bomb in room... You died ")
    killer.hp=0
elif c=="2" :
    print("You died beacuse you kind one <3")
    killer.hp=0
elif c=="3" :
    print("You died beacuse you slowly one ")
    killer.hp=0

if killer.hp > 0:
    print("Your hp is ", killer.hp)
else: print("Game Over")   

    
    

    
    
    
    
    
    
    


