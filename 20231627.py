"""" 
I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
Any code taken from other sources is referenced within my code solu􀆟on.
Student ID: 20231627
UOW Number: 20521745
Date: 13/12/2023
"""

from graphics import * 

#declare variables to store count of outcomes and data
progress = 0
trailer = 0
retriever = 0
excluded = 0
data = []

#Input Validation
def get_valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in [0, 20, 40, 60, 80, 100, 120]:  
                return user_input # Returns input to the caller if input valid
            else:
                print("Out of range, Please enter a valid value (0, 20, 40, 60, 80, 100, 120).")
        except ValueError:
            print("Integer required, Please enter a valid integer.")

def get_valid_choice(prompt,valid_character): 
    while True:
        user_input = input(prompt)
        if user_input.lower() in valid_character:
            return user_input.lower() # Returns to input to caller if its valid
        else:
            print("Invalid Input, Please enter a valid choice.\n")

# Outcome Prediction
def predict_progression ():
    global progress, trailer, retriever, excluded, data

    while True:
        # Prompts and gets valid user input
        pass_credits = get_valid_input("\nEnter your total PASS credit : ")
        defer_credits = get_valid_input("Enter your total DEFER credits : ")
        fail_credits = get_valid_input("Enter your total FAIL credit : ")

        total_credits = pass_credits + defer_credits + fail_credits
        
        # Outputs respective outcomes according to declared rules
        if total_credits == 120:
            if pass_credits == 120:
                outcome = "Progress"
                progress += 1 
            elif pass_credits >= 100 and (defer_credits == 20 or fail_credits == 20):
                outcome = "Progress (module trailer)"
                trailer += 1
            elif pass_credits < 100 and fail_credits < 80 :
                outcome = "Module retriever"
                retriever += 1 
            elif fail_credits >= 80:
                outcome = "Exclude"
                excluded += 1
            else:
                print("Unexpected Error\n")
            data.append([outcome,pass_credits,defer_credits,fail_credits])
            print (outcome,"\n") 
            break # Break out of the loop if inputs are correct
        else:
            print("Total  incorrect, Credits should add up to 120.\n")

#function to display graph   
def show_graph():
    # declare catergories, colours and count
    categories = ["Progress", "Trailer", "Retriever", "Excluded"]
    colours = ["palegreen2", "palegreen4", "olivedrab", "rosybrown"]
    count = [progress, trailer, retriever, excluded]

    #declare wdith and spacing for graph
    bar_width = 140
    spacing = 10

    try:
        #Open a window
        win = GraphWin("Histogram", 850, 500)
        win.setBackground("honeydew1")

        #Display a Title for graph
        title = Text(Point(325,30),"Histogram Results")
        title.setSize(30)
        title.setTextColor("grey")
        title.setFace("helvetica")
        title.setStyle("bold")
        title.draw(win)

        #Display a horizontal base line for histogram
        aLine = Line(Point(125,400), Point(725,400))
        aLine.setFill("grey")
        aLine.setWidth(3)
        aLine.draw(win)

        #Display Total Number of Outcomes displayed in histogram
        total_number_of_students = sum(count)
        total = Text(Point(300,455),f"{total_number_of_students} outcomes in total.")
        total.setSize(20)
        total.setTextColor("grey")
        total.setFace("helvetica")
        total.setStyle("bold")
        total.draw(win)

        #loop through 4 outcome catergories
        for i in range(4):

            #computes starting x coordinate and ending x coordinate for bars
            x_start = (((i + 1) * bar_width)+spacing)
            x_end = (i + 2) * bar_width

            #computes height of bar (percentage of largest count variable)
            height = 400 -((count[i] / max(count)) * 100) *3

            #display bars representing each catergory 
            bar = Rectangle(Point(x_start , height),Point( x_end, 400)) 
            bar.setWidth(2)
            bar.setOutline ("grey")
            bar.setFill(colours[i])
            bar.draw(win)

            #display label for each catergory
            label = Text(Point((x_start + x_end)/2, 420), categories[i])
            label.setSize(17)
            label.setTextColor("grey")
            label.setFace("helvetica")
            label.setStyle("bold")
            label.draw(win)

            #display count of outcomes above each bar
            count_text = Text(Point((x_start + x_end)/2, height -15 ), count[i])
            count_text.setSize (17)
            count_text.setTextColor("grey")
            count_text.setFace("helvetica")
            count_text.setStyle("bold")
            count_text.draw(win)

        win.getMouse()  # pause for click in window 
    except GraphicsError:
        win.close()

def display_list():
    print("\nPart 2: List")
    for record in data:
        print(f"{record[0]} - {record[1]}, {record[2]}, {record[3]}") 
        
def display_txt_file ():
    print("\nPart 3: Text File")
    with open("Data_records.txt","w") as f:
        for record in data:
            f.write(f"{record[0]} - {record[1]}, {record[2]}, {record[3]}\n")
    with open("Data_records.txt","r") as f:
        content = f.read()
        print(content)
    
def main():
    print("-" * 40 + f"\nProgression Outcome Predictor\n" + "-" * 40 + "\n")
    print("Are you a Staff member or a Student")
    user_choice = get_valid_choice("Enter 'Staff' for staff member or 'Student' for student: ",["student","staff"])
    if user_choice =="student" :
        predict_progression()
    else:
        predict_progression()
        print("Would you like to enter another set of data? ")
        user_choice = get_valid_choice("Enter 'y' for yes or 'q' to quit and view results: ",["y","q"])
        while user_choice == "y" :
            predict_progression()
            print("Would you like to enter another set of data? ")
            user_choice = get_valid_choice("Enter 'y' for yes or 'q' to quit and view results: ",["y","q"])
        show_graph()
        display_list()
        display_txt_file()

if __name__ == "__main__":
    main()

