import string
import random
N =int(input())
res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
print("The generated password : {0}".format(res))