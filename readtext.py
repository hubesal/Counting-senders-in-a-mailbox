nadawcy = []
nadawcyCount = {}

f = open('mbox-short.txt','r')
str = f.read()
dividedByLine = (str.split('\n'))

for line in dividedByLine:
    if 'received: from' in line.lower():
        emailIndex = line.lower().split().index("from") +1
        emailSender = line.split()[emailIndex]
        nadawcy.append(emailSender)
#        print(emailSender)
    else:
        continue

for sender in nadawcy:
    nadawcyCount[sender] = nadawcy.count(sender)

# print(nadawcyCount)
maksymalny = max(zip(nadawcyCount.values(), nadawcyCount.keys()))

for sender, qty in nadawcyCount.items():
   if qty == maksymalny[0]:
        print(sender, qty)
