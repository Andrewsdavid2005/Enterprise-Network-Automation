from netmiko import ConnectHandler
from inventory import devices
from pathlib import Path

def backup_config():

    Path("backups").mkdir(exist_ok=True)

    for device in devices:

        print(f"\nBacking up {device['name']}...")

        config = {
            key: value
            for key, value in device.items()
            if key != "name"
        }

        try:
            connection = ConnectHandler(**config)

            output = connection.send_command(
                "show running-config"
            )

            filename = f"backups/{device['name']}_config.txt"

            with open(filename, "w") as file:
                file.write(output)

            connection.disconnect()

            print(f"Saved: {filename}")

        except Exception as e:
            print(f"FAILED: {device['name']}")
            print(e)


if __name__ == "__main__":
    backup_config()