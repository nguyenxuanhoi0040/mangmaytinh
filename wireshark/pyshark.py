import pyshark
path = r'D:/Đại Học/mạng máy tính/data/data16a2hn020425.pcapng'
cap  = pyshark.FileCapture(path, display_filter='http.request')
for i, pkt in enumerate(cap):
    try:
        # Chuyển toàn bộ nội dung HTTP sang chữ thường để tìm kiếm dễ hơn
        http_info = str(pkt.http).lower()

        # Nếu gói tin chứa từ khóa 'login' hoặc 'test'
        if any(keyword in http_info for keyword in ['login', 'test']):
            print("=" * 50)
            print(f"GÓI #{i+1} Có chứa từ khóa")

            # Hiển thị thời gian bắt được gói tin
            print("Thời gian:", pkt.sniff_time)

            # Hiển thị địa chỉ IP nguồn và IP đích
            if hasattr(pkt, 'ip'):
                print("IP nguồn:", pkt.ip.src)
                print("IP đích:", pkt.ip.dst)
            else:
                print("Không có thông tin IP")

            # Hiển thị phương thức HTTP
            if hasattr(pkt.http, 'request_method'):
                print("Phương thức:", pkt.http.request_method)

            # Hiển thị URL nếu có đầy đủ thông tin
            if hasattr(pkt.http, 'host') and hasattr(pkt.http, 'request_uri'):
                print("URL:", f"http://{pkt.http.host}{pkt.http.request_uri}")

            # Hiển thị Cookie nếu có
            if hasattr(pkt.http, 'cookie'):
                print("Cookie:", pkt.http.cookie)
            #Hiển thị dữ liệu gửi đi trong phần thân(POST form data) 
            if hasattr(pkt.http, 'file_data'):
                print("Payload:", pkt.http.file_data)
    except Exception as e:
        print(f"Lỗi khi xử lý gói tin #{i+1}: {e}")
