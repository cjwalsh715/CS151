#Programmers: Brett Bonner, Will Gieb, Will Graney Gree, Colin Walsh

#Course: CS151, Prof Mehri

#Date: 9/28/21

#Lab Number: 2

#Program Inputs: present pop, birth rate, death rate, migration rate, and the amount of years

#Program Outputs: future population

#**Intro Comments**

#import math
import math
#user will enter value for present_pop
present_pop = float(input("Enter the present pop: "))
#user will enter value for birth_rate
birth_rate = float(input("Enter the birth rate per second: "))
#user will enter value for death_rate
death_rate = float(input("Enter the death rate per second: "))
#user will enter value for migration_rate
migration_rate = float(input("Enter the migration rate per second: "))
#user will enter value for time_years
amount_of_years = float(input("Enter the amount of years: "))
#sets year_in_secs equal to type int and value 31536000
year_in_secs = 31536000
#sets rates_per_year equal to the time_in_years multiplied by the birth_rate minus the death rate plus the migration rate
rates_per_year = year_in_secs*(birth_rate - death_rate + migration_rate)
#sets future pop equal to present_pop plus amount_of_years multiplied by the rates_per_year
future_pop = float(present_pop + amount_of_years*rates_per_year)
#outputs the future_pop variable ceiled
print("The future population is: ",math.ceil(future_pop))