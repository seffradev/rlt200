import matplotlib.pyplot as plt
import pandas as pd
import sys


def main():
    plt.close("all")

    if len(sys.argv) < 3:
        print("usage: python lab2.py <in-file> <out-file>")
        exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    frame = pd.read_csv(in_file, sep=";")
    frame["Datetime"] = pd.to_datetime(frame["Date"] + " " + frame["Time"])
    frame = frame.drop(["Date", "Time", "Unnamed: 5"], axis=1)

    frame = frame.set_index("Datetime")

    plt.figure()
    frame.plot(xlabel="")
    plt.savefig(out_file, dpi=300)


if __name__ == "__main__":
    main()
