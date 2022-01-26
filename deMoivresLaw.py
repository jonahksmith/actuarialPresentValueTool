"""
This program calculates effects of changes in interest and mortality rates on insurance
and annuity products using a CF model. It is assumed that the maximum age is 120, with
independent variables of age and interest rate.
"""

"""basics"""


def v(i, n):  # discount factor
    return (1 + (0.01 * i)) ** -n


def d(i): # discount rate
    return i / (1 + i)


def p_dml(n, x):  # nPx given DML
    return (120 - x - n) / (120 - x)


def adf_dml(i, n, x):  # actuarial discount factor with DML
    return v(i, n) * p_dml(n, x)



def a_double_dot(i, n, x):  # APV of a contingent annuity due
    sum = 0
    for t in range(120 - x):
        sum += adf_dml(i, n, t)



def a_angle_n(i, n):  # APV of a certain annuity immediate
    return (1 - v(i, n)) / (0.01 * i)


"""annuities"""


def wla_dml(i, x):  # APV of a whole life annuity
    return "foobar"


def nyta_dml(i, n, mu):  # APV of an n-year temporary annuity
    return "foobar"


def dwla_dml(i, n, mu):  # APV of a deferred whole life annuity
    return "foobar"


def nycala_dml(i, n, mu):  # APV of an n-year certain and life annuity
    return "foobar"


"""insurances"""


def wli_dml(i, x):  # APV of a whole life insurance
    return a_angle_n(i, (120 - x)) / (120 - x)


def dwli_dml(i, n, x):  # APV of a deferred whole life insurance
    return (v(i, n) * a_angle_n(i, (120 - x - n))) / (120 - x)


def nyti_dml(i, n, x):  # APV of an n-year term insurance
    return a_angle_n(i, n) / (120 - x)


def pe_dml(i, n, x):  # APV of an n-year pure endowment
    return adf_dml(i, n, x)


def ei_dml(i, n, x):  # APV of an endowment insurance of n years
    return adf_dml(i, n, x) + nyti_dml(i, n, x)


"""
graphs:
To use this section, change the type of function called for the zs var and change parameters to suit needs.
plt.title will likely need to be changed.
range of graph can also be changed manually.
"""
"""
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')
x = np.arange(0.1, 10, 0.1)
y = np.arange(20, 100, 1)
X, Y = np.meshgrid(x, y)

zs = np.array([dwli_dml(x, 20, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
ax.plot_surface(X, Y, Z)

ax.set_xlabel('Interest Rate')
ax.set_ylabel('Age at Policy Inception')
ax.set_zlabel('Actuarial Present Value')
plt.title("Twenty Year Deferred Whole Life Insurance")
plt.show()
"""

print(adf_dml(5, 5, 20))