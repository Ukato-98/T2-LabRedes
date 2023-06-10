import socket
import hashlib
from GeradorDeArquivo import gerar_arquivo

def verify_checksum(data, checksum):
    calculated_checksum = hashlib.sha256(data).digest()
    return calculated_checksum == checksum

def receive_file(sock):
    count=0
    while True:
        # Recebe o pacote
        packet, addr = sock.recvfrom(300)

        # Verifica se é um pacote vazio indicando o final do arquivo
        if len(packet) == 0:
            print("Recebido pacote vazio. Fim do arquivo.")
            break

        # Extrai o checksum e os dados do pacote
        checksum = packet[:32]
        data = packet[32:]

        # Verifica o checksum dos dados
        if verify_checksum(data, checksum):
            # Imprime os dados recebidos
            print(f'##PACOTE {count}')
            print(data.decode())
            print()
        else:
            print("Checksum inválido")
        count+=1

def server():
    host = 'localhost'
    port = 12345

    # Cria um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Vincula o socket ao endereço e porta especificados
    sock.bind((host, port))

    # Recebe o conteúdo do arquivo e exibe os dados do pacote recebido
    receive_file(sock)

    # Fecha o socket
    sock.close()

# Gera arquivo .txt para ser enviado nos pacotes
gerar_arquivo
# Executa o servidor
server()
