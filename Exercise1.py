def replace_last(list):
    x = list[-1]
    list.remove(list[-1])
    list.insert(0, x)
    return list
# list1 = [1,2,3,4]
# result = replace_last(list1)
# print(result)