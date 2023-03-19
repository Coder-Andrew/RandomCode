def radix(lst):
    temp = [None] * (max(lst) + 1)

    for i in lst:
        if temp[i] != None:
            temp[i + 1] = i
            
        else:
            temp[i] = i

    final_temp = [None] * len(lst)

    index = 0
    for i in range(len(temp)):
        if temp[i] == None:
            continue
        
        final_temp[index] = temp[i]
        index += 1

    return final_temp

#x = [50,200,30,100, 100]

x = [i for i in range(100000, 0, -1)]

print(x[:100])
print()
print(radix(x)[:100])
