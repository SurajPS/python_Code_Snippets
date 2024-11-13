import hashlib
import time

class ApplicationECU:
    def __init__(self, ecu_id):
        self.ecu_id = ecu_id
        self.sequence_number = 0

    def get_unique_message_id(self):
        # Increment sequence number
        self.sequence_number += 1
        if self.sequence_number > 255:  # Reset after reaching max 8-bit value
            self.sequence_number = 0

        # Get current timestamp
        timestamp = int(time.time() * 1000)  # Current time in milliseconds

        # Combine ECU ID, timestamp, and sequence number into a single string
        unique_string = f"{self.ecu_id}-{timestamp}-{self.sequence_number}"

        # Generate a hash of the combined string
        hash_object = hashlib.sha256(unique_string.encode())
        hash_hex = hash_object.hexdigest()

        # Convert the hash to a number and ensure it fits within 14 bits
        hash_int = int(hash_hex, 16)
        message_id = hash_int & 0x3FFF  # Use only the lowest 14 bits

        return message_id

# Example usage
ecu_w=[]
for i in range (1,256,1):
    ecu_w.append(ApplicationECU(i))

UUID=[]
for ecu in ecu_w:
    for j in range (1,256,1):
        UUID.append(ecu.get_unique_message_id())

print(len(UUID), len(set(UUID)))
