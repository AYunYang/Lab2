
import Lab2

def test_average():
    input = [5,6,7]
    result = Lab2.calc_average_temperature(input)
    assert (result == 7)
def test_min():
    input = [5, 6, 7]
    result = Lab2.calc_min_temperature(input)
    assert (result == 5)
def test_max():
    input = [5, 6, 7]
    result = Lab2.calc_max_temperature(input)
    assert (result == 7)
def test_median():
    input = [5, 6, 7]
    result = Lab2.calc_median_temperature(input)
    assert (result == 6)