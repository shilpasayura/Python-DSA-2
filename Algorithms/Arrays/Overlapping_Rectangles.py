# Given two rectanges, determine if they overlap
# If they overlap, return with rectangle area

# Take the rectangle properties as x1,y1,x2,y2
rectangle1 = map(int, raw_input().split())
rectangle2 = map(int, raw_input().split())


def overlapping_area(r1, r2):

    # Calculate the resulting x-coordinate
    rx = min(r1[2], r2[2]) - max(r1[0], r2[0])

    # Calculate the resulting y-coordinate
    ry = min(r1[3], r2[3]) - max(r1[1], r2[1])

    # return the resulting area if the values are positive
    if rx >= 0 and ry >= 0:
        return rx*ry


print overlapping_area(rectangle1, rectangle2)
