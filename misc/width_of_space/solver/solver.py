text = open("problem.txt").read()

dummy = text.replace("🌌", "0").replace("🪐", "1").replace("\u200b", "").replace("\u200c", "")
print("Dummy: "+"".join([chr(int(dummy[i: i+8], 2)) for i in range(0, len(dummy), 8)]))

text = text.replace("🌌", "").replace("🪐", "").replace("\u200b", "0").replace("\u200c", "1")
print("Flag: "+"".join([chr(int(text[i: i+8], 2)) for i in range(0, len(text), 8)]))