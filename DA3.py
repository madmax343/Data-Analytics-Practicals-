
import pandas as pd


# ---------------------------------------------------------
# HELPER FUNCTION: Build a DataFrame from user input
# ---------------------------------------------------------
def get_dataframe(df_name, columns):
    """
    columns: list of column names to collect for this dataset
    """
    print(f"\n--- Enter data for {df_name} (columns: {columns}) ---")
    num_rows = int(input(f"How many rows for {df_name}? "))

    data = {col: [] for col in columns}

    for r in range(num_rows):
        print(f" Row {r + 1}:")

        for col in columns:
            value = input(f"   {col}: ").strip()

            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

            data[col].append(value)

    df = pd.DataFrame(data)
    print(f"\n{df_name}:\n{df}\n")

    return df


# ---------------------------------------------------------
# 1. CREATE DATASETS FROM USER INPUT
# ---------------------------------------------------------
print("=" * 60)
print("STEP 1: Build Dataset 1 - Student basic info")
print("=" * 60)

students_df1 = get_dataframe(
    "Dataset 1 (Students)",
    ["StudentID", "Name", "Branch"]
)

print("=" * 60)
print("STEP 2: Build Dataset 2 - Student marks")
print("=" * 60)

marks_df2 = get_dataframe(
    "Dataset 2 (Marks)",
    ["StudentID", "Marks"]
)

print("=" * 60)
print("STEP 3: Build Dataset 3 - New batch of students")
print("=" * 60)

students_df3 = get_dataframe(
    "Dataset 3 (New Students)",
    ["StudentID", "Name", "Branch"]
)


# ---------------------------------------------------------
# 2. CONCATENATION
# ---------------------------------------------------------

# Vertical concatenation: stacking rows
combined_students = pd.concat(
    [students_df1, students_df3],
    axis=0,
    ignore_index=True
)

print("Vertical Concatenation (axis=0):\n")
print(combined_students, "\n")


# Horizontal concatenation: stacking columns
print("--- Enter extra column data to concatenate with Dataset 1 ---")

n_rows_extra = len(students_df1)

print(f"Must match Dataset 1's row count: {n_rows_extra}")

attendance_values = []

for r in range(n_rows_extra):
    val = input(f" Attendance(%) for row {r + 1}: ").strip()

    try:
        attendance_values.append(float(val))
    except ValueError:
        attendance_values.append(val)

extra_info = pd.DataFrame({
    "Attendance(%)": attendance_values
})

horizontal_concat = pd.concat(
    [students_df1, extra_info],
    axis=1
)

print("Horizontal Concatenation (axis=1):\n")
print(horizontal_concat, "\n")


# ---------------------------------------------------------
# 3. MERGE: SQL-STYLE JOINS BASED ON A COMMON KEY
# ---------------------------------------------------------

inner_merge = pd.merge(
    students_df1, marks_df2,
    on="StudentID", how="inner"
)
print("Inner Merge:\n", inner_merge, "\n")

left_merge = pd.merge(
    students_df1, marks_df2,
    on="StudentID", how="left"
)
print("Left Merge:\n", left_merge, "\n")

right_merge = pd.merge(
    students_df1, marks_df2,
    on="StudentID", how="right"
)
print("Right Merge:\n", right_merge, "\n")

outer_merge = pd.merge(
    students_df1, marks_df2,
    on="StudentID", how="outer"
)
print("Outer Merge:\n", outer_merge, "\n")


# ---------------------------------------------------------
# 4. JOIN METHOD: JOIN USING THE INDEX
# ---------------------------------------------------------

df_a = students_df1.set_index("StudentID")
df_b = marks_df2.set_index("StudentID")

joined_df = df_a.join(df_b, how="inner")
print("Join (index-based, inner):\n", joined_df, "\n")

joined_outer_df = df_a.join(df_b, how="outer")
print("Join (index-based, outer):\n", joined_outer_df, "\n")


# ---------------------------------------------------------
# 5. MERGE WITH DIFFERENT COLUMN NAMES
# ---------------------------------------------------------

marks_df_renamed = marks_df2.rename(
    columns={"StudentID": "ID"}
)

merge_diff_cols = pd.merge(
    students_df1,
    marks_df_renamed,
    left_on="StudentID",
    right_on="ID",
    how="inner"
).drop(columns=["ID"])

print("Merge with Different Column Names:\n")
print(merge_diff_cols, "\n")


# ---------------------------------------------------------
# 6. MERGE ON MULTIPLE KEYS
# ---------------------------------------------------------

print("=" * 60)
print("STEP 4: Build Dataset X - Subjects per semester")
print("=" * 60)

df_x = get_dataframe(
    "Dataset X (Subjects)",
    ["StudentID", "Semester", "Subject"]
)

print("=" * 60)
print("STEP 5: Build Dataset Y - Grades per semester")
print("=" * 60)

df_y = get_dataframe(
    "Dataset Y (Grades)",
    ["StudentID", "Semester", "Grade"]
)

merge_multi_key = pd.merge(
    df_x,
    df_y,
    on=["StudentID", "Semester"],
    how="inner"
)

print("Merge on Multiple Keys:\n")
print(merge_multi_key, "\n")
