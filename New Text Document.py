import winsound

var1 = 'Yes'

gun_input = (input('Would you like to hear gunfire?'))

if gun_input == var1 :

        winsound.PlaySound("smg.wav", winsound.SND_ASYNC)

        delay = input("Press ENTER to finish")

else :
        print('LOSER')
        


        
 
