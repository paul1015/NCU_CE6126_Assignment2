from tkinter import *
import tkinter as tkinter
import math as math
import time

#圖片的 軸是從左上角開始 x 是正 y 是負 
#theta car_angle

class car:
    #  初始化資料 主要是輸入座標和實際座標上的轉換
    def __init__(self, zero_x, zero_y, multiply_x, multiply_y, car_x, car_y, car_angle , car_r=3, car_collar="red"):
        self.zero_x = zero_x
        self.zero_y = zero_y
        self. multiply_x = multiply_x
        self. multiply_y = multiply_y
        self.car_x = zero_x + car_x * multiply_x
        self.car_y = zero_y + (car_y * -1 )*multiply_y
        self.car_r = car_r
        self.car_collar = car_collar
        self.car_orangle = car_angle
        self.car_angle = round(math.radians(car_angle),2)
        self.direction = 0
        self.ldirection = 0
        self.rdirection = 0
        self.ld = 0
        self.rd = 0
        self.d = 0
        self.b = car_r * multiply_x
        self.x1 = zero_x + -6 * multiply_x
        self.x2 = zero_x + 6 * multiply_x
        self.x3 = zero_x + 18 * multiply_x
        self.x4 = zero_x + 30 * multiply_x
        self.y1 = zero_y + -10 * multiply_y
        self.y2 = zero_y + -22* multiply_y
        self.y3 = zero_y + -50 * multiply_y
        self.g1 = zero_y + -40 * multiply_y
        self.g2 = zero_y + -37 * multiply_y

    #畫線 方程式
    def create_line(self, x1, y1, x2, y2, color):
        return canvas.create_line(zero_x+x1*multiply_x, zero_y+(y1*-1)*self.multiply_y,
                           zero_x+x2*multiply_x, zero_y+(y2*-1)*self.multiply_y, fill=color, width=3)
    #畫車方程式
    def create_car(self):  
        
        # center coordinates, radius

        x0 = self.car_x - self.car_r*self.multiply_x
        y0 = self.car_y - self.car_r*self.multiply_y
        x1 = self.car_x + self.car_r*self.multiply_x
        y1 = self.car_y + self.car_r*self.multiply_y

        

        return canvas.create_oval(x0, y0, x1, y1, fill=self.car_collar)
    
    #觀測距離方程式 針對每個邊界 做判斷取最小的值
    def sensor_distace(self, angle) :
        #sensor  sensor + angle judge
        x1d = (abs(self.car_x - self.x1 ) * -1 * (1/ math.cos(angle)))
        x1dc = abs((self.car_x - self.x1 ) * (math.tan(angle)))
        
        if(self.car_y - x1dc <= self.y2 or x1d < 0):
            #設為最大值
            x1d = 10000

        else :

            x1d = x1d / self.multiply_x
        
        #print('x1d', x1d)
        
        x2d = (abs(self.car_x - self.x2 ) * (1/ math.cos(angle)))
        x2dc = (abs(self.car_x - self.x2 ) * (math.tan(angle)))
        
        
        if(self.car_y - x2dc <= self.y1 or x2d < 0):
            #設為最大值
            x2d = 10000
            
        else :
            x2d = x2d / self.multiply_x
        
        #print('x2d', x2d)

        x3d = (abs(self.car_x - self.x3 ) * -1 *(1/ math.cos(angle)))
        x3dc = abs((self.car_x - self.x3 ) * (math.tan(angle)))
        
        #print('???? ', x3d, x3dc, self.car_y, self.y1)
        if(self.car_y - x3dc <= self.y3 or x3d < 0):
            #設為最大值
            x3d = 10000
            
        else :
            
            x3d = x3d / self.multiply_x
        
        #print('x3d', x3d)

        x4d = (abs(self.car_x - self.x4 )  * (1/ math.cos(angle)))
        x4dc = abs((self.car_x - self.x4 ) * (math.tan(angle)))
        
        if(self.car_y - x4dc <= self.y3 or x4d < 0):
            #設為最大值
            x4d = 10000
            
        else :
           
            x4d = x4d / self.multiply_x
        
        #print('x4d', x4d)

        y2d = (abs(self.car_y - self.y2) * (1/ math.sin(angle)))
        y2dc = abs((self.car_y - self.y2 ) * abs(1/math.tan(angle)))

        if(self.car_x + y2dc >= self.x3 or y2d < 0 ):
            y2d = 10000
        else :
            y2d = y2d / self.multiply_y
        
        #print('y2d', y2d)

        y1d = (abs(self.car_y - self.y1) * -1 * (1/ math.sin(angle)))
        y1dc = abs((self.car_y - self.y1 ) * (1/math.tan(angle)))

        
        if(self.car_x + y1dc <= self.x2 or y1d < 0):
            y1d = 10000
        else :
            y1d = y1d / self.multiply_y
        
        #print('y1d', y1d)

        
        y3d = (abs(self.car_y - self.y3) * (1/ math.sin(angle)))
        y3dc = abs((self.car_y - self.y3 ) * abs(1/math.tan(angle)))

        if(self.car_x + y3dc >= self.x4 or y3d < 0 ):
            y3d = 10000
        else :
            y3d = y3d / self.multiply_y
        
        #print('y3d', y3d)

        #print('d ', min(x1d, x2d, x3d, x4d, y1d, y2d, y3d))
        d = min(x1d, x2d, x3d, x4d, y1d, y2d, y3d)
        if(d <= 3):
            return 0
        else :
            return d
    #邊界距離觀測
    def distance(self) :
        
        d1 = 100
        d2 = 100
        d3 = 100
        d4 = 100
        d5 = 100
        d6 = 100
        d7 = 100
        if(self.car_x < 6):
            d1 = abs (self.car_x - self.x1)
            d2 = abs (self.car_x - self.x2)
            d6 = abs (self.car_y - self.y2)
        elif(self.car_x < 18):
            d1 = abs (self.car_x - self.x1)
            d4 = abs (self.car_x - self.x4)
            d5 = abs (self.car_y - self.y1)
            d6 = abs (self.car_y - self.y2)
        else :
            d3 = abs (self.car_x - self.x3)
            d4 = abs (self.car_x - self.x4)
            d5 = abs (self.car_y - self.y1)
            d4 = abs (self.car_y - self.y3)

        print('distance', d1, d2, d3, d4, d5, d6, d7)
        return min(d1, d2, d3, d4, d5, d6, d7)

    #終點線觀測
    def goalLine(self):

        #goal line distance
        if(self.car_x >= self.x3 and self.car_x <= self.x4): 
            x = ( self.car_x - zero_x ) / self.multiply_x
            d =  -1 * (x )/4  +  (44.5 )
            y = -1 *(self.car_y - zero_y) / self.multiply_y
            print('goal d = ', d, y)
            return d - y
        else: 
            return -1
            
    #車子移動 -> 儲存目前車子所在數據, 回傳sensor 數據
    def car_move(self, tk, car, theta):
        
        degree = theta
        #角度換算
        theta = round(math.radians(theta),2)

        #car momenton
        self.car_x = self.car_x + 10*(math.cos(self.car_angle) * math.cos(theta)) 
        self.car_y = self.car_y -  10*(math.sin(self.car_angle) * math.cos(theta))
        self.car_angle = self.car_angle - math.asin(2 * math.sin(theta) / self.car_r)

    
        x0 = self.car_x - self.car_r*self.multiply_x
        y0 = self.car_y - self.car_r*self.multiply_y
        x1 = self.car_x + self.car_r*self.multiply_x
        y1 = self.car_y + self.car_r*self.multiply_y

       
        
        #draw the car
        tk.coords(car, (x0, y0, x1, y1))

        canvas.delete(self.direction)
        canvas.delete(self.ldirection)
        canvas.delete(self.rdirection)
        # direction line 
        #car_x = zero_x + car_x * multiply_x
        #car_y = zero_y + (car_y * -1 )*multiply_y
        car_x1 =  (self.car_x - self.zero_x) / self.multiply_x
        car_y1 = (self.car_y  - self.zero_y) / self.multiply_y * -1
        
        
        x2 = car_x1 + 6* math.cos(self.car_angle)
        y2 = car_y1 + 6* math.sin(self.car_angle)

        
        #draw the direction line
        self.direction = self.create_line(car_x1, car_y1, x2, y2, "red")

        #compute the sensor angle
        round(math.radians(car_angle),2)
        langle =   self.car_angle + round(math.radians(45),2)
        rangle = self.car_angle - round(math.radians(45),2)

        #draw the the sensor line
        x2 = car_x1 + 6* math.cos(langle )
        y2 = car_y1 + 6* math.sin(langle ) 
        self.ldirection = self.create_line(car_x1, car_y1, x2, y2, "black")

        x2 = car_x1 + 6* math.cos(rangle )
        y2 = car_y1 + 6* math.sin(rangle ) 
        self.rdirection = self.create_line(car_x1, car_y1, x2, y2, "black")
        
        #sensor part
        #往回開就是腦袋開抽
        #boundary base

        d = self.sensor_distace(self.car_angle)
        ld = self.sensor_distace(langle)
        rd = self.sensor_distace(rangle)
        gd = self.goalLine()
        dd = self.distance()
      

        if(d == 0.1 or ld == 0.1 or rd == 0.1):
            canvas.delete(self.d)
            canvas.delete(self.ld)
            canvas.delete(self.rd)
            dw = Label(canvas, text = 'stop', fg='white', bg='black')
            dw.pack()
            canvas.create_window(100, 100, window=dw)

        else :
        
            dw = Label(canvas, text = 'd : ' + str(d), fg='white', bg='black')
            dw.pack()
            self.d = canvas.create_window(100, 100, window=dw)
        
            ldw = Label(canvas, text = 'ld : ' + str(ld), fg='white', bg='black')
            ldw.pack()
            self.ld = canvas.create_window(100, 75, window=ldw)
        
            rdw = Label(canvas, text = 'rd : ' + str(rd), fg='white', bg='black')
            rdw.pack()
            self.rd = canvas.create_window(100, 125, window=rdw)
        
        #self.car_x = zero_x + car_x * multiply_x
        #self.car_y = zero_y + (car_y * -1 )*multiply_y
        x = (self.car_x - zero_x)/self.multiply_x
        y = (self.car_y - zero_y)/self.multiply_y * -1
        
        # 開啟檔案
        fp = open("train6D.txt", "a")
 
        #寫入檔案
        p = str(x) + " " + str(y) + " " + str(d) + " " + str(rd) + " " + str(ld) + " " + str(degree) + "\n"
        fp.write(p)
 
        # 關閉檔案
        fp.close()

        fp = open("train4D.txt", "a")
 
        # 寫入檔案
        p = str(d) + " " + str(rd) + " " + str(ld) + " " + str(degree) + "\n"
        fp.write(p)
 
        # 關閉檔案
        fp.close()

        return (d, ld, rd, gd, dd)

    #模糊演算法
    def fuuzzyRule(self, d, ld, rd):
        #d1, d2 兩個模糊規則判定
        d1 = d
        d2 = ld - rd 
        d1a = 1
        d2a = 1
        al = 25
        am = 40
        ar = 70
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0 
        a5 = 0
        a6 = 0
        a7 = 0
        a8 = 0
        a9 = 0
        #d1 is large 
        if(d1 >= 15 ):
            if(d1 < 20 ):
                d1a = 1 * (d1 - 15) / 5
            if(d2 >= 0):
                if(d2 < 8):
                    d2a = 1 * (d2 - 0) / 8
                a1 = min(d1a, d2a)
            if(d2 < 8 and d2 >= -8):
                if(d2 > 0):
                    d2a = 1 * (8- d2) / 8
                else :
                    d2a = 1 * (d2 + 8) / 8
                a2 = min(d1a, d2a)
            if(d2 < 0):
                if(d2 < -8):
                    d2a = 1 * abs(d2) / 8
                a3 = min(d1a, d2a)
        #d1 is middle
        if(d1 < 20 and d1 >= 10 ):
            if(d1 >= 15 ):
                d1a = 1 * (20-d1) / 5
            else:
                d1a = 1 * (d1 - 10) / 5
            if(d2 >= 0):
                if(d2 < 8):
                    d2a = 1 * (d2 - 0) / 8
                a4 = min(d1a, d2a)
            if(d2 < 8 and d2 >= -8):
                if(d2 > 0):
                    d2a = 1 * (8- d2) / 8
                else :
                    d2a = 1 * (d2 + 8) / 8
                a5 = min(d1a, d2a)
            if(d2 < 0):
                if(d2 < -8):
                    d2a = 1 * abs(d2) / 8
                a6 = min(d1a, d2a)
        #d1 is small
        if(d1 < 15):
            if(d1 >= 10 ):
                d1a = 1 * (15-d1) / 5
            
            if(d2 >= 0):
                if(d2 < 8):
                    d2a = 1 * (d2 - 0) / 8
                a7 = min(d1a, d2a)
            if(d2 < 8 and d2 >= -8):
                if(d2 > 0):
                    d2a = 1 * (8- d2) / 8
                else :
                    d2a = 1 * (d2 + 8) / 8
                a8 = min(d1a, d2a)
            if(d2 < 0):
                if(d2 < -8):
                    d2a = 1 * abs(d2) / 8
                a9 = min(d1a, d2a)
        print('a', a1, a2, a3, a4, a5, a6, a7,a8, a9)

        #final output
        output = (a1 * al + a2 * am + a3 *ar +  a4 * al + a5 * am + a6 * am + a7 * al + a8 * am + a9 * ar ) / (a1 + a2 + a3 + a4 + a5 + a6 + a7 +a8 + a9)
        print('return angle ', output - 40)
        return (output - 40)
   
        
        
       


