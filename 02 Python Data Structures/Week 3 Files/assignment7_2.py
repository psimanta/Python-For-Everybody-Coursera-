# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        s = s + float(line[line.find('0'):])
        count = count + 1

print("Average spam confidence: " + str(s/count))
