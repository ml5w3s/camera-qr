import pyqrcode
code = pyqrcode.create("www.duckduckgo.com")
code.png('codigo.png', scale=6)
if code !=0:
    print('Qr code gerado!')
