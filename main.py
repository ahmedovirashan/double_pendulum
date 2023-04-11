# Двойной маятник
#
# Уравнения системы:
# Y1' = y2
# Y2' = (c2*c3*y2^2*sin(y3-y1)*cos(y3-y1)+c2*c5*sin(y3)*cos(y3-y1)+c2*c4*y4^2*sin(y3-y1)-(c1+c2)*c5*sin(y1))/((c1+c2)*c3-c2*c3*cos(y3-y1)^2)
# Y3' = y4
# Y4' = (-c2*c4*y4^2*sin(y3-y1)*cos(y3-y1)+(c1+c2)*(c5*sin(y1)*cos(y3-y1)-c3*y2^2*sin(y3-y1)-c5*y3))/((c1+c2)*c4-c2*c4*cos(y3-y1)^2)
#
# Начальные условия:
# X0 = 0, X1 = 100
# Y1(X0) = 1
# Y2(X0) = 0
# Y3(X0) = 2
# Y4(X0) = 0
#
# Параметры (константы) системы:
# C1  = 1
# C2  = 1
# C3  = 1
# C4  = 1
# C5  = 9.8
#
# Примечания:
# Выражения для графика движения второго маятника:
#  По X   sin(y1)+0.5*sin(y3)
#  По Y   -(cos(y1)+0.5*cos(y3))
#
# --------------------------------------------------------------------------------
# Файл:       C:\Users\DGTU\Documents\DRK3RUS\DBLPEND.EQN
# Изменен:    02.06.2010 9:24:18

import math
import matplotlib.pyplot as plt

# Метод Эйлера

C1 = 1
C2 = 1
C3 = 1
C4 = 1
C5 = 9.8

Y1_X0 = 1
Y2_X0 = 0
Y3_X0 = 2
Y4_X0 = 0

X0, X1 = 0, 100
step = 100000
h = (X1 + X0) / step

X = []
for _ in range(step):
    X.append(X0 + h)
    X0 += h

Y1, Y2, Y3, Y4 = [], [], [], []
y, x = [], []
Y1.append(Y1_X0)
Y2.append(Y2_X0)
Y3.append(Y3_X0)
Y4.append(Y4_X0)

y.append(math.sin(Y1[0]) + 0.5 * math.sin(Y3[0]))
x.append(-(math.cos(Y1[0]) + 0.5 * math.cos(Y3[0])))

for i in range(step - 1):
    Y1.append(Y1[i] + h * Y2[i])
    Y2.append(Y2[i] + h * ((C2 * C3 * Y2[i] ** 2 * math.sin(Y3[i] - Y1[i]) * math.cos(
        Y3[i] - Y1[i]) + C2 * C5 * math.sin(
        Y3[i]) * math.cos(Y3[i] - Y1[i]) + C2 * C4 * Y4[i] ** 2 * math.sin(Y3[i] - Y1[i]) - (
                                    C1 + C2) * C5 * math.sin(
        Y1[i])) / ((C1 + C2) * C3 - C2 * C3 * math.cos(Y3[i] - Y1[i]) ** 2)))
    Y3.append(Y3[i] + h * Y4[i])
    Y4.append(Y4[i] + h * (
            (-C2 * C4 * Y4[i] ** 2 * math.sin(Y3[i] - Y1[i]) * math.cos(Y3[i] - Y1[i]) + (
                    C1 + C2) * (
                     C5 * math.sin(Y1[i]) * math.cos(Y3[i] - Y1[i]) - C3 * Y2[i] ** 2 * math.sin(
                 Y3[i] - Y1[i]) - C5 * Y3[i])) / (
                    (C1 + C2) * C4 - C2 * C4 * math.cos(Y3[i] - Y1[i]) ** 2)))
    y.append(math.sin(Y1[i]) + 0.5 * math.sin(Y3[i]))
    x.append(-(math.cos(Y1[i]) + 0.5 * math.cos(Y3[i])))

plt.scatter(Y1, Y2)
plt.show()

size = 0.01

plt.scatter(X, Y1, size)
plt.savefig("outX_Y1.jpg")
plt.close()

plt.scatter(Y1, Y2, size)
plt.savefig("outY1_Y2.jpg")
plt.close()

plt.scatter(Y1, Y3, size)
plt.savefig("outY1_Y3.jpg")
plt.close()

plt.scatter(Y1, Y4, size)
plt.savefig("outY1_Y4.jpg")
plt.close()

plt.scatter(Y2, Y3, size)
plt.savefig("outY2_Y3.jpg")
plt.close()

plt.scatter(Y2, Y4, size)
plt.savefig("outY2_Y4.jpg")
plt.close()

plt.scatter(Y3, Y4, size)
plt.savefig("outY3_Y4.jpg")
plt.close()

plt.scatter(x,y,size)
plt.savefig("outx_y.jpg")
plt.close()

plt.scatter([1, 2, 3], [3, 2, 1], size)
plt.show()
