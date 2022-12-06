#usr/bin/python
#created by nirmit baskota
import hashlib
import time


time.sleep(1.5)
print("-----------password generator by Nirmit baskota --------------------\n")
print('''    _   ___                _ __ 
   / | / (_)________ ___  (_) /_
  /  |/ / / ___/ __ `__ \/ / __/
 / /|  / / /  / / / / / / / /_  
/_/ |_/_/_/  /_/ /_/ /_/_/\__/   ''')
time.sleep(2)
print(" ")
a = input("[*] Enter a string to generate a strong password : ")
print(" ")
paswd = a [::-1]
m = hashlib.sha256()
m.update(paswd.encode('utf-8'))
c = m.hexdigest()
time.sleep(1.5)
print(" ")
print(f"[*]Generated password by the system is : ${c}*")
