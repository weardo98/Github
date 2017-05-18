import csv
import datetime as dt
import matplotlib.pyplot as plt
arch = 'Bitcoin price.csv'
data = csv.reader(open(arch))
data = [(dt.datetime.strptime(item, "%m/%d/%Y"), float(value)) for item, value in data]
data.sort()
[x, y] = zip(*data)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.grid(True)
fig.autofmt_xdate()
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Bitcoin Price")
plt.show()