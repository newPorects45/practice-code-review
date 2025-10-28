from hello import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(200, 25) == 150
    assert calculate_discount(50, 0) == 50
