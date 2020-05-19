import numpy as np
import random
import sys
# np.set_printoptions(threshold=sys.maxsize)
# rbfn Net
class rbfNet(object):
    def __init__(self, thegma, weight, m, theta):

        self.theta = theta
        self.thegma = thegma
        self.m = m
        self.weight = weight


    def output (self, x):
        fx = self.add_thegma(0)
        # print('nn = ', nn.shape)
        # print('row of m', np.size(self.m, 0))
        for i in range(np.size(self.m, 0)):
            # print('i = ', i)
            m = self.m[i:i+1, ]
            # print('in put gaussan value', m, m.shape)
            g = self.gaussan(x, i, m)
            # print('g = ', g)
            w = self.mul_weight(g, i)
            # print('fx, w = ', fx, w)
            fx  = fx + w
            # print('return value = ', fx)
        return fx          

    def gaussan(self, x, i, m):
        theta = self.theta[0][i]
        # print('theta = ', theta, m.shape)
        n =  np.exp(-((np.sum(np.square(x-m)) / (2 * np.square(theta)))))
        return n

    def mul_weight(self, n, i):
        weight = self.weight[0][i]
        # print('weight = ', weight, n.shape)
        n = n * weight
        return n

    def add_thegma(self, n):
        n = n + self.thegma[0][0]
        return n

# geneticOptimizer
class geneticOptimizer(object):
    def __init__(self, swarm, err_rate, j, dim):
        self.swarm = swarm
        self.err_rate = abs(err_rate)
        
        self.cro_rate = 0.9
        self.mut_rate = 0.9

        self.cro_theta = 0.1
        self.mut_s = 20
        self.j = j
        self.dim = dim
        
    # reproducation by random noisy add  roulette decision ignore
    def genatic_opt(self):

        self.reproduction()
        self.crossover()
        self.mutation()
        
        return self.swarm

    # reproducation
    def reproduction(self):
        # print('self.swarm = ', self.swarm.shape)
        # error_rate = np.sort(self.err_rate , axis=0)
        # print('error_rate = ', error_rate)

        y = np.argsort(self.err_rate , axis=0) 
        # print('y = ', y)
        # print('y error rate = ')
        k = 0
        for i in (y): 
            # print('i = ', i)
            int_i = int(i[0])
            # print('int_i', int_i)
            a = self.swarm[int_i: int_i + 1, :]
            # print('a= ', a)
            if(k == 0):
                for i in range (10):
                    if(i == 0 ):
                        b = a 
                    else :
                        b = np.append(b, a, axis=0)
            else :
                 for i in range (10):
                     b = np.append(b, a, axis=0)
            k = k + 1
            if(k == np.size(self.err_rate, 0)/10): 
                break
        # print('b = ', b.shape)
        self.swarm = b
    
    #crossover
    def crossover (self):
        for i in range (np.size(self.err_rate, 0)):
            # print('i = ', i)
            size = (1, 1)
            rand_num = np.random.uniform(0, 1, size)
            # print('rand ', rand_num, self.cro_rate)
            if(rand_num < self.cro_rate):
                # print('choose b', b)
                # two point croosover
                for j in range (10):
                    n= random.randint(0, np.size(self.swarm[0], 0) - 1 )
                
                    b = random.randint(0, np.size(self.err_rate, 0) - 1 )
                    # print('np_size ', np.size(self.swarm[0], 0), np.size(self.err_rate, 0))
                    # print('n = ', n)
                    # cross over part 
                    # print('i b n ', i,  b,  n)
                    # print('self.swarm', self.swarm)
                    b0 = self.swarm[i][n]
                    b1 = self.swarm[b][n]
                    # print('b0 b1', b0, b1)
                    bs0 = self.swarm[i][n] + (b0 - b1) *  self.cro_theta
                    bs1 =self.swarm[b][n] -  (b0 - b1) *  self.cro_theta 
                    # print('bs0 bs1', bs0, bs1)
                    if(n >= self.dim - self.j ):
                        if(bs0 >= 0):
                            self.swarm[i][n] = bs0
                        # else :
                        #     self.swarm[b[0]][n] = bs0
                        if(bs1 >= 0):
                            self.swarm[b][n] = bs1
                        # else :
                        #     self.swarm[b[0]][n] = bs1

                    else :
                        self.swarm[i][n] = bs0
                        self.swarm[b][n] = bs1
                    # print('cross self.swarm', self.swarm)

                # if(k == 0):
                #     rep_swarm = np.array([self.swarm[j][:]])
                #     # print('rep 0 = ', rep_swarm)
                #     k = 1
                # else :
                #     rep_swarm = np.append(rep_swarm, np.array([self.swarm[j][:]]), axis=0)
                #     # print('rep 1 = ', rep_swarm)
    # mutation 
    def mutation (self):
        for i in range (np.size(self.err_rate, 0)):
            size = (1, 1)
            rand_num = np.random.uniform(0, 1, size)
            if(rand_num < self.mut_rate):
                
                for j in range (5):
                    n= random.randint(0, np.size(self.swarm[i], 0) - 1)
                    # creat noisy
                    size = (1, 1)
                    noisy = np.random.uniform(-1, 1, size)
                    print('n = ', n, self.swarm[i][n])
                    # print('noisy = ', noisy, i , n )
                    mut_n = self.swarm[i][n] + noisy * self.mut_s
                    print('mut_n', mut_n)
                    # print('n = ', n, self.dim , self.j ,mut_n)
                    if(n >= self.dim - self.j ):
                        # print('n in = ', n, mut_n)
                        if(mut_n >= 0):
                            # print("n non minus")
                            self.swarm[i][n] = mut_n
                        # else :
                        #     # print("n minus")
                        #     self.swarm[i][n] = 0
                    else :
                        self.swarm[i][n] = mut_n

                    # print('mut swarm', self.swarm)


