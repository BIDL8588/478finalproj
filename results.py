import hashlib
from utils import load_hashes, save_table
from crack_hash import crack_single

def an_results(hashed_file, output_file, algorithm = "sha256"): 
  hashed = load_hashes(hashed_file)
  sum_tot = []
  count = 0
  total = len(hashed)
  print(f"analysis on {total} hashed passwords...")
  for i in hashed: 
    password = crack_single(i , algorithm)

    if password: 
      count += 1
      sum_tot.append(f"{i} = {password}")
    else: 
      sum_tot.append(f"{i} = Not Cracked")

  rate = (count/total) * 100
  sum_tot.append("\n================SUMMARY================")
  sum_tot.append(f"Total Hashes: {total}")
  sum_tot.append(f"Cracked: {count}")
  sum_tot.append(f"Success Rate: {rate:.2f}%")
  save_table(sum_tot, output_file)

  print(f"analysis done. Saved results to {output_file}")

if __name__ == "__main__": 
  an_results(
      hashed_file = "data/hashed_passwords.txt",
      output_file = "data/analysis_summary.txt",
      algorithm = "sha256"
)


