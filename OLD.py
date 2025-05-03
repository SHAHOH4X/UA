import random
import requests
from colorama import Fore, init

init(autoreset=True)

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
carriers = ["Airtel", "T-Mobile", "Jio", "Grameenphone", "Robi", "Banglalink", "Verizon", "AT&T", "Vodafone"]

APPROVAL_LIST_URL = "https://raw.githubusercontent.com/SHAHOH4X/UA/main/Approval%20txt"

def print_colored_logo():
    for line in ua_logo.strip().splitlines():
        print(random.choice(colors) + line)

def check_approval(user_id):
    try:
        response = requests.get(APPROVAL_LIST_URL)
        approved_users = response.text.strip().splitlines()
        return user_id in approved_users
    except Exception as e:
        print(f"[ERROR] Approval check failed: {e}")
        return False

def generate_random_ua():
    brand = random.choice(list(devices.keys()))
    model = random.choice(devices[brand])
    android_version = random.choice(android_versions)
    fb_version = random.choice(fb_versions)
    dpi = random.choice(["xxhdpi", "xhdpi"])
    sim = random.choice(carriers)
    resolution = random.choice(["1080x2400", "720x1600", "1080x2340"])

    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/109.0.0.0 Mobile Safari/537.36 "
        f"[FB_IAB/FB4A;FBAV/{fb_version};FBBV/123456789;FBLC/en_US;FBDV/{model};"
        f"FBCR/{sim};FBMF/{brand};FBBD/{brand};FBSV/{android_version};"
        f"FBCA/armeabi-v7a:armeabi;FBDM={{density={dpi},width=1080,height=1920}}]"
    )
    return ua

if __name__ == "__main__":
    print_colored_logo()
    user_id = input("Enter your user ID for approval check: ").strip()

    if check_approval(user_id):
        print(Fore.GREEN + "[✓] Permission Approved!\n")
        try:
            count = int(input("How many random UAs do you want to generate? "))
            for _ in range(count):
                ua = generate_random_ua()
                print(random.choice(colors) + ua + "\n")
        except ValueError:
            print(Fore.RED + "[X] Invalid number.")
    else:
        print(Fore.RED + "[X] Permission Denied. Contact admin for access.")
        print("Contact: https://www.facebook.com/md.shaharia.1675275")