# # #Задача 10
# def conver_str(s):
#     dict_ = {'.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
#              'a': '2', 'b': '22', 'c': '222',
#              'd': '3', 'e': '33', 'f': '333',
#              'g': '4', 'h': '44', 'i': '444',
#              'j': '5', 'k': '55', 'l': '555',
#              'm': '6', 'n': '66', 'o': '666',
#              'p': '7', 'q': '77', 'r': '777', 's': '7777',
#              't': '8', 'u': '88', 'v': '888',
#              'w': '9', 'x': '99', 'y': '999', 'z': '9999',
#              ' ': '0'}
#
#     num_str = ''
#
#     for i in s:
#         num_str += dict_[i] + ' '
#
#     return num_str
#
# str_ = input('Enter your string in english: ').lower()
# print(conver_str(str_))

#Задача 11
def covert_list(l):
    l1 = []
    l2 = []

    if l == []:
        return []
    elif isinstance(l[0], list):
        l1 += covert_list(l[0])
        l2 += covert_list(l[1:])
        return l1 + l2
    elif not isinstance(l[0], list):
        l1.append(l[0])
        l2 += covert_list(l[1:])
        return l1 + l2

list1 = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
list2 = [[1, [2, [4, 8]]], [3], 6]
list3 = [[[1, 3], [[4, 5]], [[9], 10]], 11]
print(covert_list(list1))
print(covert_list(list2))
print(covert_list(list3))
