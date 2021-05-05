from calculator import Calc


class TestCalculator:
    def test_add(self):
        assert 4 == Calc.add(2, 2)
        assert 4 == Calc.add(1, 3)

    def test_sub(self):
        assert 4 == Calc.sub(6, 2)
        assert 5 == Calc.sub(10, 5)
