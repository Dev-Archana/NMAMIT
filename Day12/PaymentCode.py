import qrcode
from PIL import Image

upi_id = "yourupi@bank"
payee_name = "Your Name"
amount = "100.00"
note = "Payment for service"


upi_link = f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&tn={note}&cu=INR"


qr = qrcode.make(upi_link)
qr.save("upi_payment_qr.png")


img = Image.open("upi_payment_qr.png")
img.show()
