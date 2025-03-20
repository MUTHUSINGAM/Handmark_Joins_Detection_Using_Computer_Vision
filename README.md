📌 Hand Landmark & Joint Detection Using Computer Vision
This project implements real-time hand landmark and full-body joint detection using OpenCV, MediaPipe, and Streamlit. It captures video from a webcam and visualizes key hand landmarks and body joints with labeled annotations.

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
main.ipynb → Contains the core hand & body joint detection logic using MediaPipe & OpenCV.
project.py → A Streamlit-based real-time interface for detecting hand landmarks and body joints.
requirements.txt → Lists all necessary dependencies for setting up the environment.
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
# Activate on Mac/Linux  
source env/bin/activate  
# Activate on Windows  
env\Scripts\activate  
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
Open main.ipynb and run all cells to execute the code.
▶️ Run the Streamlit Application
sh
Copy
Edit
streamlit run project.py
This will launch a web-based interface for real-time hand landmark and body joint detection.
🧠 Thinking About the Workflow
Step 1: Capture Real-Time Video
Open webcam using cv2.VideoCapture(0).
Step 2: Process the Frame
Convert to RGB format using cv2.cvtColor().
Apply MediaPipe Holistic Model using mp_holistic.process().
Step 3: Detect Hand Landmarks
If results.right_hand_landmarks exists, draw points.
Label finger tips (Thumb, Index, Middle, Ring, Pinky).
Step 4: Detect Body Joints
If results.pose_landmarks exists, draw keypoints.
Label major joints (Shoulders, Elbows, Wrists, Hips, Knees, Ankles).
Step 5: Display Processed Frame
Convert back to RGB format using cv2.cvtColor().
Show in Streamlit using video_placeholder.image().
📌 Key Features
✔️ Real-time detection of hand landmarks and body joints using a webcam.
✔️ Utilizes MediaPipe's Holistic Model for full-body detection.
✔️ Streamlit UI for interactive visualization.
✔️ Labeled finger tips & body joints with clear annotations.
✔️ Supports additional model integration (custom hand pose model).

📦 Dependencies (requirements.txt)
Copy
Edit
opencv-python  
mediapipe  
streamlit  
pillow  
numpy  
📜 License
This project is open-source and available under the MIT License.
