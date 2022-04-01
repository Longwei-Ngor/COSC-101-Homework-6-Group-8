def remove_all_after(list, border):
    list2 = []
    x = 0
    try:
        indx = list.index(border)
    except ValueError:
        return list
    while x <= indx:
        list2.append(list[x])
        x += 1
        continue
    return list2
# list1 = [0,1,2,3,2,4,5]
# print(remove_all_after(list1, 2))