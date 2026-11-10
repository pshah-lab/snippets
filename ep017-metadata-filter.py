import re

chunks = [
    {"text": "Revenue grew 4% this quarter.", "company": "Globex", "quarter": "Q3 2026"},
    {"text": "Revenue grew 18% this quarter.", "company": "Acme", "quarter": "Q3 2026"},
    {"text": "Revenue grew 11% this quarter.", "company": "Acme", "quarter": "Q2 2026"},
]
question = "How much did Acme revenue grow in Q3 2026?"

words = lambda t: set(re.findall(r"\w+", t.lower()))
best = lambda pool: max(pool, key=lambda c: len(words(question) & words(c["text"])))

show = lambda label, c: print(f"{label}: {c['text']} ({c['company']}, {c['quarter']})")
show("No filter  ", best(chunks))
show("With filter", best([c for c in chunks if c["company"] == "Acme" and c["quarter"] == "Q3 2026"]))
