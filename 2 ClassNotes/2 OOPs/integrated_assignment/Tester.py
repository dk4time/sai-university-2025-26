# ---------------------------------------------------------------
# Employee Asset Management System — Python Practice Template
# ---------------------------------------------------------------
# Instructions:
# 1. Implement all the methods marked with "# Implement your code here".
# 2. Follow the class design, validations, and exception rules.
# 3. DO NOT modify the test code at the bottom (Tester section).
# 4. Use exception handling properly.
# ---------------------------------------------------------------

# -------------------------
# Custom Exceptions
# -------------------------

class InvalidAssetsException(Exception):
    # Implement your code here
    pass


class InvalidExperienceException(Exception):
    # Implement your code here
    pass


# -------------------------
# Asset Class
# -------------------------

class Asset:
    # Implement your code here

    # Do not modify the code below after implementing
    def __str__(self):
        return f"Asset Id: {self.get_asset_id()}, Asset Name: {self.get_asset_name()}, Asset Expiry: {self.get_asset_expiry()}"


# -------------------------
# Resources Class
# -------------------------

class Resources:
    # Implement your code here
    pass


# -------------------------
# Employee Base Class
# -------------------------

class Employee:
    # Implement your code here

    # Do not modify the code below after implementing
    def __str__(self):
        return f"Employee Id: {self.get_employee_id()}, Employee Name: {self.get_employee_name()}"


# -------------------------
# ContractEmployee Class
# -------------------------

class ContractEmployee(Employee):
    # Implement your code here

    # Do not modify the code below after implementing
    def __str__(self):
        return f"Employee Id: {self.get_employee_id()}, Employee Name: {self.get_employee_name()}, Wage Per Hour: {self.get_wage_per_hour()}"


# -------------------------
# PermanentEmployee Class
# -------------------------

class PermanentEmployee(Employee):
    # Implement your code here

    # Do not modify the code below after implementing
    def __str__(self):
        return f"Employee Id: {self.get_employee_id()}, Employee Name: {self.get_employee_name()}, Basic Pay: {self.get_basic_pay()}, Salary Components: {self.get_salary_components()}, Assets: {self.get_assets()}"


# -------------------------
# Admin Class
# -------------------------

class Admin:
    # Implement your code here
    pass


# -------------------------
# Tester / Main Class
# -------------------------

