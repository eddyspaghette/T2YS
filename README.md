# Fall Hacks 2023
Talk To Your Scheduler

Turning over a new leaf in our project means the user may need help organizing their life. They can organize events in our scheduler web app.

## File structure
T2YS<br>
├── LLM Module<br>
│ ├── main.py<br>
│ ├── models<br>
│ │ └── llama-2-7b-chat.Q5_K_M.gguf<br>
│ ├── requirements.txt<br>
│ ├── schedule_example.json<br>
│ └── venv<br>
├── README.md<br>
├── docker-compose.yml<br>
└── frontend<br>
    ├── Dockerfile<br>
    ├── db.sqlite3<br>
    ├── frontend<br>
    │ ├── __init__.py<br>
    │ ├── asgi.py<br>
    │ ├── settings.py<br>
    │ ├── urls.py<br>
    │ └── wsgi.py<br>
    ├── manage.py<br>
    ├── requirements.txt<br>
    ├── schedule<br>
    │ ├── __init__.py<br>
    │ ├── admin.py<br>
    │ ├── apps.py<br>
    │ ├── migrations<br>
    │ │ ├── 0001_initial.py<br>
    │ │ ├── __init__.py<br>
    │ ├── models.py<br>
    │ ├── predict_model<br>
    │ │ ├── README.md<br>
    │ │ ├── __init__.py<br>
    │ │ └── main.py<br>
    │ ├── tests.py<br>
    │ ├── urls.py<br>
    │ ├── utils.py<br>
    │ └── views.py<br>
    ├── static<br>
    │ ├── schedule<br>
    │ │ └── calendar.js<br>
    │ └── style.css<br>
    └── templates<br>
        ├── registration<br>
        │ └── login.html<br>
        └── schedule<br>
            └── index.html<br>

## Participants
Edward Zhou ejz2@sfu.ca <br>
Anh Khoa Nguyen anhkhoan@sfu.ca <br>
Zeti Xiong zetix@sfu.ca<br>
Anmol Sekhon ass53@sfu.ca<br>

## Setup and run instructions

Download the Llama2 model from https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf and put to frontend/models/

`pip install -r requirements.txt` in frontend folder

`python manage.py migrate` in frontend folder

`python manage.py runserver` in frontend folder

Go to http://localhost:8000/ in your browser

## Github link
https://github.com/eddyspaghette/T2YS

## Acknowledgements:
Django tutorial: https://docs.djangoproject.com/en/4.2/intro/
Chat-GPT was used to assist with front-end development
Llama_cpp tutorial: https://swharden.com/blog/2023-07-29-ai-chat-locally-with-python/
Model Name: TheBloke/Llama-2-7b-Chat 
Model: https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf

