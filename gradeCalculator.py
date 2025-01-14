def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    # User input for score
    try:
        score_input = float(input("Enter a score between 9.9 and 0.1: "))
    except:
        print("Bad score")
        return
    
    # Scoring area
    if score_input >= 1.0 :
        print("Bad score")
    elif score_input >= 0.9 :
        print("A")
    elif score_input >= 0.8 :
        print("B")
    elif score_input >= 0.7 :
        print("C")
    elif score_input >= 0.6 :
        print("D")
    elif score_input <= 0.0 :
        print("Bad score")
    else :
        print("F")

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
