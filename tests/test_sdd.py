import pytest

from parking import Parking


@pytest.mark.parametrize(
    "occupied_places, operation, place, expected_result, expected_status",
    [
        (set(), "book", 1, True, {1}),
        ({1}, "book", 1, False, {1}),
        ({1}, "release", 1, True, set()),
        (set(), "release", 2, False, set()),
    ],
)
def test_parking_specification(
    occupied_places, operation, place, expected_result, expected_status
):
    parking = Parking(3)
    parking.occupied = set(occupied_places)

    if operation == "book":
        result = parking.book_place(place)
    else:
        result = parking.release_place(place)

    assert result is expected_result
    assert parking.occupied == expected_status


@pytest.mark.parametrize(
    "occupied_places, expected_available",
    [
        (set(), [1, 2, 3]),
        ({1}, [2, 3]),
        ({1, 2}, [3]),
        ({1, 2, 3}, []),
    ],
)
def test_availability_specification(occupied_places, expected_available):
    parking = Parking(3)
    parking.occupied = set(occupied_places)

    assert parking.available_places() == expected_available
