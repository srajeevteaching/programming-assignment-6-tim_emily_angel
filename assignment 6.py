# Emily Catanzariti, Angel Scott, Tim Hunt
# CS151, Dr. Rajeev
# Programming Assignment 6
# Program Inputs: choice of which question to answer
# Program Outputs: rate of change in violent crime, graph of rates of crime, average of juvenile arrest

# import math plot library
import matplotlib.pyplot as plt

# index constants
NEIGHBORHOODS = 0
CRIME_RATE2010 = 1
CRIME_RATE2011 = 2
CRIME_RATE2012 = 3
CRIME_RATE2013 = 4
CRIME_RATE2014 = 5
VIOLENT2010 = 6
VIOLENT2011 = 7
VIOLENT2012 = 8
VIOLENT2013 = 9
VIOLENT2014 = 10
PROPERTY2011 = 11
PROPERTY2012 = 12
PROPERTY2013 = 13
PROPERTY2014 = 14
JUVENILE_ARREST2011 = 15
VIOLENT_ARREST2011 = 16
DRUG_ARREST2011 = 17
DOMESTIC_CALL2010 = 18
DOMESTIC_CALL2011 = 19
DOMESTIC_CALL2012 = 20
SHOOTING_CALL2011 = 21
SHOOTING_CALL2012 = 22
COMMON_CALL2011 = 23
COMMON_CALL2012 = 24
NARCOTIC_CALL2011 = 25
NARCOTIC_CALL2012 = 26
CAR_ACCIDENT2011 = 27
CAR_ACCIDENT2012 = 28
GUN_HOMICIDE2011 = 29
GUN_HOMICIDE2012 = 30
GUN_HOMICIDE2013 = 31
GUN_HOMICIDE2014 = 32
ADULT_ARREST2014 = 33
PROPERTY_NARCOTIC = 34
DV_SHOOTING = 35


# file to list of lists function
def crime_list_file():
    # empty list
    crime_list = []
    # try except open file
    try:
        crime_file = open("crime (1).csv", "r")
        line_counter = 0
        for line in crime_file:
            line_counter += 1
            each_line = line.split(",")
            # correct value types
            try:
                # type cast
                each_line[NEIGHBORHOODS] = each_line[NEIGHBORHOODS].strip()
                each_line[CRIME_RATE2010] = float(each_line[CRIME_RATE2010])
                each_line[CRIME_RATE2011] = float(each_line[CRIME_RATE2011])
                each_line[CRIME_RATE2012] = float(each_line[CRIME_RATE2012])
                each_line[CRIME_RATE2013] = float(each_line[CRIME_RATE2013])
                each_line[CRIME_RATE2014] = float(each_line[CRIME_RATE2014])
                each_line[VIOLENT2010] = float(each_line[VIOLENT2010])
                each_line[VIOLENT2011] = float(each_line[VIOLENT2011])
                each_line[VIOLENT2012] = float(each_line[VIOLENT2012])
                each_line[VIOLENT2013] = float(each_line[VIOLENT2013])
                each_line[VIOLENT2014] = float(each_line[VIOLENT2014])
                each_line[PROPERTY2011] = float(each_line[PROPERTY2011])
                each_line[PROPERTY2012] = float(each_line[PROPERTY2012])
                each_line[PROPERTY2013] = float(each_line[PROPERTY2013])
                each_line[PROPERTY2014] = float(each_line[PROPERTY2014])
                each_line[JUVENILE_ARREST2011] = float(each_line[JUVENILE_ARREST2011])
                each_line[VIOLENT_ARREST2011] = float(each_line[VIOLENT_ARREST2011])
                each_line[DRUG_ARREST2011] = float(each_line[DRUG_ARREST2011])
                each_line[DOMESTIC_CALL2010] = float(each_line[DOMESTIC_CALL2010])
                each_line[DOMESTIC_CALL2011] = float(each_line[DOMESTIC_CALL2011])
                each_line[DOMESTIC_CALL2012] = float(each_line[DOMESTIC_CALL2012])
                each_line[SHOOTING_CALL2011] = float(each_line[SHOOTING_CALL2012])
                each_line[SHOOTING_CALL2012] = float(each_line[SHOOTING_CALL2012])
                each_line[COMMON_CALL2011] = float(each_line[COMMON_CALL2011])
                each_line[COMMON_CALL2012] = float(each_line[COMMON_CALL2012])
                each_line[NARCOTIC_CALL2011] = float(each_line[NARCOTIC_CALL2012])
                each_line[NARCOTIC_CALL2012] = float(each_line[NARCOTIC_CALL2012])
                each_line[CAR_ACCIDENT2011] = float(each_line[CAR_ACCIDENT2011])
                each_line[CAR_ACCIDENT2012] = float(each_line[CAR_ACCIDENT2012])
                each_line[GUN_HOMICIDE2011] = float(each_line[GUN_HOMICIDE2011])
                each_line[GUN_HOMICIDE2012] = float(each_line[GUN_HOMICIDE2012])
                each_line[GUN_HOMICIDE2013] = float(each_line[GUN_HOMICIDE2013])
                each_line[GUN_HOMICIDE2014] = float(each_line[GUN_HOMICIDE2014])
                each_line[ADULT_ARREST2014] = float(each_line[ADULT_ARREST2014])
                each_line[PROPERTY_NARCOTIC] = each_line[PROPERTY_NARCOTIC].strip().lower()
                each_line[DV_SHOOTING] = each_line[DV_SHOOTING].strip().lower()
                crime_list.append(each_line)
            except ValueError:
                print("error: bad value found. skipping line", line_counter)
        crime_file.close()
    except FileNotFoundError:
        print("sorry, file not found. cannot complete")
    return crime_list


