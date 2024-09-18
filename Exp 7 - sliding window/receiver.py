import random
import time
import os

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]

def process_frames(frames):
    acks = []
    frame_seen = set()  # To track frames that have been acknowledged

    for frame in frames:
        frame_number = int(frame[0])
        data = frame[1]
        
        # Skip frames that have been seen and acknowledged before
        if frame_number in frame_seen:
            continue
        
        print(f"Received Frame {frame_number}: {data}")

        # Randomly simulate ACK/NACK
        if random.choice([True, False]):
            print(f"Sending ACK for frame {frame_number}")
            acks.append(f"{frame_number},ACK\n")
            frame_seen.add(frame_number)
        else:
            print(f"Sending NACK for frame {frame_number}")
            acks.append(f"{frame_number},NACK\n")
            break  # Stop after sending NACK

    return ''.join(acks)

def main_receiver():
    while True:
        time.sleep(3)  # Simulate delay in receiving data

        frames = read_from_file('Sender_Buffer.txt')
        if not frames:
            print("No frames to process, waiting...")
            continue
        
        acks = process_frames(frames)
        write_to_file('Receiver_Buffer.txt', acks)

        # Check if an end-of-transmission signal is in the frames
        if any(frame[1] == 'END' for frame in frames):
            print("End of transmission received.")
            break

if __name__ == "__main__":
    main_receiver()
