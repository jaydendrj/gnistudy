import matplotlib.pyplot as plt

from randomwalk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_wall()
    snum = [i * 0.001 for i in rw.wl]
    plt.figure(dpi=100, figsize=(10, 6))
    plt.scatter(rw.x_values, rw.y_values, c=rw.wl, cmap=plt.cm.Blues,edgecolors='none',s=snum)  # c=rw.wl,c=rw.wl,cmap=plt.cm.Reds,

    plt.axis([min(rw.x_values), max(rw.x_values), min(rw.y_values), max(rw.y_values)])
    plt.plot(rw.x_values, rw.y_values, linewidth=0.1)
    plt.title('RamdomWalk', fontsize=20)

    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    plt.axes().get_xaxis().set_visible(False)


    # plt.savefig('RamdomWalk.png')
    plt.show()

    keep_running=input('Make another walk?(y/n): ')
    if keep_running =='n':
        break

# print(len(rw.wl))