# create a menu to choose which action

# calculate change in violent crime from 2010 to 2014
# + or - 1 is no change, + or - 5 is significant change
def violent_crime_change(crime_list, new_file_name):
    # initialize counts
    sig_down = 0
    down = 0
    no_change = 0
    up = 0
    sig_up = 0
    # open new file in write mode
    new_file = open(new_file_name, "w")
    # loop through list of neighborhoods
    for neighborhood in crime_list:
        # calculate change
        change = float(neighborhood[VIOLENT2014]) - float(neighborhood[VIOLENT2010])
        # categorize change, print to new file, and add to count
        if 1 >= change >= -1:
            print("The violent crime rate in", neighborhood[NEIGHBORHOODS], "has not changed.", file=new_file)
            no_change += 1
        elif 5 > change >= 1:
            print("The violent crime rate in", neighborhood[NEIGHBORHOODS], "has gone up.", file=new_file)
            up += 1
        elif -5 < change < -1:
            print("The violent crime rate in", neighborhood[NEIGHBORHOODS], "has gone down.", file=new_file)
            down += 1
        elif change >= 5:
            print("The violent crime rate in", neighborhood[NEIGHBORHOODS], "has gone significantly up.",
                  file=new_file)
            sig_up += 1
        elif change <= -5:
            print("The violent crime rate in", neighborhood[NEIGHBORHOODS], "has gone significantly down.",
                  file=new_file)
            sig_down += 1
        else:
            print("Error. Skipping", neighborhood[NEIGHBORHOODS])
    # close file to save changes
    new_file.close()
    # make graph of change in violent crime rate
    print("Please close graph to continue the program.")
    x = ["sig down", "down", "no change", "up", "sig up"]
    plt.xlabel("Significance of change")
    y = [sig_down, down, no_change, up, sig_up]
    plt.ylabel("Number of neighborhoods")
    plt.title("Change in violent crime rate from 2010 to 2014")
    plt.bar(x, y)
    plt.show()


# graph of neighborhoods with low, moderate, or high crime rates
# low is < 20, high is > 50
def Graph_of_Neighborhood_Crime_rates(crime_list):
    Low_Crime = 0
    Med_Crime = 0
    High_Crime = 0
    for neighborhood in crime_list:
        if neighborhood[ADULT_ARREST2014] > 50:
            High_Crime += 1
        elif 20 < neighborhood[ADULT_ARREST2014] < 50:
            Med_Crime += 1
        elif neighborhood[ADULT_ARREST2014] < 20:
            Low_Crime += 1
    x = ["High Crime", "Medium Crime", "Low Crime"]
    y = [High_Crime, Med_Crime, Low_Crime]
    plt.xlabel("Intensity of Crime")
    plt.ylabel("Quantity of Neighborhoods")
    plt.title("Adult Crime in Neighborhoods 2014")
    plt.bar(x, y)
    plt.show()


