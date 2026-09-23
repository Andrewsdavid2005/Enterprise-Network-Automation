from netmiko import ConnectHandler
from inventory import devices
from pathlib import Path

def health_check():

    Path("reports").mkdir(exist_ok=True)

    for device in devices:

        print(f"\nChecking {device['name']}...")

        config = {
            key: value
            for key, value in device.items()
            if key != "name"
        }

        try:
            connection = ConnectHandler(**config)

            output = connection.send_command(
                "show ip interface brief"
            )

            filename = f"reports/{device['name']}_health.txt"

            with open(filename, "w") as file:
                file.write(output)

            connection.disconnect()

            print(f"Saved: {filename}")

        except Exception as e:
            print(f"FAILED: {device['name']}")
            print(e)


if __name__ == "__main__":
    health_check()