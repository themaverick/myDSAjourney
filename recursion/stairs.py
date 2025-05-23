def stairs(n, sum):
    if sum > n:
        return 0
    elif sum == n:
        return 1
    
    return stairs(n, sum+1) + stairs(n, sum+2)
    
n = float(input("Enter the number of stairs: "))

print(f"result: {stairs(n, 0)}")