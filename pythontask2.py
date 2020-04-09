
import random
import string


x = input('first name:')
y = input('last name:')
z = input('email address:')

first_user = []
first_user.append(x)
first_user.append(y)
first_user.append(z)

length = 5
a = (x[0:2] + y[-2:])
random.choice(string.ascii_lowercase)
password = a + ''.join(random.choice(string.ascii_lowercase) for i in range(length))
print(password)


print('are you satisfied with password')
ans = input('yes/no? ')

if (ans == 'yes'):
  print(first_user)

elif (ans == 'no'):
  newp = input('please input your password: ')
  
  while (len(newp) < 7):
    print('password must be more than 7 characters')
    newp = input('please input your password: ')

  else:
    print(first_user)


x = input('first name:')
y = input('last name:')
z = input('email address:')

sec_user = []
sec_user.append(x)
sec_user.append(y)
sec_user.append(z)

length = 5
a = (x[0:2] + y[-2:])
random.choice(string.ascii_lowercase)
password = a + ''.join(random.choice(string.ascii_lowercase) for i in range(length))
print(password)


print('are you satisfied with password')
ans = input('yes/no? ')

if (ans == 'yes'):
  print(sec_user)

elif (ans == 'no'):
  newp = input('please input your password: ')
  
  while (len(newp) < 7):
    print('password must be more than 7 characters')
    newp = input('please input your password: ')

  else:
    print(sec_user)





  
