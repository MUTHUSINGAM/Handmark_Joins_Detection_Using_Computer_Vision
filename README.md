
📌 Hand Landmark & Joint Detection Using Computer Vision
This project implements real-time hand landmark and full-body joint detection using OpenCV, MediaPipe, and Streamlit. It supports real-time video capture from a webcam and visualizes key hand and body joints with labeled annotations.

🚀 Project Structure
bash
Copy
Edit
📂 Hand Landmark  
│── custom_hand_pose_model.pt   # (Optional) Custom-trained hand pose model  
│── main.ipynb                  # Jupyter Notebook with ML code (core logic without UI)  
│── project.py                   # Streamlit-based application for real-time detection  
│── README.md                    # Project Documentation  
│── requirements.txt              # Dependencies for installation  
🎯 Project Overview
main.ipynb: Contains the core hand & body joint detection logic using MediaPipe & OpenCV.
project.py: A Streamlit-based real-time interface for detecting hand landmarks and body joints.
requirements.txt: Contains all necessary dependencies to set up the environment.
🛠️ Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/MUTHUSINGAM/Handmark_Joins_Detection_Using_Computer_Vision.git
cd Handmark_Joins_Detection_Using_Computer_Vision
2️⃣ Create a Virtual Environment (Optional but Recommended)
sh
Copy
Edit
python -m venv env  
source env/bin/activate   # On Mac/Linux  
env\Scripts\activate      # On Windows  
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
📷 How to Run
▶️ Run Jupyter Notebook (For ML Code Only)
sh
Copy
Edit
jupyter notebook
Open main.ipynb and run all cells.

▶️ Run the Streamlit Application
sh
Copy
Edit
streamlit run project.py
This will launch a web-based interface to detect hand landmarks and body joints in real time.

📌 Key Features
✔️ Real-time detection of hand landmarks and body joints using a webcam
✔️ Uses MediaPipe's Holistic Model for full-body detection
✔️ Streamlit UI for interactive visualization
✔️ Labels finger tips, body joints, and draws connections between them

📦 Dependencies (requirements.txt)
txt
Copy
Edit
opencv-python  
mediapipe  
streamlit  
pillow  
numpy  
📜 License
This project is open-source and available under the MIT License.
