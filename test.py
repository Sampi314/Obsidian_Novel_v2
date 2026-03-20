import re
with open("scripts/relationship_data.js", "r") as f:
    text = f.read()

m1 = re.search(r'\s*\],\s*"relationships":\s*\[', text)
if m1:
    print("Found rels start at", m1.start())
else:
    print("Not found rels")

m2 = re.search(r'\s*\],\s*"factions":\s*\[', text)
if m2:
    print("Found factions start at", m2.start())
else:
    print("Not found factions")

if m1:
    print(text[m1.start()-20:m1.start()+30])
