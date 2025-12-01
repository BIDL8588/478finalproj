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

def common_pwords(file_path):
  common_pass = [
      "attack12","star22","cool12","doggy7","tiger5","lover1",
        "sunny8","red123","blue44","catcat","qwer12","zxcv55",
        "simple7","pass12","test11","hello7","mine3","key123",
        "house7","light6","mike22","luna77","rock55","john88",
        "admin5","user11","coco1","baby77","rain22","frog66",
        "luck77","tree3","ghost7","tiny12","bear22","sky987",
        "love99","cute5","note23","jump44"
  ]
    
    
  with open(file_path, "a") as file: 
    for pword in common_pass: 
      file.write(pword + "\n")

  print("Added common weak passwords to the file")

if __name__ == "__main__": 
  output = "data/raw_passwords.txt"
  save_pword(output, 100)
  common_pwords(output)

    
    
    
