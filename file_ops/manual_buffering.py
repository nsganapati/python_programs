

def read_large_file(file_path, chunk_size_words=100):
    """
    Reads a large text file in 1MB chunks and prints words in specified chunk sizes.
    
    This function implements a manual buffering technique to process very large files
    without loading the entire file into memory at once.
    
    Args:
        file_path (str): The path to the text file to read.
        chunk_size_words (int): The number of words to group together and print at once. Default is 100.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        buffer = []
        leftover = ""

        while True:
            chunk = f.read(1024 * 1024)  # read 1MB at a time
            if not chunk:
                break

            chunk = leftover + chunk
            words = chunk.split()

            # handle last partial word
            if not chunk[-1].isspace():
                leftover = words.pop()
            else:
                leftover = ""

            for word in words:
                buffer.append(word)

                if len(buffer) >= chunk_size_words:
                    print(" ".join(buffer))
                    buffer = []

        if leftover:
            buffer.append(leftover)

        if buffer:
            print(" ".join(buffer))

def main():
    current_dir = "."
    chunk_size=100
    read_large_file("D:\Learnings\python\python_practice\large_file.txt", chunk_size)
    # read_large_file()

if __name__ == "__main__":
    main()