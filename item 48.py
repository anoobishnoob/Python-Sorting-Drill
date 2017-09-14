# sorting drill 
data_list = [67, 45, 2, 13, 1, 998]
new_list = []

while data_list:
    minimum = data_list[0]  # assigns the 0 as the lowest 
    for x in data_list: 
        if x < minimum: # so this part checks whether or not x is less than min
            minimum = x # if yes then x is new min
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)


data_list_2 = [89, 23, 33, 45, 12, 10, 45, 45, 45]
new_list_2 = []

while data_list_2:
    minimum = data_list_2[0]  # assigns the 0 as the lowest 
    for x in data_list_2: 
        if x < minimum: # so this part checks whether or not x is less than min
            minimum = x # if yes then x is new min
    new_list_2.append(minimum)
    data_list_2.remove(minimum)    

print (new_list_2)
