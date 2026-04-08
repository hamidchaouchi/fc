from typing import Dict

class MirrorAPI:
    def __init__(self, engine):
        self.engine = engine
        self.version = "1.0.0-beta"
        self.node = "Khemis-Miliana-Alpha"

    def get_response(self, user_query: str, lang: str = "AR") -> Dict:
        # استدعاء المحرك الرئيسي
        process_result = self.engine.process_query(user_query, lang=lang)
        
        # تنسيق المخرج كـ JSON احترافي
        return {
            "status": "Success",
            "model": "Mirror-LLM-v1",
            "node": self.node,
            "response": process_result,
            "security_hash": self.engine.anchor[:32]
        }

print("✅ api_gateway.py ready.")