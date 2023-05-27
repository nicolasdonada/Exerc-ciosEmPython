def LerInt(numero):
    while True:
        try:
            entrada = int(input(numero))
    
        except(ValueError, TypeError, KeyboardInterrupt):
            print("\033[0;31mERRO! O valor digitado não é INTEIRO.\033[m")
            continue
    
        else:
            print(f"\033[0;32mO valor INTEIRO digitado foi {entrada}\033[m")
            break

def LerFloat(numero):
    while True:
        try:
            entrada = float(input(numero))

        except(ValueError, TypeError, KeyboardInterrupt):
            print("\033[0;31mERRO! O valor digitado não é REAL.\033[m")
            continue
        
        else:
            print(f"\033[0;32mO valor REAL digitado foi {entrada}\033[m")
            break