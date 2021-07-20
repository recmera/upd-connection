


def bitstringABytes(strng):
    K = int(strng, 2)
    byts = bytearray()
    while K:
        byts.append(K & 0xff)
        K >>= 8
    return bytes(byts[::-1])

def bytesABitstring(byts):
    strng = ''
    for i in byts:
        strng += "{0:08b}".format(i)
    return strng



def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler='0'):
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    """
    # calcula el crc reminder de un string de bits usando polinomio https://en.wikipedia.org/wiki/Cyclic_redundancy_check
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)

    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')

        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))

    return ''.join(input_padded_array)[len_input:]

def crc_check(input_bitstring, polynomial_bitstring, check_value):
    """Calculate the CRC check of a string of bits using a chosen polynomial."""

    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)

    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')

        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ('1' not in ''.join(input_padded_array)[len_input:])

