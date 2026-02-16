def check_vm_health(vm_name, cpu_usage):
    print(f"\n 🔍 Checking {vm_name}...")

    if cpu_usage < 70:
        status = "✅ Healthy"

    else:
        status = "⚠️ High CPU Usage"

    print(f"    CPU: {cpu_usage}%")
    print(f"    Status: {status}")
    return status

# Test it VMs
vms = [
    {"name": "web-server", "cpu": 120},
    {"name": "database", "cpu": 100},
    {"name": "app-server", "cpu": 0}

]

print("=== Azure VM Helath Check ===")
for vm in vms:
    check_vm_health(vm["name"], vm["cpu"])
