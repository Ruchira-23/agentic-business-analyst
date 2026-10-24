from analytics import percent_change
from datatools import get_revenue

june_rev= get_revenue('June','Home Care')
july_rev= get_revenue('July', 'Home Care')

if june_rev is not None and july_rev is not None:
    change = percent_change(june_rev,july_rev)
    if change is None:
        print(f"Revenue changed from ${june_rev:,} to ${july_rev:,}."
                "Percentage change is undefined because baseline is zero")
    elif change>0:
        print(f"Home Care revenue increased by {change:.1f}% from June to July")
    elif change<0:
        print(f"Home Care revenue decreased by {abs(change):.1f}% from June to July")
    else:
        print('No change in revenue from June to July')
else:
    change = None
    print ('Cannot calculate revenue change: data is missing.')

