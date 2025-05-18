from src.loader import load_data
from src.plotter import (
    plot_overall_average,
    plot_overall_by_term,
    plot_per_department_average,
    plot_per_department_average_by_term,
)
from src.analysis import (
    analyze_overrall_average,
    analyze_overrall_average_by_term,
    analyze_per_department_average,
    analyze_per_department_average_by_term,
)


def main():
    data = load_data()

    overall_avg = analyze_overrall_average(data)
    overall_avg_per_term = analyze_overrall_average_by_term(data)
    per_dept_avg = analyze_per_department_average(data)
    per_dept_per_term_avg = analyze_per_department_average_by_term(data)

    plot_overall_average(overall_avg)
    plot_overall_by_term(overall_avg_per_term)
    plot_per_department_average(per_dept_avg)
    plot_per_department_average_by_term(per_dept_per_term_avg)


if __name__ == "__main__":
    main()
