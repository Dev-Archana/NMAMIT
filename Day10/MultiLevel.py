# Multi Level Inheritance :
class WhatsAppv1:
    def whatsappv1(self):
        print("This Version Containing Only Text Message")
class WhatsAppv2(WhatsAppv1):
    def whatsappv2(self):
        print("This Version Containing Video And Audio Calls")
class WhatsAppv3(WhatsAppv2):
    def __init__(self):
        super().__init__()
    def whatsappv3(self):
        print("This Version Containing Payment Module")
v3=WhatsAppv3()
v3.whatsappv1()
v3.whatsappv2()
v3.whatsappv3()