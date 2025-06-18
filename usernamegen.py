import random
import string
import os

def generate_usernames():
    # Get user input
    length = int(input("Enter username length (e.g. 3, 4): "))
    count = int(input("How many usernames to generate? "))
    
    # Character set: lowercase letters, digits, and underscore
    chars = string.ascii_lowercase + string.digits + "_"
    
    # Make sure the output directory exists
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "names_to_check.txt")
    
    # Generate usernames and write to file
    with open(output_file, "w") as f:
        for _ in range(count):
            username = ''.join(random.choices(chars, k=length))
            f.write(username + "\n")
    
    print(f"\n{count} usernames saved to {output_file}")

if __name__ == "__main__":
    generate_usernames()
