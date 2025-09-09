# COVID-19 Tracker & Chatbot

This is a **multi-page Streamlit app** built with Python.  
It has the following features:



- **COVID Tracker**: Track COVID status in different countries. 
     
      This project is a **COVID-19 Tracker Web Application** built with **Streamlit**.  
It allows users to search for the latest COVID-19 statistics (cases, deaths, recovered) by entering a country name.  

The app fetches live data from the **[disease.sh API](https://disease.sh/)** and presents it in a simple, user-friendly interface.  

Custom CSS styling is applied to enhance the UI and highlight important metrics.

    Features
            -  Search for any country by name to get the latest COVID-19 statistics  
            -  Displays total cases, deaths, and recoveries in styled metric cards  
            -  Custom CSS for better visuals  
            -  Real-time data fetching from the public API  

    Technologies Used
            -Python 3 – Core programming language
            - Streamlit – For building the interactive web app
            - Pandas – For handling and displaying data (optional extension if needed later)
            - Requests – To fetch real-time COVID-19 data from the API
            - HTML + CSS – For custom styling and layout of the app




- **Chat Bot**: Ask questions related to COVID.  
   
   This is a **COVID-19 Chatbot Web Application** built with **Streamlit** and **LangChain**.  
   It acts as a friendly virtual assistant that can answer questions about COVID-19, including:  
- Symptoms, prevention, and safety measures  
- Vaccination and booster information  
- Travel and quarantine guidelines  
- Steps to follow if exposed or tested positive  

The chatbot uses **OpenRouter API** (via LangChain) to connect with advanced AI language models and provide accurate, conversational responses.  

Custom CSS styling is applied to display a chat-like interface.
            
         Features
                -  Interactive chatbot for COVID-19 guidance  
                -  Maintains **chat history** using conversation memory  
                -  Styled messages for user and assistant responses  
                -  Uses **environment variables** for secure API key handling  
                -  Real-time responses from GPT-based AI models
        
         Technologies Used
                - Python 3 – Core programming language  
                - Streamlit – For building the interactive chatbot UI  
                - LangChain – For managing prompts, memory, and AI interaction  
                - OpenRouter API – To access GPT-based AI models  
                - dotenv– For securely loading API keys from environment variables  
                - HTML + CSS – For custom styling of the chat window  
        


## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   

## Create a virtual environment and install dependencies:  
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt

## Run the Streamlit app:
streamlit run app.py