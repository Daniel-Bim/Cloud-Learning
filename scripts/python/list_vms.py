from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient

# Connect to Azure using your CLI login
credential = AzureCliCredential()
subscription_id = "ff190e2b-0ba4-4932-8614-38db2dff7d89"

# Create client
compute_client = ComputeManagementClient(credential, subscription_id)

# List all VMs
print("=== My Azure VMs ===")
vms = list(compute_client.virtual_machines.list_all())

if len(vms) == 0:
    print("No VMs found")
else:
    for vm in vms:
        print(f"VM: {vm.name} | Location: {vm.location}")