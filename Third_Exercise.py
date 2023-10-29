list1=[54,76,2,4,98,100]
try:
    int1=int(input('Please enter your first integer:'))
    int2=int(input('Please enter your second integer:'))


    if int1<=int2:
        for i in list1:
            if i>=int1 and i<=int2:
                print(i)
    else:
        for i in list1:
            if i>=int2 and i<=int1:
                print(i)

except:
    print("Invalid input. Please enter valid integers.")