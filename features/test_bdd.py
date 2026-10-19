from pytest_bdd import given, scenarios, then, when

from parking import Parking


scenarios("parking.feature")


@given("парковочное место 1 свободно", target_fixture="parking")
def free_place():
    return Parking(3)


@given("парковочное место 1 уже занято", target_fixture="parking")
def occupied_place():
    parking = Parking(3)
    assert parking.book_place(1) is True
    return parking


@given("парковочное место 1 занято", target_fixture="parking")
def occupied_place_for_release():
    parking = Parking(3)
    assert parking.book_place(1) is True
    return parking


@when("бронирую парковочное место 1")
def book_place(parking):
    parking.result = parking.book_place(1)


@when("пытаюсь забронировать парковочное место 1")
def try_book_occupied_place(parking):
    parking.result = parking.book_place(1)


@when("освобождаю парковочное место 1")
def release_place(parking):
    parking.result = parking.release_place(1)


@then("место 1 становится занятым")
def place_becomes_occupied(parking):
    assert parking.result is True
    assert parking.is_occupied(1) is True


@then("бронирование места 1 отклоняется")
def booking_is_rejected(parking):
    assert parking.result is False
    assert parking.is_occupied(1) is True


@then("место 1 становится свободным")
def place_becomes_free(parking):
    assert parking.result is True
    assert parking.is_occupied(1) is False
