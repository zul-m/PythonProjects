import pyqrcode
import png

link = "https://github.com/zul-m/PythonProjects"

qr_code = pyqrcode.create(link)
qr_code.png("github.png", scale = 5)