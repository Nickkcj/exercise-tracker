from api.nutritionix import get_exercise_data
from api.sheety import add_exercise_to_sheet

def main():
    exercise_text = input("Tell me which exercises you did: ")
    exercise_data = get_exercise_data(exercise_text)
    add_exercise_to_sheet(exercise_data)

if __name__ == "__main__":
    main()
    
