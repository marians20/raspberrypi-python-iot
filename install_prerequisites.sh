cat /sys/firmware/devicetree/base/model
apt install python3-full -y
apt install i2c-tools -y
apt install python3-smbus -y
apt install git -y
apt install build-essential -y
pip3 install adafruit-circuitpython-htu21d --break-system-packages
apt install pigpio python3-pigpio
pip3 install dependency-injector --break-system-packages
pip3 install adafruit-circuitpython-dht --break-system-packages
pip3 install Adafruit_DHT --break-system-packages --install-option="--force-pi"
systemctl enable pigpiod
systemctl start pigpiod
pigpiod
i2cdetect -y 1
