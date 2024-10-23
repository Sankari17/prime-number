import csv

def write_dicts_to_csv(file_path, dicts):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = dicts[0].keys() if dicts else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in dicts:
            writer.writerow(row)

# Example usage:
csv_file_path = 'output.csv'
dicts_list = [
    {'Name': 'Alice', 'Age': 30},
    {'Name': 'Bob', 'Age': 25},
    {'Name': 'Charlie', 'Age': 35}
]

write_dicts_to_csv(csv_file_path, dicts_list)
print("Data has been written to", csv_file_path)
