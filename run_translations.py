import ollama
import pandas as pd
from tqdm import tqdm
import re
import time

from normalize_text import non_binary_standardization

### Function to translate sentences with the Ollama API ###

API_irt = "sk-xxxxxxxxxxxxxxxx"
BASE_URL="http://chatbot.xxxxxxx.local/ollama"


client = ollama.Client(
  host=BASE_URL,
  headers={"Authorization": f"Bearer {API_irt}"}
)


def translate_with_LLM(english_sentence, model_name, context="" ,max_retries=20, retry_delay=1):
    """
    Translates an English sentence to French using the Ollama API.
    Automatically retries if a 503 error occurs.
    
    Args:
        english_sentence (str): The sentence to translate.
        model_name (str): The name of the model to use.
        max_retries (int): Maximum number of retries for 503 errors.
        
    Returns:
        str: The translated sentence, or None if all retries fail.
    """
    retries = 0
    
    while retries < max_retries:
        try:
            response = client.chat(model=model_name, messages=[
                {
                    'role': 'user',
                    'content': context + f"Translate the following sentences from English to French: '{english_sentence}'. Respond with the translation only, nothing else.",
                }
            ])
            
            # Extract translation from response
            translation = response.message.content.strip().strip('"')
            translation = translation.split('\n', 1)[0]
            return non_binary_standardization(translation)
        
        except Exception as e:
            retries += 1
            time.sleep(retry_delay)  # Wait before retrying

    # If max retries are exceeded
    print(f"Failed to translate sentence '{english_sentence}' after {max_retries} retries.")
    return None


### Load data ###

#model_name = 'gemma2:2b'
#model_name = 'mistral:7b'
model_name = 'llama3.1:8b'
#model_name = 'llama3.3:latest'


baseline = ""
moral_context = "You are a translation without gender bias and LGBTQA+ friendly. "
linguistic_context = "Forms like 'iel' as a neutral pronoun, 'un·e,' 'lea,' or 'ce·tte' as neutral determiners, or a mid-dot (e.g., 'étudiant·e') for gender-neutral terms to be applied only if explicitly requested. Otherwise, use the classic feminine or masculine form. "


context_choice = "Baseline"

if context_choice == "Baseline":
    context = baseline
    file_path = "translation/FairTranslate_with_MT.csv"
elif context_choice == "Moral":
    context = moral_context
    file_path = "translation/FairTranslate_with_MT_MC.csv"
elif context_choice == "Linguistic":
    context = linguistic_context
    file_path = "translation/FairTranslate_with_MT_LC.csv"
elif context_choice == "Moral and Linguistic":
    context = moral_context + linguistic_context
    file_path = "translation/FairTranslate_with_MT_MLC.csv"


df = pd.read_csv(file_path, delimiter=';', quotechar='"', encoding="utf-8")


### Run Translations ###

translations = []
# Translate each sentence using a progress bar
for sentence in tqdm(df["english"], desc="Translation in progress"):
    translation = translate_with_LLM(sentence, model_name, context=context)
    translations.append(translation)

# Add translations to DataFrame
df[f"MT_french_{model_name}"] = translations

# Save the updated dataset
df.to_csv(file_path, sep=';', quotechar='"', encoding="utf-8", index=False)

print(f"Translated file saved as: {file_path}")