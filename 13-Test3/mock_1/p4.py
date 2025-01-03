# (p4.py) The prods array contains the names of the products in stock. Create a function f(fnc,prods) that maps product names to their IDs, according to the fnc function. The f function returns a comma-separated list of product IDs, with no spaces. Example:


def f(fnc, prods):
    return ",".join(map(fnc, prods))


prods = ["water", "cheese", "tomato"]
fnc1 = lambda x: "id:" + x[:2]
print(f(fnc1, prods))
#  " id:wa,id:ch,id:to"
fnc2 = lambda x: (x[0] + x[-1]).upper()
print(f(fnc2, prods))
#  "WR,CE,TO"
