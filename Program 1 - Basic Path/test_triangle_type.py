import csv
import subprocess

def read_test_cases_from_csv(file_path):
    test_cases = []
    test_results = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                test_cases.append(row[0])
                test_results.append(row[1])
    return test_cases, test_results

def compare_results(from_test, from_set):
    return from_set in from_test

def test_triangle_type():
    test_cases, test_results = read_test_cases_from_csv("basic_path_test_case.csv")

    results = []
    for case in test_cases:
        process = subprocess.Popen(['python', 'triangle_type.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        output, _ = process.communicate(input=case)
        last_line = output.strip().splitlines()[-1]  # Extracting the last line
        results.append(last_line)

    with open("basic_path_test_results.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Input Data", "Result", "Expected Result", "Is result the same"])
        for case, result, test_result in zip(test_cases, results, test_results):
            writer.writerow([case, result, test_result, compare_results(result, test_result)])

if __name__ == "__main__":
    test_triangle_type()
