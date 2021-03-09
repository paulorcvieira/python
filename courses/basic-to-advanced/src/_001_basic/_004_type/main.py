"""
Types of data
str - string - text 'anything' or "anything"
int - integer - 123456 0 -10 -20 -50 -60 -1500 1500
float - real/float 10.50 1.5 -10.10 -50.93 0.0
bool - boolean/logic - true/false - 10 == 10 true
"""

print('Paulo', type('Paulo'))
print('Paulo', type('Paulo'), str(34))
print('10', type('10'))
print('10', type(10))
print(10, type(10))
print(0, type(0))
print(25.23, type(25.23))
print('25.23', type('25.23'))
print(10 == 10, type(10 == 10))
print('l' == 'L', type('l' == 'L'))
print('l' == 'l', type('l' == 'l'))
print('l' == 'l', type('l' == 'l'))

# type casting
print('Paulo', type('Paulo'), bool('Paulo'))
print('10', type('10'), int('10'), type(int('10')))
print('10', type('10'), float('10'))
print(10, type(10), 10 != 10)
print(10, type(10), 10 > 18)
print(10, type(10), 10 < 18)
print('', type(''))
