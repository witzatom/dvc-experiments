import sys
import os

if __name__ == "__main__":
    directory = sys.argv[1]
    output_dir = sys.argv[2]
    # with open(output_file, "w") as f:
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for child in os.listdir(directory):
        data_file = os.path.abspath(os.path.join(directory, child))
        link_file = os.path.join(output_dir, child)
        if os.path.isdir(data_file):
            continue
        if not data_file.endswith("inmodel.png"):
            continue
        print(f"Linking {link_file} -> {data_file}")
        os.symlink(
            data_file,
            link_file
        )
