d = {}
f = open("/nfs/2019/p/pveda/Desktop/names.txt", 'r')
for line in f:
    (key, value) = line.split()
    d[key] = value

key_list = list(d.keys())
value_list = list(d.values())
repeats = []
duplicates = {}
final = {}

for x in value_list:
    if x not in repeats:
        repeats.append(x)
    elif x in repeats:
        duplicates[x] = 2
    elif x in duplicates:
        duplicates[x] += 1

for x in duplicates:
    for ch in d:
        if x == d[ch]:
            

#for x in duplicates:
 #   if x in final:
  #      x == x 
   # elif x in d:
    #    final[x] = d[x]

print("** Shared First Names! **")
print(final)
print(repeats)
print(duplicates)




    

#print(d)
#print(key_list)
#print(value_list)
