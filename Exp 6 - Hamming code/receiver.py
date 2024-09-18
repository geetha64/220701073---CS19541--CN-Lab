def read_from_channel():
    """Read the hamming code from the 'channel' file."""
    with open('channel', 'r') as file:
        return file.read()

def calculate_redundant_bits(m):
    """Calculate the number of redundant bits needed."""
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def detect_error(arr, nr):
    """Detect if there's an error in the received data."""
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-j])

        res = res + val * (10 ** i)

    return int(str(res), 2)

def correct_error(arr, pos):
    """Correct the error in the received data."""
    if pos >= 1:
        arr = arr[:len(arr) - pos] + str(1 - int(arr[len(arr) - pos])) + arr[len(arr) - pos + 1:]
    return arr

def remove_redundant_bits(arr, nr):
    """Remove the redundant bits from the data."""
    n = len(arr)
    j = 0
    res = ''

    for i in range(1, n + 1):
        if i != 2 ** j:
            res += arr[-i]
        else:
            j += 1

    return res[::-1]

def binary_to_text(binary_data):
    """Convert binary data back to text."""
    text = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        text += chr(int(byte, 2))
    return text

if __name__ == "__main__":
    hamming_code = read_from_channel()
    r = calculate_redundant_bits(len(hamming_code) - len(hamming_code.replace('0', '')))
    error_position = detect_error(hamming_code, r)

    if error_position:
        print(f"Error detected at position: {error_position}")
        hamming_code = correct_error(hamming_code, error_position)
    else:
        print("No error detected.")

    corrected_data = remove_redundant_bits(hamming_code, r)
    text = binary_to_text(corrected_data)
    print("error is corrected!.")
    print("The decoded text is:", text)
def read_from_channel():
    """Read the hamming code from the 'channel' file."""
    with open('channel', 'r') as file:
        return file.read()

def calculate_redundant_bits(m):
    """Calculate the number of redundant bits needed."""
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def detect_error(arr, nr):
    """Detect if there's an error in the received data."""
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-j])

        res = res + val * (10 ** i)

    return int(str(res), 2)

def correct_error(arr, pos):
    """Correct the error in the received data."""
    if pos >= 1:
        arr = arr[:len(arr) - pos] + str(1 - int(arr[len(arr) - pos])) + arr[len(arr) - pos + 1:]
    return arr

def remove_redundant_bits(arr, nr):
    """Remove the redundant bits from the data."""
    n = len(arr)
    j = 0
    res = ''

    for i in range(1, n + 1):
        if i != 2 ** j:
            res += arr[-i]
        else:
            j += 1

    return res[::-1]

def binary_to_text(binary_data):
    """Convert binary data back to text."""
    text = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        text += chr(int(byte, 2))
    return text

if __name__ == "__main__":
    hamming_code = read_from_channel()
    r = calculate_redundant_bits(len(hamming_code) - len(hamming_code.replace('0', '')))
    error_position = detect_error(hamming_code, r)

    if error_position:
        print(f"Error detected at position: {error_position}")
        hamming_code = correct_error(hamming_code, error_position)
    else:
        print("No error detected.")

    corrected_data = remove_redundant_bits(hamming_code, r)
    text = binary_to_text(corrected_data)
    print("error is corrected!.")
    print("The decoded text is:", text)
