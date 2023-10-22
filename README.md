# Fall Hacks 2023
Talk To Your Scheduler

Turning over a new leaf in our project means the user may need help organizing their life. They can organize events in our scheduler web app.

## File structure
T2YS<br>
├── LICENSE <br>
├── LLM Module<br>
│   ├── requirements.txt<br>
│   ├── schedule_example.json<br>
├── README.md<br>
├── backend<br>
├── docker-compose.yml<br>
├── frontend<br>
│   ├── Dockerfile<br>
│   ├── frontend<br>
│   ├── manage.py<br>
│   ├── requirements.txt<br>
│   ├── schedule<br>
│   ├── static<br>
│   └── templates<br>

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

## Github link
https://github.com/eddyspaghette/T2YS

## Acknowledgements:
Django tutorial: https://docs.djangoproject.com/en/4.2/intro/
Chat-GPT was used to assist with front-end development
Llama_cpp tutorial: https://swharden.com/blog/2023-07-29-ai-chat-locally-with-python/
Model Name: TheBloke/Llama-2-7b-Chat 
Model: https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf

