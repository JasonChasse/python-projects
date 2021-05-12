#Based on 24 hour clock

import time


def my_counter() :
    
    count = 10

    if time.strftime("%H:%M:%S:%p") == "14:35:00:PM"  :
        
        while True :

        
            print(count)
            count = count - 1
            time.sleep(1)
            if count <= 0 :
                print('KABOOM!!!!!!!!!!!')
                break
                

while 1 == 1 :
    my_counter()



