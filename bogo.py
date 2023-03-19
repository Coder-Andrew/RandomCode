from random import choice, randint
from time import time

def issorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False

    return True

def bogo(lst):
    copy = lst[:]
    temp = [0 for i in copy]

    for i in range(len(temp)):
        rand_ele = choice(copy)
        temp[i] = rand_ele
        copy.remove(rand_ele)

    return temp

def write(file_name, count, total_time, sort_time):
    with open(file_name,'r') as file:
        file.readline()
        info = file.readline()


        info = info.split(',')
        #print(info)
    #print(info[0])
    if count > int(info[0]):
        with open(file_name,'w') as file:
            file.write(f'count,total_time,sort_time\n{count},{total_time},{sort_time}\n')
        
    

length = 5
x = [randint(0,100) for i in range(length)]



bogo_x = bogo(x)
count = 0
start_total = time()
while True:
    start = time()
    while not issorted(bogo_x):
        bogo_x = bogo(x)
        count += 1
        #print(bogo_x)

    #print()
    stop = time()
    stop_total = time()
    write('test4.txt',count,stop_total - start_total,stop-start)
    count = 0
    bogo_x = bogo(x)
    
    

print(count,stop-start)



