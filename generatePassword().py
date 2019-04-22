import random
import string
generatePassword = ''.join(random.choice(string.printable) for x in range(random.randint(4,16)))
 
print (generatePassword)