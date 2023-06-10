import socket
import struct
import hashlib

def calculate_checksum(data):
    checksum = hashlib.sha256(data).digest()
    return checksum

def send_file(sock, filename, server_address):
    # Abre o arquivo em modo binário
    with open(filename, 'rb') as file:
        while True:
            # Lê os dados do arquivo em blocos de 256 bytes
            data = file.read(256)

            # Verifica se chegou ao final do arquivo
            if not data:
                # Envia um pacote vazio indicando o final do arquivo
                sock.sendto(b'', server_address)
                print("Enviado pacote vazio. Fim do arquivo.")
                break

            # Calcula o checksum dos dados
            checksum = calculate_checksum(data)

            # Monta o pacote com o checksum e os dados
            packet = checksum + data

            # Envia o pacote
            sock.sendto(packet, server_address)

def client():
    host = 'localhost'
    port = 12345
    server_address = (host, port)

    # Cria um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Nome do arquivo a ser enviado
    filename = 'file.txt'

    # Envia o arquivo para o servidor
    send_file(sock, filename, server_address)

    # Fecha o socket
    sock.close()

# Executa o cliente
client()
