
THIRD_DIGIT = 13
FOURTH_DIGIT = 2

# Convert string characters to ascii list 
def get_ascii_list(code: str) -> list[int]:
    """
    Takes a code and returns a list with its characters transformed to ascii

    Args:
        code (str): code to be transformed
    Returns:
        list[int]: list with the ascii code of the characters

    Example:
        >>> get_ascii_list("Dog")
            [68, 111, 103]
        >>> get_ascii_list("Hello")
            [72, 101, 108, 108, 111]
    Note:
        Special and non-printable characters will also be transformed to their ASCII values.
    """
    return [ord(char) for char in code]

# Sum a digits number
def sum_digits(num: int) -> int:
    """
    Takes a number and returns the sum of its digits, if the sum is greater than 9, the function
    is called recursively until the sum is less than 10.

    Args:
        num (int): number to be summed
    Returns:
        int: sum of the digits of the number

    Example:
        >>> sum_digits(123)
            6
        >>> sum_digits(123456789)
            45
    """
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    
    if total_sum > 9:
        return sum_digits(total_sum)
    
    return total_sum

# Average a digits number
def average_digits(num: int) -> int:
    """
    Takes a number and returns the average of its digits rounded down

    Args:
        num (int): number to be averaged
    Returns:
        int: average of the digits of the number

    Example:
        >>> average_digits(123)
            2
        >>> average_digits(123456789)
            5
    
    Note:
        The result of the division is rounded down.
    """
    sum = sum_digits(num)
    len_num = len(str(num))
    return int(sum / len_num)

# Encrypt the first digit of the ascii code
def first_digit_encrypted(ascii_char: int) -> int:
    """
    Toma el código ascii de un caracter y devuelve el primer dígito de su encriptación,
    si el código ascii es par, devuelve la suma de sus dígitos, si es impar, devuelve el
    promedio de la suma de sus dígitos.

    Args:
        ascii_char (int): código ascii del caracter a encriptar
    Returns:
        int: primer dígito de la encriptación del caracter

    Example:
        >>> first_digit_encrypted(68)
            5
        >>> first_digit_encrypted(111)
            1
    """
    if ascii_char % 2 == 0:
        return sum_digits(ascii_char)
    else:
        return average_digits(ascii_char)

# Encrypt the second digit of the ascii code
def second_digit_encrypted(ascii_char: int) -> int:
    """
    Takes the ascii code of a character and returns the second digit of its encryption,
    if the sum of its digits is greater than 10, returns the sum of its digits minus the last digit,
    if it is less than or equal to 10, it returns the last digit.

    Args:
        ascii_char (int): ascii code of the character to encrypt.
    Returns:
        int: second digit of the character encryption.

    Example:
        >>> second_digit_encrypted(871)
            1
        >>> second_digit_encrypted(90)
            9
    """
    if sum_digits(ascii_char) > 7:
        return sum_digits(ascii_char - int(str(ascii_char)[-1]))
    else:
        return int(str(ascii_char)[-1])

# Encrypt the third digit of the ascii code
def third_digit_encrypted(ascii_char: int, digit_1: int, digit_2: int) -> int:
    """
    Takes the ascii code of a character and returns the third digit of its encryption,
    if the first digit is greater than the second, it returns the sum of the first and second digits,
    if the first digit is less than the second, it returns the sum of the ascii code and the first and second digits,
    if the first digit is equal to the second, it returns the sum of the ascii code and the first and second digits,
    if the sum of the ascii code and the first and second digits is less than 10, it returns the sum of the ascii code and the first and second digits,
    if the sum of the ascii code and the first and second digits is greater than 10, it returns the sum of the ascii code and the first and second digits plus the third digit.

    Args:
        ascii_char (int): ascii code of the character to encrypt.
        digit_1 (int): first digit of the character encryption.
        digit_2 (int): second digit of the character encryption.
    Returns:
        int: third digit of the character encryption.

    Example:
        >>> third_digit_encrypted(111, 9, 6)
            6
        >>> third_digit_encrypted(68, 5, 6)
            7
        >>> third_digit_encrypted(1, 7, 7)
            1
    """
    if digit_1 > digit_2:
        return sum_digits(sum_digits(digit_1) + sum_digits(digit_2))
    elif digit_1 < digit_2:
        return sum_digits(sum_digits(ascii_char) + sum_digits(digit_1) + sum_digits(digit_2))
    else:
        return ( (sum_digits(ascii_char) - digit_1 - digit_2) 
                 if ( (sum_digits(ascii_char) - digit_1 - digit_2) < 10 
                        and (sum_digits(ascii_char) - digit_1 - digit_2) > 0 )
                 else sum_digits(sum_digits(ascii_char) + 
                      sum_digits(digit_1) + 
                      sum_digits(digit_2) + 
                      THIRD_DIGIT)
                )

