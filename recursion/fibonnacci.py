def fibonnacci(n1):
    if n1 in [1, 2]:
        return n1-1
    return fibonnacci(n1-1) + fibonnacci(n1-2)

n1 = int(input("Enter the number number: "))
print(f"result: {fibonnacci(n1)}")