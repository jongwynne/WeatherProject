x = '   kUbrick-grouPings               ...        '
y = 'r'
z = 'PC1234-LON-2016'
# print x[::2]
# print x.strip(' ''.')
# print x.join(y)
# print x.split('-', 1)
# print x.lower()
# print x.capitalize()
# print x.find(y)
# print x.replace('k', 'z')
# print x.strip(' ''.').replace('k', 'z').lower().capitalize()
z = z.split('-', 2)
a = z[0][2:7]
z[0] = z[0][0:2]
print z[1]
print a
print z[2]
print z[0]