# Encrypt the fourth digit of the ascii code
def fourth_digit_encrypted(ascii_char: str) -> int:
    """
    Takes the ascii code of a character and returns the fourth digit of its encryption,
    if the character is a number, it returns the sum of the number and 1,
    if the character is a letter, it returns the sum of the last digit of the ascii code and 1 if the letter is uppercase,
    if the character is a letter, it returns the sum of the last digit of the ascii code and 1 if the letter is lowercase,
    if the character is a special character, it returns the last digit of the ascii code.

    Args:
        ascii_char (str): ascii code of the character to encrypt.
    Returns:
        int: fourth digit of the character encryption.

    Example:
        >>> fourth_digit_encrypted("T")
            5
        >>> fourth_digit_encrypted("l")
            9
        >>> fourth_digit_encrypted("}")
            8
        >>> fourth_digit_encrypted("13")
            3
    """
    if ascii_char.isnumeric():
        return sum_digits(int(ascii_char[0]) + FOURTH_DIGIT)
    elif ascii_char.isalpha():
        return (sum_digits(ord(ascii_char) + FOURTH_DIGIT) 
                if ascii_char.isupper() 
                else sum_digits(ord(ascii_char) * FOURTH_DIGIT)
               )
    else:
        return sum_digits(ord(ascii_char))

# Get the four digits of the ascii code
def get_digits(ascii_char: int) -> list[int]:
    """
    Takes the ascii code of a character and returns the four digits of its encryption.

    Args:
        ascii_char (int): ascii code of the character to encrypt.
    Returns:
        list[int]: list with the four digits of the character encryption.

    Example:
        >>> get_digits(68)
           
        >>> get_digits(111)
          
    """
    digits = []

    digits.append(sum_digits(first_digit_encrypted(ascii_char)))
    digits.append(sum_digits(second_digit_encrypted(ascii_char)))
    digits.append(sum_digits(third_digit_encrypted(ascii_char, digits[0], digits[1])))
    digits.append(sum_digits(fourth_digit_encrypted(chr(ascii_char))))

    return digits

# Get the numeric sequence of a string
def numeric_sequence(code: str) -> str:
    """
    Takes a code and returns its numeric sequence encrypted

    Args:
        code (str): code to be transformed
    Returns:
        str: numeric sequence of the code

    Example:
        >>> numeric_sequence("Dog")
            589711161388
        >>> numeric_sequence("Hello")
            97720134911991191116
    """
    list_ascii_code = get_ascii_list(code)
    code_encrypted = ""

    for ascii_char in list_ascii_code:
        digits = get_digits(ascii_char)
        code_encrypted += "".join([str(digit) for digit in digits])
    
    return code_encrypted

# Get the encrypted code
def get_encrypted(code: int) -> str:
    """
    Takes a code and returns its encryption

    Args:
        code (str): code to be transformed
    Returns:
        str: encryption of the code

    Example (just numeric sequence):
        >>> encryption_algorithm("Dog")
            589711161388
        >>> encryption_algorithm("Hello")
            97720134911991191116
    """
    code = numeric_sequence(code)
#   code = alpha_sequence(code)
#   code = symbol_sequence(code)
    return code

# Get the long encryptation of a code
def encryption_long_algorithm(string_encrypted: str, number: int) -> str:
    """
    In progress
    """
#   if number == 0:
#       return code
#
#   string_encrypted = get_encrypted(string_encrypted)
#
#   return encryption_long_algorithm(string_encrypted, (number - 1))
#
    pass

# Encrypt a string
def encyption(code: str) -> str:
    """
    Takes a code and returns its encryption

    Args:
        code (str): code to be transformed
    Returns:
        str: encryption of the code

    Example (just numeric sequence):
        >>> encryption_algorithm("Dog")
            589711161388
        >>> encryption_algorithm("Hello")
            97720134911991191116
    """
    # number = natural_random_number()

    string_encrypted = get_encrypted(code)

    # if number != 0:
    #     string_encrypted = encryption_long_algorithm(string_encrypted, (number - 1))

    return string_encrypted