import json
import random
from collections import defaultdict

def gen_topology(hostnames, target_links=(20, 23)):
    nodes = [{"id": h, "type": guess_type(h)} for h in hostnames]
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
    hostnames = [
        "satellite_nairobi", "satellite_sao_paulo",
        "drone_beijing", "drone_mumbai", "drone_london",
        "ground_station_hanoi", "ground_station_paris", "ground_station_moscow",
        "mobile_device_tokyo", "mobile_device_riyadh", "mobile_device_newyork", "mobile_device_singapore",
        "ship_singapore", "ship_tokyo", "ship_london"
    ]

    topo = gen_topology(hostnames, target_links=(20, 23))
    with open("topology.json", "w") as f:
        json.dump(topo, f, indent=2)
    print("✅ Generated topology.json with", len(topo["links"]), "links")
