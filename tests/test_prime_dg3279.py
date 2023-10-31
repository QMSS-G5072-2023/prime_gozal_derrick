from prime_dg3279 import prime_dg3279
import math

def test_is_prime_param(param = [(2, True), (7, True), (4, False), (10, False), (0, False), (1, False), (-3, False)]):
    for i in param:
        actual = prime_dg3279.is_prime(i[0])
        expected = i[1]
        assert expected == actual, "Value is not a prime number"
