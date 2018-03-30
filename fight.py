from Cratures import *
#punch1=Knight.Punch()
health1=Knight.Health()
health2=Knight2.Health()
health3=Archer.Health()
#punch2=Knight2.Punch()
def fight():
    hp1=health1
    hp2=health2
    hp3=health3
    lenght = randint(1,10)
    print("Distance between Knight 2 and Archer is " + str(lenght))
    coldown1 = 0
    coldown2 = 0
    attachment_area1=Archer.weapon_distance()
    attachment_area2=Knight2.weapon_distance()
    while hp2 or hp3 <=0:
        if lenght <=attachment_area1 :
            if coldown1==0:
                coldown1 = Archer.weapon_coldown()
                archer_dmg=int(Archer.weapon_dmg())
                hp2 = int(hp2) - int(archer_dmg)
                print('Archer punched on  ' + str(archer_dmg))
                mess1="Knight 2 now has a "+ str(hp2)+" healpoints"
                print(str(mess1))
                if hp2 <= 0:
                    print("Archer is winner")
                    break
                print("next stage")
            else:
                print("Archer can not punch,because it is being recharged")
                coldown1 = coldown1 - 1
            if lenght<=attachment_area2:
                if coldown2==0:
                    coldown2=Knight2.weapon_coldown()
                    knight2_dmg=Knight2.weapon_dmg()
                    hp3 = int(hp3) - int(knight2_dmg)
                    print('Knight 2 punched on  '+str(knight2_dmg))
                    mess2="Archer now has a "+ str(hp3)+" healpoints"
                    print(mess2)
                    if hp3 <= 0:
                        print("Knight 1 is winner")
                        break
                    print("next stage")
                else:
                    print("Knight can not punch")
                    coldown2 = coldown2 - 1
            else:
                print("Knight move to archer")
                lenght=lenght-1
        else:
            lenght = lenght-2
            print("Knight 2 move to Archer and Archer move to Knight")
fight()