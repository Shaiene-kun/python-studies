# This program returns all prime numbers in a range
start = 1
end = 100
for num in range(start, end+1):
    div = 0
    for i in range(start, num+1):
        if ((num % i) == 0):
            div += 1
    if (div == 2): print(num) 
    