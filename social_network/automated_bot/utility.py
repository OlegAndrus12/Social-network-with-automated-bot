import random
import string

def random_email_generator(length = 10):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(length)) + "@gmail.com"


def generate_random_password(length = 12):
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#$%^&*()")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    alphabets_count = 4
    digits_count = 4
    special_characters_count = 4
    
    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        alphabets_count += length - characters_count
    
    password = []
	
    for i in range(alphabets_count):
    	password.append(random.choice(alphabets))


    for i in range(digits_count):
    	password.append(random.choice(digits))

    for i in range(special_characters_count):
    	password.append(random.choice(special_characters))

    if characters_count < length:
    	random.shuffle(characters)
    	for i in range(length - characters_count):
    		password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)

