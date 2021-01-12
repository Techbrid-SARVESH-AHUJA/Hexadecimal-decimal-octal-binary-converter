import sys
from termcolor import colored, cprint
print("THIS IS A CALCULATOR WHICH CAN DO CONVERSIONS FROM HEX, DECIMAL, OCTAL OR BINARY ; TO HEX, DECIMAL, OCTAL OR BINARY")
while True:
    print(' ')
    f = input(('From which form do you want to convert ; enter 1 for hex, 2 for decimal, 3 for octal, 4 for binary, q for quit:  '))
    print(' ')
    if (f == '1' or f == '2' or f == '3' or f == '4'):
        t = input(('To which form do you want to convert ; enter 1 for hex, 2 for decimal, 3 for octal, 4 for binary, q for quit:  '))
        print(' ')
        if (t == '1' or t == '2' or t == '3' or t == '4'):
            num = input(('Enter the number you want to convert:  '))
            print(' ')
            if (f == '2' and t == '4'): # dec - bin
                num2 = int (num)
                a=str(bin(num2))
                print('   the result in binary is: ', a[2:])
                print(' ')
            if (f == '1' and t == '3'): # hex - oct
                a=int(num, 16)
                a=oct(a)
                print('   the result in octal is: ', a[2:])
                print(' ')
            if (f == '1' and t == '4'): # hex - bin
                a=int(num, 16)
                a=bin(a)
                print('   the result i binary is: ', a[2:])
                print(' ')
            if (f == '1' and t == '2'): # hex - dec
                a=int(num, 16)
                print('   the result in decimal is: ', a)
                print(' ')
            if (f == '2' and t == '1'): # dec - hex
                num2 = int (num)
                a=hex(num2)
                print('   the result in hex is: ', a[2:])
                print(' ')
            if (f == '2' and t == '3'): # dec - oct
                num2 = int (num)
                a=oct(num2)
                print('   the result in octal is: ', a[2:])
                print(' ')
            if (f == '3' and t == '1'): # oct - hex
                a=str(int(num, 8))
                a2 = int(a)
                a=hex(a2)
                print('   the result in hex is: ', a[2:])
                print(' ')
            if (f == '3' and t == '2'): # oct - dec
                a=str(int(num, 8))
                print('   the result in decimal is: ', a)
                print(' ')
            if (f == '3' and t == '4'): # oct - bin
                a=(int(num, 8))
                a=bin(a)
                print('   the result in decimal is: ', a[2:])
                print(' ')
            if (f == '4' and t == '1'): # bin - hex
                num2=str(num)
                a=int(num2, 2)
                a=hex(a)
                print('   the result in hex is: ', a[2:])
                print(' ')
            if (f == '4' and t == '2'): # bin - dec
                num2=str(num)
                a=int(num2, 2)
                print('   the result in decimal is: ', a)
                print(' ')
            if (f == '4' and t == '3'): # bin - oct
                num2=str(num)
                a=int(num2, 2)
                a=oct(a)
                print('   the result in octal is: ', a[2:])
                print(' ')
            if (f == '1' and t == '1'): # hex - hex
                print('   the result in hex is: ', num)
                print(' ')
            if (f == '2' and t == '2'): # dec - dec
                print('   the result in decimal is: ', num)
                print(' ')
            if (f == '3' and t == '3'): # oct - oct
                print('   the result in octal is: ', num)
                print(' ')
            if (f == '4' and t == '4'): # bin - bin
                print('   the result in binary is: ', num)
                print(' ')
        elif(t == 'q'):
            break
        else:
            cprint("   ERROR 438: Enter only 1, 2, 3 or 4   ", 'red', attrs=['bold'], file=sys.stderr)
            print(' ')
            continue
    elif(f == 'q'):
        break
    else:
        cprint("   ERROR 438: Enter only 1, 2, 3 or 4   ", 'red', attrs=['bold'], file=sys.stderr)
        print(' ')
        continue
cprint("   THANK YOU FOR USING ME   ", 'red', attrs=['bold'], file=sys.stderr)
print(' ')
cprint("   MADE BY SARVESH AHUJA    ", 'red', attrs=['bold'], file=sys.stderr)



















