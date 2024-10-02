# StudentPerformanceAnalyzer

StudentPerformanceAnalyzer is a Python tool designed to analyze and visualize student performance data across multiple semesters. It provides insights into average scores for different subjects and overall performance trends.

## Features

- Calculate and display semester averages for each subject
- Generate a bar chart comparing subject averages across semesters
- Create a line plot showing overall average performance trend
- Print overall averages by semester

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/StudentPerformanceAnalyzer.git
   ```
2. Navigate to the project directory:
   ```
   cd StudentPerformanceAnalyzer
   ```
3. Install the required packages:
   ```
   pip install pandas numpy matplotlib
   ```

## Usage

1. Prepare your CSV file with student scores. The file should have the following structure:
   - Each row represents one student in one semester
   - Columns should be named with subject names
   - Values should be the scores of that student in that subject

2. Update the CSV file name in the main section of the script:
   ```python
   analyzer = StudentPerformanceAnalyzer("your_file_name.csv")
   ```

3. Run the script:
   ```
   python student_performance_analyzer.py
   ```

4. The script will generate:
   - A console output with semester averages and overall averages
   - A bar chart saved as 'subject_averages_by_semester.png'
   - A line plot saved as 'overall_average_by_semester.png'

## Class Structure

The `StudentPerformanceAnalyzer` class contains the following main methods:

- `__init__(self, csv_file)`: Initializes the analyzer with the given CSV file
- `calculate_semester_averages()`: Calculates average scores for each subject in each semester
- `print_semester_averages()`: Prints the average scores in a tabular format
- `create_subject_averages_bar_chart()`: Creates and saves a bar chart of subject averages
- `create_overall_average_line_plot()`: Creates and saves a line plot of overall averages
- `print_overall_averages()`: Prints the overall averages by semester
- `run_code()`: Executes all the above methods in sequence

