def summation():
    sum = 0
    for n in range(1, 100):
        if n % 2 != 0:
            sum += n  
    return sum


add = summation()
print("The summation is:", add)