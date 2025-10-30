import re
from math import ceil

# -----------------------------------------------------
# Custom Exceptions
# -----------------------------------------------------
class InvalidAssetsException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidExperienceException(Exception):
    def __init__(self, message):
        super().__init__(message)


# -----------------------------------------------------
# Asset Class
# -----------------------------------------------------
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
        return f"Asset Id: {self.asset_id}, Name: {self.asset_name}, Expiry: {self.asset_expiry}"


# -----------------------------------------------------
# Resources Class
# -----------------------------------------------------
class Resources:
    MONTHS = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    @staticmethod
    def get_month(month):
        return Resources.MONTHS.get(month, 0)


# -----------------------------------------------------
# Employee Base Class
# -----------------------------------------------------
class Employee:
    contract_id_counter = 10000
    permanent_id_counter = 10000

    def __init__(self, employee_name):
        self.employee_id = None
        self.employee_name = None
        self.salary = 0.0
        self.set_employee_name(employee_name)

    def set_employee_name(self, name):
        pattern = r"^[A-Z][a-zA-Z]{1,}( [A-Z][a-zA-Z]{1,})+$"
        if re.match(pattern, name):
            self.employee_name = name
        else:
            raise ValueError(f"Invalid Employee Name: {name}")

    def get_employee_name(self):
        return self.employee_name

    def get_employee_id(self):
        return self.employee_id

    def set_salary(self, salary):
        self.salary = salary if salary > 0 else 0

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"Employee Id: {self.employee_id}, Employee Name: {self.employee_name}"


# -----------------------------------------------------
# ContractEmployee Class
# -----------------------------------------------------
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
        return f"Employee Id: {self.employee_id}, Employee Name: {self.employee_name}, Wage Per Hour: {self.wage_per_hour}"


# -----------------------------------------------------
# PermanentEmployee Class
# -----------------------------------------------------
class PermanentEmployee(Employee):
    def __init__(self, employee_name, basic_pay, salary_components, assets):
        super().__init__(employee_name)
        Employee.permanent_id_counter += 1
        self.employee_id = f"E{Employee.permanent_id_counter}"
        self.basic_pay = basic_pay
        self.salary_components = salary_components
        self.assets = assets
        self.experience = 0.0

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
            print(f"⚠️ {e}")
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
            if Resources.get_month(am) == 0:
                continue
            a_val = int(f"{ay}{Resources.get_month(am):02d}{ad}")
            if a_val <= cutoff:
                valid_assets.append(a)
        if not valid_assets:
            raise InvalidAssetsException("No assets found for the given criteria!")
        return valid_assets

    def __str__(self):
        asset_ids = [a.get_asset_id() for a in self.assets] if self.assets else []
        return f"Employee Id: {self.employee_id}, Employee Name: {self.employee_name}, Basic Pay: {self.basic_pay}, Assets: {asset_ids}"


# -----------------------------------------------------
# Admin Class
# -----------------------------------------------------
class Admin:
    def generate_salary_slip(self, employees, salary_factors):
        for emp, factor in zip(employees, salary_factors):
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

    def generate_assets_report_by_category(self, employees, category):
        all_ids = [None] * (len(employees) * 3)
        idx = 0
        for emp in employees:
            if isinstance(emp, PermanentEmployee) and emp.assets:
                for asset in emp.assets:
                    if asset.get_asset_id()[0].lower() == category.lower():
                        all_ids[idx] = asset.get_asset_id()
                        idx += 1
        return all_ids


# -----------------------------------------------------
# Tester / Main Demo
# -----------------------------------------------------
if __name__ == "__main__":
    try:
        # Assets
        a1 = Asset("DSK-876761L", "Dell-Desktop", "2020-Dec-01")
        a2 = Asset("LTP-987125L", "HP-Laptop", "2022-Oct-25")
        a3 = Asset("IPH-110130h", "VoIP", "2020-Nov-30")

        # Employees
        e1 = PermanentEmployee("Roger Fed", 15500, ["DA-50", "HRA-40"], [a1, a3])
        e2 = ContractEmployee("Rafael N", 70)

        # Salary Calculation
        admin = Admin()
        employees = [e1, e2]
        factors = [3.9, 189]

        admin.generate_salary_slip(employees, factors)

        for e in employees:
            print(e)
            print("Salary:", e.get_salary())
            print()

        # Asset Report
        count = admin.generate_assets_report([e1], "2021-Dec-31")
        print("Assets expiring before 2021-Dec-31:", count)

        report = admin.generate_assets_report_by_category([e1], 'D')
        print("All D assets:", [r for r in report if r])
    except Exception as e:
        print("Error:", e)
