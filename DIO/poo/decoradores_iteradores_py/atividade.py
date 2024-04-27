def countdown(n): 
    while n > 0: 
        yield n 
        n -= 1 
        
a = list(countdown(3))
print(a)