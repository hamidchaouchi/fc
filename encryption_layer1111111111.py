import base64

class MirrorCryptor:
    def __init__(self, anchor):
        # استخدام بداية النواة كمفتاح تشفير ديناميكي
        self.key = str(anchor)[:32]
        
    def encrypt_payload(self, text: str) -> str:
        """تشفير المخرج باستخدام إزاحة ترددية تعتمد على النواة"""
        encoded = []
        for i, char in enumerate(text):
            key_char = ord(self.key[i % len(self.key)])
            # عملية الإزاحة (Shift)
            encoded.append(chr((ord(char) + key_char) % 1114112))
        
        # التحويل إلى Base64 للنقل الآمن
        combined = "".join(encoded)
        return base64.b64encode(combined.encode()).decode()

print("✅ encryption_layer.py ready.")
