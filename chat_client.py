import socket
import threading
from crypto_helper import encrypt_message, decrypt_message

host = "192.168.157.128"
port = 12345

s = socket.socket()
s.connect((host, port))

def receive():
    while True:
        try:
            data = s.recv(4096)
            if not data:
                print ("å°æ–¹å·²é›¢ç·š")
                break
            decrypted = decrypt_message(data.decode())
            print (f"\nå°æ–¹èªªï¼š{decrypted}")
        except Exception as e:
            print ("æŽ¥æ”¶éŒ¯èª¤ï¼š", e)
            break
def send():
    while True:
        msg = input("ä½ èªªï¼š")
        encrypted = encrypt_message(msg)

        if isinstance(encrypted, str):
            s.send(encrypted.encode())
        else:
            s.send(encrypted)

        if msg.lower() == 'exit':
            print ("ä½ å·²é›¢é–‹èŠå¤©å®¤ã€‚")
            s.close()
            break

recv_thread = threading.Thread(target=receive, daemon=True)
send_thread = threading.Thread(target=send)

recv_thread.start()
send_thread.start()

send_thread.join()