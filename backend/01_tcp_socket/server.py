# 소켓: 네트워크의 출입문(창구) 같은 역할을 한다. 프로그램이 OS의 네트워크 기능을 쓰기위한 출입구이고 endpoint라고도 불린다.
import socket

# 1. 접속 정보 정의
host = "127.0.0.1"
port = 5000
address = (host, port)

# 2. 소켓 생성
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 3. 바인딩: 소켓에 address(IP:포트)를 묶어, 이 주소로 오는 요청을 이 소켓이 받도록 OS에 등록한다.
s.bind(address)

# 4. Listening: 연결 요청을 받을 수 있는 상태로 전환한다. (바로 반환되며 여기서 대기하지 않음)
s.listen()      # backlog(선택): accept되기 전에 대기시킬 수 있는 연결 수. 정수로 지정하며 생략하면 OS 기본값을 사용한다.

# 5. 연결 수락: 클라이언트가 접속할 때까지 여기서 블로킹된다.
conn, addr = s.accept()

"""
- conn: 해당 클라이언트 전용 새 통신 소켓. 이후 송수신에 사용
- addr: 클라이언트 주소. (IP, 포트) 튜플 (예: ("127.0.0.1", 53124))
        클라이언트 포트는 OS가 임의로 배정하므로 접속할 때마다 달라진다.
"""
# print(f"connect: {conn} / address: {addr}")

#################################################################
### 2단계: 수신 → 응답 → 종료                                    ###
#################################################################


# 2-1. 데이터 수신
print("클라이언트 데이터 수신 대기 중...")
recv_data = conn.recv(1024)

# 2-2. 수신 데이터 출력
print(f"순수 byte객체: {recv_data}")
print(f"디코딩 결과: {recv_data.decode("utf-8")}")

# 2-3. 응답 생성
response = "수신 완료"

# 2-4. 응답 송신
send_data = response.encode("utf-8")
conn.sendall(send_data)
print("응답 송신 완료")

"""
- send: 보낸 만큼만 처리하고 실제 전송한 바이트 수를 반환. 데이터가 크면 일부만 보낼 수 있어 직접 재시도 필요
- sendall: 전부 보낼 때까지 내부에서 반복. 학습용은 이쪽이 안전
"""

# 2-5. 통신 종료
print("응답 종료")
conn.close()        # 통신 소켓 닫기
s.close()           # 리스닝 소켓 닫기