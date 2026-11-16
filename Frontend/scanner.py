import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(2)  # wait for scan results
    results = iface.scan_results()

    networks = []

    for network in results:
        networks.append({
            "ssid": network.ssid,
            "signal": network.signal  # RSSI (negative number)
        })

    return networks

if __name__ == "__main__":
    print(scan_wifi())