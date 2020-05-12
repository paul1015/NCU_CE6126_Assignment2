import numpy as np
import random

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
        return fx          

    def gaussan(self, x, i, m):
        theta = self.theta[0][i]
        # print('theta = ', theta)
        n =  np.exp(-((np.sum(np.square(x-m)) / (2 * np.square(theta)))))
        return n

    def mul_weight(self, n, i):
        n = n * self.weight[0][i]
        return n

    def add_thegma(self, n):
        n = n + self.thegma[0][0]
        return n

# geneticOptimizer
class geneticOptimizer(object):
    def __init__(self, swarm, err_rate):
        self.swarm = swarm
        
        self.rep_rate = 0.3
        self.cro_rate = 0.5
        self.mut_rate = 0.4

        # err_rate to fitness function

        fitness = np.abs(err_rate)
        fitness = 1 - fitness 
        sum_fit = np.sum(fitness)
        fitness = fitness/ sum_fit

        # print('fitness = ', fitness, np.sum(fitness), np.size(fitness, 0))
        self.fitness = fitness
        
    # reproducation by random noisy add  roulette decision ignore
    def genatic_opt(self):

        self.reproduction()
        self.crossover()
        self.mutation()
        
        return self.swarm

    # reproducation
    def reproduction(self):
        self.swarm = self.swarm
        #  roulette
        # ignore probability
        # for i in range(np.size(fitness, 0)):
            
        
        # add noisy
        # noisy = 0.3
        # k = 0
        # l = np.size(self.swarm[0][:], 0)
        # print('l = ', l)
        # mod = l % 3
        # print('mod = ', mod)
        # for i in range (np.size(self.fitness, 0)):
        #     if(k == 0):
        #         print('self.swarm = ', self.swarm[i][0: mod + 1])
        #         self.swarm[i][0: mod + 1] = self.swarm[i][0: mod + 1] + self.swarm[i][0: mod + 1]
        #         self.swarm[i][:]
        #         k = 1

        #     else :
        #         rep_swarm = np.append(rep_swarm, np.array([self.swarm[i][:]]), axis=0)
                
        # print('rep_swarm', self.swarm)  
    
    #crossover
    def crossover (self):
        for i in range (np.size(self.fitness, 0)):
            # print('i = ', i)
            size = (1, 1)
            rand_num = np.random.uniform(0, 1, size)
            # print('rand ', rand_num, self.cro_rate)
            if(rand_num < self.cro_rate):
                
                b = np.random.randint(0,self.swarm.shape[0],2)
                # print('choose b', b)
                # two point croosover
                for j in range (2):
                    n= random.randint(0, np.size(self.swarm[0], 0) - 1 )
                    # print('n = ', n)
                    # cross over part 
                    reg_val = self.swarm[b[0]][n]
                    self.swarm[b[0]][n] = self.swarm[b[1]][n]
                    self.swarm[b[1]][n] = reg_val
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
        for i in range (np.size(self.fitness, 0)):
            size = (1, 1)
            rand_num = np.random.uniform(0, 1, size)

            if(rand_num < self.mut_rate):
                n= random.randint(0, np.size(self.swarm[i], 0) - 1)
                # creat noisy
                size = (1, 1)
                noisy = np.random.uniform(-1, 1, size)

                # print('noisy = ', noisy, i , n )
                self.swarm[i][n] = self.swarm[i][n] + noisy

                # print('mut swarm', self.swarm)

def main():
    # set initial data
    dataset = '4d'
    print('dataset = ', dataset)
    j = 10
    swarm_num = 50
    epoch_num = 100
    dim = 1 + j + 3*j + j
    print('dim = ', dim)

    # sigle data
    x = np.array([[22, 8.4, 8.4, 0]])
    ix = x[: 1, 0: 3]
    y = x[: 1, 3: ]
    print('ix, y', ix, y)
    # normalize data
    ix = (ix - 40) /40
    y = y/40
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
    print('i = ', i)
    print('shpae of xx , yy = ', xx.shape, yy.shape)
    xx = (xx - 40)/40
    yy = yy/40
    # creat initial generatic set
    size = (swarm_num, dim)
    g_data = np.random.uniform(-1, 1, size)
    
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
    best_err = 1
    for e in range (epoch_num):
        for i in range(swarm_num):
            thegma = g_data[i:i+1, 0:1]
            # print('thegma = ', thegma.shape)
            weight = g_data[i:i+1, 1: j+1]
            # print('weight = ', weight.shape)
            theta = g_data[i:i+1, dim-j: dim]
            # print('theta = ', theta.shape)
            m = g_data[i: i+1, j+1: j+1+(3*j )]
            m = np.reshape(m, (j, 3))
            # print('m = ', m.shape)

            # set input data
            net = rbfNet(thegma, weight, m, theta)

            for k in range  (num_x):
                # print('k = ', k)
                # print('input data = ', xx[k:k+1, : ])
                fx = net.output(xx[k:k+1, : ])
                fx = np.array([[fx]])

                if(k == 0):
                    fout = np.array(fx)
                else :
                    fout = np.append(fout, np.array(fx), axis=0)

            # print('output = ', fout.shape, yy.shape, num_x)

            # compute error 
            error = np.sum(fout-yy)/num_x
            # print('error = ', abs(error))

            # save error as fitness function
            
            if(i == 0):
                err_rate = np.array([[error]])
            else :
                err_rate = np.append(err_rate, np.array([[error]]), axis=0)
                
            # angle = fx * 40
            # print('output_angle = ', angle)
            if(abs(error) < best_err):
                best_err = abs(error)
                best_var = g_data[i]



        # print('error rate = ',  err_rate)

        # put data and error rate in geneticOptimizer
        g_opt = geneticOptimizer(g_data, err_rate)

        #update variable 
        g_opt.genatic_opt()
        # print('undpte_swarm = ', undpte_swarm)
        # print('best -->', best_err, best_angle, best_var)
        print('best -->', best_err, best_var)

    print('best final err = ', best_err, best_var)

if __name__ == "__main__":
    main()