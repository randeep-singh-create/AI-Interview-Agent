## AI-powered Interview Assistant 

An interactive, AI-driven mock interview platform designed to simulate real-world technical and behavioral interviews. 
This application leverages advanced Language Models to generate dynamic questions and provide instantaneous, constructive feedback to users.

##  Features
* **Dynamic Question Generation:** Adapts questions in real-time based on the user's role, experience, and previous answers.
* **Instantaneous Feedback:** Provides constructive evaluation, highlighting strengths and areas for improvement.
* **Modern UI:** Built with a clean, responsive front-end interface.
* **High-Performance Backend:** Engineered with a robust API layer for fast response times.

##  Tech Stack
* **Frontend:** Streamlit
* **Backend API:** FastAPI
* **AI Core:** Groq LLM
* **Language:** Python 

##  Project Structure
```text
├── backend/          # FastAPI backend logic and LLM integration
├── frontend/         # Streamlit user interface
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation

## Installation & Setup

Follow these steps to run the project locally:
1. Clone the Repository
git clone [https://github.com/randeep-singh-create/AI-Interview-Agent.git](https://github.com/randeep-singh-create/AI-Interview-Agent.git)
cd AI-Interview-Agent

2. Set Up a Virtual Environment (Recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a ⁠.env⁠ file in the root directory and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

5. Run the Application
Because the frontend and backend are decoupled, you need to run them simultaneously in separate terminal windows:
Terminal 1: Start the FastAPI Backend
cd backend
uvicorn app:app --reload
Terminal 2: Start the Streamlit Frontend
cd frontend
streamlit run streamlitapp.py







