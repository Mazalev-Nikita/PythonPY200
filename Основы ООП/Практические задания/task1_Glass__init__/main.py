from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Ошибка")
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(200, 100)
    glass_2 = Glass("100", 40)

    print(glass_1)
    print(glass_2)
