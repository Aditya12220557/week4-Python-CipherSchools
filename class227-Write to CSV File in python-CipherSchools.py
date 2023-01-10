from csv import writer
with open('file3.csv','w') as f:
    csv_writer=writer(f)
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['mohit','INDIA'])
    # csv_writer.writerow(['Harshit','INDIA'])
    csv_writer.writerows([['name','country'],['mohit','INDIA'],['harshit','INDIA']])