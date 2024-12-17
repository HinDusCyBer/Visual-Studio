import random
import time

def main():
    packets = [random.randint(1, 9) for _ in range(5)]
    content = 0
    bucket_size = int(input("\nEnter the bucket size: "))
    output_rate = int(input("Enter the output rate of the bucket: "))
    
    for i in range(5):
        if (packets[i] + content) > bucket_size:
            if packets[i] > bucket_size:
                print(f"\nIncoming packet size {packets[i]} greater than the size of the bucket\n")
            else:
                print("\nBucket size exceeded\n")
        else:
            new_content = packets[i]
            content += new_content
            print(f"\nIncoming Packet: {new_content}\n")
            print(f"Transmission Left: {content}\n")
            time_left = random.randint(1, 9)
            print(f"Next packet will come at {time_left}\n")
            for clk in range(time_left):
                print(f"Left time: {time_left - clk}")
                time.sleep(1)
                if content:
                    print("\nTransmitted\n")
                    if content < output_rate:
                        content = 0
                    else:
                        content -= output_rate
                    print(f"Bytes remaining: {content}\n")
                else:
                    print("\nNo packets to send\n")
        
if __name__ == "__main__":
    main()