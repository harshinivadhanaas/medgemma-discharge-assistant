import google.generativeai as genai

API_KEY = "AIzaSyCHDN_fSizB9pUU1euneD5g1LvsadD7sZU"

try:
    genai.configure(api_key=API_KEY)
    
    # List available models
    print("Available models:")
    for model in genai.list_models():
        print(f"  - {model.name}")
        if 'generateContent' in model.supported_generation_methods:
            print(f"    ✓ Supports generateContent")
    
    # Try to generate
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say hello")
    print(f"\n✅ SUCCESS! Response: {response.text}")
    
except Exception as e:
    print(f"❌ ERROR: {e}")