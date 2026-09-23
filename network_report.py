from netmiko import ConnectHandler
from inventory import devices
from pathlib import Path
from datetime import datetime

def network_report():

    Path("reports").mkdir(exist_ok=True)

    report_file = "reports/network_health_report.txt"

    with open(report_file, "w") as report:

        report.write("====================================\n")
        report.write("   ENTERPRISE NETWORK HEALTH REPORT\n")
        report.write("====================================\n")
        report.write(f"Generated: {datetime.now()}\n\n")

        for device in devices:

            report.write(f"\n===== {device['name']} =====\n")

            config = {
                key: value
                for key, value in device.items()
                if key != "name"
            }

            try:
                connection = ConnectHandler(**config)

                report.write("\n--- INTERFACES ---\n")
                report.write(
                    connection.send_command(
                        "show ip interface brief"
                    )
                )

                report.write("\n--- ROUTING TABLE ---\n")
                report.write(
                    connection.send_command(
                        "show ip route"
                    )
                )

                report.write("\n--- OSPF NEIGHBORS ---\n")
                report.write(
                    connection.send_command(
                        "show ip ospf neighbor"
                    )
                )

                connection.disconnect()

                report.write("\nSTATUS: SUCCESS\n")

            except Exception as e:

                report.write("\nSTATUS: FAILED\n")
                report.write(f"ERROR: {e}\n")

    print(f"Report created: {report_file}")


if __name__ == "__main__":
    network_report()