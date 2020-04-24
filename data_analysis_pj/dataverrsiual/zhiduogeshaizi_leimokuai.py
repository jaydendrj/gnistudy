from die import Die

class Multiple_Die():
    def __init__(self,*num_sides,times=100):
        self.num_sides=num_sides
        self.times=times
        self.result=[]
        self.results=[]
        self.resultss = []
        self.sides_range = range(len(self.num_sides),sum(self.num_sides)+1)

    def reults_of_multiple_dies(self):
        for side in self.num_sides:
            die=Die(side)
            self.results=[]
            for i in range(self.times):
                self.result=die.roll()
                self.results.append(self.result)
            self.resultss.append(self.results)
        return self.resultss

    def frequence(self):
        a = [0 for j in range(self.times)]
        for i in range(len(self.resultss)):
            for j in range(self.times):
                a[j]=a[j]+self.resultss[i][j]

        frequences = []
        for i in multiple_die.sides_range:
            frequence = a.count(i)
            frequences.append(frequence)
        return frequences

#实例
multiple_die=Multiple_Die(*(2,9),times=2000)

multiple_die.reults_of_multiple_dies()
print(multiple_die.frequence())


'''可视化'''
import pygal

hist=pygal.Bar()

hist.title='Results of rolling one D6 1000 times'
hist.x_labels=[str(i) for i in multiple_die.sides_range]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'

hist.add("D6",multiple_die.frequence())
hist.render_to_file('die_visual.svg')

