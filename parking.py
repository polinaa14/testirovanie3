class Parking:
    """Система управления парковочными местами."""

    def __init__(self, total_places):
        if total_places <= 0:
            raise ValueError("Количество мест должно быть положительным")
        self.total_places = total_places
        self.occupied = set()

    def _valid_place(self, place_number):
        return 1 <= place_number <= self.total_places

    def book_place(self, place_number):
        """Забронировать свободное парковочное место."""
        if not self._valid_place(place_number):
            return False
        if place_number in self.occupied:
            return False
        self.occupied.add(place_number)
        return True

    def release_place(self, place_number):
        """Освободить занятое парковочное место."""
        if not self._valid_place(place_number):
            return False
        if place_number not in self.occupied:
            return False
        self.occupied.remove(place_number)
        return True

    def is_occupied(self, place_number):
        """Проверить, занято ли место."""
        if not self._valid_place(place_number):
            return False
        return place_number in self.occupied

    def available_places(self):
        """Получить список свободных парковочных мест."""
        return [
            place
            for place in range(1, self.total_places + 1)
            if place not in self.occupied
        ]
