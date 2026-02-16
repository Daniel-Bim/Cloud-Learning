# Define it
#-----------------------

def check_vm_status(vm_name):
    print(f"Checking {vm_name}...")
    return "Running"

# Test it
#------------------------
status = check_vm_status("Web-server")
print(f"status: {status}")

# Loop

vms = ["Web-server", "database", "app-server", "Sql-server", "Virtual Desktop"]
for vm in vms:
    status = check_vm_status(vm)
    print(f"{vm} is {status} \n")