from flask import Flask, Response
import pandas as pd
import os

app = Flask(__name__)

# Carregar dados do Excel
xlsx_path = "/app/AzureResourceInventory_Report_2025-04-29_22_56.xlsx"
vms = pd.read_excel(xlsx_path, sheet_name="Virtual Machines")
storages = pd.read_excel(xlsx_path, sheet_name="Storage Accounts")
vnets = pd.read_excel(xlsx_path, sheet_name="Virtual Networks")
nsgs = pd.read_excel(xlsx_path, sheet_name="Network Security Groups")
pip = pd.read_excel(xlsx_path, sheet_name="Public IPs")
peering = pd.read_excel(xlsx_path, sheet_name="Peering")
rt = pd.read_excel(xlsx_path, sheet_name="Route Tables")


@app.route("/metrics")
def metrics():
    result = []

    # Virtual Machines
    for _, row in vms.iterrows():
        name = row.get("VM Name", "unknown")
        rg = row.get("Resource group", "unknown")
        status = row.get("PowerState", "unknown")
        result.append(f'azure_vm_info{{name="{name}",resource_group="{rg}",status="{status}"}} 1')

    # Storage Accounts
    for _, row in storages.iterrows():
        name = row.get("Name", "unknown")
        rg = row.get("Resource group", "unknown")
        sku = row.get("SKU", "unknown")
        result.append(f'azure_storage_account_info{{name="{name}",resource_group="{rg}",sku="{sku}"}} 1')

    # vNETs
    for _, row in vnets.iterrows():
        name = row.get("Name", "unknown")
        rg = row.get("Resource group", "unknown")
        address_space = row.get("Address space", "unknown")
        result.append(f'azure_vnet_info{{name="{name}",resource_group="{rg}",address_space="{address_space}"}} 1')

    # NSGs
    for _, row in nsgs.iterrows():
        name = row.get("Name", "unknown")
        rg = row.get("Resource group", "unknown")
        location = row.get("Location", "unknown")
        result.append(f'azure_nsg_info{{name="{name}",resource_group="{rg}",location="{location}"}} 1')

    # PIP
    for _, row in pip.iterrows():
        name = row.get("Name", "unknown")
        rg = row.get("Resource group", "unknown")
        location = row.get("Location", "unknown")
        result.append(f'azure_pip_info{{name="{name}",resource_group="{rg}",location="{location}"}} 1') 

    # Peering
    for _, row in peering.iterrows():
        name = row.get("Peering Name", "unknown")
        rg = row.get("Resource group", "unknown")
        location = row.get("Location", "unknown")
        result.append(f'azure_peering_info{{name="{name}",resource_group="{rg}",location="{location}"}} 1')

    # Route Table
    for _, row in rt.iterrows():
        name = row.get("Name", "unknown")
        rg = row.get("Resource group", "unknown")
        location = row.get("Location", "unknown")
        result.append(f'azure_rt_info{{name="{name}",resource_group="{rg}",location="{location}"}} 1')         

    return Response("\n".join(result), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
