import pandas

visitors = [1235, 6424, 9345, 6518, 6513]
errors = [25, 11, 45, 3, 12]

def calc_mean(number_list):
    total = 0
    # This is a terrible idea. The general idea of emulate sum() using a list comprehension goes against the whole purpose of a list comprehension. You should not use a list comprehension in this case (sum a list of integers/float).
    [total := total + num for num in number_list]
    # print(total)

    return total/len(number_list)


# generate the data frame
df = pandas.DataFrame({"Visitors": visitors, "Errors": errors}, index=["Mon", "Tues", "Wed", "Thurs", "Fri"])

print(df)

# mean method
print(df["Errors"].mean())

# calc_mean for comparison
print(calc_mean(errors))
