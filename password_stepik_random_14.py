from random import *
from string import ascii_uppercase as a_upper,ascii_lowercase as a_lower, digits as dig
list_upper = [up for up in a_upper if up not in 'LIO']
list_lower = [l for l in a_lower if l not in 'lio']
list_digits = [str(d) for d in dig if str(d) not in '01']
list_common = list_lower + list_upper + list_digits 
#list_letter_not = ['l','L','I','i','1','o','O','0']
#Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.
#result = [choice(i) for i in (chars1, chars2, chars3)] + [choice(chars) for _ in range(3, length)]
    
def generate_password(length):
    p = ''.join(sample(list_upper,1) + sample(list_lower,1) + sample(list_digits,1) + sample(list_common,length - 3))
    return p
def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(m))

n, m = int(input('Количество паролей: ')), int(input('Длину паролей: '))

generate_passwords(n, m)
