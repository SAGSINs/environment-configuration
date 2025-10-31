import json
import random
from collections import defaultdict

def gen_topology(nodes_info, target_links=(20, 23)):
    nodes = [
        {
            "id": info["hostname"],
            "type": info["type"],
            "lat": info["lat"],
            "lng": info["lng"],
            "weather": info["weather"]
        }
        for info in nodes_info
    ]
    hostnames = [info["hostname"] for info in nodes_info]
    n = len(nodes)

    # Đảm bảo mỗi node có ít nhất 1 link
    links = []
    for i in range(n - 1):
        links.append({"source": hostnames[i], "target": hostnames[i+1]})

    # Kiểm tra degree
    degree = defaultdict(int)
    for l in links:
        degree[l["source"]] += 1
        degree[l["target"]] += 1

    # Nếu node nào degree == 1 thì nối thêm link
    for node in hostnames:
        if degree[node] == 1:
            other = random.choice([h for h in hostnames if h != node])
            if not link_exists(links, node, other):
                links.append({"source": node, "target": other})
                degree[node] += 1
                degree[other] += 1

    # Bổ sung random link đến khi đủ target
    min_links, max_links = target_links
    while len(links) < random.randint(min_links, max_links):
        a, b = random.sample(hostnames, 2)
        if not link_exists(links, a, b):
            links.append({"source": a, "target": b})
            degree[a] += 1
            degree[b] += 1

    return {"nodes": nodes, "links": links}


def link_exists(links, a, b):
    return any((l["source"] == a and l["target"] == b) or 
               (l["source"] == b and l["target"] == a) for l in links)

def guess_type(name):
    if "satellite" in name: return "space"
    if "drone" in name: return "air"
    if "ground" in name: return "ground"
    if "mobile" in name: return "mobile"
    if "ship" in name: return "sea"
    return "unknown"


if __name__ == "__main__":
    nodes_info = [
        # Original 15 nodes
        {"hostname": "satellite_nairobi", "type": "space", "lat": -1.2921, "lng": 36.8219, "weather": "clear"},
        {"hostname": "satellite_sao_paulo", "type": "space", "lat": -23.5505, "lng": -46.6333, "weather": "rainy"},
        {"hostname": "drone_beijing", "type": "air", "lat": 39.9042, "lng": 116.4074, "weather": "cloudy"},
        {"hostname": "drone_mumbai", "type": "air", "lat": 19.0760, "lng": 72.8777, "weather": "rainy"},
        {"hostname": "drone_london", "type": "air", "lat": 51.5074, "lng": -0.1278, "weather": "rainy"},
        {"hostname": "ground_station_hanoi", "type": "ground", "lat": 21.0285, "lng": 105.8542, "weather": "cloudy"},
        {"hostname": "ground_station_paris", "type": "ground", "lat": 48.8566, "lng": 2.3522, "weather": "cloudy"},
        {"hostname": "ground_station_moscow", "type": "ground", "lat": 55.7558, "lng": 37.6173, "weather": "cloudy"},
        {"hostname": "mobile_device_tokyo", "type": "mobile", "lat": 35.6764, "lng": 139.6500, "weather": "clear"},
        {"hostname": "mobile_device_riyadh", "type": "mobile", "lat": 24.7136, "lng": 46.6753, "weather": "clear"},
        {"hostname": "mobile_device_newyork", "type": "mobile", "lat": 40.7128, "lng": -74.0060, "weather": "cloudy"},
        {"hostname": "mobile_device_singapore", "type": "mobile", "lat": 1.3521, "lng": 103.8198, "weather": "rainy"},
        {"hostname": "ship_singapore", "type": "sea", "lat": 1.5321, "lng": 104.2, "weather": "stormy"},
        {"hostname": "ship_tokyo", "type": "sea", "lat": 35.0, "lng": 141.0, "weather": "rainy"},
        {"hostname": "ship_london", "type": "sea", "lat": 51.0, "lng": 1.5, "weather": "stormy"},
        
        # New 10 nodes - geographically distributed
        {"hostname": "satellite_sydney", "type": "space", "lat": -33.8688, "lng": 151.2093, "weather": "clear"},      # Australia
        {"hostname": "drone_capetown", "type": "air", "lat": -33.9249, "lng": 18.4241, "weather": "cloudy"},         # South Africa
        {"hostname": "drone_toronto", "type": "air", "lat": 43.6532, "lng": -79.3832, "weather": "cloudy"},          # Canada
        {"hostname": "ground_station_cairo", "type": "ground", "lat": 30.0444, "lng": 31.2357, "weather": "clear"},  # Egypt
        {"hostname": "ground_station_jakarta", "type": "ground", "lat": -6.2088, "lng": 106.8456, "weather": "rainy"}, # Indonesia
        {"hostname": "mobile_device_dubai", "type": "mobile", "lat": 25.2048, "lng": 55.2708, "weather": "clear"},   # UAE
        {"hostname": "mobile_device_berlin", "type": "mobile", "lat": 52.5200, "lng": 13.4050, "weather": "cloudy"}, # Germany
        {"hostname": "mobile_device_seoul", "type": "mobile", "lat": 37.5665, "lng": 126.9780, "weather": "cloudy"}, # South Korea
        {"hostname": "ship_miami", "type": "sea", "lat": 25.7617, "lng": -80.1918, "weather": "rainy"},              # Atlantic Ocean
        {"hostname": "ship_vancouver", "type": "sea", "lat": 49.2827, "lng": -123.1207, "weather": "cloudy"}         # Pacific Ocean
    ]

    topo = gen_topology(nodes_info, target_links=(30, 35))
    with open("topology.json", "w") as f:
        json.dump(topo, f, indent=2)
    print("✅ Generated topology.json with", len(topo["links"]), "links")
