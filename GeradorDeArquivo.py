def gerar_arquivo():
    file_size = 1024 * 1024
    chunk_size = 300  # Tamanho dos chunks

    with open("file.txt", "w") as file:
        # Escreve dados no arquivo até atingir o tamanho desejado
        while file.tell() < file_size:
            file.write("x" * chunk_size)

gerar_arquivo()