import random
import string

def gen_weak_password():
  letters = string.ascii_lowercase
  password_length = random.randint(4,8)
  password = ""

  for i in range(password_length): 
    password += random.choice(letters) 
  return password 

def gen_medium_password():
  letters_num = string.ascii_lowercase + string.digits
  password_length = random.randint(8,12) 
  password = ""

  for i in range(password_length): 
    password += random.choice(letters_num)
  return password

def gen_strong_password():
  chars = (string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*?")
  password_length = random.randint(12, 16)
  password = "" 

  for i in range(password_length): 
    password += random.choice(chars) 
  return password 

def gen_password_data(quantity):
  passwords = []
  for i in range(quantity): 
    difficult = random.choice(["weak", "medium", "strong"])

    if difficult == "weak": 
      pword = gen_weak_password()

    elif difficult == "medium": 
      pword = gen_medium_password()

    else: 
      pword = gen_strong_password()
      
    passwords.append(pword)
  return passwords

def save_pword(output_file, quantity): 
  password_set = gen_password_data(quantity)

  with open(output_file, "w") as file: 
    for password in password_set:
      file.write(password + "\n")

  print(f"Saved {quantity} passwords to {output_file}")


if __name__ == "__main__": 
  save_pword("data/raw_passwords.txt", 100)

    
    
    
