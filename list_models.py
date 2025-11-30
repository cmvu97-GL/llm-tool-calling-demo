"""List available Gemini models"""
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

print("Available models:")
print("=" * 60)

try:
    models = client.models.list()
    for model in models:
        print(f"- {model.name}")
        if hasattr(model, 'supported_generation_methods'):
            print(f"  Supported methods: {model.supported_generation_methods}")
except Exception as e:
    print(f"Error: {e}")
