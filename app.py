import os
import time
from typing import Any

from gtts import gTTS
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from google import genai
from google.genai import types
from PIL import Image


from utils.custom import css_code


from dotenv import load_dotenv


load_dotenv(".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("Gemini Key:", GEMINI_API_KEY)

client = genai.Client(api_key=GEMINI_API_KEY)






def progress_bar(amount_of_time: int) -> Any:
    """
    A very simple progress bar the increases over time,
    then disappears when it reached completion
    :param amount_of_time: time taken
    :return: None
    """
    progress_text = "Please wait, Generative models hard at work"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(amount_of_time):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

def generate_text_from_image(image_path):

    image = Image.open(image_path)

    prompt = """
You are an AI vision assistant.

Analyze this image and provide:

1. Image Scenario
2. A creative story (maximum 100 words).

Return exactly in this format:

Image Scenario:
...

Story:
...
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            prompt,
            image
        ]
    )

    return response.text




def generate_speech_from_text(message):

    filename = "generated_audio.mp3"

    tts = gTTS(
        text=message,
        lang="en",
        slow=False
    )

    tts.save(filename)

    print("Audio saved:", os.path.abspath(filename))

def main() -> None:

    st.set_page_config(
        page_title="IMAGE TO STORY CONVERTER",
        page_icon="🖼️"
    )

    st.markdown(css_code, unsafe_allow_html=True)

    st.title("🖼️ VisionSpeak AI")
    st.subheader("Generate Image Descriptions, Creative Stories & Speech with Gemini AI")

    uploaded_file = st.file_uploader(
        "Please choose a file to upload",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

       bytes_data = uploaded_file.getvalue()

       with open(uploaded_file.name, "wb") as file:
        file.write(bytes_data)

       st.image(uploaded_file, caption="Uploaded Image", width="stretch")

       progress_bar(100)

       result = generate_text_from_image(uploaded_file.name)

       scenario =""
       story = ""

       if "Story:" in result:
        parts = result.split("Story:", 1)
        scenario = parts[0].replace("Image Scenario:", "").strip()
        story = parts[1].strip()
       else:
        scenario = result
        story = "Story could not be generated."

       generate_speech_from_text(story)

       with st.expander("🖼️ Generated Image Scenario"):
        st.write(scenario)

       with st.expander("📖 Generated Story"):
        st.write(story)
        st.download_button(
        label="📄 Download Story",
        data=story,
        file_name="generated_story.txt",
        mime="text/plain"
        )

       if os.path.exists("generated_audio.mp3"):
        st.audio("generated_audio.mp3")
        with open("generated_audio.mp3", "rb") as audio_file:
         st.download_button(
         label="⬇️ Download Audio",
         data=audio_file,
         file_name="generated_story.mp3",
         mime="audio/mpeg"
         )
       else:
        st.error("Audio file was not created.")

        

if __name__ == "__main__":
    main()