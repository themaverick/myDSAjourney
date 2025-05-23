def sayDigits(num):
    if num == 0:
        return
    sayDigits(num//10)
    print(num%10)
    
num = int(input("Enter the base number: "))

sayDigits(num)