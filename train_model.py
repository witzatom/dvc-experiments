import sys
import os

if __name__ == "__main__":
    data_folder = sys.argv[1]
    model_output = sys.argv[2]
    with open(model_output, "w") as of:
        for file in os.listdir(data_folder):
            of.write(f"{file}\n")
