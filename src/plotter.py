from src.analysis import (
    OverrallAverageResult,
    OverrallAverageResultByTerm,
    PerDepartmentAverageByTermResult,
    PerDepartmentAverageResult,
)

import matplotlib.pyplot as plt
import os
import numpy as np


def plot_overall_average(overall_avg: OverrallAverageResult):
    years = sorted(overall_avg.keys())
    averages = [overall_avg[year] for year in years]
    overall_mean = sum(averages) / len(averages)

    # Regression line
    coeffs = np.polyfit(years, averages, 1)
    trend = np.poly1d(coeffs)

    plt.figure(figsize=(8, 4))
    plt.plot(years, averages, marker="o", label="Yearly Average")
    plt.plot(years, trend(years), linestyle="--", color="gray", label="Trendline")
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

    os.makedirs("plot/by_year", exist_ok=True)
    plt.savefig("plot/by_year/overall.png")
    plt.close()


def plot_per_department_average(per_dept_avg: PerDepartmentAverageResult):
    os.makedirs("plot/by_year", exist_ok=True)
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
            continue

        dept_mean = sum(valid_avgs) / len(valid_avgs)

        plt.figure(figsize=(8, 4))
        plt.plot(years, dept_avgs, marker="o", label="Yearly Avg")

        # Regression line
        x = np.array(years)[~np.isnan(dept_avgs)]
        y = np.array(dept_avgs)[~np.isnan(dept_avgs)]
        if len(x) > 1:
            coeffs = np.polyfit(x, y, 1)
            trend = np.poly1d(coeffs)
            plt.plot(
                years, trend(years), linestyle="--", color="gray", label="Trendline"
            )

        plt.axhline(
            dept_mean, color="red", linestyle="--", label=f"Dept Avg: {dept_mean:.2f}"
        )
        plt.title(f"{dept} Course Averages by Year")
        plt.xlabel("Year")
        plt.ylabel("Average Grade")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"plot/by_year/{dept}.png")
        plt.close()


def plot_overall_by_term(overall_avg: OverrallAverageResultByTerm):
    terms = sorted(overall_avg.keys())
    averages = [overall_avg[term] for term in terms]
    overall_mean = sum(averages) / len(averages)

    term_labels = [f"{term.season.name[0]}{term.year}" for term in terms]
    x = np.arange(len(terms))

    # Regression line
    coeffs = np.polyfit(x, averages, 1)
    trend = np.poly1d(coeffs)

    plt.figure(figsize=(10, 4))
    plt.plot(term_labels, averages, marker="o", label="Termly Average")
    plt.plot(term_labels, trend(x), linestyle="--", color="gray", label="Trendline")
    plt.axhline(
        overall_mean,
        color="red",
        linestyle="--",
        label=f"Overall Avg: {overall_mean:.2f}",
    )
    plt.title("Overall Course Average by Term")
    plt.xlabel("Term")
    plt.ylabel("Average Grade")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    os.makedirs("plot/by_term", exist_ok=True)
    plt.savefig("plot/by_term/overall.png")
    plt.close()


def plot_per_department_average_by_term(
    per_dept_term_avg: PerDepartmentAverageByTermResult,
):
    os.makedirs("plot/by_term", exist_ok=True)

    terms = sorted(per_dept_term_avg.keys())
    all_departments = set()
    for dept_map in per_dept_term_avg.values():
        all_departments.update(dept_map.keys())

    term_labels = [f"{term.season.name[0]}{term.year}" for term in terms]
    x = np.arange(len(terms))

    for dept in sorted(all_departments):
        dept_avgs = []
        for term in terms:
            avg = per_dept_term_avg[term].get(dept)
            dept_avgs.append(avg if avg is not None else np.nan)

        valid_avgs = [x for x in dept_avgs if not np.isnan(x)]
        if not valid_avgs:
            continue

        dept_mean = sum(valid_avgs) / len(valid_avgs)

        plt.figure(figsize=(10, 4))
        plt.plot(term_labels, dept_avgs, marker="o", label="Term Avg")

        # Regression line
        y = np.array(dept_avgs)
        mask = ~np.isnan(y)
        if mask.sum() > 1:
            coeffs = np.polyfit(x[mask], y[mask], 1)
            trend = np.poly1d(coeffs)
            plt.plot(
                term_labels, trend(x), linestyle="--", color="gray", label="Trendline"
            )

        plt.axhline(
            dept_mean, color="red", linestyle="--", label=f"Dept Avg: {dept_mean:.2f}"
        )
        plt.title(f"{dept} Course Averages by Term")
        plt.xlabel("Term")
        plt.ylabel("Average Grade")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"plot/by_term/{dept}.png")
        plt.close()
