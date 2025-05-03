import random
import requests
import os
from colorama import Fore, init

init(autoreset=True)

# GitHub information
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"  # Replace with your GitHub username
REPO_NAME = "YOUR_REPO_NAME"  # Replace with your GitHub repo name
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub personal access token

APPROVED_TOKENS_FILE = "approved_tokens.txt"  # File where approved tokens are stored
USED_TOKENS_FILE = "used_tokens.txt"  # File to store used tokens

# UAs generator data
devices = {
    "Samsung": ["SM-G991B", "SM-A515F", "SM-M127F"],
    "Xiaomi": ["M2012K11AG", "21091116UG", "M2007J20CG"],
    "Huawei": ["LYA-L29", "ELE-L29", "VOG-L29"],
    "Redmi": ["Redmi Note 10", "Redmi 9A", "Redmi Note 11 Pro"],
    "Vivo": ["Vivo Y20", "Vivo V23", "Vivo Y51A"],
    "Oppo": ["OPPO A54", "OPPO F19 Pro", "OPPO Reno6"]
}

android_versions = ["10", "11", "12", "13"]
fb_versions = ["425.0.0.28.60", "424.0.0.37.64", "423.1.0.36.68"]
carriers = ["Airtel", "T-Mobile", "Jio", "Grameenphone", "Robi", "Banglalink", "Verizon", "AT&T", "Vodafone"]

# Function to get the list of approved tokens from GitHub
def get_approved_tokens():
    url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/{APPROVED_TOKENS_FILE}"
    response = requests.get(url)
    return response.text.splitlines()

# Function to check if a token has been used
def check_used_token(token):
    if os.path.exists(USED_TOKENS_FILE):
        with open(USED_TOKENS_FILE, "r") as file:
            used_tokens = file.read().splitlines()
        return token in used_tokens
    return False

# Function to mark a token as used
def mark_token_as_used(token):
    with open(USED_TOKENS_FILE, "a") as file:
        file.write(token + "\n")

# Function to generate a random user-agent (UA)
def generate_random_ua():
    brand = random.choice(list(devices.keys()))
    model = random.choice(devices[brand])
    android_version = random.choice(android_versions)
    fb_version = random.choice(fb_versions)
    dpi = random.choice(["xxhdpi", "xhdpi"])
    sim = random.choice(carriers)

    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/109.0.0.0 Mobile Safari/537.36 "
        f"[FB_IAB/FB4A;FBAV/{fb_version};FBBV/123456789;FBLC/en_US;FBDV/{model};"
        f"FBCR/{sim};FBMF/{brand};FBBD/{brand};FBSV/{android_version};"
        f"FBCA/armeabi-v7a:armeabi;FBDM={{density={dpi},width=1080,height=1920}}]"
    )
    return ua

# Main function
if __name__ == "__main__":
    token = input("Enter your approval token: ").strip()

    # Check if the token is approved
    approved_tokens = get_approved_tokens()
    if token in approved_tokens:
        if check_used_token(token):
            print(Fore.RED + "[X] This token has already been used. You cannot use it again.")
        else:
            print(Fore.GREEN + "[✓] Token validated successfully.")
            mark_token_as_used(token)

            try:
                count = int(input("How many random UAs do you want to generate? "))
                for _ in range(count):
                    ua = generate_random_ua()
                    print(random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.WHITE]) + ua + "\n")
            except ValueError:
                print(Fore.RED + "[X] Invalid number.")
    else:
        print(Fore.RED + "[X] Invalid or unapproved token.")
