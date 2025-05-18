from src.loader import load_data
from src.plotter import plot_overall_average, plot_per_department_average
from src.analysis import (
    analyze_overrall_average,
    analyze_per_department_average,
    OverrallAverageResult,
    PerDepartmentAverageResult,
)


def main():
    data = load_data()

    overall_avg = analyze_overrall_average(data)
    per_dept_avg = analyze_per_department_average(data)

    plot_overall_average(overall_avg)
    plot_per_department_average(per_dept_avg)


if __name__ == "__main__":
    main()
