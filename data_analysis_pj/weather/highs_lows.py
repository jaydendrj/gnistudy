import csv

from datetime import datetime

from matplotlib  import pyplot as plt


#从文件中提取最高温度
filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #查看标题得知第0列和第一列储存的是日期和最高温度
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header.strip())

    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)   #y由于第一行已经被读取，所以highs列表中不会包含标题
            lows.append(low)


fig = plt.figure(dpi=128,figsize=(20,6))
             # plt.axis([0-1,len(highs)+5,min(highs),max(highs)+5])
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,lows,highs,facecolor="blue",alpha=0.1)
plt.title('Daily high-low temperatures-2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=10)

plt.show()

# date='2017-2-3'
# print(datetime.strptime(date,'%Y-%m-%d'))
