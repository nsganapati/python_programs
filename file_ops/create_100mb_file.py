def create_10mb_single_line_file(filename):
    """
    Creates a 10MB text file consisting of repetitively generated string data.
    
    Args:
        filename (str): The path or name of the file to create and write data to.
    """
    target_size = 10*1024*1024
    chunk = "word " * 100 # 5000 bytes

    with open (filename, "w", encoding="utf-8") as f:
        written = 0
        while written < target_size:
            f.write(chunk)
            written+=len(chunk.encode("utf-8"))



create_10mb_single_line_file("tmp.txt")