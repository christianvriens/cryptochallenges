__author__ = 'christianvriens'
__license__ = ''

import utils


# Challenge 1
the_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
should_produce = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
result = utils.hex_to_base64(the_string)
print(utils.check_result(result,should_produce))