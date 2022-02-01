### 4. Write a program that calculates number of seconds to pass based on days input
### • Sample value: 5 days
### • Expected Result : 432000 seconds

days = int(input("Enter number of days: "))

seconds = days*24*60*60

print(days, "days =", seconds, "seconds")