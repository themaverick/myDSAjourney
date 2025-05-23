def exponent(n1, n2):
    if n1 == n2 and n2 == 0:
        print("undefined")
        return
    elif n2 == 0:
        return 1
    else:
        return n1*exponent(n1, n2-1)
    
n1 = float(input("Enter the base number: "))
n2 = int(input("Enter the integer exponent: "))

print(f"result: {exponent(n1, n2)}")