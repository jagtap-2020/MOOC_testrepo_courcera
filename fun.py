num = 0
largest = -1
smallest = 100
while True:
    num = input("Enter a number: ")
    #if num == "done" :
    #    break
    #try :
    numb = int(num)
    #except :
    #    print('Invalid input')

    #if smallest is None :
    #    smallest = numb
    if numb < smallest :
        smallest = numb
        print("Minimum is", smallest)
    elif numb > largest :
        largest = numb
        print("Maximum is", largest)
