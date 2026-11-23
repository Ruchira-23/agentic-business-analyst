def percent_change(old_val: float|None , new_val: float|None )-> float | None:
    """
    Calculate the percentage change between an old and new value.

    Args:
        old_val: Original numeric value.
        new_val: Updated numeric value.

    Returns:
        Percentage change as a float, or None if old_val is zero or either of the values are None.
    """

    print(f"🔧 TOOL EXECUTED: percent_change(old_val={old_val}, new_val={new_val})")

    if old_val is None or new_val is None or old_val==0:
       return None


    return ((new_val-old_val)/old_val )* 100

