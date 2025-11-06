import re
from math import ceil

# ---------------------------------------------------------------
# Custom Exceptions
# ---------------------------------------------------------------

class InvalidAssetsException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidExperienceException(Exception):
    def __init__(self, message):
        super().__init__(message)


# ---------------------------------------------------------------
# Asset Class
# ---------------------------------------------------------------

class Asset:
    def __init__(self, asset_id, asset_name, asset_expiry):
        self.asset_id = None
        self.asset_name = asset_name
        self.asset_expiry = asset_expiry
        self.set_asset_id(asset_id)

    def set_asset_id(self, asset_id):
        pattern = r"^(DSK|LTP|IPH)-\d{6}[HLhl]$"
        if re.match(pattern, asset_id):
            self.asset_id = asset_id
        else:
            raise InvalidAssetsException(f"Invalid Asset Id: {asset_id}")

    def get_asset_id(self):
        return self.asset_id

    def get_asset_name(self):
        return self.asset_name

    def get_asset_expiry(self):
        return self.asset_expiry

    def __str__(self):
        return f"Asset Id: {self.get_asset_id()}, Asset Name: {self.get_asset_name()}, Asset Expiry: {self.get_asset_expiry()}"


# ---------------------------------------------------------------
# Resources Class
# ---------------------------------------------------------------

class Resources:
    MONTHS = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    @staticmethod
    def get_month(month):
        if month in Resources.MONTHS:
            return Resources.MONTHS[month]
        return 0


# ---------------------------------------------------------------
# Employee Base Class
# ---------------------------------------------------------------

class Employee:
    contract_id_counter = 10000
    permanent_id_counter = 10000

    def __init__(self, employee_name):
        self.employee_id = None
        self.employee_name = None
        self.salary = 0.0
        self.set_employee_name(employee_name)

    def set_employee_name(self, name):
        pattern = r"^[A-Z][a-zA-Z]+( [A-Z][a-zA-Z]*)+$"

        if re.match(pattern, name):
            self.employee_name = name
        else:
            raise ValueError(f"Invalid Employee Name: {name}")

    def get_employee_name(self):
        return self.employee_name

    def set_salary(self, salary):
        self.salary = salary if salary > 0 else 0

    def get_salary(self):
        return self.salary

    def get_employee_id(self):
        return self.employee_id

    def __str__(self):
        return f"Employee Id: {self.get_employee_id()}, Employee Name: {self.get_employee_name()}"


# ---------------------------------------------------------------
# ContractEmployee Class
# ---------------------------------------------------------------

class ContractEmployee(Employee):
    def __init__(self, employee_name, wage_per_hour):
        super().__init__(employee_name)
        Employee.contract_id_counter += 1
        self.employee_id = f"C{Employee.contract_id_counter}"
        self.wage_per_hour = wage_per_hour

    def calculate_salary(self, hours_worked):
        if hours_worked < 190:
            deduction = 0.5 * self.wage_per_hour * (190 - hours_worked)
            salary = self.wage_per_hour * hours_worked - deduction
        else:
            salary = self.wage_per_hour * hours_worked
        self.salary = round(salary)

    def get_wage_per_hour(self):
        return self.wage_per_hour

    def __str__(self):
        return f"Employee Id: {self.get_employee_id()}, Employee Name: {self.get_employee_name()}, Wage Per Hour: {self.get_wage_per_hour()}"


# ---------------------------------------------------------------
# PermanentEmployee Class
# ---------------------------------------------------------------

class PermanentEmployee(Employee):
    def __init__(self, employee_name, basic_pay, salary_components, assets):
        super().__init__(employee_name)
        Employee.permanent_id_counter += 1
        self.employee_id = f"E{Employee.permanent_id_counter}"
        self.basic_pay = basic_pay
        self.salary_components = salary_components
        self.assets = assets
        self.experience = 0.0

    def get_basic_pay(self):
        return self.basic_pay

    def get_salary_components(self):
        return self.salary_components

    def get_assets(self):
        return self.assets

    def get_experience(self):
        return self.experience

    def calculate_bonus(self, experience):
        if experience < 2.5:
            raise InvalidExperienceException("A minimum of 2.5 years is required for bonus!")
        elif 2.5 <= experience < 5:
            return 0.10 * self.basic_pay
        elif 5 <= experience < 10:
            return 0.20 * self.basic_pay
        else:
            return 0.35 * self.basic_pay

    def calculate_salary(self, experience):
        self.experience = experience
        da, hra = 0, 0
        for comp in self.salary_components or []:
            name, val = comp.split("-")
            if name == "DA":
                da = (float(val) / 100) * self.basic_pay
            elif name == "HRA":
                hra = (float(val) / 100) * self.basic_pay
        try:
            bonus = self.calculate_bonus(experience)
        except InvalidExperienceException as e:
            print(e)
            bonus = 0
        self.salary = round(self.basic_pay + da + hra + bonus)

    def get_assets_by_date(self, last_date):
        if not self.assets:
            raise InvalidAssetsException("No assets found for the given criteria!")

        y, m, d = last_date.split("-")
        month_num = Resources.get_month(m)
        if month_num == 0:
            raise InvalidAssetsException("Invalid month in date!")

        cutoff = int(f"{y}{month_num:02d}{d}")
        valid_assets = []
        for a in self.assets:
            ay, am, ad = a.get_asset_expiry().split("-")
            am_num = Resources.get_month(am)
            if am_num == 0:
                continue
            a_val = int(f"{ay}{am_num:02d}{ad}")
            if a_val <= cutoff:
                valid_assets.append(a)
        if not valid_assets:
            raise InvalidAssetsException("No assets found for the given criteria!")
        return valid_assets

    def __str__(self):
        return f"Employee Id: {self.get_employee_id()}, Employee Name: {self.get_employee_name()}, Basic Pay: {self.get_basic_pay()}, Salary Components: {self.get_salary_components()}, Assets: {self.get_assets()}"


