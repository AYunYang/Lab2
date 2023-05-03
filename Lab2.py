def display_main_menu():
 print("Numbers")
def get_user_input():
     print('Enter numbers with commas=')
     x = input()
     #print('numbers=' + x)
     txt = x.split(", ")
     print(txt)
     #convert from string to float
def eqn():

     sum = sum(txt)
     print(sum)

def main():
     print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
     display_main_menu()
     get_user_input()
     eqn()

     num_list = get_user_input()



if __name__ == "__main__":
     main()