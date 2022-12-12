'''
object1 = {"a":{"b":{"c":"d"}}}
object = {'x':{'y':{'z':'a'}}}
for i in object1:
    print(i)
    print(object1.get(i))
'''
#print(object.keys())
#print(object1.values())

#object.keys()

#print(object.get('a'))


def show(obj):
    print(obj)
    for k in obj:
        print(k, '=',obj[k])
        return obj
obj = {"a":{"b":{"c":"d"}}}
new_obj = show(obj)

def show(obj1):
    print(obj1)
    for k in obj1:
        print(k, '=',obj1[k])
        return obj1
obj1 = {'x':{'y':{'z':'a'}}}
new_obj1 = show(obj1)
