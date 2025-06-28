def circularTour(p):

    front = 1
    rear = 1
    balance = 0
    deficit = 0

    for i in range(1, len(p.keys())+1):
        balance += p[rear][0] - p[rear][1]
        if balance < 0:
            deficit += balance
            balance = 0
            front = rear+1
            rear = front
        else:
            rear += 1

    if balance >= deficit:
        return front
    return -1




p = {
    1: [6, 5],
    2: [7, 6], 
    3: [4, 7],
    4: [10, 8],
    5: [6, 6],
    6: [5, 4],
}

print(circularTour(p))
