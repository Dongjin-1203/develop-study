import socket

# 0. 접속 정보 정의
host = "127.0.0.1"
port = 5000
address = (host, port)

# 1. 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 서버에 연결
s.connect(address)

# 3. 문자열 송신
send_message = "클라이언트 텍스트 송신"
s.sendall(send_message.encode("utf-8"))
print("정상 송신 완료")

# 4. 응답 수신
receive_message = s.recv(1024)
if receive_message != "":
    print("데이터 정상 수신")

# 5. 종료
print("통신 종료")
s.close()