name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
diction = {}
for line in handle:
    if line.startswith('From '):
        words = line.split()
        diction[words[1]] = diction.get(words[1], 0) + 1

Max_count = 0
Max_key = ''
for key, value in diction.items():
    if value > Max_count:
        Max_count = value
        Max_key = key
print(Max_key, Max_count)
