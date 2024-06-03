import requests

def translate_text(text, target_language, source_language='en'):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source_language}|{target_language}"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        response_json = response.json()
        
        # Check if the 'translatedText' key is in the response
        if 'responseData' in response_json and 'translatedText' in response_json['responseData']:
            translation = response_json['responseData']['translatedText']
            return translation
        else:
            print("Error: 'translatedText' not found in the response.")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# User input for text to translate and target language
text_to_translate = input("Enter the text to translate: ")
target_language = input("Enter the target language (e.g., 'es' for Spanish): ")

# Perform translation
translated_text = translate_text(text_to_translate, target_language)
if translated_text:
    print("Translated text:", translated_text)
else:
    print("Translation failed.")

