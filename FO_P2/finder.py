import platform
import socket

def detect_os():
    # Get the operating system name
    os_name = platform.system()

    if os_name == "Windows":
        # For Windows, get hostname and IP address
        hostname = platform.node()
        ip_address = socket.gethostbyname(hostname)
        print("Detected OS: Windows")
        print("Hostname:", hostname)
        print("IP Address:", ip_address)
    elif os_name == "Linux":
        # For Linux, get hostname and IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print("Detected OS: Linux")
        print("Hostname:", hostname)
        print("IP Address:", ip_address)
    else:
        print("Unsupported OS detected.")

if __name__ == "__main__":
    detect_os()
