c = 0
for i in range(len(s)):
    if(s[i:i+3] == 'bob'):
        c += 1

print('Number of times bob occurs is:', c)
