d = {}
h = {}
f = open("/nfs/2019/p/pveda/Desktop/names.txt", 'r')
for line in f:
    (key, value) = line.split()
    if key not in d:
        d[key] = value
    elif key in d:
        h[key] = value

key_list = list(d.keys())
value_list = list(d.values())
repeats = []
duplicates = {}
final = []

for x in value_list:
    if x not in repeats:
        repeats.append(x)
    elif x in repeats:
        duplicates[x] = 2
    elif x in duplicates:
        duplicates[x] += 1
print()
print("** Shared Last Names! **")
for ch in duplicates:
    for a in d:
        if d[a] == ch:
            final.append(a)
    print(ch, "("+str(duplicates[ch])+")"+":", final)
    final = []
            
repeat = []
duplicate = {}
finals = []

for x in key_list:
    if x in duplicate:
        duplicate[x] += 1
    elif x in h:
        repeat.append(x)
        duplicate[x] = 2

print()

print("** Shared First Names! **")
for c in repeat:
    finals.append(d[c])
    finals.append(h[c])
    print(c, "("+str(duplicate[c])+")"+":", finals)
    finals = []


