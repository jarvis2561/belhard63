# def offset(list, step):
#     if step > 0:
#         step = abs(step)
#
#     for i in range (step):
#         list.append(list.pop(0))
#     else :
#         for i in range (step):
#             list.insert(0 , lst.pop())
# list = [1,2,3,4,5,6,7,8,9]
# print(offset(list, -2))

def offset_list(lst: list, offset: int) -> list:
    if abs(offset) < len(lst):
        return lst[-offset:] + lst[:-offset]
    if abs(offset) == len(lst):
        return lst
    if abs(offset) > len(lst):
        offset -= (offset // len(lst)) * len(lst)
        return lst[-offset:] + lst[:-offset]


lst = [1, 2, 3, 4, 'dsfgsd', 'dsfgdsfg', 'sdfg', 3, 4, 5, 'sdfgsdfg', 'dfgsdfg']
lst = list(filter(lambda x: isinstance(x, str), lst))
print(lst)