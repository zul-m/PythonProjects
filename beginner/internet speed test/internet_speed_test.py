import speedtest

wifi = speedtest.Speedtest()

print("Wifi download speed is ", wifi.download())
print("Wifi upload speed is ", wifi.upload())