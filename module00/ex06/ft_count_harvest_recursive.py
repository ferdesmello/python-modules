def ft_count_harvest_recursive(days=None, day=1):
    if days is None:
        days = int(input("Days until harvest: "))
    if day <= days:
        print(f"Day {day}")
        ft_count_harvest_recursive(days, day + 1)
    else:
        print("Harvest time!")
