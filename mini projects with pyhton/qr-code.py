import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://youtu.be/rLyYb7BFgQI?si=NO45EFlZ22ickXiV"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("qrcode.svg", scale = 8) 