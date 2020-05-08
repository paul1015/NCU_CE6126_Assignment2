import numpy as np

class rbfNet(object):
    def __init__(self, thegma, weight, m, theta):

        self.theta = theta
        self.thegma = thegma
        self.m = m
        self.weight = weight


    def output (self, x):
        fx = self.add_thegma(0)
        nn = np.array([1, 1, 1])
        # print('nn = ', nn.shape)
        # print('row of m', np.size(self.m, 0))
        for i in range(np.size(self.m, 0)):
            # print('i = ', i)
            m = self.m[i:i+1, ]
            # print('in put gaussan value', m, m.shape)
            g = self.gaussan(x, i, m)
            # print('g = ', g)
            w = self.mul_weight(g, i)
            print('fx, w = ', fx, w)
            fx  = fx + w
        return fx
            

    def gaussan(self, x, i, m):
        theta = self.theta[0][i]
        print('theta = ', theta)
        n =  np.exp(-((np.sum(np.square(x-m)) / (2 * np.square(theta)))))
        return n

    def mul_weight(self, n, i):
        n = n * self.weight[0][i]
        return n

    def add_thegma(self, n):
        n = n + self.thegma[0][0]
        return n


def main():
    #set initial data
    dataset = '4d'
    print('dataset = ', dataset)
    j = 2
    swarm_num = 5
    dim = 1 + j + 3*j + j
    print('dim = ', dim)
    x = np.array([[22, 8.4, 8.4, 0]])
    ix = x[: 1, 0: 3]
    y = x[: 1, 3: ]
    print('ix, y', ix, y)
    ix = (ix - 40) /40
    y = y/40
    print('ix, y', ix, y)

    f_output = np.array([])
    # creat initial generatic set
    size = (swarm_num, dim)
    g_data = np.random.uniform(-1, 1, size)
    

    thegma = np.array([[1]])
    weight = np.array([[1,1]])
    theta = np.array([[1,1]])
    m = np.array([[1, 1, 1], [1, 1, 1]])
    
    # set input data 
    net = rbfNet(thegma, weight, m, theta)
    fx = net.output(ix)
    fx = np.array([[fx]])
    

    print('fff', f_output)
    # compute error 
    error = np.sum(fx-y)/1
    print('error = ', error)
    angle = fx * 40
    print('output_angle', angle)
    # for i in range(swarm_num):
    #     thegma = g_data[i:i+1, 0:1]
    #     print('thegma = ', thegma.shape)
    #     weight = g_data[i:i+1, 1: j+1]
    #     print('weight = ', weight.shape)
    #     theta = g_data[i:i+1, dim-j: dim]
    #     print('theta = ', theta.shape)
    #     m = g_data[i: i+1, j+1: j+1+(3*j )]
    #     m = np.reshape(m, (j, 3))
    #     print('m = ', m.shape)

    #     net = rbfNet(thegma, weight, m, theta)
    #     net.output(x)

if __name__ == "__main__":
    main()