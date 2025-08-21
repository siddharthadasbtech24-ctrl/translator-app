import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

# Language mappings
LANGUAGES = {
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
}

translator = Translator()

def translate_text(sentence, lang_choice):
    try:
        result = translator.translate(sentence, dest=LANGUAGES[lang_choice])
        return result.text
    except Exception as e:
        return f"Translation failed: {e}"

def text_to_speech(text, lang_choice):
    tts = gTTS(text=text, lang=LANGUAGES[lang_choice])
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

# Streamlit UI
st.title("🧠 Multi-Language Translator (EN ➡ Indian Languages) with Voice")

lang_choice = st.selectbox("Select target language:", options=list(LANGUAGES.keys()))

sentence = st.text_input("Enter a sentence in English:")

if st.button("Translate"):
    if sentence.strip() == "":
        st.warning("Bruh, enter something first.")
    else:
        with st.spinner("Translating..."):
            translation = translate_text(sentence, lang_choice)
        
        st.success(f"Translation in {lang_choice}: {translation}")

        # TTS
        try:
            audio_file = text_to_speech(translation, lang_choice)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")
            os.remove(audio_file)
        except Exception as e:
            st.error(f"TTS failed: {e}")
