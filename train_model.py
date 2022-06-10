import sys
import os

if __name__ == "__main__":
    dataset = sys.argv[1]
    model_output = sys.argv[2]
    with open(dataset, "r") as f:
        with open(model_output, "w") as of:
            of.writelines(f.readlines())
