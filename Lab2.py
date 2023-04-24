def display_main_menu():
 print("Numbers")
def get_user_input():
     print('Enter numbers with commas=')
     x = input()
     print('numbers=' + x)

def main():
     print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
     display_main_menu()
     num_list = get_user_input()

if __name__ == "__main__":
     main()