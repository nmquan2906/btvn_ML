def grad_2(x):
    return x**2 - 1
def cost_2(x):
    return (1/3) * x**3 - x
def myGD1_2(x0,eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta * grad_2(x[-1])
        if abs(grad_2(x_new)) < 1e-3:
            break
        x.append(x_new)
        return(x, it)
(x2, it2) = myGD1_2(5, 0.1)
print('Solution x2 = %f, cost = %f, after %d iterations' % (x2[-1], cost_2(x2[-1]), it2))