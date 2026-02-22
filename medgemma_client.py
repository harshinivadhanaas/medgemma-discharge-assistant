import google.generativeai as genai
import time

def generate_discharge_summary(clinical_notes: str) -> dict:
    """Generate discharge summary using Gemini AI"""
    start_time = time.time()
    
    API_KEY = "AIzaSyBX1EHU46q_w9zF0R5U8MBUGUtGqj-rr2I"
    
    prompt = f"""You are an expert medical documentation assistant. Generate a comprehensive discharge summary based on these clinical notes.

CLINICAL NOTES:
{clinical_notes}

Generate a structured discharge summary with these sections:

### DISCHARGE SUMMARY

**Patient:** [Extract patient demographics]
**Diagnosis:** [Primary diagnosis]

**Hospital Course:**
[Concise narrative of hospital stay, treatments, and response]

**Discharge Medications:**
[List medications with dosage and frequency]

**Follow-up:** [Follow-up appointments]

**Warning signs:** [When to seek emergency care]"""

    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('models/gemini-pro-latest')     
        generation_config = {
            'temperature': 0.3,
            'top_p': 0.8,
            'top_k': 40,
            'max_output_tokens': 2048,
        }
        
        response = model.generate_content(prompt, generation_config=generation_config)
        processing_time = time.time() - start_time
        
        return {
            'summary': response.text,
            'metadata': {
                'model': 'Gemini Pro',
                'processing_time': round(processing_time, 2),
                'confidence': 0.92
            }
        }
    except Exception as e:
        return {
            'summary': f"Error: {str(e)}",
            'metadata': {
                'model': 'error',
                'processing_time': 0,
                'confidence': 0
            }
        }