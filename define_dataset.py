import sys
import os
import hashlib

if __name__ == "__main__":
    directory = sys.argv[1]
    output_file = sys.argv[2]
    with open(output_file, "w") as f:
        for child in os.listdir(directory):
            data_file = os.path.join(directory, child)
            if os.path.isdir(data_file):
                continue
            if not data_file.endswith("inmodel.png"):
                continue
            with open(data_file, "rb") as df:
                file_md5 = hashlib.md5(df.read()).hexdigest()
            f.write(data_file)
            f.write(" ")
            f.write(file_md5)
            f.write("\n")
