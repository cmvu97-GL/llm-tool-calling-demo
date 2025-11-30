# LLM Tool Calling Demo

Autor: **Cuong Manh Vu**

Demonstrační Python projekt, který ukazuje použití LLM API (Google Gemini) s nástrojem (function calling). Program zavolá LLM API, použije nástroj pro získání počasí a vrátí výsledek zpět LLM pro vytvoření přirozené odpovědi.

---

## 📋 Popis projektu

Tento projekt demonstruje:
1. **Volání LLM API** - komunikace s Google Gemini
2. **Function calling** - LLM rozpozná potřebu použít nástroj
3. **Spuštění nástroje** - Python funkce se skutečně provede
4. **Vrácení výsledku** - data se pošlou zpět LLM
5. **Finální odpověď** - LLM vytvoří přirozenou odpověď v češtině/angličtině

---

## 🛠️ Implementovaný nástroj

### **get_weather**
Simuluje získání informací o počasí pro zadané město.

**Vstup:** název města (Prague, Brno, Ostrava, Plzen, Olomouc)

**Výstup:** 
- Teplota (°C)
- Podmínky (cloudy, sunny, rainy)
- Vlhkost (%)

**Poznámka:** V reálné aplikaci by tento nástroj volal skutečné weather API (např. OpenWeatherMap).

---

## 🚀 Instalace a spuštění

### Požadavky
- Python 3.8 nebo novější
- Google API klíč (zdarma z https://aistudio.google.com/app/apikey)

### Postup instalace

#### 1. Naklonuj repositář
```bash
git clone [URL-tohoto-repositáře]
cd llm-tool-calling-demo
```

#### 2. Vytvoř virtuální prostředí
```bash
python -m venv venv
```

#### 3. Aktivuj virtuální prostředí

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

#### 4. Nainstaluj závislosti
```bash
pip install -r requirements.txt
```

#### 5. Nastav API klíč

Vytvoř soubor `.env` v kořenové složce projektu:
```env
GOOGLE_API_KEY=tvůj-api-klíč-zde
```

**⚠️ DŮLEŽITÉ:** Soubor `.env` NIKDY nenahrávej na GitHub! (Je v `.gitignore`)

#### 6. Spusť program
```bash
python main.py
```

---

## 💡 Příklad použití

### Vstup:
```
User: What is the weather in Prague?
```

### Průběh:
1. LLM obdrží dotaz
2. LLM rozpozná, že potřebuje nástroj `get_weather`
3. Program spustí funkci `get_weather(city="Prague")`
4. Funkce vrátí: `{"temperature": 15, "condition": "cloudy", "humidity": 65}`
5. Výsledek se pošle zpět LLM
6. LLM vytvoří přirozenou odpověď

### Výstup:
```
The weather in Prague is currently cloudy with a temperature 
of 15 degrees Celsius and humidity of 65%.
```

---

## 📚 Jak to funguje

```
┌─────────────────────