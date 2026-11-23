import csv
revenue_cache = {}
def get_revenue(month: str, dept: str) -> dict:
    """
    Retrieve revenue for a given month and department
    from the business_data.csv dataset.

    Args:
        month: Month name, such as June or July.
        dept: Department name, such as Home Care or Rehab.

    Returns:
        Returns a dictionary containing status, requested month, department, and revenue. Includes an explanatory message when no matching record exists
    """

    print(f"🔧 TOOL EXECUTED: get_revenue(month={month}, dept={dept})")

    cache_key = (month, dept)
    if cache_key in revenue_cache:
        print("CACHE HIT")
        return revenue_cache[cache_key]
    

    with open('business_data.csv', mode='r') as file:
        csv_reader= csv.DictReader(file) #create dictionary reader


        for data in csv_reader:
            if month== data['month'] and dept == data['department']:
               # returning a dictionary to tell Gemini SDK that we have or do not have the requested data to avoid multiple tool calls
                result= {
                "status": "success",
                "revenue": int(data['revenue']),
                "month" : month,
                "department" : dept,
                }
                revenue_cache[cache_key]=result
                return result

        

        result= {
                "status": "not_found",
                "month" : month,
                "department" : dept,
                "revenue": None,
                "message": "No matching revenue record found."
            }
        revenue_cache[cache_key]=result
        return result
    
