import numpy as np

class RbfNet(object):
    def __init__(self, theta, thegma, weight):
        self.value = 1
        self.theta = theta
        self.thegma = thegma
        self.weight = weight

    def gaussian (self,x, m):

        n =  np.exp(-((np.sum(np.square(x-m)) / (2 * np.square(self.theta)))))
        n = self.mul_weight(n)
        n = self.add_thegma(n)

        return n
    
    def mul_weight(self, n):
        n = n * self.weight
        return n

    def add_thegma(self, n):
        n = n + self.thegma
        return n


def main():
    x = np.array([-0.45, -0.79, -0.79])
    m = np.array([1, 1, 1])

    theta = np.array([1])
    thegma = np.array([1])
    weight = np.array([1])

    rbfn = RbfNet(theta, thegma, weight)
    g = rbfn.gaussian(x, m)

    print('g = ', g)

    dataset = '4d'
    print('dataset = ', dataset)
    j = 2
    swarm_num = 5
    dim = 1 + j + 3*j + j

    print('dim = ', dim)
    size = (swarm_num, dim)
    g_data = np.random.uniform(-1, 1, size)
    print('g_data = ', g_data.shape, g_data)
    for i in range(swarm_num):
        thegma = g_data[i:i+1, 0:1]
        print('thegma = ', thegma)
        weight = g_data[i:i+1, 1: j+1]
        print('weight = ', weight)
        theta = g_data[i:i+1, dim-j: dim]
        print('theta = ', theta)
        m = g_data[i: i+1, j+1: j+1+(3*j )]
        m = np.reshape(m, (j, 3))
        print('m = ', m)

if __name__ == "__main__":
    main()