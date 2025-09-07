# Config Environment - Topology Simulation

## Project Description

This project is a network topology simulation using Docker Compose to create a network of nodes representing different environments: space, air, ground, and sea. Each node is deployed as a Docker container with a static IP address in the `topo_net` network.

## Network Structure

- **Space nodes**: satellite_tokyo, satellite_newyork (192.168.100.11, 192.168.100.12)
- **Air nodes**: drone_beijing, drone_mumbai, drone_london (192.168.100.21, 192.168.100.22, 192.168.100.23)
- **Ground nodes**: ground_station_hanoi, ground_station_paris, ground_station_moscow, mobile_device_tokyo, mobile_device_london, mobile_device_newyork, mobile_device_singapore (192.168.100.31 to 192.168.100.37)
- **Sea nodes**: ship_singapore, ship_tokyo, ship_london (192.168.100.41, 192.168.100.42, 192.168.100.43)

## Network Scenario

This topology simulates a distributed network spanning the Northern Hemisphere, from East Asia across Europe to North America, representing a realistic regional communication system with global connectivity potential.

### Device Locations and Roles

- **Satellites**: Provide regional and intercontinental coverage
  - `satellite_tokyo`: Orbiting over East Asia
  - `satellite_newyork`: Orbiting over North America

- **Drones**: Aerial platforms for surveillance and data collection
  - `drone_beijing`: Operating in East Asia
  - `drone_mumbai`: Operating in South Asia
  - `drone_london`: Operating in Western Europe

- **Ground Stations**: Fixed communication hubs
  - `ground_station_hanoi`: Vietnam (Southeast Asia)
  - `ground_station_paris`: France (Western Europe)
  - `ground_station_moscow`: Russia (Eastern Europe)

- **Mobile Devices**: Portable communication units
  - `mobile_device_tokyo`: Japan (East Asia)
  - `mobile_device_london`: UK (Western Europe)
  - `mobile_device_newyork`: USA (North America)
  - `mobile_device_singapore`: Singapore (Southeast Asia)

- **Ships**: Maritime communication vessels
  - `ship_singapore`: Operating in Southeast Asian waters
  - `ship_tokyo`: Operating in East Asian waters
  - `ship_london`: Operating in European waters

### Regional Coverage Map (Northern Hemisphere)

```
East Asia:     satellite_tokyo, drone_beijing, ground_station_hanoi, mobile_device_tokyo, ship_tokyo
South Asia:    drone_mumbai
Southeast Asia: mobile_device_singapore, ship_singapore
Western Europe: drone_london, ground_station_paris, mobile_device_london, ship_london
Eastern Europe: ground_station_moscow
North America: satellite_newyork, mobile_device_newyork
```

This setup enables testing of:
- Transcontinental communication links
- Satellite-ground station coordination
- Mobile device roaming across regions
- Maritime-air-ground integration
- Network resilience in regional scenarios

## System Requirements

- Docker
- Docker Compose

## Installation and Running

1. Clone the repository:
   ```bash
   git clone https://github.com/pbl4-sagsins-and-heuristic/config-environment.git
   cd config-environment
   ```

2. Build and run the containers:
   ```bash
   docker-compose -f topology.docker-compose.yml up --build
   ```

3. To run in background mode:
   ```bash
   docker-compose -f topology.docker-compose.yml up -d --build
   ```

## Usage

After the containers are started, you can:

- Connect to a specific container:
  ```bash
  docker exec -it <container_name> bash
  ```

- Inspect the network:
  ```bash
  docker network inspect configenvironment_topo_net
  ```

- Stop the containers:
  ```bash
  docker-compose -f topology.docker-compose.yml down
  ```

## Customization

- To add new nodes, edit the `topology.docker-compose.yml` file
- The `custom_hosts` file is mounted to `/etc/hosts` in each container for DNS customization

## Contributing

Please create an issue or pull request to contribute to the project.

## License

[Add license information if available]