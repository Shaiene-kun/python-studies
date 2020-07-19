# Creating size
size = 5
x = y = list(range(1,size+1))

# Creating and drawing map
map = {"x": x, "y": y} 
for i in x:
    for j in y:
        print ("□", end="")
    print("")
    

