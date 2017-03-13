import random
import csv

file_name = 'immigration_vocabulary.csv' #this needs to be set to the current path
dict_list = []

with open(file_name, 'rb') as fd:
    reader = csv.DictReader(fd)
    for line in reader:
        dict_list.append(line)        
        
ands = ['Through','Beyond','Eternal','When','Explorations of','The Origins of','The Future of'] 
ors = ['and','or','without', 'since','under the','with']
discp = ['A Hisory of','Gender and','The Political Economy of','A Discourse on','The Politics of','Outline of a Theory of']
word1 = random.choice(dict_list)
word2 = random.choice(dict_list)
ands1 = random.choice(ands)
disp1 = random.choice(discp)
ors1 = random.choice(ors)
word3 = random.choice(dict_list)


print ands1,word1['Word'],ors1, word2['Word'],'-',disp1, word3['Word']