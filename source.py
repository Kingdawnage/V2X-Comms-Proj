import traci

# Start the SUMO simulation with the desired scenario file
sumo_cmd = ['sumo', '-c', 'sim.sumocfg']
traci.start(sumo_cmd)

# Main simulation loop
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    if traci.simulation.getTime() % 5 == 0:
        # Retrieve information about vehicles
        vehicle_ids = traci.vehicle.getIDList()
        for vehicle_id in vehicle_ids:
            # Get vehicle position and speed
            position = traci.vehicle.getPosition(vehicle_id)
            speed = traci.vehicle.getSpeed(vehicle_id)
            # Print vehicle information
            print(f"Vehicle {vehicle_id}: Position {position}, Speed {speed}")

# End simulation and close TraCI connection
traci.close()