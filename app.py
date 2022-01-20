from cryptography.fernet import Fernet

# print (Fernet.generate_key())
key= "A1exbF2vvjTLjneNUbVitXdyF6hRSFnvHqkvu_tlvG0="
agent = Fernet(key)

word = " السلام عليكم ورحمة الله"
encrypted = agent.encrypt(bytes(word, "utf-8"))
# encrypted = str(encrypted, "utf-8")
# with open("encrypt.txt", "w") as f:
#     f.write(encrypted)


with open("encrypt.txt", "r", encoding="utf-8") as f:
    line = f.readline()

print(line)
x = agent.decrypt(bytes(line, "utf-8"))

with open("decrypt.txt", "w", encoding="utf-8") as f:
    f.write(str(x, "utf-8"))
# hello mmm good
