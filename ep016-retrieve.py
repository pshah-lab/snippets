import re

docs = [
    "Paris is the capital of France.",
    "The Transformer paper came out in 2017.",
    "Fine-tuning changes the model itself.",
]
question = "When did the Transformer paper come out?"

words = lambda t: set(re.findall(r"\w+", t.lower()))
best = max(docs, key=lambda d: len(words(question) & words(d)))

print(f"Context: {best}\nQuestion: {question}")
