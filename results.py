import hashlib
from utils import load_hashes, save_table
from crack_hash import crack_single
import time

def an_results(hashed_file, output_file, algorithm="sha256"):
    hashes = load_hashes(hashed_file)

    summary_lines = []
    cracked_count = 0
    total = len(hashes)

    print(f"Starting analysis on {total} hashed passwords...\n")

    for h in hashes:
        start = time.time()
        result = crack_single(h, algorithm, use_dict=True, use_brute=False)
        elapsed = time.time() - start

        if result:
            cracked_count += 1
            summary_lines.append(f"{h} = {result}   (time: {elapsed:.4f} sec)")
        else:
            summary_lines.append(f"{h} = Not Cracked   (time: {elapsed:.4f} sec)")

    success_rate = (cracked_count / total) * 100

    summary_lines.append("\n============== SUMMARY ==============")
    summary_lines.append(f"Total Hashes: {total}")
    summary_lines.append(f"Cracked: {cracked_count}")
    summary_lines.append(f"Success Rate: {success_rate:.2f}%")
    summary_lines.append("====================================")

    save_table(summary_lines, output_file)

    print(f"Analysis complete. Saved results to {output_file}")

if __name__ == "__main__":
    an_results(
        hashed_file="data/hashed_dictionary.txt",
        output_file="data/analysis_summary.txt",
        algorithm="sha256"
    )


