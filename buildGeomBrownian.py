from basicFunctions import *
import numpy as np


def main():
    # constant drift
    mu = 1
    # The Wiener process parameter - volatility.
    delta = 0.8
    # Total time.
    T = 1
    # Number of steps.
    N = 365
    # Time step size
    dt = T/N
    # Number of realizations to generate.
    m = 50
    # Create an empty array to store the realizations.
    x = np.empty((m, N+1))
    # Initial values of x.
    x0 = 1
    x[:, 0] = x0

    geomBrownian(x[:,0], N, dt, delta, mu, out=x[:,1:])

    # Get drift values
    driftValues = x0 * np.exp(getLinearDrift(N+1, dt, mu))

    displayCharts(m, N, dt, x, driftValues, 'Geometric Brownian Motion')


if __name__ == '__main__':
    main()

