from transformers import pipeline

model = pipeline("text-generation", model = "gpt2")

# Here’s how you can generate text using Python by using the GPT-2 model.
sentence = model("Hi, my name is John Cena. I am here",
                 do_sample = True,
                 top_k = 50,
                 temperature = 0.9,
                 max_length = 100,
                 num_return_sentences = 2)

for i in sentence:
    print(i["generated_text"])