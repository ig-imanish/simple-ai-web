import google.generativeai as genai

class AI:
    def __init__(self, api):
        genai.configure(api_key=api)
        self.client = genai.GenerativeModel(
            'gemini-pro',
            safety_settings=[
                {
                    "category": "HARM_CATEGORY_DANGEROUS",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE",
                },
            ]
        )

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.generate_content(prompt) 
            return response.text if hasattr(response, 'text') else str(response)
        except Exception as e:
            return e  
