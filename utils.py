import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    return wrapper

def load_hashes(path):
    hashes = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                hashes.append(line)
    return hashes

def save_table(data, output_file):
    with open(output_file, "w") as file:
        for row in data:
            file.write(row + "\n")
