import pyqrcode

def generate_qr_code(content, error="H", version=None, mode=None, encoding=None):
    qr = pyqrcode.QRCode(
        version=version,
        error=error,
        mode=mode,
        encoding=encoding,
        version= version,
        scale=8,
        module_color=[0, 0, 0, 255],
        background=[255, 255, 255, 255],
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.png_as_base64_str(scale=8)
    with open("qr_code.png", "wb") as f:
        f.write(base64.b64decode(img))

# Test the function
generate_qr_code("Hello, World!", error="Q", version=15)