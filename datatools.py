import csv
def get_revenue(month: str, dept: str) -> int | None:
    """
    Retrieve revenue for a given month and department
    from the business_data.csv dataset.

    Args:
        month: Month name, such as June or July.
        dept: Department name, such as Home Care or Rehab.

    Returns:
        Revenue as an integer, or None if no matching data exists.
    """

    print(f"🔧 TOOL EXECUTED: get_revenue(month={month}, dept={dept})")

    with open('business_data.csv', mode='r') as file:
        csv_reader= csv.DictReader(file) #create dictionary reader

        # data_list = [] #list to store dictionaries
        # for row in csv_reader:
        #     data_list.append(row)

        for data in csv_reader:
            if month== data['month'] and dept == data['department']:
                return int(data['revenue'])
        
        return None
    

# rev = get_revenue('August','Home Care')
# print(rev)