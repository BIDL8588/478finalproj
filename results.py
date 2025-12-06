import time
from crack_hash import dictionary_crack, brute_force
from hash_password import hash_pass

def analyze_hashes(input_file, output_file, algorithm="sha256", use_dict=True, use_brute=True):

    results = []
    total = 0
    cracked = 0
    dict_time_total = 0
    brute_time_total = 0

    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            if "," in line:
                original, hash_val = line.split(",", 1)
                hash_val = hash_val.strip()
            else:
                continue

            total += 1
            found = None

            if use_dict:
                start = time.time()
                found = dictionary_crack(hash_val, algorithm)
                dt = time.time() - start
                dict_time_total += dt

                if found:
                    cracked += 1
                    results.append(f"{hash_val} = {found}  (dictionary: {dt:.4f}s)")
                    continue

            if use_brute:
                start = time.time()
                found = brute_force(hash_val, algorithm, max_len=4)
                bt = time.time() - start
                brute_time_total += bt

                if found:
                    cracked += 1
                    results.append(f"{hash_val} = {found}  (bruteforce: {bt:.4f}s)")
                else:
                    results.append(f"{hash_val} = Not Found")
    results.append("\n================ SUMMARY ================")
    results.append(f"Total Hashes: {total}")
    results.append(f"Cracked: {cracked}")
    results.append(f"Success Rate: {cracked/total * 100:.2f}%")

    if use_dict:
        results.append(f"Avg Dictionary Time: {dict_time_total/max(total,1):.4f}s")

    if use_brute:
        results.append(f"Avg BruteForce Time: {brute_time_total/max(total,1):.4f}s")

    with open(output_file, "w") as file:
        for r in results:
            file.write(r + "\n")

    print(f"Analysis saved -> {output_file}")