# Initial Form 
tk = Tk()
tk.title('assignment1')
tk.resizable(0, 0)


#Intial Value
width = 500
height = 500

multiply_x = width/60
multiply_y = height/60
zero_x = int(width/4)
zero_y = int(height/1.1)

#讀取檔案資料
f = open(r'case01.txt')
i = 0
for line in f:
    s = line.split(",")
    if(i == 0):
        print('line s ', s)
        car_x = int(s[0])
        car_y = int(s[1])
        car_angle = int(s[2])

    i = i + 1

        
car = car(zero_x, zero_y, multiply_x, multiply_y, car_x, car_y, car_angle)

canvas = Canvas(tk, width=width, height=height, bg='ivory')
canvas.pack(fill=BOTH, expand=1)
canvas.pack()
#讀兩次檔
f = open(r'case01.txt')
i = 0
x1 = 0
y1 = 0 
x2 = 0 
y2 = 0
for line in f:
    s = line.split(",")
    if(i > 0) :
        if(i % 2 != 0):
            x1 = int(s[0])
            y1 = int(s[1])
        else :
            x2 = int(s[0])
            y2 = int(s[1])
    if(i == 2) : 
        print('goal', x1, y1, x2, y2)
        car.create_line(x1, y1, x2, y2, "red")

    if(i > 3):
        car.create_line(x1, y1, x2, y2, "blue")

    i = i + 1

# CAR
car_obj = car.create_car()

#起跑線 0,0
car.create_line(-12, 0, 12, 0, "black")

t = 0


#初始角度 為 0
d,ld,rd,gd, dd = car.car_move(canvas, car_obj, 0)

dd = 100

while 1:
    
    if(gd == -1):
        gd = 100
    if(gd >= 3 and dd >=3):
        print("t  = ", t)
        #fuzzy system
        t = car.fuuzzyRule(d, ld, rd)
        #move based on fuzzy system
        d,ld,rd,gd, dd = car.car_move(canvas, car_obj, t)
        time.sleep(0.7)
        tk.update()
        canvas.update()
    else :
        print('Stop')
        break
        

