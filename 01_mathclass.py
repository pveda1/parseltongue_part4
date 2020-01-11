import sys
g = sys.argv
num_lst = list(g)
del num_lst[0]
num_lst = sorted(num_lst, key = lambda x: (int(x)), reverse = False)

def find_min():
    return num_lst[0]

#print(find_min())

def find_max():
    x = len(num_lst)
    return num_lst[x-1]

#print(find_max())

def find_mean():
    count = 0 
    for x in num_lst:
        count += int(x)
    mean = count/len(num_lst)
    return mean 

#print(find_mean())

def find_median():
    x = len(num_lst)//2
    y = x + 1 
    if len(num_lst) % 2 == 0:
        median = (int(num_lst[x-1])+int(num_lst[y-1]))/2
    else:
        median = num_lst[y-1]
    return median 

#print(find_median())

def find_mode():
    d = {}
    for x in num_lst:
        if x not in d:
            d[x] = num_lst.count(x)
        else: 
            d[x] = d[x]+1
    values = d.values()
    key = d.keys()
    m_value = list(key)[0]
    for ch in d:
        if int(d[ch]) > int(m_value):
            m_value = ch
        else:
            ch == ch 
    return m_value

print(find_mode())




