import os

def text_to_binary(text):
    """Convert text to binary."""
    return ''.join(format(ord(char), '08b') for char in text)

def calculate_redundant_bits(m):
    """Calculate the number of redundant bits needed."""
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def position_redundant_bits(data, r):
    """Insert redundant bits into their appropriate positions."""
    j = 0
    k = 1
    m = len(data)
    res = ''

    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res += '0'
            j += 1
        else:
            res += data[-k]
            k += 1

    return res[::-1]

def calculate_parity_bits(arr, r):
    """Calculate the parity bits for the array."""
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[-j])

        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]

    return arr

def apply_hamming_code(data):
    """Apply Hamming code to data."""
    m = len(data)
    r = calculate_redundant_bits(m)
    arranged_data = position_redundant_bits(data, r)
    hamming_code = calculate_parity_bits(arranged_data, r)
    return hamming_code

def save_to_channel(hamming_code):
    """Save the hamming code to a file called 'channel'."""
    with open('channel', 'w') as file:
        file.write(hamming_code)

if __name__ == "__main__":
    text = input("Enter the text: ")
    binary_data = text_to_binary(text)
    hamming_code = apply_hamming_code(binary_data)
    save_to_channel(hamming_code)
    print("Data has been encoded and saved to 'channel' file.")