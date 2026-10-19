from parking import Parking


def test_user_can_book_free_parking_place():
    parking = Parking(3)

    result = parking.book_place(1)

    assert result is True
    assert parking.is_occupied(1) is True


def test_user_cannot_book_already_occupied_place():
    parking = Parking(3)
    parking.book_place(1)

    result = parking.book_place(1)

    assert result is False
    assert parking.is_occupied(1) is True


def test_user_can_release_occupied_parking_place():
    parking = Parking(3)
    parking.book_place(1)

    result = parking.release_place(1)

    assert result is True
    assert parking.is_occupied(1) is False


def test_user_can_view_parking_availability():
    parking = Parking(3)
    parking.book_place(1)

    assert parking.available_places() == [2, 3]
