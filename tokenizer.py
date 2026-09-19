import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")
ids = tokenizer.encode("Hello World!")
print(ids)
tokens = tokenizer.decode(ids)
print(tokens)