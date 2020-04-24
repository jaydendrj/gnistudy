from die import Die

#创建N个N面色子的函数    升级重构
def an(*sides):
    dies=[]
    resultss = []
    times=20000
    # dies=[[]for i in range(len(sides))]
    for side in sides:
        results = []

        die=Die(side)
        # dies.append(die)
        for i in range(times):
            result=die.roll()
            # print(result)
            results.append(result)
        resultss.append(results)
        # print(results)
    # return resultss
    a = [0 for j in range(times)]
    for i in range(len(resultss)):
        # a=[0 for j in range(times)]
        for j in range(times):
            a[j]=a[j]+resultss[i][j]
    # print(a,'e')
    return a

# 上面这一串最好做成类，这样就能多输出一些结果（调用方法）


ans=(5,6,4,6)
s=an(*ans)
# print(s)
frequences = []
for i in range(len(ans),sum(ans)+1):
    frequence=s.count(i)
    frequences.append(frequence)
print(frequences)
# print(results)

'''可视化'''
import pygal

hist=pygal.Bar()

hist.title='Results of rolling one D6 1000 times'
hist.x_labels=[str(i) for i in range(len(ans),sum(ans)+1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'

hist.add("D6",frequences)
hist.render_to_file('die_visual.svg')











# #创建一个6面色子的实例
# die1=Die()
# die2=Die(10)
#
# results = []
#
# #掷色子
# for roll_num in range(1000):
#     result = die1.roll()+die2.roll()
#     results.append(result)
#
# frequences = []
# for i in range(2,die1.num_sides+die2.num_sides+1):
#     frequence=results.count(i)
#     frequences.append(frequence)
# print(frequences)
# # print(results)
#
# '''可视化'''
# import pygal
#
# hist=pygal.Bar()
#
# hist.title='Results of rolling one D6 1000 times'
# hist.x_labels=[str(i) for i in range(2,die1.num_sides+die2.num_sides+1)]
# hist.x_title = 'Results'
# hist.y_title = 'Frequency of Results'
#
# hist.add("D6",frequences)
# hist.render_to_file('die_visual.svg')