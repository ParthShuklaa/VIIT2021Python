import matplotlib.pyplot as pt


x = [10,15]
y =[20,50]
pt.plot(x,y)
pt.draw()
pt.xlabel("Amount in INR")
pt.ylabel("Time in Years")
pt.bar(x,y)
pt.show()