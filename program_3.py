#Matthew Tyler
#09/26/2025
#Average Rainfall

def main():
    total_rain = 0
    months = 0
    print("This program will help you find the average rainfall over a period of time")
    years = int(input("how many years do you want to calculate?"))
    for y in range(1, years + 1):
        for m in range(1,13):
            while True:
                rain = float(input("How many inches of rain were there for this month "))
                if rain < 0:
                    print("This number cannot be negative")
                else:
                    break
            months += 1
            total_rain += rain
    Ave_rain = total_rain / months
    print("The average number for inches of rain/month was: ", Ave_rain)
    
if __name__ == '__main__':
    main()
