name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
diction = {}
for line in handle:
    if line.startswith('From '):
        words = line.split()
        hour = words[5]
        hour = hour[:2]
        diction[hour]=diction.get(hour,0) + 1
#print(diction)
diction = sorted(diction.items())
for k, v in diction:
    print(k,v)
