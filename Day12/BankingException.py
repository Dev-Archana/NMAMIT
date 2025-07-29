# Custom Exception for insufficient funds
class InsufficientFundsError(Exception):
    pass

# Dictionary for multilingual messages
messages = {
    "en": {
        "enter_balance": "Enter your current balance: ",
        "enter_withdraw": "Enter the amount to withdraw: ",
        "error_non_numeric": "Error: Please enter a valid number.",
        "error_insufficient": "Error: Insufficient funds for this transaction.",
        "success": "Withdrawal successful. Remaining balance: "
    },
    "hi": {
        "enter_balance": "अपना वर्तमान बैलेंस दर्ज करें: ",
        "enter_withdraw": "निकालने की राशि दर्ज करें: ",
        "error_non_numeric": "त्रुटि: कृपया एक मान्य संख्या दर्ज करें।",
        "error_insufficient": "त्रुटि: इस लेनदेन के लिए अपर्याप्त धनराशि।",
        "success": "निकासी सफल। शेष राशि: "
    },
    "kn": {
        "enter_balance": "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಶೇಷವನ್ನು ನಮೂದಿಸಿ: ",
        "enter_withdraw": "ತೆಗೆದುಕೊಳ್ಳಬೇಕಾದ ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ: ",
        "error_non_numeric": "ದೋಷ: ದಯವಿಟ್ಟು ಮಾನ್ಯ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.",
        "error_insufficient": "ದೋಷ: ಈ ವ್ಯವಹಾರದಿಗಾಗಿ ಸಾಕಷ್ಟು ಹಣ ಇಲ್ಲ.",
        "success": "ತೆಗೆದುಕೊಳ್ಳುವುದು ಯಶಸ್ವಿಯಾಗಿದೆ. ಉಳಿದ ಶೇಷ: "
    }
}

# Select language (en = English, hi = Hindi, kn = Kannada)
lang = input("Choose language (en/hi/kn): ").strip().lower()
if lang not in messages:
    print("Unsupported language. Defaulting to English.")
    lang = "en"

# Access language-specific messages
msg = messages[lang]

# Transaction logic
try:
    balance = float(input(msg["enter_balance"]))
    withdraw = float(input(msg["enter_withdraw"]))

    if withdraw > balance:
        raise InsufficientFundsError

    balance -= withdraw
    print(msg["success"], balance)

except ValueError:
    print(msg["error_non_numeric"])
except InsufficientFundsError:
    print(msg["error_insufficient"])
