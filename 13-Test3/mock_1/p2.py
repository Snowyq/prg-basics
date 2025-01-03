# (p2.py) Create a function f(x,y,digit) that returns how many times the given digit appears in numbers in the range from x to y. Example: 

def f(x,y,digit):
    count = 0
    for num in  range(x,y + 1):
        for dig in str(num):
            if dig == str(digit):
                count += 1
    return count

print(f(10,15,1)) # à 7 
print(f(28,32,2)) # à 3 
print(f(100,105,6)) # à 0 
print(f(100,101,0)) # à 3 