# ---------------------------------------------------------------
# Admin Class
# ---------------------------------------------------------------

class Admin:
    def generate_salary_slip(self, employees, salary_factor):
        for emp, factor in zip(employees, salary_factor):
            if isinstance(emp, PermanentEmployee):
                emp.calculate_salary(factor)
            elif isinstance(emp, ContractEmployee):
                emp.calculate_salary(factor)

    def generate_assets_report(self, employees, last_date):
        count = 0
        for emp in employees:
            if isinstance(emp, PermanentEmployee):
                try:
                    assets = emp.get_assets_by_date(last_date)
                    count += len(assets)
                except InvalidAssetsException:
                    return -1
        return count

    def generate_assets_report(self, employees, asset_category):
        result = [None] * (len(employees) * 3)
        idx = 0
        for emp in employees:
            if isinstance(emp, PermanentEmployee) and emp.get_assets():
                for a in emp.get_assets():
                    if a.get_asset_id()[0].lower() == asset_category.lower():
                        result[idx] = a.get_asset_id()
                        idx += 1
        return result


# ---------------------------------------------------------------
# Tester / Main Class
# ---------------------------------------------------------------

if __name__ == "__main__":
    admin = Admin()

    # Assets
    try:
        asset1 = Asset("DSK-876761L", "Dell-Desktop", "2020-Dec-01")
        asset2 = Asset("DSK-876762L", "Acer-Desktop", "2021-Mar-31")
        asset3 = Asset("DSK-876763L", "Dell-Desktop", "2022-Jun-12")
        asset4 = Asset("LTP-987123H", "Dell-Laptop", "2021-Dec-31")
        asset5 = Asset("LTP-987124h", "Dell-Laptop", "2021-Sep-20")
        asset6 = Asset("LTP-987125L", "HP-Laptop", "2022-Oct-25")
        asset7 = Asset("LTP-987126l", "HP-Laptop", "2021-Oct-02")
        asset8 = Asset("IPH-110110h", "VoIP", "2021-Dec-12")
        asset9 = Asset("IPH-110120h", "VoIP", "2020-Dec-31")
        asset10 = Asset("IPH-110130h", "VoIP", "2020-Nov-30")
    except Exception as e:
        print(e)

    assets = [asset1, asset2, asset3, asset4, asset5, asset6, asset7, asset8, asset9, asset10]
    print("\nDetails of all available assets\n")
    for i, asset in enumerate(assets, 1):
        print(f"Details of asset{i}")
        print(f"\tAsset Id: {asset.get_asset_id()}")
        print(f"\tAsset Name: {asset.get_asset_name()}")
        print(f"\tAsset Valid Till: {asset.get_asset_expiry()}\n")

    # Employees
    permanent_employee1 = PermanentEmployee("Roger Fed", 15500.0, ["DA-50", "HRA-40"], [asset1, asset10])
    permanent_employee2 = PermanentEmployee("Serena W", 14000.0, ["DA-40", "HRA-40"], [asset6, asset9])
    permanent_employee3 = PermanentEmployee("James Peter", 18500.0, ["DA-50", "HRA-45"], [asset4])
    permanent_employee4 = PermanentEmployee("Catherine Maria", 20000.0, ["DA-50", "HRA-45"], [asset2, asset5])
    permanent_employee5 = PermanentEmployee("Jobin Nick", 21000.0, ["DA-50", "HRA-50"], None)

    contract_employee1 = ContractEmployee("Rafael N", 70)
    contract_employee2 = ContractEmployee("Ricky Neol", 72.5)

    employees = [
        permanent_employee1, permanent_employee2, permanent_employee3,
        permanent_employee4, permanent_employee5, contract_employee1, contract_employee2
    ]
    salary_factor = [3.9, 2.3, 4.0, 8.1, 12.5, 189, 211]

    print("\nInitiating salary calculation...\n")
    admin.generate_salary_slip(employees, salary_factor)
    permanent_employee5.set_salary(-1)

    print("\nDetails of employees\n")
    for e in employees:
        print(e)
        print(f"\tSalary: {e.get_salary()}")
        if isinstance(e, PermanentEmployee):
            print(f"\tExperience: {e.get_experience()}")
        print()

    print("\nReports\n")
    report = admin.generate_assets_report(employees, 'D')
    print("Desktop Assets:")
    for r in report:
        if r:
            print("\t", r)
