"""A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled."""


def angry_professor(threshhold, student_timing):
    # Get count of numbers from array where number <= 0
    result = len([x for x in student_timing if x <= 0])

    # If number >= a ? NO : YES
    if result >= threshhold:
        return "NO"
    return "YES"

    # Python style
    # return "NO" if result >= threshhold else "YES"
