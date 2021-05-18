#Average Rainfall program

#Define Variables
month = 0
total_inches = 0

#Ask user for numbers of years
years = int(input('Enter the number of years: '))

#Set raifall variable as 0 cuz initial state 

rainfall = 0

# each iteration using for loops

for year in range(1, years + 1):
    for month in range(1, 13):
        monthly_inches = float(input("Enter the number of inches of rainfall for month " + format(month, "d") + ": "))
        total_inches += monthly_inches
        month += 1

#formula to calculate average
                               
rainfall_avg = total_inches / monthly_inches

#Display number of months, total inches of rainfall and the average rainfall per month

print( "Number of months: " + format( month, "d"), ", Total" + \
    " inches of rainfall: " + format(total_inches, ".2f"), \
    "Average of rainfall: " + format(rainfall_avg, ".2f"), sep="\n")        
