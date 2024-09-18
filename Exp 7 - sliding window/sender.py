import time
import os

def input_window_size():
    return int(input("Enter window size: "))

def input_text_message():
    return input("Enter text message: ")

def create_frames(text_message):
    frames = [(i, char) for i, char in enumerate(text_message)]
    frames.append((len(text_message), 'END'))  # Add end-of-transmission frame
    return frames

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for frame in data:
            file.write(f"{frame[0]},{frame[1]}\n")

def read_from_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]

def send_frames(frames, window_size):
    i = 0
    while i < len(frames):
        # Send a window of frames
        window = frames[i:i + window_size]
        print(f"Sending frames: {window}")
        write_to_file('Sender_Buffer.txt', window)

        # Wait for acknowledgment with delay
        time.sleep(3)

        # Read from Receiver_Buffer to check ACK/NACK
        receiver_buffer = read_from_file('Receiver_Buffer.txt')
        if not receiver_buffer:
            print("No acknowledgement received yet.")
            continue

        ack_frame = receiver_buffer[0]  # Consider the first line as acknowledgment
        ack_number, ack_type = int(ack_frame[0]), ack_frame[1]

        if ack_type == 'ACK':
            print(f"ACK received for frame {ack_number}, sending next set of frames.")
            i += window_size
        elif ack_type == 'NACK':
            print(f"NACK received for frame {ack_number}, resending frames from frame {ack_number}.")
            # Resend starting from NACK frame
            i = ack_number

def main_sender():
    window_size = input_window_size()
    text_message = input_text_message()
    frames = create_frames(text_message)
    send_frames(frames, window_size)

if __name__ == "__main__":
    main_sender()