# average of juvenile arrests for each category of dv-shootings column
def juvenile_arrests(crime_list):
    # counters for sum of jv arrests per dv-shooting category
    # counters for number of neighborhoods in each dv-shootings category
    sum_one = 0
    total_one = 0
    sum_two = 0
    total_two = 0
    sum_three = 0
    total_three = 0
    sum_four = 0
    total_four = 0
    sum_five = 0
    total_five = 0
    sum_six = 0
    total_six = 0
    # loop through each neighborhood and add to counters accordingly
    for neighborhood in crime_list:
        if neighborhood[DV_SHOOTING] == "high-domestic violence:moderate-shootings":
            total_one += 1
            sum_one += neighborhood[JUVENILE_ARREST2011]
        elif neighborhood[DV_SHOOTING] == "moderate-domestic-violence:moderate-shootings":
            total_two += 1
            sum_two += neighborhood[JUVENILE_ARREST2011]
        elif neighborhood[DV_SHOOTING] == "moderate-domestic-violence:low-shootings":
            total_three += 1
            sum_three += neighborhood[JUVENILE_ARREST2011]
        elif neighborhood[DV_SHOOTING] == "high-domestic violence:low-shootings":
            total_four += 1
            sum_four += neighborhood[JUVENILE_ARREST2011]
        elif neighborhood[DV_SHOOTING] == "high-domestic violence:high-shootings":
            total_five += 1
            sum_five += neighborhood[JUVENILE_ARREST2011]
        elif neighborhood[DV_SHOOTING] == "low-domestic-violence:low-shootings":
            total_six += 1
            sum_six += neighborhood[JUVENILE_ARREST2011]
        else:
            print("Error. Skipping ", neighborhood[NEIGHBORHOODS])
    # calculate and output average number of juvenile arrests for each dv-shootings category
    avg_hdv_ms = sum_one / total_one
    print("The average number of juvenile arrests for", total_one, "neighborhoods with High-Domestic Violence: "
                                                                   "Moderate Shootings is %.2f" % avg_hdv_ms)
    avg_mdv_ms = sum_two / total_two
    print("The average number of juvenile arrests for", total_two, "neighborhoods with Moderate-Domestic Violence:"
                                                                   " Moderate Shootings is %.2f" % avg_mdv_ms)
    avg_mdv_ls = sum_three / total_three
    print("The average number of juvenile arrests for", total_three, "neighborhoods with Moderate-Domestic Violence:"
                                                                     " Low Shootings is %.2f" % avg_mdv_ls)
    avg_hdv_ls = sum_four / total_four
    print("The average number of juvenile arrests for", total_four, "neighborhoods with High-Domestic Violence: "
                                                                    "Low Shootings is %.2f" % avg_hdv_ls)
    avg_hdv_hs = sum_five / total_five
    print("The average number of juvenile arrests for", total_five, "neighborhoods with High-Domestic Violence: "
                                                                    "High Shootings is %.2f" % avg_hdv_hs)
    avg_ldv_ls = sum_six / total_six
    print("The average number of juvenile arrests for", total_six, "neighborhoods with Low-Domestic Violence: "
                                                                   "Low Shootings is %.2f" % avg_ldv_ls)


# which neighborhood had the most automobile accident calls for service per 1000 residents in 2011.
def max_calls(crime_list):
    max_calls_index = 0
    for x in range(len(crime_list)):
        if crime_list[x][CAR_ACCIDENT2011] > crime_list[max_calls_index][CAR_ACCIDENT2011]:
            max_calls_index = x
    print("The neighborhood with the most automobile accident calls for service per 1000 residents in 2011 "
          "is:", crime_list[max_calls_index][NEIGHBORHOODS])


# main function
