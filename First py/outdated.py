def month():
    return [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
    ]

monthList = month()

def input_date():
    while True:
        date = input("Date: ")

        # Attempt to parse as MM/DD/YYYY format
        try:
            month, day, year = map(int, date.split('/'))
            if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                return month, day, year
        except ValueError:
            pass

        # Attempt to parse as Month DD, YYYY format
        try:
            parts = date.split()
            if len(parts) == 3:
                month_str = parts[0].capitalize()
                day = parts[1]

                # Ensure the last character of day is a comma
                if day[-1] != ',':
                    raise ValueError

                day = day.rstrip(',')
                year = parts[2]

                if month_str in monthList and day.isdigit() and year.isdigit():
                    if 1 <= int(day) <= 31 and int(year) > 0:
                        return monthList.index(month_str) + 1, int(day), int(year)
        except (ValueError, IndexError):
            pass

        print("Invalid date format. Please use MM/DD/YYYY or Month DD, YYYY.")

if __name__ == "__main__":
    MM, DD, YYYY = input_date()
    print(f"{YYYY}-{MM:02d}-{DD:02d}")
