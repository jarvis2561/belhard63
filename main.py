# from string import printable
# def sms_spliter(sms: str)-> int:
#     bytes_count = len(sms.encode())
    # bytes_count = 0
    # for elem in sms:
    #     bytes_count +=1 if elem in printable else 2
#     count = bytes_count / 140
#     if count.is_integer():
#         return int(count)
#     else:
#         return int(count) + 1
#

# print(len(str(sms)))


# def deposit_calculator(deposit: float, percent: float) -> int:
#     year = 0
#     percent += 1
#     double_deposit = deposit * 2
#     while deposit < double_deposit:
#         deposit *= percent
#         year += 1
#     return year

# seconds = 7336
# hours = seconds / 3600
# minutes = seconds / 60
# seconds %= 60
# print(int(hours))
# print(int(minutes))
# print(int(seconds))
# class User:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name.title()
#         self.age = age
#
# users: list[User] = [ #[User] как аннотация
#     User(name='Vlad', age = 34),
#     User(name='Vd', age = 24),
#     User(name='vadim', age = 39)
# ]
# users.sort(key=lambda n: n.age)
# for user in users:

#     print(user.name, user.age)


# наследование
# class Transport:
#     def __init__(self, weight: int, color: str, power: int, name: str) -> None:
#         self.name = name
#         self.power = power
#         self.color = color
#         self.weight = weight
#         def __str__(self) -> str:
#             return self.name
#
# class Car(Transport):
#     def __init__(self, weight: int, color: str, power: int, name: str, max_speed: int):
#         super().__init__(weight,color,power)
#         self.max_speed

