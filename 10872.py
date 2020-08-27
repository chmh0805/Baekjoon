def factorial(k) :
    if k >= 2 :
        result = k * factorial(k-1)
    else :
        result = 1
    return result

print(factorial(int(input())))
