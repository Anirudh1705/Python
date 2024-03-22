def sum_and_average_digits(s):
    total = 0
    count = 0

    for i in s:
        if i.isdigit():
            total += int(i)
            count += 1

    if count == 0:
        return "No digits found"

    average = total / count
    return f"Sum: {total}, Average: {average}"

# Test the function
s = "Hello123World456"
print(sum_and_average_digits(s))