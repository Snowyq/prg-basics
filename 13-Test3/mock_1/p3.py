# (p3.py) The uid array contains user IDs in one of the popular websites. Identifiers should be unique. Create a function f(uid) that returns true if all ids are unique. Otherwise, the function returns false. Example: 

# f(["john5","ann123","JOHN5","xxx","abc333","a10"]) à True 
# f(["abc123","ann","abc123","a10"]) à False 
# f(["bob2","bob2"]) à False 
# f(["bob2","BOB2"]) à True 

def f(uid):
    seen = set()
    for id in uid:
        if id in seen:
            return False
        else: 
            seen.add(id)
    return True

def f2(uid):
    return len(uid) == len(set(uid))

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]) )
#à True 
print(f(["abc123","ann","abc123","a10"]) )
# False 
print(f(["bob2","bob2"]) )
# False 
print(f(["bob2","BOB2"]) )
 # True 