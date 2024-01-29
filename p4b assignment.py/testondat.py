def calculate_sum(sales):
    driver_sums = {}
    for sale in sales:
        driver, amount = sale
        if driver in driver_sums:
            driver_sums[driver] += amount
        else:
            driver_sums[driver] = amount
    return driver_sums

sales = [['DRI04', 6.38], ['DRI05', 25.50], ['DRI01', 25.65], ['DRI05', 19.35], ['DRI02', 26.32], ['DRI05', 27.05], ['DRI01', 9.60], ['DRI03', 9.22], ['DRI03', 9.22], ['DRI04', 14.53], ['DRI02', 19.08], ['DRI02', 24.61], ['DRI03', 12.29], ['DRI05', 8.96], ['DRI01', 9.52], ['DRI04', 13.66], ['DRI02', 19.94], ['DRI03', 23.67], ['DRI04', 29.59], ['DRI02', 20.00], ['DRI03', 15.22]]

sales_sums = calculate_sum(sales)

for driver, amount in sales_sums.items():
    print(f"The total sales for {driver} is {amount}.")