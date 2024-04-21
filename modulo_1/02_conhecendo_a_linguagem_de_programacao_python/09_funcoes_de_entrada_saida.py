with open("output.txt", "w") as f:
    print("Escrevendo no arquivo de texto", file=f)


import time

for i in range(10):
    print(f"Contagem: {i}", flush=True)
    time.sleep(2)
