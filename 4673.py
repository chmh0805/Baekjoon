def self_number():
    list = []
    n = 1
    while n <= 10000 :
        n = n + n//10 + n//100 + n//1000
        list.append(n)
    for i in range (1, 10001) :
        if i not in list :
            print (i)

self_number()
