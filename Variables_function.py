#Program to convert Kilograms(kg) to Pounds(lb)

#Kilogram Variable amounts
kg_value_1=151.953
kg_value_2=102.058
kg_value_3=188.241
kg_value_4=61.235

#Conversion factor: 1 kg = 2.20462 lb
conversion=2.20462

#Calculating lb's for kg values
lb_value_1=kg_value_1*conversion
lb_value_2=kg_value_2*conversion
lb_value_3=kg_value_3*conversion
lb_value_4=kg_value_4*conversion

#Print functions to produce results of conversion
print(f"{kg_value_1} kilograms is equal to {lb_value_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lb_value_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lb_value_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lb_value_4:.2f} pounds.")