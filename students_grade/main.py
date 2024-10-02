import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class StudentPerformanceAnalyzer:
    def __init__(self, csv_file):
        """
        Initialize StudentPerformanceAnalyzer with a CSV file.

        Args:
            csv_file (str): the path to the CSV file to be analyzed.

        The CSV file should contain student scores with each row representing one student in one semester.
        The columns should be named with the subject names, and the values should be the scores of that student in that subject.
        """
        self.data = pd.read_csv(csv_file)
        self.numeric_data = self.data.select_dtypes(include=['number'])
        self.semesters = ['Semester 1', 'Semester 2', 'Semester 3', 'Semester 4']
        self.semester_averages = None

    def calculate_semester_averages(self):
        """
        Calculate average scores for each subject in each semester.

        Each row in the `numeric_data` is assumed to contain scores for one student in one semester.
        The average scores for each subject in each semester are calculated and stored in
        `semester_averages`.

        The `semester_averages` DataFrame has the semesters as index and the subjects as columns.
        The values in the DataFrame are the average scores for each subject in each semester.
        """
        self.semester_averages = pd.DataFrame(index=self.semesters, columns=self.numeric_data.columns)
        for i, semester in enumerate(self.semesters):
            start = i * 5
            end = start + 5
            self.semester_averages.loc[semester] = self.numeric_data.iloc[start:end].mean()
        self.semester_averages = self.semester_averages.round(2)
        self.semester_averages['Overall Average'] = self.semester_averages.mean(axis=1)

    def print_semester_averages(self):
        """
        Print the average scores for each subject in each semester.

        The average scores for each subject in each semester are printed in a tabular form.
        The table has the semesters as index and the subjects as columns.
        The values in the table are the average scores for each subject in each semester.
        """
        print("Semester Averages:")
        print(self.semester_averages)

    def create_subject_averages_bar_chart(self):
        """
        Create a bar chart of average scores for each subject by semester.

        This method first creates a figure of specified size, then iterates over the subjects
        and plots a bar for each subject in each semester. The x-axis represents the semesters,
        and the y-axis represents the average scores. The legend shows which bar corresponds
        to which subject. The chart is then saved as 'subject_averages_by_semester.png'.

        """
        plt.figure(figsize=(12, 6))
        bar_width = 0.15
        index = np.arange(len(self.semesters))

        for i, subject in enumerate(self.numeric_data.columns):
            plt.bar(index + i * bar_width, self.semester_averages[subject],
                    bar_width, label=subject, alpha=0.8)

        plt.xlabel('Semesters')
        plt.ylabel('Average Scores')
        plt.title('Average Subject Scores by Semester')
        plt.xticks(index + bar_width * 2, self.semesters)
        plt.legend()
        plt.tight_layout()
        plt.savefig('subject_averages_by_semester.png')
        print("\nBar chart has been saved as 'subject_averages_by_semester.png'")

    def create_overall_average_line_plot(self):
        """
        Create a line plot of the overall average scores for each semester.

        This method first creates a figure of specified size, then plots a line with
        circle markers for the overall average scores for each semester. The x-axis
        represents the semesters, and the y-axis represents the overall average scores.
        The grid is turned on for easier comparison of the scores. The chart is then
        saved as 'overall_average_by_semester.png'.

        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.semesters, self.semester_averages['Overall Average'], marker='o')
        plt.xlabel('Semesters')
        plt.ylabel('Overall Average Score')
        plt.title('Overall Average Score by Semester')
        plt.grid(True)
        plt.savefig('overall_average_by_semester.png')
        print("Line plot has been saved as 'overall_average_by_semester.png'")

    def print_overall_averages(self):
        print("\nOverall Averages by Semester:")
        print(self.semester_averages['Overall Average'])

    def run_code(self):
        """
        Run the code to calculate the semester averages, print the semester averages,
        create the subject averages bar chart, create the overall average line plot,
        print the overall averages, and show the plots.

        This method is a convenience method to run all the relevant methods in the
        correct order. It should be called after the instance of the class has been
        created with a valid CSV file.

        """
        self.calculate_semester_averages()
        self.print_semester_averages()
        self.create_subject_averages_bar_chart()
        self.create_overall_average_line_plot()
        self.print_overall_averages()
        plt.show()


if __name__ == "__main__":
    analyzer = StudentPerformanceAnalyzer("student_scores_random_names.csv")
    analyzer.run_code()
