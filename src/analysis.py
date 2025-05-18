from collections import defaultdict
from typing import DefaultDict

from src.loader import load_data
from src.models import *


OverrallAverageResult = dict[int, float]
PerDepartmentAverageResult = dict[int, dict[str, float]]


def analyze_overrall_average(data: list[Datapoint]) -> OverrallAverageResult:
    year_to_grades: dict[int, list[int]] = defaultdict(list)

    for datapoint in data:
        year_to_grades[datapoint.term.year].append(datapoint.course_average)

    year_to_avg: dict[int, float] = {}
    for k, v in year_to_grades.items():
        year_to_avg[k] = sum(v) / len(v)

    return year_to_avg


def analyze_per_department_average(data: list[Datapoint]) -> PerDepartmentAverageResult:
    year_dept_to_grades: dict[int, dict[str, list[int]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for datapoint in data:
        year = datapoint.term.year
        dept = datapoint.course.department
        year_dept_to_grades[year][dept].append(datapoint.course_average)

    result: PerDepartmentAverageResult = {}

    for year, dept_to_grades in year_dept_to_grades.items():
        result[year] = {}
        for dept, grades in dept_to_grades.items():
            result[year][dept] = sum(grades) / len(grades)

    return result
