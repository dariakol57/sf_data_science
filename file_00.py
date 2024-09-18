import numpy as np
#print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
#print(np.iinfo(np.int16()))

#arrr = np.linspace(-6,21,60,endpoint=False)
#print(arrr[1]-arrr[0])
#list1 = [1,2,3,4]
#list2 = [11,12,13,14]
#list_sum = [x+y for x,y in zip(list1,list2)]
#print(list_sum)
#vec = np.arange(6)

def get_chess(a):
    arr = np.zeros((a,a))
    arr[1::2, ::2] = 1
    print(arr)
    arr[::2, 1::2] = 1
    print(arr)
    return arr

#https://apps.skillfactory.ru/learning/course/course-v1:SkillFactory+DST-3.0+28FEB2021/block-v1:SkillFactory+DST-3.0+28FEB2021+type@sequential+block@0959cbca26284375bd443c705b7c8624/block-v1:SkillFactory+DST-3.0+28FEB2021+type@vertical+block@c87f03b96a0d4ac8baf78a711943661f
from collections import Counter
north = [['Milk', 'Milk', 'Beer'], ['Chocolate', 'Bread', 'Chips'], ['Cola', 'Cola', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Milk'],['Milk', 'Cola', 'Cola', 'Beer', 'Beer', 'Bread', 'Bread', 'Soap', 'Cola', 'Cola', 'Beer', 'Meat', 'Bread', 'Chips'], ['Beer', 'Beer', 'Beer', 'Chips', 'Milk', 'Cola', 'Chocolate', 'Beer', 'Chocolate', 'Beer', 'Beer', 'Cola', 'Meat', 'Yoghurt', 'Beer'], ['Bread'], ['Chocolate', 'Beer', 'Meat', 'Yoghurt'], ['Cola', 'Beer', 'Beer', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Beer', 'Chips', 'Soap', 'Chocolate', 'Bread', 'Chips', 'Cola', 'Bread', 'Beer', 'Cola', 'Bread']]
center = [['Soap', 'Soap', 'Cola', 'Cola', 'Chips'], ['Milk', 'Beer', 'Meat', 'Ketchup', 'Cola', 'Cola', 'Chips', 'Chips', 'Cola', 'Cola'], ['Beer', 'Bread', 'Bread', 'Beer', 'Beer', 'Beer', 'Bread', 'Cheese']]
south = [['Yoghurt', 'Beer', 'Chips', 'Milk', 'Soap', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Cola', 'Cola', 'Beer', 'Ketchup', 'Beer', 'Beer', 'Beer', 'Soap'], ['Chips', 'Cola', 'Beer', 'Chips', 'Cola', 'Cola', 'Beer']]


north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]
c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)
print(c - (n + s))
# Counter()
print(n - (s + c))
# Counter({'Cola': 6})
print(s - (c + n))
# Counter()


#ЗАДАНИЕ 9.6

# Не забудьте импортировать numpy и сразу задать seed 2021
import numpy as np
np.random.seed(2021)

# В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.rand()

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)

# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 101, size=(3,2))

# В переменную even сохраните чётные числа от 2 до 16 (включительно)
even = np.arange(2,17,2)

# Скопируйте even в переменную mix. Перемешайте числа в mix так,
# чтобы массив mix изменился
mix = even
np.random.shuffle(mix)

# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(even, replace=False, size=3)

# Получите переменную triplet, которая должна содержать перемешанные
# значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)