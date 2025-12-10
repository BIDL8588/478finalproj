import os
import time
import pandas as pd
from src.generator import PasswordGenerator
from src.hasher import Hasher
from src.cracker import Cracker

ARTIFACTS_DIR = "artifacts/release"
RAW_PASSWORDS_FILE = os.path.join(ARTIFACTS_DIR, "raw_passwords.txt")
HASHED_PASSWORDS_FILE = os.path.join(ARTIFACTS_DIR, "hashed_passwords.txt")
REPORT_FILE = os.path.join(ARTIFACTS_DIR, "analysis_report.csv")

def main():
    print("===================================================")
    print("   PASSWORD STRENGTH & CRACKING ANALYSIS SYSTEM    ")
    print("===================================================")

    os.makedirs(ARTIFACTS_DIR, exist_ok=True)

    print("\nStep 1: Generating Synthetic Dataset...")
    gen = PasswordGenerator()
    passwords = gen.generate_dataset(count=50)
    
    gen.save_to_file(passwords, RAW_PASSWORDS_FILE)
    print(f"    - Generated {len(passwords)} passwords.")
    print(f"    - Saved raw list to {RAW_PASSWORDS_FILE}")

    print("\nStep 2: Hashing Passwords...")
    target_algo = "sha256"
    hashed_data = Hasher.process_file(RAW_PASSWORDS_FILE, HASHED_PASSWORDS_FILE, algo=target_algo)
    print(f"    - Hashed {len(hashed_data)} passwords using {target_algo}.")
    print(f"    - Saved hash list to {HASHED_PASSWORDS_FILE}")

    print(f"\nStep 3: Initializing Attack Engine ({target_algo})...")
    cracker = Cracker()
    results = []

    print("    - Starting Dictionary and Brute-Force attacks...")
    start_total = time.time()

    for original_pw, target_hash in hashed_data:
        start_crack = time.time()
        cracked_val = cracker.dictionary_attack(target_hash, target_algo)
        method = "Dictionary"

        if not cracked_val:
            cracked_val = cracker.brute_force_attack(target_hash, target_algo, max_len=4, timeout=0.5)
            method = "Brute-Force"
        
        duration = time.time() - start_crack
        success = (cracked_val == original_pw)

        results.append({
            "original_len": len(original_pw),
            "algorithm": target_algo,
            "cracked": success,
            "method": method if success else "Failed",
            "time_taken": round(duration, 5),
            "password_sample": "*" * 6 
        })

    total_time = time.time() - start_total
    print(f"    - Attack phase complete in {round(total_time, 2)} seconds.")

    print("\nStep 4: Generating Final Report...")
    df = pd.DataFrame(results)
    
    total_cracked = df[df['cracked'] == True].shape[0]
    success_rate = (total_cracked / len(df)) * 100

    df.to_csv(REPORT_FILE, index=False)
    
    print("\n--- FINAL RESULTS SUMMARY ---")
    print(f"Total Targets: {len(df)}")
    print(f"Total Cracked: {total_cracked}")
    print(f"Success Rate:  {success_rate:.2f}%")
    
    print("\n--- DETAILED BREAKDOWN ---")
    print(df[['method', 'time_taken', 'cracked']].head(10).to_string())
    print("\n[!] Full report saved to:", REPORT_FILE)

if __name__ == "__main__":

    main()

