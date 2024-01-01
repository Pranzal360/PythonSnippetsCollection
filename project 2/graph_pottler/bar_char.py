import matplotlib.pyplot as plt

left = [1,2,3,4,5]
height = [10,11,12,32,5]

tick_label = ['one','two','three','four','five']

plt.bar(left,height,tick_label = tick_label,width = 0.8, color= ['blue','orange'])

plt.xlabel('people')
plt.ylabel('income')

plt.title('Demo Bar ')

plt.show()