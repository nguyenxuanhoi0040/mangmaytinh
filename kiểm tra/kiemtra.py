#Nhóm gồm:
# Nguyễn Xuân Hội-22174600040
# Lê Tuấn Thành -22174600119
import pyshark

# Mở file .pcapng để phân tích
cap = pyshark.FileCapture('C:/Users/hoi26/Desktop/kiemtr2/kiemtra.pcapng')


    # Duyệt qua các gói tin và in ra thông tin theo tầng trong mô hình OSI
for packet in cap:
    print("\n--------------------------------------")
    print("Thông tin về gói tin: ")

    # Tầng 2 (Data Link Layer) - Thông tin Ethernet
    if 'eth' in packet:
        print("Tầng 2 - Ethernet:")
        print(f"  Source MAC: {packet.eth.src}")
        print(f"  Destination MAC: {packet.eth.dst}")
        print(f"  Type: {packet.eth.type}")
        
    # Tầng 3 (Network Layer) - Thông tin IP
    if 'ip' in packet:
        print("\nTầng 3 - IP:")
        print(f"  Source IP: {packet.ip.src}")
        print(f"  Destination IP: {packet.ip.dst}")
        print(f"  Protocol: {packet.ip.proto}")
# Đóng file khi hoàn tất phân tích
cap.close()