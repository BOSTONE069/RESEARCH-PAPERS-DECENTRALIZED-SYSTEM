def calculate_staffing(students, contact_hours, courses, teaching_load, ssr):
    total_contact_hours = students * contact_hours * courses
    staff_by_workload = total_contact_hours / teaching_load
    staff_by_ssr = students / ssr
    recommended_staff = max(staff_by_workload, staff_by_ssr)

    return {
        "Total Contact Hours": total_contact_hours,
        "Staff by Workload": round(staff_by_workload, 2),
        "Staff by SSR": round(staff_by_ssr, 2),
        "Recommended Optimal Staff": round(recommended_staff, 2)
    }


# Example use:
result = calculate_staffing(
    students=300,
    contact_hours=3,
    courses=5,
    teaching_load=3,
    ssr=20
)

for key, value in result.items():
    print(f"{key}: {value}")
