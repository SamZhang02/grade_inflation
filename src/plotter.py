from src.analysis import (
    OverrallAverageResult,
    PerDepartmentAverageResult,
)

import matplotlib.pyplot as plt
import os
import numpy as np


def plot_overall_average(overall_avg: OverrallAverageResult):
    years = sorted(overall_avg.keys())
    averages = [overall_avg[year] for year in years]
    overall_mean = sum(averages) / len(averages)

    plt.figure(figsize=(8, 4))
    plt.plot(years, averages, marker="o", label="Yearly Average")
    plt.axhline(
        overall_mean,
        color="red",
        linestyle="--",
        label=f"Overall Avg: {overall_mean:.2f}",
    )
    plt.title("Overall Course Average by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Grade")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    os.makedirs("plot", exist_ok=True)
    plt.savefig("plot/overall.png")
    plt.close()


def plot_per_department_average(per_dept_avg: PerDepartmentAverageResult):
    os.makedirs("plot", exist_ok=True)
    years = sorted(per_dept_avg.keys())

    all_departments = set()
    for yearly in per_dept_avg.values():
        all_departments.update(yearly.keys())

    for dept in sorted(all_departments):
        dept_avgs = []
        for year in years:
            avg = per_dept_avg[year].get(dept)
            dept_avgs.append(avg if avg is not None else np.nan)

        valid_avgs = [x for x in dept_avgs if not np.isnan(x)]
        if not valid_avgs:
            continue  # skip departments with no data

        dept_mean = sum(valid_avgs) / len(valid_avgs)

        plt.figure(figsize=(8, 4))
        plt.plot(years, dept_avgs, marker="o", label="Yearly Avg")
        plt.axhline(
            dept_mean, color="red", linestyle="--", label=f"Dept Avg: {dept_mean:.2f}"
        )
        plt.title(f"{dept} Course Averages by Year")
        plt.xlabel("Year")
        plt.ylabel("Average Grade")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"plot/{dept}.png")
        plt.close()
