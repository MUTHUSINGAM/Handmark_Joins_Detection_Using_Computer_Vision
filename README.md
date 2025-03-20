# ✋ **HAND LANDMARK & JOINT DETECTION USING COMPUTER VISION**

🚀 **Real-time hand landmark and full-body joint detection using OpenCV, MediaPipe, and Streamlit.** 
This project captures video from a webcam and visualizes key hand landmarks and body joints with labeled annotations.

---

## 📂 Project Structure
```
📂 Hand Landmark Detection  
│── custom_hand_pose_model.pt   # (Optional) Custom-trained hand pose model  
│── main.ipynb                  # Jupyter Notebook with ML code (core logic without UI)  
│── project.py                   # Streamlit-based application for real-time detection  
│── README.md                    # Project Documentation  
│── requirements.txt              # Dependencies for installation  
```

### 🎯 Project Overview
- **`main.ipynb`**: 
  - Contains core hand & body joint detection logic using MediaPipe & OpenCV.
  - Captures and processes real-time video for detecting and annotating landmarks.
  - Used for debugging and testing the detection pipeline.
- **`project.py`**: 
  - Implements a Streamlit-based web interface for real-time visualization.
  - Provides an interactive UI for running landmark detection.
  - Displays processed frames with annotated landmarks in a user-friendly format.
- **`requirements.txt`**: Lists all necessary dependencies for setting up the environment.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository:
```sh
git clone https://github.com/MUTHUSINGAM/Handmark_Joins_Detection_Using_Computer_Vision.git
cd Handmark_Joins_Detection_Using_Computer_Vision
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended):
```sh
python -m venv env  
# Activate on Mac/Linux  
source env/bin/activate  
# Activate on Windows  
env\Scripts\activate  
```

### 3️⃣ Install Dependencies:
```sh
pip install -r requirements.txt
```

---

## 📷 How to Run

▶️ **Run Jupyter Notebook (For ML Code Only):**
```sh
jupyter notebook
```
Open `main.ipynb` and run all cells.

▶️ **Run the Streamlit Application:**
```sh
streamlit run project.py
```
This will launch a web-based interface for real-time hand landmark and body joint detection.

---

## 📌 Key Features
✔️ **Real-time detection** of hand landmarks and body joints using a webcam.  
✔️ **MediaPipe's Holistic Model** for full-body detection.  
✔️ **Interactive Streamlit UI** for better visualization.  
✔️ **Labeled finger tips & body joints** with clear annotations.  
✔️ **Supports additional model integration** (custom hand pose model).  

---

## 📦 Dependencies (`requirements.txt`):
```txt
opencv-python  
mediapipe  
streamlit  
pillow  
numpy  
```
## Model Output Image in Streamlit:
##Image 1 with Full Body

![image](https://github.com/user-attachments/assets/2a289c90-f2fa-4012-b283-da15d4f3b3e4)


![WhatsApp Image 2025-03-20 at 18 51 40_29a66527](https://github.com/user-attachments/assets/f895508e-0f3e-403c-bbfc-5d918fcd3702)

## Image 2 with handmark with fingers name
![WhatsApp Image 2025-03-20 at 18 53 57_95eca945](https://github.com/user-attachments/assets/dc539880-3a7a-45dc-b0ec-8c242a13531c)


---

