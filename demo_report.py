from datetime import datetime
from pathlib import Path

Path("reports").mkdir(exist_ok=True)

with open("reports/demo_network_report.txt", "w") as f:
    f.write("====================================\n")
    f.write("   ENTERPRISE NETWORK HEALTH REPORT\n")
    f.write("====================================\n")
    f.write(f"Generated: {datetime.now()}\n\n")

    f.write("HQ-R1              : READY\n")
    f.write("HQ-L3-SW1          : READY\n")
    f.write("HQ-L3-SW2          : READY\n\n")

    f.write("Automation Modules\n")
    f.write("------------------\n")
    f.write("Device Connectivity : READY\n")
    f.write("Health Check        : READY\n")
    f.write("Config Backup       : READY\n")
    f.write("OSPF Monitoring     : READY\n")
    f.write("Network Reporting   : READY\n")

print("Demo report created successfully!")