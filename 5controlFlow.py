x = 0

#if and ifelse and else
if(x < 0):
    x = 0
    print('Negative changed to zero')
elif(x == 0):
    print('0')
else:
    print('More')

# for
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#short form of the typical for loop
for i in range(5):
    print(i)

#range function
print(range(5, 10))
print(range(0, 10, 3))

#usually in python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(a[i])