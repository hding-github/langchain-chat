# https://docs.gpt4all.io/gpt4all_python/home.html

from gpt4all import GPT4All



# 7.37 GB	16 GB	13 billion	q4_0	Nomic AI	GPL
strModel = "gpt4all-13b-snoozy-q4_0.gguf"

# 2.18 GB	4 GB	3.8 billion	q4_0	Microsoft	MIT
strModel = "Phi-3-mini-4k-instruct.Q4_0.gguf" 

# 4.66 GB	8 GB	8 Billion	q4_0	Meta	    Llama 3 License
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM

with model.chat_session():
    print(model.generate("extract subject verb and object relation from 'How can I run LLMs efficiently on my laptop?'", max_tokens=1024))


print("Complete")