def grad_1(x):
    return 2 * x

def cost_1(x):
    return x**2 - 2

def myGD1_1(x0, eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta * grad_1(x[-1])
        if abs(grad_1(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)

(x1, it1) = myGD1_1(5, 0.1)
print('Solution x1 = %f, cost = %f, after %d iterations' % (x1[-1], cost_1(x1[-1]), it1))