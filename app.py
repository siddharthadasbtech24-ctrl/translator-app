import streamlit as st
from anuvaad import Anuvaad
from gtts import gTTS
from googletrans import Translator
import tempfile, os

# gTTS language codes
LANG_CODES = {"Hindi": "hi", "Kannada": "kn", "Tamil": "ta", "Telugu": "te", "Malayalam": "ml"}

# Models supported by Anuvaad
ANU_MODEL = {"Hindi": "english-hindi"}  # ✅ only Hindi works

from deep_translator import GoogleTranslator

def translate_sentence(sentence, lang_choice):
    # Use deep-translator for all languages
    translated_text = GoogleTranslator(
        source="en",
        target=TTS_CODES[lang_choice]  # example: "hi", "kn", "ta"
    ).translate(sentence)
    return translated_text

def text_to_speech(text, lang_choice):
    tts = gTTS(text=text, lang=LANG_CODES[lang_choice])
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    return tmp.name

st.title("Translator (EN → Indian Languages) with Voice")

lang_choice = st.selectbox("Target language:", list(LANG_CODES.keys()))
sentence = st.text_input("English sentence:")

if st.button("Translate"):
    if not sentence.strip():
        st.warning("Bruh, enter something first.")
    else:
        try:
            translation = translate_sentence(sentence, lang_choice)
            st.success(f"{lang_choice}: {translation}")
            audio_file = text_to_speech(translation, lang_choice)
            st.audio(open(audio_file, "rb").read(), format="audio/mp3")
            os.remove(audio_file)
        except Exception as e:
            st.error(f"Error for {lang_choice}: {e}")
