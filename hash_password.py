import hashlib
import sys 

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

    print(f"Hashed {len(hashed_l)} passwords -> {output_file}") 
    print(f"Algorithm used -> {algorithm}")


if __name__ == "__main__": 

    if len(sys.argv) < 3: 
        print("Usage: python hash_password.py <mode> <algorithm>")
        print("Modes: raw, dict")
        print("Algorithms: md5, sha1, sha256")
        sys.exit(1)

    mode = sys.argv[1].lower()
    algorithm = sys.argv[2].lower()

    if algorithm not in ("md5", "sha1", "sha256"): 
        print("Error: Algorithm must be md5, sha1, or sha256")
        sys.exit(1)
    if mode == "raw": 
        input_file = "data/raw_passwords.txt"
        output_file = "data/hashed_raw.txt"
    elif mode == "dict": 
        input_file = "data/dictionary.txt"
        output_file = "data/hashed_dictionary.txt"
    else: 
        print("Error: mode has to be raw or dict")
        sys.exit(1)
      
    hash_pass_file(input_file, output_file, algorithm)
