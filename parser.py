import csv
import sys

# Define the target file and the specific IoC we are hunting
CSV_FILE = 'splunk_logs.csv'
TARGET_IOC = 'rdrleakdiag.exe'

def analyze_logs():
    print(f"[*] Initializing SOC parser...\n[*] Scanning {CSV_FILE} for T1003.001 activity...")
    detection_count = 0

    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert the entire row to a string to catch the IoC in any Splunk column
                row_string = str(row).lower()
                
                if TARGET_IOC.lower() in row_string:
                    print(f"\n[!] CRITICAL ALERT: OS Credential Dumping Detected (T1003.001)")
                    # Splunk exports usually default to '_time' for timestamps
                    print(f"    Time: {row.get('_time', 'Timestamp not found')}")
                    print(f"    Host: {row.get('host', 'Host not found')}")
                    print(f"    Payload: {TARGET_IOC}")
                    detection_count += 1
                    
        print(f"\n[*] Scan complete. Total threats detected: {detection_count}")

    except FileNotFoundError:
        print(f"\n[-] ERROR: '{CSV_FILE}' is missing.")
        print("    Please ensure your Splunk export is named exactly 'splunk_logs.csv'")
        print("    and is located in the SOC LAB folder.")

if __name__ == '__main__':
    analyze_logs()