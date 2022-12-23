class Button:
    color ='white'
    colors = ('white', 'black', 'blue', 'red', 'purple')
    def __init__(self , width: int, height: int, text: str) -> None:
        if not isinstance(width,int):
            raise TypeError('афыбка')
        if not isinstance(height,int):
            raise TypeError('error')
        if not isinstance(text,str):
            raise TypeError('Oshibka')
        self.width = width
        self.height = height
        self.text = text
        self.is_pressed = False
p1 = Button (32,  45,  'sjagushwidid')
print(p1.width, p1.height, p1.text)


@classmethod
def change_color(cls, color: str) -> None:
    if not isinstance(color, str):
        raise TypeError('Error color')
    if color not in cls.colors:
        raise ValueError('this color isn\'t in list')

    cls.color = color

def press(self)-> None:
    self.is_pressed = not self.is_pressed

def __str__(self) -> str:
    return self.text

def to_dict(self) -> dict:
    slovar = {
        'width': self.width,
        'height': self.height,
        'text' : self.text
    }
    return self.slovar

@classmethod
def from_dict(cls, slovar: dict) -> 'Button':
    butt = Button(**slovar)
    return slovar



