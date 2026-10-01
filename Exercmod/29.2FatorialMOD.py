#DeclararVR
i: int = 0
fat: int 
num: int = 0
j: int =  0
primeiro = int

def divi ( primeiro , fat):
    return primeiro / fat


def ffat(num):
    global i
 
    global fat 
   
    global div
    fat = 1
    for i in range (1, num + 1):
        fat = fat * i
        

    
    return(fat)
ffat(num)


def main():
    global num
    global total
    global j
    
    num = int(input('digite o fatorial: '))    
    total = 1    
    for j in range (1, num + 1):
        resultadofatorial = ffat(j)
        resultadoDivisao = divi (1 , resultadofatorial)
        total = total + resultadoDivisao
        print (total)
if __name__ == '__main__':
    main()
