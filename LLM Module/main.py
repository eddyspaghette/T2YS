# load the large language model file
from llama_cpp import Llama
from datetime import datetime
import json
LLM = Llama(model_path="models/T2YS/llama-2-7b-chat.Q5_K_M.gguf")

def searchValueFromString(s, ss):
    lines = s.split("\n")
    for line in lines:
        pos = line.find(ss)
        if (pos != -1):
            return line[pos+len(ss):]
    return None

def outputParser(s_input):
    name = searchValueFromString(s_input, "Name: ")
    startTime = searchValueFromString(s_input, "Starting Time: ")
    endingTime = searchValueFromString(s_input, "Ending Time: ")
        
    return {"name":name,"start_time":startTime,"end_time": endingTime}

# create a text prompt
#prompt = "Q:Give me an example json like this with an additional fake event element event3: "


prompt = "Q:Give me the Name, startingTime and the endingTime with datetime format YYYY-MM-DDTHH:MM:SS from this sentence without any different information:\n"

instruction = "an event starting 2023-10-21 at 10pm and ending at 11pm 2023-10-22 call it \"Dinner\""

prompt += instruction + "\nA:"


output = LLM(prompt,max_tokens=0)

# display the response
print(output["choices"][0]["text"])

json_output = outputParser(output["choices"][0]["text"])
print(json_output)