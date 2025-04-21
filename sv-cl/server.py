import socket

# Thiết lập server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))  # Lắng nghe trên IP và cổng 5000
server_socket.listen(5)  # Cho phép tối đa 5 kết nối chờ
print("Server đang lắng nghe kết nối trên cổng 5000...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Kết nối từ {client_address}")
    
    while True:
        # Nhận dữ liệu từ client
        data = client_socket.recv(1024).decode()
        if not data:
            break  # Nếu client đóng kết nối, thoát khỏi vòng lặp
        
        print(f"Dữ liệu nhận được: {data}")
        
        # Nếu nhận được "exit" thì đóng server
        if data.lower() == "exit":
            print("Server nhận được lệnh thoát! Đang tắt...")
            client_socket.send("Server đang đóng...".encode())
            client_socket.close()
            server_socket.close()
            print("Server đã đóng hoàn toàn.")
            exit()
        
        # Phản hồi client
        response = "Server đã nhận dữ liệu!"
        client_socket.send(response.encode())
    
    # Đóng kết nối với client khi kết thúc trao đổi
    client_socket.close()
    print("Kết nối với client đã đóng.")
