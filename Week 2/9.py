# Задание 9.
#Сгенерируйте случайный пароль с заданным количеством символов, 
#обязательно включающий заглавные и прописные символы латинского алфавита, 
#специальные символы и цифры.

#''.join(password) - join преобразует из списка строку вставляя между символами то, что до точки 
# random.shuffle() - перемешиавает в списке (изменяемое), но не возвращает ничего, поэтому нельзя писать pw = random.shuffle(pw)

import random
import string 
a = int(input())
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
numbers = "1234567890"
abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
s_c = random.choice(special_chars)
n = random.choice(numbers) 
letter_l = random.choice(abc)
letter_u = random.choice(ABC)

password_4 = [s_c, n, letter_l, letter_u] 
password = random.choices(string.ascii_letters + special_chars + numbers, k=a-4) # random.choices со списком работает 
password = password_4 + password 
random.shuffle(password)

print(''.join(password))
