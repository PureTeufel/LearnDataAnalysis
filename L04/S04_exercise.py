import numpy as np

persontype = np.dtype({
    'names':['name', 'chinese', 'english', 'math', 'total'],
    'formats':['S32', 'i', 'i', 'i', 'i']})
peoples = np.array([("ZhangFei",66,65,30,0),("GuanYu",95,85,98,0),("ZhaoYun",93,92,96,0),("HuangZhong",90,88,77,0),("DianWei",80,90,90,0)],dtype=persontype)

names = peoples[:]['name']
chineses = peoples[:]['chinese']
englishs = peoples[:]['english']
maths = peoples[:]['math']

def show(names, obj):
    print('{} | {} | {} | {} | {} | {}'
          .format(names,np.mean(obj),np.min(obj),np.max(obj),np.var(obj),np.std(obj)))

print("object | cj_avg | cj_min | cj_max | cj_var | cj_std")
show("chinese", chineses)
show("english", englishs)
show("math", maths)

peoples[:]['total'] = peoples[:]['chinese'] + peoples[:]['english'] + peoples[:]['math']

# cj_sum = peoples['chinese']+peoples['english']+peoples['math']

ranking = np.sort(peoples, axis = -1, kind = 'quicksort', order = 'total')
ranking[:]['total']
print(ranking)
