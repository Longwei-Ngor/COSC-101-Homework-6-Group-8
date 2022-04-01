def index_power(list, n):
    try:
        x = list[n]
        result = x**n
    except IndexError:
        result = -1
    return result
# list1=[1,2,3,4]
# try:
#     N = int(input("input the value of N: "))
# except ValueError:
#     print ("invalid input")
# print(index_power(list1, N))