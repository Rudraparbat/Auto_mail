# AUTO COLD EMAIL GENERATOR APP LANGCHAIN , GROQ , STREAMLIT , Llama-3.3-70b-versatile MODEL    
## Description :
Unlock Opportunities with Personalized Cold Emails <br>
Our Cold Email Generator App is designed to streamline your job application process by crafting personalized cold emails tailored to specific job postings. Simply provide a job post URL, and the app will generate a professional email that aligns with the job description and company requirements.

## Key Features :

Web scrapping : Extracts key information from the job post URL, such as required skills, company culture, and job expectations.
Advanced LLM Integration: Powered by Llama-3.3-70b-versatile, the app creates highly contextual and human-like email drafts, making your outreach stand out.
Dynamic Workflow with LangChain: Ensures seamless integration between data extraction, email composition, and user interaction.
User-Friendly Interface: Built with Streamlit, the app offers an intuitive UI for effortless input and real-time email generation.
Deployable Anywhere: Streamlit deployment capabilities make it easy to run the app in the cloud or locally.

### Installation Process :
1. Create a virtual enviornemnt :
python -m venv env<br>
2. Acticate the ENV :
env\scripts\activate<br>
3. Clone the Repo :
git clone https://github.com/Rudraparbat/Auto_mail.git <br>
4. Go to the directory :
cd Auto_mail
5. Install Dependencies :
pip install -r requirements.txt
#### Note : Before starting the app, Obtain and Store the API Key
Follow these steps to obtain your API key and securely store it for use in the application:
i>. Obtain the API Key :
-Visit the official website of groq .
-Create an account or log in if you already have one.
-Navigate to the API Keys section in your account dashboard.
-Generate a new API key and copy it. Keep this key secure, as it provides access to the API.
ii>. store the API Key Locally in secrets.toml :
- Create a file named secrets.toml in the root directory of your project.
- Add your API key in the following format:
api_key = <"your_actual_api_key">

6. Start The App :
streamlit run stream.py

enjoy your app at http://localhost:8501/ 

LIVE-LINK : -  https://rudraparbat-auto-mail-stream-kffhpm.streamlit.app/ 

