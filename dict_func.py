
def employee_print(employee_info):
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")
    
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")
    
    info_extra= employee_info.copy()
    info_extra.pop("Name", None)
    info_extra.pop("Salary", None)
    info_extra.pop("Role", None)

    if len(info_extra)==0:
        print("No other info!")
    else:
        for key, value in info_extra.items():
            print(f"{key}: {value}")

