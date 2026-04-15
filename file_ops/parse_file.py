import os
# Threshold: 1 TB
# ONE_TB = 1024 ** 4  # bytes
HUNDRED_MB=100 * 1024 * 1024 

def find_large_files(directory):
    large_files = []
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            if size >= HUNDRED_MB:
                large_files.append(path)
    return large_files


def read_in_chunks(file_path, chunk_size=100):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        buffer = []

        for line in f:  # streaming (safe even for TB files)
            words = line.split()

            for word in words:
                buffer.append(word)

                if len(buffer) >= chunk_size:
                    print(" ".join(buffer))
                    buffer = []

        # print remaining words
        if buffer:
            print(" ".join(buffer))

def read_in_chunks1(file_path, chunk_size=100):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        buffer = []
        leftover=""

    while True:
        chunk = f.read(1024*1024)
        if not chunk:
            break
        
        chunk=leftover+chunk    
        words=chunk.split()
        if not chunk[-1].isspace():
            leftover=words.pop()
        else:
            leftover=""

        for word in words:  # streaming (safe even for TB files)
            buffer.append(word)

            if len(buffer) >= chunk_size:
                print(" ".join(buffer))
                buffer = []
        
        if leftover:
            buffer.append(leftover)

        # print remaining words
        if buffer:
            print(" ".join(buffer))


def main():
    current_dir = "."
    files = find_large_files(current_dir)

    if not files:
        print("No files larger than 100 MB found.")
        return

    for file in files:
        print(f"\nProcessing file: {file}\n")
        read_in_chunks(file, chunk_size=100)


if __name__ == "__main__":
    main()