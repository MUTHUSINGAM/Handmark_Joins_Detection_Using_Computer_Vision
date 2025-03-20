
📌 Hand Landmark & Joint Detection Using Computer Vision
This project implements real-time hand landmark and full-body joint detection using OpenCV, MediaPipe, and Streamlit. It captures video from a webcam and visualizes key hand landmarks and body joints with labeled annotations.

🚀 Project Structure
📂 Hand Landmark  
│── custom_hand_pose_model.pt   # (Optional) Custom-trained hand pose model  
│── main.ipynb                  # Jupyter Notebook with ML code (core logic without UI)  
│── project.py                   # Streamlit-based application for real-time detection  
│── README.md                    # Project Documentation  
│── requirements.txt              # Dependencies for installation  

🎯 Project Overview
- `main.ipynb`: Contains the core hand & body joint detection logic using MediaPipe & OpenCV.
- `project.py`: A Streamlit-based real-time interface for detecting hand landmarks and body joints.
- `requirements.txt`: Lists all necessary dependencies for setting up the environment.

🛠️ Installation & Setup
1️⃣ Clone the Repository:
```sh
git clone https://github.com/MUTHUSINGAM/Handmark_Joins_Detection_Using_Computer_Vision.git
cd Handmark_Joins_Detection_Using_Computer_Vision
```
2️⃣ Create a Virtual Environment (Optional but Recommended):
```sh
python -m venv env  
# Activate on Mac/Linux  
source env/bin/activate  
# Activate on Windows  
env\Scripts\activate  
```
3️⃣ Install Dependencies:
```sh
pip install -r requirements.txt
```

📷 How to Run
▶️ Run Jupyter Notebook (For ML Code Only):
```sh
jupyter notebook
```
Open `main.ipynb` and run all cells.

▶️ Run the Streamlit Application:
```sh
streamlit run project.py
```
This will launch a web-based interface for real-time hand landmark and body joint detection.

📌 Key Features
✔️ Real-time detection of hand landmarks and body joints using a webcam.  
✔️ Utilizes MediaPipe's Holistic Model for full-body detection.  
✔️ Streamlit UI for interactive visualization.  
✔️ Labeled finger tips & body joints with clear annotations.  
✔️ Supports additional model integration (custom hand pose model).  

📦 Dependencies (`requirements.txt`):
```txt
opencv-python  
mediapipe  
streamlit  
pillow  
numpy  
```

📜 License  
This project is open-source and available under the MIT License.
```

Would you like any modifications or additional formatting? 😊
