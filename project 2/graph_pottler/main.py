import matplotlib.pyplot as plt

x = [2, 4, 5]
y = [2, 3, 6]

x2 = [1, 2, 3]
y2 = [1, 2, 3]

plt.plot(x,y,color='green', linestyle='dashed', linewidth=3,marker='o',label = "line 1")
plt.plot(x2,y2,label = "line 2")

plt.ylim(1,8)
plt.xlim(1,8)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Demo Graph - Two lines')

plt.legend()

plt.show()
