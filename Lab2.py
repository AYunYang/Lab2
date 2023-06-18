def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input("Enter temp:")
    num_list = user_input.split(",") #when numbers are split the type is str
    float_list = list(map(float, num_list))  #Change str type to floating number
    print(float_list)
    return float_list

def calc_average_temperature(float_list): #(float_list), taking variable from a different function
    average = sum(float_list)/len(float_list) #sum(),is to find the sum. len(), number of numbers in the list
    print("average value is = " + str(average))
    return average
def calc_min_temperature(float_list):
    min_value = min(float_list)
    print("The min value is = " + str(min_value))  # min(), find the min in list
    return min_value

def calc_max_temperature(float_list):
    max_value = max(float_list)
    print("The max value is = " + str(max_value))  #max(), find the max in list
    return max_value

def calc_median_temperature(float_list):
    import statistics   #Need import library, like c++ include.
    median_value = statistics.median(float_list)
    print("The median value is = " + str(median_value))  #statistics.median(),find median
    return median_value

def main():
    display_main_menu()
    float_list = get_user_input()
    calc_average_temperature(float_list)
    calc_min_temperature(float_list)
    calc_max_temperature(float_list)
    calc_median_temperature(float_list)

if __name__ == "__main__":
    main()
