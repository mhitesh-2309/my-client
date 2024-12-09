import socket
import threading


host=input("Enter the link for server: ")
nickname=input("Enter your nickname: ")
channel=input("Enter the channel name which u want to enter: ")
port=6667
try:
    IRC=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IRC.connect((host,port))
    print("Successfully Ocnnected to Liberachat")
except:
    print("Connection to Freenode Failed!")

IRC.send(f"NICK {nickname}\r\n".encode("utf-8"))
IRC.send(f"USER {nickname} 0 * :Naaradha\r\n".encode("utf-8"))
IRC.send(f"JOIN {channel}\r\n".encode("utf-8"))

def thekickback():
    while True:
        feedback=IRC.recv(2048).decode("utf-8")
        if feedback.startswith("PING"):
            IRC.send(f"PONG{feedback.split()[1]}\r\n".encode("utf-8"))
        elif feedback.find("PRIVMSG "+channel)>-1:
            endofusername=feedback.find("~")-1
            theirnick=feedback[1:endofusername]
            print("\n")
            print(theirnick+feedback[feedback.find("PRIVMSG "+channel):])


def tlk():
    while True:
        print("Enter your message: ")
        mess = input()
        if mess.lower() == "/quit":
            irc.send(f"PART {channel}\r\n".encode("utf-8"))
            irc.send(f"QUIT :Goodbye!\r\n".encode("utf-8"))
            irc.close()
            break
        IRC.send(f"PRIVMSG {channel} :{mess}\r\n".encode("utf-8"))

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=thekickback, daemon=True)
send_thread = threading.Thread(target=tlk, daemon=True)

send_thread.start()
receive_thread.start()


# Wait for threads to finish
send_thread.join()
receive_thread.join()
