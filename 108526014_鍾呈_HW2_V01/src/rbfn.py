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
    def __init__(self, swarm, err_rate, j ,dim):
        self.swarm = swarm
        self.err_rate = abs(err_rate)
        
        self.cro_rate = 0.9
        self.mut_rate = 0.9

        self.cro_theta = 0.01
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
                for j in range (50):
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
                    rand_num = np.random.uniform(0, 1, size)
                    if(rand_num >= 0.5):
                        bs0 = self.swarm[i][n] + (b1 - b0) *  self.cro_theta
                        bs1 =self.swarm[b][n] -  (b1 - b0) *  self.cro_theta 
                    else :
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
                
                for j in range (30):
                    n= random.randint(0, np.size(self.swarm[i], 0) - 1)
                    # creat noisy
                    size = (1, 1)
                    noisy = np.random.uniform(-1, 1, size)

                    # print('noisy = ', noisy, i , n )
                    mut_n = self.swarm[i][n] + noisy * self.mut_s
                    # print('n = ', n, self.dim , self.j ,mut_n)
                    if(n >= self.dim - self.j ):
                        # print('n in = ', n, mut_n)
                        if(mut_n >= 0):
                            # print("n non minus")
                            self.swarm[i][n] = mut_n
                        # else :
                        #     # print("n minus")
                        #     self.swarm[i][n] = 0.001
                    else :
                        self.swarm[i][n] = mut_n

                    # print('mut swarm', self.swarm)

def main():
    # set initial data
    dataset = '4d'
    print('dataset = ', dataset)
    j = 20
    swarm_num = 60
    epoch_num = 100
    train_barch = 5
    dim = 1 + j + 3*j + j
    print('dim = ', dim)

    # sigle data
    # 09.7355, 10.9379, 18.5740, -40.000
    # 26.7355, 09.0238, 08.6122, 000.000
    # 11.5011, 20.8353, 11.1280, 40.000

    x = np.array([[09.7355, 10.9379, 18.5740, -40.000]])
    ix = x[: 1, 0: 3]
    y = x[: 1, 3: ]
    print('ix, y', ix, y)
    # normalize data
    # ix = (ix - 40) /40
    # y = y/40
    print('ix, y', ix, y)

    # multiple data 
    #讀取檔案資料
    f = open(r'testFile.txt')
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
        if(i == 10):
            break
        
        
    print('i = ', i)
    print('shpae of xx , yy = ', xx.shape, yy.shape)
    # xx = (xx - 40)/40
    # yy = yy/40
    # creat initial generatic set
    size = (swarm_num, dim)
    g_data = np.random.uniform( 20, -20, size)
    # print('g_data = ', g_data)
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
    for epoch  in range (epoch_num):
        print('e = ', epoch)
        for b in range (num_x):
            # bx = xx[b:b+train_barch, : ]
            # by = yy[b:b+train_barch, :]
            bx = xx[b: b+ 1:, :]
            # print('by = > ', b,by)
            for i in range(swarm_num):
                g_data[i:i+1, dim-j: dim] = abs(g_data[i:i+1, dim-j: dim])
                # print('e, i = ', e, i)
                thegma = g_data[i:i+1, 0:1]
                # print('thegma = ', thegma.shape)
                weight = g_data[i:i+1, 1: j+1]
                # print('weight = ', weight.shape)
                theta = g_data[i:i+1, dim-j: dim]
                # print('theta = ', theta)
                m = g_data[i: i+1, j+1: j+1+(3* j )]
                m = np.reshape(m, (j, 3))
                # print('m = ', m.shape)

                # set batch input data
                net = rbfNet(thegma, weight, m, theta)
                # for bb in range  (num_x):
                #     # print('k = ', k)
                #     # print('input data = ', xx[k:k+1, : ])
                #     f_total = net.output(bx[bb:bb+1, : ])
                #     f_total= np.array([[f_total]])

                #     if(bb == 0):
                #         f_b = np.array(f_total)
                #     else :
                #         f_b = np.append(f_b, np.array(f_total), axis=0)

                # error = np.sum(abs(f_b - yy))/num_x
                # if(i == 0):
                #     err_rate = np.array([[error]])
                # else :
                #     err_rate = np.append(err_rate, np.array([[error]]), axis=0)
               
                # single input
                # print('bx = ', bx)
                fx = net.output(bx)
                fx = np.array([[fx]])
                error = np.sum(abs(fx - yy[b]))/1
                # print('error => ', error)
                if(i == 0):
                    err_rate = np.array([[error]])
                else :
                    err_rate = np.append(err_rate, np.array([[error]]), axis=0)
                # # single error
                # print('fx yy => ', epoch, i,fx, yy[b])
                # error = np.sum(fx - yy[b])/1
                # if(i == 0):
                #     err_rate = np.array([[error]])
                # else :
                #     err_rate = np.append(err_rate, np.array([[error]]), axis=0)

                # check total error rate input
                for k in range  (num_x):
                    # print('k = ', k)
                    # print('input data = ', xx[k:k+1, : ])
                    f_total = net.output(xx[k:k+1, : ])
                    f_total= np.array([[f_total]])

                    if(k == 0):
                        fout = np.array(f_total)
                    else :
                        fout = np.append(fout, np.array(f_total), axis=0)

                # print('output = ', fout, yy, num_x)

                # compute error 
                # multiple output
                error_total = np.sum(abs(fout-yy))/num_x
                if(error_total < best_err):
                    best_err  = error_total
                    best_var = g_data[i]
                    pre_angle = fout
                    best_epoch = epoch
                if(i == 0):
                    error_t = np.array([[error_total]])
                else :
                    error_t = np.append(err_rate, np.array([[error_total]]), axis=0)
                

            # put data and error rate in geneticOptimizer
            # print('error_rate = ', err_rate, epoch)
            g_opt = geneticOptimizer(g_data, err_rate, j,  dim)

            # update variable 
            g_data = g_opt.genatic_opt()
            # print('undpte_swarm = ', undpte_swarm)
            # print('best -->', best_err, best_angle, best_var)


        print('epoch best --> ', best_err, best_var, pre_angle, best_epoch, pre_angle.shape, j, dim)
        
    print('global best --> ', best_err, best_var, pre_angle, best_epoch)
    

if __name__ == "__main__":
    main()