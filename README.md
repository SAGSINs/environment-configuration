# Config Environment - Topology Simulation

## Mô tả dự án

Dự án này là một mô phỏng topology mạng sử dụng Docker Compose để tạo ra một mạng lưới các node đại diện cho các môi trường khác nhau: không gian (space), không khí (air), mặt đất (ground), và biển (sea). Mỗi node được triển khai dưới dạng container Docker với địa chỉ IP tĩnh trong mạng `topo_net`.

## Cấu trúc mạng

- **Space nodes**: space1, space2 (192.168.100.11, 192.168.100.12)
- **Air nodes**: air1, air2, air3 (192.168.100.21, 192.168.100.22, 192.168.100.23)
- **Ground nodes**: ground1 đến ground7 (192.168.100.31 đến 192.168.100.37)
- **Sea nodes**: sea1, sea2, sea3 (192.168.100.41, 192.168.100.42, 192.168.100.43)

## Yêu cầu hệ thống

- Docker
- Docker Compose

## Cài đặt và chạy

1. Clone repository:
   ```bash
   git clone https://github.com/pbl4-sagsins-and-heuristic/config-environment.git
   cd config-environment
   ```

2. Build và chạy các containers:
   ```bash
   docker-compose -f topology.docker-compose.yml up --build
   ```

3. Để chạy ở chế độ nền:
   ```bash
   docker-compose -f topology.docker-compose.yml up -d --build
   ```

## Cách sử dụng

Sau khi các containers được khởi động, bạn có thể:

- Kết nối vào một container cụ thể:
  ```bash
  docker exec -it <container_name> bash
  ```

- Kiểm tra mạng:
  ```bash
  docker network inspect configenvironment_topo_net
  ```

- Dừng các containers:
  ```bash
  docker-compose -f topology.docker-compose.yml down
  ```

## Tùy chỉnh

- Để thêm node mới, chỉnh sửa file `topology.docker-compose.yml`
- File `custom_hosts` được mount vào `/etc/hosts` của mỗi container để tùy chỉnh DNS

## Đóng góp

Vui lòng tạo issue hoặc pull request để đóng góp vào dự án.

## Giấy phép

[Thêm thông tin giấy phép nếu có]