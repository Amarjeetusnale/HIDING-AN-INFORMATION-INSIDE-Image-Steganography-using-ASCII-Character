
import streamlit as st
from PIL import Image
from encryption_utils import encode_message, decode_message # Ensure you have this module with the encode/decode functions defined
# encryption_utils.py should contain the encode_message and decode_message functions as defined in the previous code snippet.
import io

st.set_page_config(page_title="Image Steganography", layout="centered")

st.title("🔐 Image Steganography Web App")
option = st.radio("Choose Operation", ["Encode", "Decode"])

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if option == "Encode":
        message = st.text_area("Enter the secret message")
        if st.button("Encrypt and Download"):
            if message:
                output_image = encode_message(image.copy(), message + "~~")
                buf = io.BytesIO()
                output_image.save(buf, format="PNG")
                st.download_button("Download Encrypted Image", buf.getvalue(), file_name="encrypted.png", mime="image/png")
            else:
                st.warning("Please enter a message to encrypt.")
    else:  # Decode
        if st.button("Decode Message"):
            decoded = decode_message(image)
            st.success(f"🔍 Hidden Message: {decoded}")
