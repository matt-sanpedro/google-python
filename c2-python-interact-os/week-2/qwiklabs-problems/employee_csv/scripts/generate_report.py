#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
        # purpose of dialect is to remove any leading spaces while parsing the CSV file
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        # initialize var
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        # print(employee_list)
        return employee_list

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])

        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')
                f.close()


employee_list = read_employees("/home/student-03-260f93ef059c/data/employees.csv")
# print(employee_list)
dictionary = process_data(employee_list)
# print(dictionary)
write_report(dictionary, "/home/student-03-260f93ef059c/test_report.txt")
