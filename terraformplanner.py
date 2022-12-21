import json
import sys

def print_resource(resource, indent=0):
    # Extract the resource type, name, and action
    resource_type = resource["type"]
    resource_name = resource["name"]
    action = resource["change"]["actions"][0]

    # Print the resource type, name, and action
    print(" " * indent + f"{resource_type} {resource_name}: {action}")

    # Print the resource attributes
    for attribute in resource["change"]["before"]:
        before = resource["change"]["before"][attribute]
        after = resource["change"]["after"][attribute]
        if before != after:
            print(" " * (indent + 2) + f"{attribute}: {before} => {after}")

    # Recursively print any nested resources
    for nested_resource in resource["change"]["before_nested"]:
        print_resource(nested_resource, indent + 2)

# Open the Terraform plan file
with open(sys.argv[1], "r") as plan_file:
    # Load the plan file as a JSON object
    plan = json.load(plan_file)

# Print a header
print("Terraform Plan Summary:")

# Iterate over the resources in the plan
for resource in plan["resource_changes"]:
   

