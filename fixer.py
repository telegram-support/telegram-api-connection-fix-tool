import socket

def check_telegram_connection():
    print("Starting Telegram API Connection Diagnostic...")
    telegram_servers = [
        "149.154.167.50", # DC 1
        "149.154.175.50", # DC 2
        "149.154.167.51", # DC 3
    ]
    
    for ip in telegram_servers:
        try:
            socket.setdefaulttimeout(5)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, 443))
            print(f"Connection to {ip} successful.")
        except Exception as e:
            print(f"Connection to {ip} failed: {e}")

if __name__ == "__main__":
    check_telegram_connection()
