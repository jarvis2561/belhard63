class Car(object):

    def __init__(self, count_passenger_seat: int, is_baby_seat: bool, color: str) -> None:
        self.color = color
        self.count_passenger_seat = count_passenger_seat
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self) -> str:
        return f'Car {self.count_passenger_seat=} {self.is_baby_seat=} {self.is_busy=} {self.color=}'


class Taxi(object):

    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passenger: int, is_baby: bool) -> Car | None:
        if is_baby:
            cars = list(filter(lambda x: not x.is_busy and x.is_baby_seat, self.cars))
        else:
            cars = list(filter(lambda x: not x.is_busy, self.cars))
        for car in cars:
            if car.count_passenger_seat >= count_passenger:
                car.is_busy = True
                return car
class Category(list):
    category = ['simple', 'comfort', 'business']
@classmethod
def add(category_name: list) -> list:


