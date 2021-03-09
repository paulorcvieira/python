"""
Manipulando string
* String indíces
* Fatiamento de strings [inicio:fim:passo]
* Funções build-in, len, abs, type, print e etc...
Essas funções podem ser usadas diretamente em cada tipo

https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""

# positivos [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
url = 'www.google.com/'
# negativos [-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

print(url[7])
print(url[2:8])
print(url[:8])
print(url[4:])
print(url[0::2])

for letra in url:
    print(letra)
