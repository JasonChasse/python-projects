# Room security check off list

var1 = 'Yes'
var2 = 'No'
var3 = '007'

lights_input = (input('Are the lights off?  '))

if lights_input == var1 :
        print('Lights Secured')

if lights_input == var2 :
    print('Please Secure Lights')

doors_input = (input('Are the doors locked?  '))

if doors_input == var1 :
    print('Doors Secured')

if doors_input == var2 :
    print('Please Secure Doors')

windows_input = (input('Are the windows closed? '))

if windows_input == var1 :
    print('Windows Secured')

if windows_input == var2 :
    print('Please Secure Windows')

ac_input = (input('Is the AC off?  '))

if ac_input == var1 :
    print('AC is off')

if ac_input == var2 :
    print('Please secure AC  ')

code_input = (input('Please enter security code  '))

if code_input == var3 :
    print('Thank you Jason, have a great evening')

else :
    print('CODE WRONG DISINTEGRATION IN 5 \n  4 \n 3 \n 2 \n 1')
    
    

    
