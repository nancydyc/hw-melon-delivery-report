def print_delivery_report(daily_txt_report):
    
    the_file = open(daily_txt_report) # read day 1 report 
    for line in the_file: # iterate through each line in the report
        line = line.rstrip() # clear whitespace on the right of each line
        words = line.split('|') # split line by "|" into a list of string

        melon = words[0] # assign the 1st element of the words list to melon
        count = words[1] # assign the 1st element of the words list to count
        amount = words[2] # assign the 1st element of the words list to amount

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount)) # format the three variables to fill in the string
    the_file.close() # close the report

print("Day 1")
print_delivery_report("um-deliveries-20140519.txt")
print("Day 2")
print_delivery_report("um-deliveries-20140520.txt")
print("Day 3")
print_delivery_report("um-deliveries-20140521.txt")
