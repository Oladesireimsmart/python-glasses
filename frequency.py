test_dict={'Codingal':2, 'Codingal1':3, 'Codingal2':4, 'Codingal3':5}

print("The dictionary is:",test_dict)

k=2


res=0
for key in test_dict:
    res+=test_dict[key]==k
    res=res+1
    
    print("The value of key",key,"is:"+ str(key))