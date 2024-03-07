import pandas as pd

# Read data from Excel file
excel_file = r'C:\‪\Users\Admin\Desktop\one1.xlsx'
df = pd.read_excel(excel_file)

# Define Terraform file name
terraform_file = r'C:\\Users\Admin\Desktop\one1.tf'

# Open Terraform file for writing
with open(terraform_file, 'w') as f:
    # Write Terraform header
    f.write('### Terraform Configuration Generated from Excel Data ###\n\n')
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract data from Excel columns
        name = row['Resource Name']
        resource_type = row['Resource Type']
        region = row['Region']
        instance_type = row['Instance Type']
        ami = row['AMI']
        subnet_id = row['Subnet ID']
        security_group_ids = row['Security Group IDs']

        # Write Terraform resource block
        f.write(f'resource "{resource_type}" "{name}" {{\n')
        f.write(f'    region      = "{region}"\n')
        f.write(f'    instance_type = "{instance_type}"\n')
        f.write(f'    ami          = "{ami}"\n')
        f.write(f'    subnet_id    = "{subnet_id}"\n')
        f.write(f'    security_group_ids = "{security_group_ids}"\n')
        f.write('}\n\n')

print(f'Terraform code has been written to {terraform_file}')
