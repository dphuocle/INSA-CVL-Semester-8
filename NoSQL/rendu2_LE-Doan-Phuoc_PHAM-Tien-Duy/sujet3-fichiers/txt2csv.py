import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-input', type=str, help='input file', required=True)
parser.add_argument('-output', type=str, help='output file', required=True)

args = parser.parse_args()
# Replace 'your_file.txt' with the path to your text file
input_file = args.input
# Replace 'output_file.csv' with the desired path for your CSV file
output_file = args.output

# Open the text file for reading and the CSV file for writing
with open(input_file, 'r') as txtfile, open(output_file, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Optionally write a header row, if you want
    # csvwriter.writerow(['Column1', 'Column2'])
    
    # Read each line in the text file
    for line in txtfile:
        # Split the line into fields using the space as a delimiter
        fields = line.strip().split(' ')
        
        # Write the fields to the CSV file
        csvwriter.writerow(fields)

print('Conversion completed successfully.')