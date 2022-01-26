"""
This program calculates effects of changes in interest and mortality rates on
insurance and annuity products using a CF model.
"""
import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

"""basics"""


def v(i, n):  # discount factor
    return (1 + (0.01 * i)) ** -n


def d(i):  # discount rate
    return i / (100 + i)


def p_cf(mu, n):  # nPx given CF
    return np.e ** (-0.01 * mu * n)


def adf_cf(i, n, mu):  # actuarial discount factor
    return v(i, n) * p_cf(mu, n)


def a_double_dot_cf(i, mu):  # APV of a contingent annuity due
    return 1 / (1 - adf_cf(i, 1, mu))


def a_angle_n(i, n):  # APV of a certain annuity due
    return (1 - v(i, n)) / (0.01 * i)


def a_double_dot_angle_n(i, n):  # APV of a certain annuity immediate
    return (1 - v(i, n)) / (d(i))


"""annuities"""


def wla_cf(i, mu):  # APV of a whole life annuity
    return a_double_dot_cf(i, mu)


def nyta_cf(i, n, mu):  # APV of an n-year temporary annuity
    return a_double_dot_cf(i, mu) - dwla_cf(i, n, mu)


def dwla_cf(i, n, mu):  # APV of a deferred whole life annuity
    return adf_cf(i, n, mu) * a_double_dot_cf(i, mu)


def nycala_cf(i, n, mu):  # APV of an n-year certain and life annuity
    return a_double_dot_angle_n(i, n) + dwla_cf(i, n, mu)


"""insurances"""


def wli_cf(i, mu):  # APV of a whole life insurance
    return (v(i, 1) - adf_cf(i, 1, mu)) * a_double_dot_cf(i, mu)


def dwli_cf(i, n, mu):  # APV of a deferred whole life insurance
    return adf_cf(i, n, mu) * wli_cf(i, mu)


def nyti_cf(i, n, mu):  # APV of an n-year term insurance
    return wli_cf(i, mu) - dwli_cf(i, n, mu)


def pe_cf(i, n, mu):  # APV of an n-year pure endowment
    return adf_cf(i, n, mu)


def ei_cf(i, n, mu):  # APV of an endowment insurance of n years
    return adf_cf(i, n, mu) + nyti_cf(i, n, mu)


"""
graphs:
To use this section, change the type of function called for the zs var and change parameters to suit needs.
plt.title will likely need to be changed.
range of graph can also be changed manually.
"""

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0.1, 10, 0.1)
X, Y = np.meshgrid(x, y)

zs = np.array([wli_cf(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
ax.plot_surface(X, Y, Z)

ax.set_xlabel('Interest Rate')
ax.set_ylabel('Force of Mortality')
ax.set_zlabel('Actuarial Present Value')
plt.suptitle("Whole Life Insurance", fontsize = 20)
plt.title("Constant Force Assumption", fontsize = 10)
plt.show()

