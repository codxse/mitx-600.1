flag = s[0]
temp = ''
maxim = ''
new_s = s + '0'

for c in new_s[1:]:
    if(flag[-1] <= c):
        flag += c
    if(flag[-1] > c):
        temp = flag
        if(len(temp) > len(maxim)):
            maxim = temp
        flag = c

print('Longest substring in alphabetical order is:', maxim)
