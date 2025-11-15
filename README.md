🚀 AutoFlow — AI Automation Dashboard

AI-powered productivity & automation tool built with Django + TailwindCSS

AutoFlow is a smart automation dashboard designed to simplify repetitive daily tasks.
It uses AI (OpenAI APIs) + CSV analytics to generate insights, summaries, and email drafts — all in a clean, modern UI.

🔥 Features

✔ CSV Upload & Analysis
✔ AI-Generated Summary (OpenAI)
✔ Smart Email Draft Generator
✔ Clean, Fast TailwindCSS Interface
✔ REST API built with Django + DRF
✔ Fully responsive dashboard

🛠 Tech Stack

Backend: Django, Django REST Framework, Python

AI: OpenAI API

Frontend: TailwindCSS

Tools: Pandas (CSV parsing), Render (deployment)


📦 API Endpoints
POST /api/process-csv/


{
  "file": "data.csv"
}

POST /api/generate-email/

Send summary → get AI-generated draft email

{
  "summary": "CSV insights here..."
}

🧩 How it Works

User uploads CSV

Data is parsed using Pandas

AI (OpenAI) generates insights

AutoFlow drafts a professional email

User reviews & sends

🧑‍💻 My Role

I developed the entire backend (APIs, logic, integration) and connected it to a modern TailwindCSS UI.
Focus: AI integration, automation workflows, and clean API design.

🌐 Live Demo

🔗 https://autoflow-av9n.onrender.com

(If Render is sleeping, wait 30–60 seconds)

📁 Code

🔗 GitHub: https://github.com/Tarun08940/Autoflow

📝 License

MIT License