def main():
    # set initial data
    dataset = '4d'
    print('dataset = ', dataset)
    j = 1
    swarm_num = 50
    epoch_num = 10
    dim = 1 + j + 3*j + j
    print('dim = ', dim)

    # 09.7355, 10.9379, 18.5740, -40.000
    # 26.7355, 09.0238, 08.6122, 000.000
    # 11.5011, 20.8353, 11.1280, 40.000

    # sigle data
    x = np.array([[26.7355, 09.0238, 08.6122, 000.000]])
    ix = x[: 1, 0: 3]
    y = x[: 1, 3: ]
    print('ix, y', ix, y)
    # normalize data
    # ix = (ix - 40) /40
    # y = y/40
    print('ix, y', ix, y)

    # multiple data 
    #讀取檔案資料
    f = open(r'train4dAll.txt')
    i = 0
    for line in f:
        s = line.split(" ")
        # print('line s ', s)
        d = float(s[0])
        ld = float(s[1])
        rd = float(s[2])
        car_angle = float(s[3].split('\n')[0])
        # print('car information = ', d, ld, rd, car_angle)
        if(i == 0):
            xx = np.array([[d, ld, rd]])
            yy = np.array([[car_angle]])
        else :
            xx = np.append(xx, np.array([[d, ld, rd]]), axis=0)
            yy = np.append(yy, np.array([[car_angle]]), axis=0)

        i = i + 1
        if(i == 50) :
            break
    print('i = ', i)
    print('shpae of xx , yy = ', xx.shape, yy.shape)
    # xx = (xx - 40)/40
    # yy = yy/40
    # creat initial generatic set
    size = (swarm_num, dim)
    g_data = np.random.uniform(-1, 1, size)
    print('g_data = ', g_data)
    # print('g_data = ', g_data)
    
    # authntication rbfNet used
    # thegma = np.array([[1]])
    # weight = np.array([[1,1]])
    # theta = np.array([[1,1]])
    # m = np.array([[1, 1, 1], [1, 1, 1]])
    
    # net = rbfNet(thegma, weight, m, theta)
    # fx = net.output(ix)
    # fx = np.array([[fx]])
    
    # error = np.sum(fx-y)/1
    # print('error = ', error)
    # angle = fx * 40
    # print('output_angle', angle)
    num_x = i 
    best_err = 100
    best_var = 100
    for e in range (epoch_num):
        print('e = ', e)
        for i in range(swarm_num):
            g_data[i:i+1, dim-j: dim] = abs(g_data[i:i+1, dim-j: dim] / 10)
            # print('e, i = ', e, i)
            thegma = g_data[i:i+1, 0:1]
            # print('thegma = ', thegma.shape)
            weight = g_data[i:i+1, 1: j+1]
            # print('weight = ', weight.shape)
            theta = np.absolute(g_data[i:i+1, dim-j: dim])
            # print('theta = ', theta.shape)
            m = g_data[i: i+1, j+1: j+1+(3*j )]
            m = np.reshape(m, (j, 3))
            # print('m = ', m.shape)

            # set input data
            net = rbfNet(thegma, weight, m, theta)
            # single input

            fx = net.output(ix)
            fx = np.array([[fx]])

            # multuple input
            # for k in range  (num_x):
            #     # print('k = ', k)
            #     # print('input data = ', xx[k:k+1, : ])
            #     fx = net.output(xx[k:k+1, : ])
            #     fx = np.array([[fx]])

            #     if(k == 0):
            #         fout = np.array(fx)
            #     else :
            #         fout = np.append(fout, np.array(fx), axis=0)

            # print('output = ', fout, yy, num_x)

            # compute error 
            # multiple output
            # error = np.sum(abs(fout-yy))/num_x
            # print('fx, y', fx, y)

            # single error
            error = np.sum(fx-y)/1
            # print('error = ', abs(error))

            # save error as fitness function
            
            if(i == 0):
                err_rate = np.array([[error]])
            else :
                err_rate = np.append(err_rate, np.array([[error]]), axis=0)
                
            # angle = fx * 40
            # print('output_angle = ', angle)
            if(abs(error) < best_err):
                print('error update =>  ', abs(error), g_data[i:i+1, :])
                best_err = abs(error)
                best_var = g_data[i:i+1, :]
                # best_angle = fout
                best_angle = fx
                prdict_angle = y



        # print('error rate = ',  err_rate)
        # print('best -->', best_err, best_var, best_angle, prdict_angle)
        # put data and error rate in geneticOptimizer
        # print('input genatic = ', err_rate)
        g_opt = geneticOptimizer(g_data, err_rate, j, dim)

        #update variable 
        g_data = g_opt.genatic_opt()
        # print('undpte_swarm = ', undpte_swarm)
        # print('best -->', best_err, best_angle, best_var)
        

    print('best --> ', best_err, best_var)
    print('best angle --> ', best_angle)
    print('predict angle --> ', prdict_angle)
    

if __name__ == "__main__":
    main()
