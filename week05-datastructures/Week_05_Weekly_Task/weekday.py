import datetime

weekIndex = {
0 : "Weekday",
1 : "Weekday",
2 : "Weekday",
3 : "Weekday",
4 : "Weekday",
5 : "Weekend",
6 :  "Weekend"
    }

x = datetime.date.today() 
y = x.weekday()

for key, value in weekIndex.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if key == y:
        print(value)




