fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for w in words:
        #print(w)
        if w not in lst:
            lst.append(w)
            #print(lst)
lst.sort()
print(lst)
