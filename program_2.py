#Matthew Tyler
#09/26/2025
#Movie Tix

def main():
    #variables
    more_tickets = True
    total_tickets = 0

    #list of movies
    movies = ["thor", "superman", "ironMan", "spiderman", "batman"]
    
    print("What movies would you like to watch today?")
    print('We have "thor", "superman", "ironMan", "spiderman", and "batman". ')

    #while loop to keep asking what movies the user wants
    while more_tickets == True:
        movie = input('Enter which movie you would like to watch or "done" to finish. Please use lowercase')
        if movie == "done":
            more_tickets = False
        elif movie in movies:
            ticket_quant = int(input("How many tickets? please enter a non-zero whole number"))
            total_tickets += ticket_quant
        else:
            print("sorry we do not have that movie")
    #Print total number of tickets the user will need
    print("you will need" , total_tickets," tickets")
    
            
            
        
if __name__ == '__main__':
    main()
