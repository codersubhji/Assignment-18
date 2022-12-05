"""6. Write a python program to create a dictionary that contains three dictionaries.
(nested)"""

dics={
    'Python':{'duration':"3 Month",'fees':15000},
    'Java':{'duration':"3 Month",'fees':12000},
    'Php':{'duration':"3 Month",'fees':13000}  
}
print(dics['Python']['duration'])
print(dics['Python']['fees'])
