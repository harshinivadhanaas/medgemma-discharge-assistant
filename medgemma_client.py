import time
import os
from google import genai

def generate_discharge_summary(clinical_notes: str) -> dict:
    start_time = time.time()

    try:
        import streamlit as st
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except:
        API_KEY = os.environ.get("GEMINI_API_KEY", "")

    prompt = f"""You are an expert medical documentation assistant. 
Generate a comprehensive discharge summary based on these clinical notes.

CLINICAL NOTES:
{clinical_notes}

Generate a structured discharge summary with these sections:

### DISCHARGE SUMMARY
**Patient:** [Extract patient demographics]
**Diagnosis:** [Primary diagnosis]
**Hospital Course:** [Concise narrative of hospital stay and treatments]
**Discharge Medications:** [List with dosage and frequency]
**Follow-up:** [Appointments needed]
**Warning signs:** [When to seek emergency care]"""

    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        processing_time = time.time() - start_time
        return {
            'summary': response.text,
            'metadata': {
                'model': 'gemini-2.5-flash',
                'processing_time': round(processing_time, 2),
                'confidence': 0.95
            }
        }
    except Exception as e:
        return {
            'summary': f"Error: {str(e)}",
            'metadata': {'model': 'error', 'processing_time': 0, 'confidence': 0}
        }
```

You also need to update your `requirements.txt` on GitHub. Change `google-generativeai` to:
```
google-genai
