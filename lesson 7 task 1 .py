# def pascal_triangle(n):
#     row = [1]
#     y = [0]
#     for x in range(max(n, 0)):
#         if x < n:
#             print((n-x)*" ",row)
#         else:
#             print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
#
# a = pascal_triangle(10)
