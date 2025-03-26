def write_to_file(data): 
    with open("data.txt", "a") as file: // creates and appends to a file called data.txt. Could name based on current time
        file.write(data + "\n") 