if __name__ == "__main__":
    admin = Admin()

    asset1 = asset2 = asset3 = asset4 = asset5 = asset6 = asset7 = asset8 = asset9 = asset10 = None

    permanent_employee1 = permanent_employee2 = permanent_employee3 = permanent_employee4 = permanent_employee5 = None
    contract_employee1 = contract_employee2 = None
    employees = None
    salary_factor = None

    # ------------------------
    # Asset Creation
    # ------------------------
    try:
        asset1 = Asset("DSK-876761L", "Dell-Desktop", "2020-Dec-01")
        asset2 = Asset("DSK-876762L", "Acer-Desktop", "2021-Mar-31")
        asset3 = Asset("DSK-876763L", "Dell-Desktop", "2022-Jun-12")
        asset4 = Asset("LTP-987123H", "Dell-Laptop", "2021-Dec-31")
        asset5 = Asset("LTP-987124h", "Dell-Laptop", "2021-Sep-20")
        asset6 = Asset("LTP-987125L", "HP-Laptop", "2022-Oct-25")
        asset7 = Asset("LTP-987126l", "HP-Laptop", "2021-Oct-02")
        asset8 = Asset("IPH-110110h", "VoIP", "2021-Dec-12")
        asset9 = Asset("IPH-1101201h", "VoIP", "2020-Dec-31")
        asset10 = Asset("IPH-110130h", "VoIP", "2020-Nov-30")
    except Exception as e:
        print(e)

    print("Details of all available assets\n")
    try:
        assets = [asset1, asset2, asset3, asset4, asset5, asset6, asset7, asset8, asset9, asset10]
        counter = 1
        for asset in assets:
            print(f"Details of asset{counter}")
            print(f"\tAsset Id: {asset.get_asset_id()}")
            print(f"\tAsset Name: {asset.get_asset_name()}")
            print(f"\tAsset Valid Till: {asset.get_asset_expiry()}\n")
            counter += 1
    except Exception as e:
        print(e)

    print("Correcting all the invalid assetIds\n")
    try:
        asset9.set_asset_id("IPH-110120h")
        print("Details of asset9")
        print(f"\tAsset Id: {asset9.get_asset_id()}")
        print(f"\tAsset Name: {asset9.get_asset_name()}")
        print(f"\tAsset Valid Till: {asset9.get_asset_expiry()}\n")
    except Exception as e:
        print(e)

    # ------------------------
    # Employee Creation
    # ------------------------
    try:
        permanent_employee1 = PermanentEmployee("Roger Fed", 15500.0, ["DA-50", "HRA-40"], [asset1, asset10])
        permanent_employee2 = PermanentEmployee("Serena W", 14000.0, ["DA-40", "HRA-40"], [asset6, asset9])
        permanent_employee3 = PermanentEmployee("James Peter", 18500.0, ["DA-50", "HRA-45"], [asset4])
        permanent_employee4 = PermanentEmployee("Catherine Maria", 20000.0, ["DA-50", "HRA-45"], [asset2, asset5])
        permanent_employee5 = PermanentEmployee("Jobin Nick", 21000.0, ["DA-50", "HRA-50"], None)

        contract_employee1 = ContractEmployee("Rafael N", 70)
        contract_employee2 = ContractEmployee("Ricky Neol", 72.5)
    except Exception as e:
        print(e)

    print("\nInitiating salary calculation...\n")
    try:
        employees = [
            permanent_employee1, permanent_employee2, permanent_employee3,
            permanent_employee4, permanent_employee5, contract_employee1, contract_employee2
        ]
        salary_factor = [3.9, 2.3, 4.0, 8.1, 12.5, 189, 211]
        admin.generate_salary_slip(employees, salary_factor)
    except Exception as e:
        print(e)

    permanent_employee5.set_salary(-1)

    print("\nDetails of employees\n")
    try:
        p_counter = c_counter = 1
        for emp in employees:
            if isinstance(emp, PermanentEmployee):
                print(f"Details of permanentEmployee{p_counter}")
                print(f"\tEmployee Id: {emp.get_employee_id()}")
                print(f"\tEmployee Name: {emp.get_employee_name()}")
                print(f"\tSalary: {emp.get_salary()}")
                print(f"\tExperience: {emp.get_experience()}")
                print(f"\tAssets Allocated: ", end="")
                if emp.get_assets() is not None:
                    for asset in emp.get_assets():
                        print(asset.get_asset_id(), end=" ")
                    print()
                else:
                    print("No assets allocated!")
                print()
                p_counter += 1
            else:
                print(f"Details of contractEmployee{c_counter}")
                print(f"\tEmployee Id: {emp.get_employee_id()}")
                print(f"\tEmployee Name: {emp.get_employee_name()}")
                print(f"\tSalary: {emp.get_salary()}\n")
                c_counter += 1
    except Exception as e:
        print(e)

    print("\nReports\n")
    try:
        employees = [
            permanent_employee1, permanent_employee2, permanent_employee3,
            permanent_employee4, contract_employee1, contract_employee2
        ]

        asset_count = admin.generate_assets_report(employees, "2021-Dec-31")
        if asset_count >= 0:
            print(f"Number of allocated assets expiring on or before 2021-Dec-31: {asset_count}")
        else:
            print("Sorry, report cannot be generated!")

        print()

        asset_count = admin.generate_assets_report(employees, "2020-Sep-30")
        if asset_count >= 0:
            print(f"Number of allocated assets expiring on or before 2020-Sep-30: {asset_count}")
        else:
            print("Sorry, report cannot be generated!")

        print()

        desktop_asset_ids = admin.generate_assets_report(employees, 'D')
        print("All the allocated desktop assets")
        for aid in desktop_asset_ids:
            if aid:
                print(f"\t{aid}")
        print()

        laptop_asset_ids = admin.generate_assets_report(employees, 'L')
        print("All the allocated laptop assets")
        for aid in laptop_asset_ids:
            if aid:
                print(f"\t{aid}")
        print()

        voip_asset_ids = admin.generate_assets_report(employees, 'i')
        print("All the allocated VoIP assets")
        for aid in voip_asset_ids:
            if aid:
                print(f"\t{aid}")
        print()

    except Exception as e:
        print(e)
