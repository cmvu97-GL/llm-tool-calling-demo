"""
LLM Tool Calling Demo - Kompletní verze
Autor: Cuong Manh Vu
Popis: Zavolá LLM API, použije nástroj a vrátí odpověď zpět LLM
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Načtení API klíče
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

# ===== IMPLEMENTACE NÁSTROJE =====
def get_weather(city: str) -> dict:
    """
    Simulace získání počasí pro město.
    V reálné aplikaci by volalo skutečné API.
    """
    # Simulovaná data
    weather_data = {
        "prague": {"temperature": 15, "condition": "cloudy", "humidity": 65},
        "brno": {"temperature": 17, "condition": "sunny", "humidity": 55},
        "ostrava": {"temperature": 14, "condition": "rainy", "humidity": 80},
        "plzen": {"temperature": 12, "condition": "rainy", "humidity": 90},
        "olomouc": {"temperature": 15, "condition": "sunny", "humidity": 35}
    }
    
    city_lower = city.lower()
    if city_lower in weather_data:
        return weather_data[city_lower]
    else:
        return {"error": f"Weather data not available for {city}"}


# ===== DEFINICE NÁSTROJE PRO LLM =====
tools = [
    {
        "name": "get_weather",
        "description": "Use this function to get weather information for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city, e.g. Prague, Brno",
                }
            },
            "required": ["city"],
        },
    },
]

# ===== KONFIGURACE KLIENTA =====
client = genai.Client(api_key=api_key)
gemini_tools = types.Tool(function_declarations=tools)
config = types.GenerateContentConfig(tools=[gemini_tools])

print("=" * 60)
print("LLM TOOL CALLING DEMO")
print("=" * 60)

# ===== KROK 1: Odeslání dotazu LLM =====
print("\n[1] Sending query to LLM...")
user_query = "What is the weather in Prague?"
print(f"User: {user_query}")

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=user_query,
    config=config,
)

print("\n[2] LLM Response received")

# ===== KROK 2: Zpracování tool call =====
# Zkontroluj, jestli LLM chce použít nástroj
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    function_name = function_call.name
    function_args = dict(function_call.args)
    
    print(f"\n[3] LLM wants to call tool: {function_name}")
    print(f"    Arguments: {function_args}")
    
    # ===== KROK 3: Spuštění nástroje =====
    print(f"\n[4] Executing tool...")
    if function_name == "get_weather":
        result = get_weather(**function_args)
        print(f"    Result: {result}")
    
    # ===== KROK 4: Vrácení výsledku zpět LLM =====
    print(f"\n[5] Sending result back to LLM...")
    
    # Vytvoř function response
    function_response = types.FunctionResponse(
        name=function_name,
        response={"result": result}
    )
    
    # Pošli výsledek zpět LLM
    final_response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=[
            types.Content(
                role="user",
                parts=[types.Part(text=user_query)]
            ),
            types.Content(
                role="model",
                parts=[types.Part(function_call=function_call)]
            ),
            types.Content(
                role="user",
                parts=[types.Part(function_response=function_response)]
            )
        ],
        config=config,
    )
    
    # ===== KROK 5: Finální odpověď =====
    print(f"\n[6] Final response from LLM:")
    print("=" * 60)
    print(final_response.text)
    print("=" * 60)
else:
    # LLM odpovědělo přímo bez použití nástroje
    print("\n[3] LLM responded directly (no tool used):")
    print("=" * 60)
    print(response.text)
    print("=" * 60)