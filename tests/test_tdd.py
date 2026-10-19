from parking import Parking


def test_book_free_place():
    parking = Parking(3)

    assert parking.book_place(1) is True
    assert parking.is_occupied(1) is True


def test_cannot_book_occupied_place():
    parking = Parking(3)
    parking.book_place(1)

    assert parking.book_place(1) is False


def test_release_occupied_place():
    parking = Parking(3)
    parking.book_place(1)

    assert parking.release_place(1) is True
    assert parking.is_occupied(1) is False


def test_cannot_release_free_place():
    parking = Parking(3)

    assert parking.release_place(1) is False


def test_available_places_after_booking():
    parking = Parking(3)
    parking.book_place(1)

    assert parking.available_places() == [2, 3]


def test_invalid_place_cannot_be_booked():
    parking = Parking(3)

    assert parking.book_place(0) is False
    assert parking.book_place(4) is False
