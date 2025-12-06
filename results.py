import time
import sys

from crack_hash import dictionary_crack, brute_force


def analyze_hashes(input_file, output_file, algorithm="sha256",
                   use_dict=True, use_brute=True):

    results = []
    total = 0
    cracked = 0

    dict_time_total = 0.0
    brute_time_total = 0.0

    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()

            if "," not in line:
                continue

            original, hash_val = line.split(",", 1)
            hash_val = hash_val.strip()
            total += 1

            # --- Dictionary cracking ---
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

            # --- Brute force cracking ---
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

    # ---- Summary Block ----
    results.append("\n================ SUMMARY ================")
    results.append(f"Total Hashes: {total}")
    results.append(f"Cracked: {cracked}")
    results.append(f"Success Rate: {(cracked / total) * 100:.2f}%")

    if use_dict:
        avg = dict_time_total / max(total, 1)
        results.append(f"Avg Dictionary Time: {avg:.4f}s")

    if use_brute:
        avg = brute_time_total / max(total, 1)
        results.append(f"Avg BruteForce Time: {avg:.4f}s")

    # ---- Save Output ----
    with open(output_file, "w") as f:
        for r in results:
            f.write(r + "\n")

    print(f"Analysis saved → {output_file}")


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Usage:")
        print("  python results.py <hashed_file> <output_file> <mode>")
        print("Modes: dict | brute | both")
        sys.exit(1)

    hashed_file = sys.argv[1]
    output = sys.argv[2]
    mode = sys.argv[3].lower()

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
        print("Error: mode must be dict, brute, or both")
        sys.exit(1)

    analyze_hashes(hashed_file, output, algorithm="sha256",
                   use_dict=use_dict, use_brute=use_brute)
