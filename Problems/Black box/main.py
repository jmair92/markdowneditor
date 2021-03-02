# use the function blackbox(lst) that is already defined
lst = [1, 2, 3]
lst2 = blackbox(lst)
if id(lst) == id(lst2):
    print("modifies")
else:
    print("new")
