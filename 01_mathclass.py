import sys
g = sys.argv
num_lst = list(g)
del num_lst[0]
for x in num_lst:
    x = int(x)
num_lst = sorted(num_lst, key = lambda x:int(x), reverse = False)


def find_min():
    return num_lst[0]

print("Minimum: ",find_min())

def find_max():
    x = len(num_lst)
    return num_lst[x-1]

print("Maximum: ",find_max())

def find_mean():
    count = 0 
    for x in num_lst:
        count += int(x)
    mean = count/len(num_lst)
    return mean 

print("Mean: ",find_mean())

def find_median():
    x = len(num_lst)//2
    y = x + 1 
    if len(num_lst) % 2 == 0:
        median = (int(num_lst[x-1])+int(num_lst[y-1]))/2
    else:
        median = num_lst[y-1]
    return median 

print("Median: ",find_median())

def find_mode():
    from collections import Counter
    count = dict(Counter(num_lst))
    count1 = sorted(count, key = lambda x: (count[x]), reverse = True)
    mod = []
    m_value = list(count1)[0]
    if count[m_value] != 1:
        mod.append(m_value)
    for x in count1:
        if count[x] == count[m_value]:
            mod.append(x)
        else:
            x == x
    m = []
    for ch in mod:
        if ch not in m:
            m.append(ch)
        else: 
            m == m 
    return m 
    
print("Mode: ", find_mode())


def find_range():
    r = int(num_lst[-1]) - int(num_lst[0])
    return r

print("Range: ",find_range())
