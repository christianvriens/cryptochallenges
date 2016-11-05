__author__ = 'christianvriens'
__license__ = ''

import utils

# Challenge 2
x = '1c0111001f010100061a024b53535009181c'
y = '686974207468652062756c6c277320657965'
should_produce = '746865206b696420646f6e277420706c6179'

result = utils.xor_two_hex(x,y)
print(utils.check_result(result,should_produce))


