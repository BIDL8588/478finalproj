import hashlib

def hash_pass(password, algorithm): 
  passwordly = password.encode()

  if algorithm == "md5":
    hashed = hashlib.md5(passwordly).hexdigest()

  elif algorithm == "sha1":
    hashed = hashlib.sha1(passwordly).hexdigest()

  elif algorithm == "sha256":
    hashed = hashlib.sha256(passwordly).hexdigest()
  else:
    raise ValueError("hashing algorithm invalid")

  return hashed 

def hash_pass_file(input_file, output_file, algorithm = "sha256"): 
  hashed_l = []
  
  with open(input_file, "r") as file:
    for line in file:
      password = line.strip()
      hashed = hash_pass(password, algorithm) 
      hashed_l.append(f"{password}, {hashed}") 

  with open(output_file, "w") as file: 
    for i in hashed_l: 
      file.write(i + "\n")

  print(f"Hashed password saved to {output_file} using {algorithm}") 

if __name__ == "__main__": 
  input_p = "data/raw_passwords.txt"
  output_p = "data/hashed_passwords.txt"

  hash_pass_file(input_p, output_p, algorithm = "sha256")
