# Creating a list the long way
list1 = []
rang = range(1,6)
for i in rang:
    list1.append(i)
print ("\nList 1: " + str(list1))

# The short way
list2 = list(range(1,11))
print ("\nList 2: " + str(list2))

# The lambda-short way
list3 = lambda ran = range(1,16) : list(ran)
print("\nList 3: " + str(list3()))