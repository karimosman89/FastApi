import pandas as pd


QUESTIONS_FILE = "C:/Users/Fikrat Qasimov/Documents/DataTest/questions_en.xlsx"

def read_questions_from_excel():
    try:
        df = pd.read_excel(QUESTIONS_FILE)
        return df
    except FileNotFoundError:
        print(f"File '{QUESTIONS_FILE}' not found.")
        return None

def add_new_question_to_excel(question_data):
    try:
        existing_data = read_questions_from_excel()
        if existing_data is None:
            df = pd.DataFrame(columns=['question', 'subject', 'use', 'correct', 'responseA', 'responseB', 'responseC', 'responseD', 'remark'])
        else:
            df = existing_data

        new_row = pd.DataFrame({
            'question': [question_data.question],
            'subject': [question_data.subject],
            'use': [question_data.use],
            'correct': [question_data.correct],
            'responseA': [question_data.responseA],
            'responseB': [question_data.responseB],
            'responseC': [question_data.responseC],
            'responseD': [question_data.responseD],
            'remark': [question_data.remark]
        })

        df = pd.concat([df, new_row], ignore_index=True)

        df.to_excel(QUESTIONS_FILE, index=False)
        print("New question added to the Excel file.")
        return True
    except Exception as e:
        print(f"An error occurred while adding the question: {e}")
        return False
