# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="models/T2YS/llama-2-7b-chat.Q3_K_L.gguf")

# create a text prompt
prompt = "Q: Generate a basic json file A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
