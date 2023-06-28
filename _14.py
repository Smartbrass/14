my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def inp(x):
    if not x:
        print("End of List")
    else:
        print(x.pop(0))        
        inp(x)
    

inp(my_list)
