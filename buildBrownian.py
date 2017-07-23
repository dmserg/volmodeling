from basicFunctions import *
from scipy.stats import norm
import numpy as np
from pylab import plot, show, grid, xlabel, ylabel


def main():
    # The Wiener process parameter.
    delta = 0.2
    # Total time.
    T = 1
    # Number of steps.
    N = 365
    # Time step size
    dt = T/N
    # Number of realizations to generate.
    m = 20
    # Create an empty array to store the realizations.
    x = np.empty((m,N+1))
    # Initial values of x.
    x[:, 0] = 1

    brownian(x[:,0], N, dt, delta, out=x[:,1:])

    # Apply drift vector
    driftVector = getLinearDrift(N, dt, 1)
    x += driftVector

    timeValues = np.linspace(0.0, N*dt, N+1)
    for k in range(m):
        plot(timeValues, x[k])

    plot(timeValues, driftVector[0])

    xlabel('Time', fontsize=16)
    ylabel('S', fontsize=16)
    grid(True)
    show()


if __name__ == '__main__':
    main()

