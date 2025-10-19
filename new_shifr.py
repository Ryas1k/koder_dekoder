 # шифрирование
b = "To be, or not to be, that is the question!"

en_lower = "abcdefghijklmnopqrstuvwxyz"
en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = ''
for i in b:
  if i.isalpha():
    if i.isupper():
      new_t = chr((ord(i)-ord('A') + 17) % 26 + ord('A'))
      t += new_t
    else:
      new_t = chr((ord(i)-ord('a')+17) % 26 + ord('a'))
      t += new_t
  else:
    t += i 
print(t)
# дешифрирование
c = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
upper_letters=list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
lower_letters=list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()) 
desh =''
for i in c:
  if i.isalpha():
    if i.islower():
      text = chr((ord(i)-ord('а') - 7) % 32 + ord('а'))
      desh += text
    else:
      text = chr((ord(i)-ord('А') - 7) % 32 + ord('А') ) 
      desh += text
  else:
    desh += i
print(desh)


# дешифрирование
f = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
en_lower = "abcdefghijklmnopqrstuvwxyz"
en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
desh1 =''
for i in f:
  if i.isalpha():
    if i.islower():
      text = chr((ord(i)-ord('a') - 25) % 26 + ord('a'))
      desh1 += text
    else:
      text = chr((ord(i)-ord('A') - 25) % 26 + ord('A') ) 
      desh1 += text
  else:
    desh1 += i
print(desh1)



# дешифрирование
f1 = 'Hawnj pk swhg xabkna ukq nqj.'
en_lower = "abcdefghijklmnopqrstuvwxyz"
en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for n in range(1,26):
  desh2 =''
  for i in f1:
    
    if i.isalpha():
      if i.islower():
        text = chr((ord(i)-ord('a') - n) % 26 + ord('a'))
        desh2 += text
      else:
        text = chr((ord(i)-ord('A') - n) % 26 + ord('A') ) 
        desh2 += text
    else:
      desh2 += i
  print(desh2)


  