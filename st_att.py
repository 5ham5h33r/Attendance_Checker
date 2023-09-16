import re
import streamlit as st

# Define the calculate_attendance function


def calculate_attendance(subjects, text):
    # Initialize dictionaries to store counts for each subject
    subject_counts = {subject: {"P": 0, "U": 0} for subject in subjects}

    # Iterate through subjects and count attendance for each
    for subject in subjects:
        # Regular expression pattern to find lines containing the subject followed by "P" or "U"
        pattern = fr"\d+\s+70092000111\s+{re.escape(subject)}.*[PU]"

        # Find all matches for the current subject
        matches = re.findall(pattern, text)

        # Update counts for the current subject
        for match in matches:
            status = match[-1]
            if status == "P":
                subject_counts[subject]["P"] += 1
            elif status == "U":
                subject_counts[subject]["U"] += 1

    # Create a dictionary to store results
    results = {}

    # Calculate counts and percentages for each subject
    for subject in subjects:
        count_p = subject_counts[subject]["P"]
        count_u = subject_counts[subject]["U"]
        total_hours = count_p + count_u
        if total_hours > 0:
            attendance_percentage = (count_p / total_hours) * 100
        else:
            attendance_percentage = 0

        results[subject] = {
            "P": count_p,
            "U": count_u,
            "Percentage of Hours Attended": attendance_percentage,
        }

    return results

# Streamlit app


def main():
    st.title("Attendance Calculator")

    # Text input for user to enter the attendance data
    text = st.text_area("Enter the attendance data:")

    # Button to trigger the calculation
    if st.button("Calculate Attendance"):
        subjects_to_check = [
            "Big Data Analytics",
            "Advanced DBMS",
            "DevOps",
            "Management Through Movies",
            "MLOps",
            "Neural Networks and Deep Learning",
            "Speech and NLP",
        ]

        # Call the calculate_attendance function
        attendance_results = calculate_attendance(subjects_to_check, text)

        # Display the results
        for subject, results in attendance_results.items():
            st.subheader(subject)
            st.write(
                f"Total number of hours attended: {results['P']}/{results['P'] + results['U']}")
            st.write(
                f"Percentage: {results['Percentage of Hours Attended']:.2f}%")
            st.write("---")


if __name__ == "__main__":
    main()
