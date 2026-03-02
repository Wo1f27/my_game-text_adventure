

class Item:
    def __init__(self, name: str, description: str, weight: float, is_take: bool = True):
        self.name = name
        self.description = description
        self._weight = weight
        self._is_take = is_take

    def __str__(self) -> str:
        return f'Предмет: {self.name}'

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, new_weight: float) -> None :
        if not isinstance(new_weight, (float, int)):
            print(f'Вес предмета должен быть типа float')
            return
        if not (0.0 <= new_weight <= 200.0):
            print(f'Вес предмета не может быть отрицательным или более 200 кг')
            return
        self._weight = new_weight

    @property
    def is_take(self) -> bool:
        return self._is_take

    @is_take.setter
    def is_take(self, new_value: bool) -> None:
        if not isinstance(new_value, bool):
            print(f'Должно быть булево значение (True/False)')
            return
        self._is_take = new_value
