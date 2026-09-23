from netmiko import ConnectHandler
from inventory import devices

for device in devices:
    print(f"\nConnecting to {device['name']}...")

    try:
        config = {key: value for key, value in device.items() if key != "name"}

        connection = ConnectHandler(**config)

        print(f"SUCCESS: Connected to {device['name']}")

        connection.disconnect()

    except Exception as e:
        print(f"FAILED: {device['name']}")
        print(e)