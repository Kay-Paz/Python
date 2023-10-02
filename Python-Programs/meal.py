# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
# Wouldn’t it be nice if you had a program that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
# If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the
# corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    user_time = input("What time is it? Use 24-hour time like so: 9:00 or 13:00 ").strip()
    convert(user_time)
    mealtime(dec_time)

def convert(time):
    # convert user's time to a list of integers (12:15 = [12, 15])
    time_list = time.split(":")
    time_conv = list(map(int, time_list))
    # convert list of integers to hours and minutes, add them together for time in decimal (12:15 -> [12, 15] -> 12.25)
    hours = time_conv[0]
    min_conv = time_conv[1]
    minutes = min_conv / 60
    global dec_time
    dec_time = hours + minutes
    return dec_time

def mealtime(time):
    if dec_time >= 7.0 and dec_time <= 8.0:
        print("breakfast time")
    elif dec_time >= 12.0 and dec_time <= 13.0:
        print("lunch time")
    elif dec_time >= 18.0 and dec_time <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()