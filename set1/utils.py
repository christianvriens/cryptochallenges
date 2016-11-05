__author__ = 'christianvriens'
__license__ = 'MIT'

import base64
from collections import Counter

def check_result(result, should_produce):
    """
    :param result: this is the result of the function
    :param should_produce: the is the result it should be according to the challenge
    :return: True or False
    """
    print("result = " + result)
    print("should produce = " + should_produce)
    if result == should_produce:
        return True
    else:
        return False


def hex_to_base64(hex):
    """
    :param hex: hex string as an input
    :return: it returns the base64 equivalent
    """
    hex_decoded = hex.decode("hex")
    print("original hex = " + hex)
    print("hex decoded = " + hex_decoded)
    base_encoded = base64.standard_b64encode(hex_decoded)
    print("base encoded = " + base_encoded)
    return base_encoded

def xor_two_hex(x,y):
    """
    :param x: first hex string
    :param y: second hex string
    :return: xor of the two strings
    """
    a = int(x,16)
    print("a = " + str(a))
    b = int(y,16)
    print("b = " + str(b))
    return hex((a^b)).lstrip("0x").rstrip("L")

def character_counter(text):
    result= [text[i] for i in range(0, len(text))]
    return Counter(result)

