# Hiding Information Inside Image Steganography Using ASCII Character

## Capstone Project  
**Presented By:** Amrjeet Usnale  
**College Name:** MIT ADT University  
**Department:** BCA in Cloud Computing  

---

## 📑 Table of Contents
- [Problem Statement](#problem-statement)
- [System Development Approach](#system-development-approach)
- [Algorithm & Deployment](#algorithm--deployment)
- [Result](#result)
- [Conclusion](#conclusion)
- [Future Scope ](#future-scope-optional)
- [References](#references)

---

## 🧩 Problem Statement
In an era where data security and privacy are critical, securing sensitive information from unauthorized access is essential. Traditional encryption methods often signal the presence of protected data, making them targets for attack. Steganography offers a stealthy alternative by hiding data within other files, such as images.

This project focuses on implementing **image steganography using ASCII character encoding**, allowing secret messages to be embedded in images without perceptible changes. The aim is to ensure secure communication and safe data transfer while maintaining the integrity and appearance of the cover image.

---

## ⚙️ System Development Approach

The approach involves using the **Least Significant Bit (LSB)** method to embed messages in image files.

### 🛠️ Technologies Used
- **Python 3.9+**
- **Streamlit**: for interactive web-based GUI
- **PIL (Pillow)**: for image processing

### 💻 System Features
- A user-friendly web interface to encode and decode messages.
- Image upload and message input directly through the browser.

---

## 📋 Algorithm & Deployment

### Step-by-Step Procedure:
1. Import necessary libraries (`Streamlit`, `PIL`).
2. Build a `Streamlit`-based UI for image upload and message entry.
3. Create an ASCII encoding function to convert messages to binary and embed it in the image pixels.
4. Create a decoding function to extract and reconstruct the hidden message.
5. Add buttons for encoding and decoding within the `Streamlit` app.
6. Display original and stego images in the UI.
7. Validate correctness by comparing original vs. stego image visually and by decoding successfully.

---

## 📸 Result

- A GUI using `Streamlit.py` was developed.
- Full encryption and decryption functionality was implemented.
- Real-time interaction with image steganography features.
---
![Screenshot 2025-06-19 103516](https://github.com/user-attachments/assets/1477ce44-5071-404f-b554-9530fe93995c)

![Screenshot 2025-06-19 104521](https://github.com/user-attachments/assets/67513e67-3315-480f-9637-e0088df39aec)


---

## ✅ Conclusion

The project **"Hiding an Information Inside Image Steganography Using ASCII Character"** demonstrates a practical and secure method for concealing messages within digital images.

By utilizing steganography and ASCII character encoding, the system ensures that hidden data remains **imperceptible** to the human eye. The `Streamlit` interface simplifies both the embedding and extraction processes, offering a **user-friendly experience**.

### 🚧 Key Challenges:
- Preserving original image quality
- Enabling real-time previews in the browser

---

## 🔮 Future Scope 
- Integrate message encryption before embedding
- Support image-to-image hiding
- Enhance performance for larger file sizes
- Add drag-and-drop functionality
- Extend to audio/video steganography

---

## 📚 References
- [Python Pillow Documentation](https://pillow.readthedocs.io/)
- [GeeksforGeeks: Image Steganography Using Python](https://www.geeksforgeeks.org/image-steganography-using-python/)
- [Wikipedia: Steganography](https://en.wikipedia.org/wiki/Steganography)
- Various academic papers on data hiding and secure communication

---

## How to Run the App

```sh
streamlit run streamlit_app.py
