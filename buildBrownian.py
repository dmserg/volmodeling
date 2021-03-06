from basicFunctions import *
import numpy as np


def main():
    # constant drift
    nu = 1
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
    x = np.zeros((m,N+1))
    # Initial values of x.
    x0 = 1
    x[:, 0] = x0

    brownian(x[:,0], N, dt, delta, out=x[:,1:])

    # Apply drift vector
    driftVector = getLinearDrift(N+1, dt, nu)
    x += driftVector

    displayCharts(m, N, dt, x, driftVector + x0, 'Brownian Motion')


if __name__ == '__main__':
    main()

