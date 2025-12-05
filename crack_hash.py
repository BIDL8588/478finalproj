import random
import hashlib
import itertools
import string
import sys

from gen_pass import (
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
                print(f"Tried {count} guesses...current = {guess}")

            if hash_pass(guess, algorithm) == hash_val:
                return guess
    return None


def crack_single(hash_value, algorithm="sha256", use_dict=True, use_brute=True):
    if use_dict:
        result = dictionary_crack(hash_value, algorithm)
        if result:
            return result

    if use_brute:
        result = brute_force(hash_value, algorithm, max_len=4)
        if result:
            return result

    return None


def crack_hfile(hashed_file, output_file, algorithm="sha256",
                use_dict=True, use_brute=True):

    results = []

    with open(hashed_file, "r") as file:
        for line in file:
            line = line.strip()

            if "," in line:
                original_pass, hashed = line.split(",", 1)
                hashed = hashed.strip()
            else:
                hashed = line.strip()

            cracked_p = crack_single(hashed, algorithm,
                                     use_dict=use_dict, use_brute=use_brute)

            if cracked_p:
                results.append(f"{hashed} = {cracked_p}")
            else:
                results.append(f"{hashed} = Not found")

    with open(output_file, "w") as file:
        for r in results:
            file.write(r + "\n")

    print(f"Cracked Results saved to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python crack_hash.py dict")
        print("  python crack_hash.py brute")
        print("  python crack_hash.py both")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "dict":
        use_dict = True
        use_brute = False
    elif mode == "brute":
        use_dict = False
        use_brute = True
    elif mode == "both":
        use_dict = True
        use_brute = True
    else:
        print("Error: mode must be 'dict', 'brute', or 'both'")
        sys.exit(1)

    crack_hfile(
        hashed_file="data/hashed_raw.txt",
        output_file="data/cracked_raw_results.txt",
        algorithm="sha256",
        use_dict=use_dict,
        use_brute=use_brute
    )

    crack_hfile(
        hashed_file="data/hashed_dictionary.txt",
        output_file="data/cracked_dictionary_results.txt",
        algorithm="sha256",
        use_dict=use_dict,
        use_brute=use_brute
    )
