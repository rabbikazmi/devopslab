import time
import json
import logging

# Setup logging
logging.basicConfig(
    filename="provision.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Sample configuration (like cloud config)
config = {
    "vm": {"name": "web-server", "cpu": 2, "ram": "4GB"},
    "storage": {"size": "50GB", "type": "SSD"},
    "network": {"vpc": "vpc-01", "subnet": "subnet-01"}
}

def create_vm(vm_config):
    print(f"Creating VM: {vm_config['name']}")
    time.sleep(1)
    logging.info(f"VM created: {vm_config}")
    return {"status": "running", "ip": "192.168.1.10"}

def setup_storage(storage_config):
    print(f"Allocating Storage: {storage_config['size']}")
    time.sleep(1)
    logging.info(f"Storage allocated: {storage_config}")
    return {"status": "attached"}

def setup_network(network_config):
    print(f"Configuring Network: {network_config['vpc']}")
    time.sleep(1)
    logging.info(f"Network configured: {network_config}")
    return {"status": "connected"}

def save_state(state):
    with open("infra_state.json", "w") as f:
        json.dump(state, f, indent=4)
    print("Infrastructure state saved!")

def provision():
    print("Starting Cloud Provisioning...\n")
    logging.info("Provisioning started")

    state = {}

    try:
        state["vm"] = create_vm(config["vm"])
        state["storage"] = setup_storage(config["storage"])
        state["network"] = setup_network(config["network"])

        state["status"] = "SUCCESS"
        print("\nProvisioning Completed Successfully!")

    except Exception as e:
        logging.error(f"Provisioning failed: {e}")
        state["status"] = "FAILED"
        print("\nProvisioning Failed!")

    save_state(state)
    logging.info("Provisioning finished")

# Run
if __name__ == "__main__":
    provision()