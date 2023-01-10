from csv import DictReader
# ordered dict 
with open('filec.csv','r') as f:
    csv_reader=DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row['email'])