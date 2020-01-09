print("Day 1")
the_file = open("um-deliveries-20140519.txt") # read day 1 report 
for line in the_file: # iterate through each line in the report
    line = line.rstrip() # clear whitespace on the right of each line
    words = line.split('|') # split line by "|" into a list of string

    melon = words[0] # assign the 1st element of the words list to melon
    count = words[0] # assign the 1st element of the words list to count
    amount = words[0] # assign the 1st element of the words list to amount

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount)) # format the three variables to fill in the string
the_file.close() # close the report


print("Day 2")
the_file = open("um-deliveries-20140520.txt") # read day 2 report
for line in the_file:
    line = line.rstrip() 
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt") # read day 3 report
for line in the_file:
    line = line.rstrip() 
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
