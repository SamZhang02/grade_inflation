from collections import defaultdict
from src.models import *


OverrallAverageResult = dict[int, float]
OverrallAverageResultByTerm = dict[Term, float]
PerDepartmentAverageResult = dict[int, dict[str, float]]
PerDepartmentAverageByTermResult = dict[Term, dict[str, float]]


def analyze_overrall_average(data: list[Datapoint]) -> OverrallAverageResult:
    year_to_grades: dict[int, list[int]] = defaultdict(list)

    for datapoint in data:
        year_to_grades[datapoint.term.year].append(datapoint.course_average)

    year_to_avg: dict[int, float] = {}
    for k, v in year_to_grades.items():
        year_to_avg[k] = sum(v) / len(v)

    return year_to_avg


def analyze_overrall_average_by_term(
    data: list[Datapoint],
) -> OverrallAverageResultByTerm:
    term_to_grades: dict[Term, list[int]] = defaultdict(list)

    for datapoint in data:
        term_to_grades[datapoint.term].append(datapoint.course_average)

    term_to_avg: dict[Term, float] = {}
    for k, v in term_to_grades.items():
        term_to_avg[k] = sum(v) / len(v)

    return term_to_avg


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


def analyze_per_department_average_by_term(
    data: list[Datapoint],
) -> PerDepartmentAverageByTermResult:
    term_dept_to_grades: dict[Term, dict[str, list[int]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for datapoint in data:
        term = datapoint.term
        dept = datapoint.course.department
        term_dept_to_grades[term][dept].append(datapoint.course_average)

    result: PerDepartmentAverageByTermResult = {}

    for term, dept_to_grades in term_dept_to_grades.items():
        result[term] = {}
        for dept, grades in dept_to_grades.items():
            result[term][dept] = sum(grades) / len(grades)

    return result
