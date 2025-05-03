import random
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# UA ASCII Logo
ua_logo = """
 ██    ██  █████  ██████  
 ██    ██ ██   ██ ██   ██ 
 ██    ██ ███████ ██████  
 ██    ██ ██   ██ ██   ██ 
  ██████  ██   ██ ██   ██ 
"""

colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.WHITE]

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

APPROVAL_LIST_URL = "https://raw.githubusercontent.com/yourusername/your-repo/main/approved_users.txt"  # Replace this

def print_colored_logo(logo):
    for line in logo.splitlines():
        print(random.choice(colors) + line)

def check_approval(user_id):
    try:
        response = requests.get(APPROVAL_LIST_URL)
        approved_users = response.text.strip().splitlines()
        return user_id in approved_users
    except Exception as e:
        print(f"[ERROR] Approval check failed: {e}")
        return False

def generate_fbmf_ua():
    print("\nChoose a brand:")
    for i, brand in enumerate(devices.keys(), start=1):
        print(f"{i}. {brand}")
    brand_choice = int(input("Enter choice number: ")) - 1
    brand = list(devices.keys())[brand_choice]

    print(f"\nChoose a model for {brand}:")
    for i, model in enumerate(devices[brand], start=1):
        print(f"{i}. {model}")
    model_choice = int(input("Enter model number: ")) - 1
    model = devices[brand][model_choice]

    android_version = random.choice(android_versions)
    fb_version = random.choice(fb_versions)
    dpi = random.choice(["xxhdpi", "xhdpi"])
    resolution = random.choice(["1080x2400", "720x1600", "1080x2340"])

    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/109.0.0.0 Mobile Safari/537.36 "
        f"[FB_IAB/FB4A;FBAV/{fb_version};FBBV/123456789;FBLC/en_US;FBDV/{model};"
        f"FBCR/Carrier;FBMF/{brand};FBBD/{brand};FBSV/{android_version};"
        f"FBCA/armeabi-v7a:armeabi;FBDM={{density={dpi},width=1080,height=1920}}]"
    )

    color = random.choice(colors)
    print(f"\n{color}Generated User-Agent:\n{ua}\n")

if __name__ == "__main__":
    print_colored_logo(ua_logo)
    print("Enter your user ID for approval check:")
    user_id = input("User ID: ").strip()
    
    if check_approval(user_id):
        print(Fore.GREEN + "[✓] Permission Approved!\n")
        while True:
            generate_fbmf_ua()
            again = input("Generate another UA? (y/n): ").strip().lower()
            if again != 'y':
                break
    else:
        print(Fore.RED + "[X] Permission Denied. Contact admin for access.")
        print("Contact: https://www.facebook.com/md.shaharia.1675275")
