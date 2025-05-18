from src.models import *
import os
import pandas as pd


DATA_PATH = "data"
GRADES_PATH = os.path.join(DATA_PATH, "grades.csv")


def load_data() -> list[Datapoint]:
    data = pd.read_csv(GRADES_PATH)
    course_data: list[Datapoint] = []

    for _, row in data.iterrows():
        course = Course.from_string(row["Course"])
        term = Term.from_string(row["Term Name"])
        datapoint = Datapoint(course, term, row["Class Ave.1"])

        course_data.append(datapoint)

    return course_data
