from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from datetime import datetime

credential = AzureCliCredential()
subscription_id = "ff190e2b-0ba4-4932-8614-38db2dff7d89"

compute_client = ComputeManagementClient(credential, subscription_id)

def check_vm_health():
    print(f"\n{'='*40}")
    print(f"Cloudlet Health Check")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*40}")

    vms = list(compute_client.virtual_machines.list_all())

    if len(vms) == 0:
        print("⚠️  No VMs found")
        return

    for vm in vms:
        vm_status = compute_client.virtual_machines.get(
            vm.id.split('/')[4],
            vm.name,
            expand='instanceView'
        )

        power_state = "Unknown"
        for status in vm_status.instance_view.statuses:
            if status.code.startswith('PowerState'):
                power_state = status.display_status

        icon = "✅" if power_state == "VM running" else "❌"
        print(f"{icon} {vm.name} | {vm.location} | {power_state}")

check_vm_health()