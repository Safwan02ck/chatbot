AI Chatbot using OpenAI API & Flask:

This is a simple yet functional AI chatbot built using **Python**, **Flask**, and **OpenAI GPT-4-Turbo**. The chatbot has both a web interface and a terminal-based console mode. It allows users to interact with an AI model and get real-time responses.

---

Features:

-  Powered by OpenAI GPT-4 Turbo
-  Web-based interface using Flask
-  Console mode chatbot included
-  Simple and clean frontend with HTML/CSS
-  Secure API key storage via `.env`

---

Project Structure:
AICHAT/
├── chatbot.py           # Chat logic using OpenAI API
├── app.py               # Flask web server
├── templates/
│ └── index.html         # HTML frontend template
├── static/
│ └── style.css          # Custom CSS styling
├── .env                 # Environment variables (not shared)
└── README.md            # Project documentation

---

Requirements:

Make sure you have Python 3.8+ installed.

Install the required packages:

'''bash 
pip install openai flask python-dotenv

---

Setup Instructions:
1. Clone the Repository (if using Git):git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create a .env File
Create a file named .env in your project root and add your OpenAI API key:OPENAI_API_KEY=your_openai_api_key_here
3. Run the Flask App:python app.py
Then open your browser and go to:
http://127.0.0.1:5000

Console Mode (Optional)-
To use the chatbot in your terminal:python chatbot.py
You can chat with the bot by typing messages. To exit, type:
exit
quit
bye

---

CUSTOMIZE THE LOOK

Edit the static/style.css and templates/index.html files to change the chatbot's appearance.

IMPORTANT NOTES

- This chatbot is stateless — it doesn't remember past questions.
- Keep your .env file secure and never upload it publicly.
- To deploy it online, consider using Render, Heroku, or Vercel (with modifications).

LICENSE

This project is provided for educational and personal use. Feel free to modify and extend it!

CREDITS

Created using:
- OpenAI API (https://platform.openai.com/)
- Flask (https://flask.palletsprojects.com/)
- Python Dotenv (https://pypi.org/project/python-dotenv/)

