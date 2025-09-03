# ask user to enter number of seconds
total_seconds = int(input("enter length of time in seconds: "))
# define nuimber of seconds in each time unit
seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_year = 365 * seconds_in_day

# calculate number of years
years = total_seconds // seconds_in_year
remaining_seconds = total_seconds % seconds_in_year

# calculate number of days
days = remaining_seconds // seconds_in_day
remaining_seconds = remaining_seconds % seconds_in_day

# calculate number of hours
hours = remaining_seconds // seconds_in_hour
remaining_seconds = remaining_seconds % seconds_in_hour

# calculate number of minutes 
minutes = remaining_seconds // seconds_in_minute
seconds = remaining_seconds % seconds_in_minute

# print 
print("years  :", years)
print("days  :",days)
print("hours :",hours)
print("minute :",minutes)
print("seconds :",seconds)