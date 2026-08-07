import socket
import requests
from urllib.parse import urlparse
from datetime import datetime
import threading
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# ---------------- CONFIG ----------------
MAX_THREADS = 100
TIMEOUT = 0.5

open_ports = []
lock = threading.Lock()

# ---------------- ML MODEL ----------------
def train_model():
    # Synthetic dataset
    data = {
        "open_ports": [1, 2, 5, 10, 3, 8, 15, 20],
        "sensitive_ports": [0, 1, 2, 3, 1, 2, 4, 5],
        "missing_headers": [0, 1, 2, 3, 1, 2, 3, 4],
        "risk": ["Low", "Low", "Medium", "High", "Low", "Medium", "High", "High"]
    }

    df = pd.DataFrame(data)

    X = df[["open_ports", "sensitive_ports", "missing_headers"]]
    y = df["risk"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model

model = train_model()

# ---------------- RESOLVE ----------------
def resolve_target(url):
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path
    ip = socket.gethostbyname(domain)
    return domain, ip

# ---------------- PORT SCAN ----------------
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)

        if sock.connect_ex((ip, port)) == 0:
            with lock:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

        sock.close()
    except:
        pass

def threaded_scan(ip, start, end):
    print(f"\n🔍 Scanning ports {start}-{end}...\n")
    threads = []

    for port in range(start, end + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

        if len(threads) >= MAX_THREADS:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

# ---------------- HEADER CHECK ----------------
def check_headers(url):
    print("\n🌐 Checking web security headers...\n")
    missing = 0

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        checks = [
            "X-Frame-Options",
            "X-XSS-Protection",
            "X-Content-Type-Options",
            "Strict-Transport-Security"
        ]

        for header in checks:
            if header not in headers:
                print(f"[!] Missing {header}")
                missing += 1

        print(f"\n[INFO] Server: {headers.get('Server', 'Unknown')}")
        return missing

    except Exception as e:
        print(f"[ERROR] {e}")
        return 0

# ---------------- ML PREDICTION ----------------
def predict_risk(open_ports, missing_headers):
    sensitive_list = [21, 22, 23, 25, 3389]

    sensitive_count = sum(1 for p in open_ports if p in sensitive_list)

    features = [[
        len(open_ports),
        sensitive_count,
        missing_headers
    ]]

    prediction = model.predict(features)[0]

    return prediction

# ---------------- REPORT ----------------
def save_report(domain, ip, open_ports, missing_headers, prediction):
    filename = f"scan_report_{domain}.txt"

    with open(filename, "w") as f:
        f.write("=== AI Vulnerability Report ===\n\n")
        f.write(f"Target: {domain}\nIP: {ip}\n\n")

        f.write("Open Ports:\n")
        for p in open_ports:
            f.write(f"- {p}\n")

        f.write(f"\nMissing Headers: {missing_headers}\n")
        f.write(f"\nPredicted Risk: {prediction}\n")

    print(f"\n📄 Report saved as {filename}")

# ---------------- MAIN ----------------
def main():
    print("🔐 AI-Based Vulnerability Scanner\n")

    url = input("Enter Target URL: ")
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))

    start_time = datetime.now()

    domain, ip = resolve_target(url)

    print(f"\n🎯 Target: {domain}")
    print(f"🌍 IP: {ip}")

    threaded_scan(ip, start_port, end_port)

    missing_headers = check_headers(url)

    prediction = predict_risk(open_ports, missing_headers)

    print(f"\n🤖 AI Predicted Risk: {prediction}")

    save_report(domain, ip, open_ports, missing_headers, prediction)

    print(f"\n⏱ Completed in: {datetime.now() - start_time}")

if __name__ == "__main__":
    main()