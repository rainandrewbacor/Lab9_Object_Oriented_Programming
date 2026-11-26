STUDENT_ID = "TUPM-26-1879"
id_digits = "".join(d for d in STUDENT_ID if d.isdigit())
id_sum = sum(map(int, id_digits))
hourly_wage = (id_sum * 200) + 50

class EmployeePayrollSystem:
    def __init__(self, hour_wage):
        if hour_wage < 0:
            raise ValueError(f"Hourly wage cannot be negative.")
        self.hour_wage = hour_wage   
        self.__employee_list = []

    def display_employ(self):
            if not self.__employee_list:
                return f"[WARNING] No employees are added in the system yet."
            output = [f"\n=============== EMPLOYEE PAYROLL LIST - HOURLY WAGE: {self.hour_wage} ==============="]
            for employ in self.__employee_list:
                status = "Yes" if employ[2] > 160 else "No"
                output.append(f"Name: {employ[0]:<40} | Hours Worked: {employ[2]:<25} | Overtime?: {status} | Overtime Hours: {max(0, employ[2] - 160)} | Salary: {employ[3]:.2f}")
            return "\n".join(output) + "\n"
    
    def add_employee(self, name, hour_worked):
        if hour_worked < 0:
            return f"The system cannot accept negative integers. Enter valid work hours."
        self.__employee_list.append([name, self.hour_wage, hour_worked, 0.0])
        return f"Added Employee: {name}, Hours Worked: {hour_worked}"

    def compute_salary(self):
        if not self.__employee_list:
            return f"No employee has been added in the system. Ensure at least one employee entered."
        
        for employ in self.__employee_list:
            if employ[2] > 160:
                base_salary = employ[1] * 160
                rate = employ[1] * 1.5
                xtra_hrs = employ[2] - 160
                ot_extra = xtra_hrs * rate 
                ot_salary = base_salary + ot_extra
                total_salary = ot_salary
            else:
                base_salary = employ[1] * employ[2]
                total_salary = base_salary
            employ[3] = total_salary
        return f"{self.display_employ()}"

employ = EmployeePayrollSystem(hourly_wage)
print(employ.add_employee("Bacor", 170))
print(employ.compute_salary())
