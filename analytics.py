def percent_change(old_val, new_val):
    if old_val!=0: 
     change = ((new_val-old_val)/old_val )* 100
    elif old_val==0:
       change=None
    return change

print(percent_change(20,10))  