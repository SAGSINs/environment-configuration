# SAGSIN Network Environment Configuration

Hệ thống môi trường Docker cho mạng lưới phân tán đa tầng (vệ tinh, máy bay, mặt đất, di động, tàu biển).

## 🏗️ Kiến Trúc Hệ Thống

```
┌─────────────────────────────────────────────────────────┐
│  Backend (NestJS) + MongoDB + Heuristic Service         │
│  Ports: 3000 (API), 50051 (Node gRPC), 50053 (Timeline) │
└─────────────────────────────────────────────────────────┘
                          ▲
                          │
┌─────────────────────────┴─────────────────────────┐
│              Network: 192.168.100.0/24             │
├────────────────────────────────────────────────────┤
│  🛰️  Satellites (2)    │  ✈️  Drones (3)          │
│  🏢  Ground Stations (3)│  📱 Mobile Devices (4)   │
│  🚢  Ships (3)          │                          │
└────────────────────────────────────────────────────┘
```

### Thành Phần

- **Backend**: API server, gRPC services (monitoring + timeline tracking)
- **Heuristic**: Route optimization service
- **MongoDB**: Database lưu trữ nodes, metrics, timelines
- **15 Agents**: Nodes phân tán theo địa lý thực tế

## 📁 Cấu Trúc

```
environment-configuration/
├── topology.docker-compose.yml   # Docker Compose orchestration
├── topology.json                 # Network topology definition
├── custom_hosts                  # DNS mapping cho agents
├── random_connected.py           # Script tạo topology ngẫu nhiên
└── .dockerignore                # Docker ignore rules
```

### Topology Definition

- **Nodes**: 15 nodes với tọa độ GPS thực tế
- **Types**: space, air, ground, mobile, sea
- **Links**: 20-23 connections đảm bảo connectivity

## 🚀 Hướng Dẫn Chạy

### Yêu Cầu

- Docker Engine 20.10+
- Docker Compose v2+
- 8GB RAM khả dụng

### Khởi Động

```bash
# Pull images từ Docker Hub
docker-compose -f topology.docker-compose.yml pull

# Start toàn bộ hệ thống
docker-compose -f topology.docker-compose.yml up -d

# Kiểm tra trạng thái
docker-compose -f topology.docker-compose.yml ps

# Xem logs
docker-compose -f topology.docker-compose.yml logs -f
```

### Truy Cập Services

- **Backend API**: http://localhost:3000
- **MongoDB**: mongodb://localhost:27017
- **Frontend**: http://localhost:5173 (chạy riêng)

### Tắt Hệ Thống

```bash
# Dừng containers
docker-compose -f topology.docker-compose.yml down

# Xóa volumes (reset database)
docker-compose -f topology.docker-compose.yml down -v
```

## 🎯 Kết Quả

### ✅ Đạt Được

1. **Multi-tier Network**: 15 nodes phân tầng space/air/ground/mobile/sea
2. **Auto-discovery**: Agents tự động connect và register với backend
3. **Metric Monitoring**: Real-time CPU, RAM, network, disk metrics
4. **File Transfer**: Hop-by-hop transfer với MD5 verification
5. **Timeline Tracking**: Millisecond-precision transfer timeline
6. **Heuristic Routing**: Tối ưu route dựa trên metrics và topology
7. **Health Checks**: Auto-restart và dependency management

### 📊 Metrics

- **Startup Time**: ~30-45 giây cho toàn bộ stack
- **Network Latency**: <10ms giữa các containers
- **Resource Usage**: ~6GB RAM, ~4GB disk
- **Agents Connected**: 15/15 nodes

### 🔍 Monitoring

- **Node Status**: Dashboard hiển thị realtime 15 nodes
- **Metrics Graphs**: CPU, RAM, bandwidth visualization
- **Timeline View**: File transfer tracking với tooltips
- **Network Topology**: Force-directed graph visualization

## 🛠️ Tùy Chỉnh

### Thay Đổi Topology

```bash
# Chỉnh sửa hostnames trong random_connected.py
python random_connected.py

# Hoặc edit trực tiếp topology.json
# Sau đó restart containers
```

### Thêm/Xóa Nodes

1. Thêm service mới vào `topology.docker-compose.yml`
2. Cập nhật `custom_hosts` với IP mapping
3. Cập nhật `topology.json` với node/link mới
4. Restart: `docker-compose up -d`

### Environment Variables

```yaml
# Backend
- NODE_ENV=production
- DATABASE_URL=mongodb://mongodb:27017/sagsin-db
- GRPC_URL=0.0.0.0:50051
- TIMELINE_GRPC_PORT=0.0.0.0:50053

# Agents
- HOST_NAME=<node_name>
- LAT=<latitude>
- LNG=<longitude>
```

## 📝 Notes

- Agents sử dụng `/etc/hosts` mapping cho communication
- Backend health check đảm bảo agents chỉ start khi backend ready
- Topology file được mount read-only vào agents
- Network sử dụng custom subnet `192.168.100.0/24`

---

**Docker Images**: `baocules/sagsin-be`, `baocules/sagsin-agent`, `baocules/sagsin-heuristic`
