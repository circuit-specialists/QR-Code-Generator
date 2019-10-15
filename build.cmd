pyinstaller -F -w -i lib\CircuitSpecialists.ico .\qrcode-generator.py -n "QR Code Generator.exe" --clean
del setup.py
:: py2applet --make-setup gui.py
:: python setup.py build