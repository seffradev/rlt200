import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def main():
    plt.close("all")

    rs = [1e6, 1e3, 1, 1e-3, 1e-6]
    ls = [1e6, 1e3, 1, 1e-3, 1e-6]
    cs = [1e6, 1e3, 1, 1e-3, 1e-6]

    i = 0

    r = 1e6
    l = 1e3
    c = 1e-6

    A = np.matrix([[-r/l, -1/l], [1/c, 0]])
    B = np.matrix([[1/l], [0]])
    C = np.matrix([[0, 1]])
    D = np.matrix([[0]])

    ss = sp.signal.StateSpace(A, B, C, D)

    plt.figure()
    time, response = sp.signal.step(ss)
    plt.semilogx(time, response)
    plt.savefig(str(i) + ".png", dpi=300)
    i += 1

if __name__ == "__main__":
    main()
