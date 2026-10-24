import csv
def get_revenue(month, dept):

    with open('business_data.csv', mode='r') as file:
        csv_reader= csv.DictReader(file) #create dictionary reader

        # data_list = [] #list to store dictionaries
        # for row in csv_reader:
        #     data_list.append(row)

        for data in csv_reader:
            if month== data['month'] and dept == data['department']:
                return int(data['revenue'])
        
        return None
    

rev = get_revenue('August','Home Care')
print(rev)