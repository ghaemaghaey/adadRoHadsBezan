from random import randint
asli = randint(0,100)

for i in range(20):
    try:
        originInput = input(' enter number => ')
        inputsList = originInput.split(' ')
        input1 = int(inputsList[0])
        input2 = int(inputsList[1])
        listOfNumbers = []
        for i in range(input1,input2+1):
            listOfNumbers.append(i)
        if asli in listOfNumbers:
            print('yes in this list')
        else:
            print('that is wrong')
        listOfNumbers.clear()
        if input1 == input2:
            if input1 == asli:
                print('you win')
            else:
                print('you lose')
                break
    except:
        print("______________ERROR________________________")
        print('you must write two number with space')
        print("___________________________________________")