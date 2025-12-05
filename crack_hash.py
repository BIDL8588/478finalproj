import random
import hashlib
import itertools
import string

from gen_pass import(
    gen_weak_password, 
    gen_medium_password, 
    gen_strong_password
)

from hash_password import hash_pass

def dictionary_crack(hash_val, algorithm="sha256"):
    try:
        with open("data/dictionary.txt", "r") as file:
            for word in file:
                word = word.strip()
                if hash_pass(word, algorithm) == hash_val:
                    return word
    except FileNotFoundError:
        print("Dictionary file missing: data/dictionary.txt")
    return None

def brute_force(hash_val, algorithm="sha256", max_len=7):
    low = string.ascii_lowercase
    count = 0
    
    for length in range(1, max_len + 1):
        for i in itertools.product(low, repeat=length):
            guess = "".join(i)
            count += 1
            if count % 100000 == 0:
                print(f"Tried {count} guesses so far... (current = {guess})")
            if hash_pass(guess, algorithm) == hash_val:
                return guess
    return None


def crack_single(hash_value, algorithm="sha256", brute_forced=True):
    result = dictionary_crack(hash_value, algorithm)
    if result:
        return result
    
    if brute_forced:
        return brute_force(hash_value, algorithm, max_len=4)
    
    return None


def crack_hfile(hashed_file, output_file, algorithm="sha256", brute_forced=True):
    results = []

    with open(hashed_file, "r") as file:
        for line in file:
            line = line.strip()

            if "," in line:
                original_pass, hashed = line.split(",", 1)
                hashed = hashed.strip()
            else:
                hashed = line.strip()

            cracked_p = crack_single(hashed, algorithm, brute_forced=brute_forced)

            if cracked_p:
                results.append(f"{hashed} = {cracked_p}")
            else:
                results.append(f"{hashed} = Not found")

    with open(output_file, "w") as file:
        for r in results:
            file.write(r + "\n")

    print(f"Cracked Results saved to: {output_file}")


if __name__ == "__main__":
    crack_hfile(
        hashed_file="data/hashed_raw.txt",
        output_file="data/cracked_raw_results.txt",
        algorithm="sha256",
        brute_forced=True
    )

    crack_hfile(
        hashed_file="data/hashed_dictionary.txt",
        output_file="data/cracked_dictionary_results.txt",
        algorithm="sha256",
        brute_forced=False
    )
