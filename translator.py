import requests
import json
import time

def translate_batch(texts, api_key):

```
data = {
    str(i): text
    for i, text in enumerate(texts)
}

prompt = f"""
```

You are a professional subtitle translator.

Translate from English to Persian.

Rules:

* Natural and colloquial Persian.
* Keep emotions and tone.
* Keep line breaks.
* Translate only values.
* Keep JSON keys unchanged.
* Return valid JSON only.

JSON:

{json.dumps(data, ensure_ascii=False)}
"""

```
url = (
    "https://generativelanguage.googleapis.com/"
    f"v1beta/models/gemini-2.5-flash:generateContent"
    f"?key={api_key}"
)

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ],
    "generationConfig": {
        "responseMimeType": "application/json",
        "temperature": 0.4
    }
}

headers = {
    "Content-Type": "application/json"
}

for _ in range(3):

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=120
        )

        if response.status_code != 200:
            time.sleep(2)
            continue

        result = response.json()

        raw_text = (
            result["candidates"][0]
            ["content"]["parts"][0]
            ["text"]
        )

        translated = json.loads(raw_text)

        return [
            translated.get(str(i), texts[i])
            for i in range(len(texts))
        ]

    except Exception:
        time.sleep(2)

return texts
```
