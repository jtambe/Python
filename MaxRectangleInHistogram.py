
def MaxRectangleAreaInHistogram(histogram):
    stack = []
    maxArea, area, i = 0,0,0

    while(i < len(histogram)):
        if(len(stack) ==0 or  histogram[stack[-1]] <= histogram[i]):
            stack.append(i)
            i += 1
        else:
            top = stack.pop()

            if(len(stack) == 0):
                area = histogram[top] * i
            else:
                area = histogram[top]*(i - stack[-1] -1)

            if area > maxArea:
                maxArea = area


    while( len(stack) > 0):
        top = stack.pop()

        if( len(stack) == 0):
            area = histogram[top] * i
        else:
            area = histogram[top] * (i - stack[-1] - 1)

        if area > maxArea:
            maxArea = area


    return maxArea


def main():
    histogram = [4,2,3,5,7,6,5,3,5]
    print(MaxRectangleAreaInHistogram(histogram)) #21

    histogram = [4, 2, 3, 5, 7, 6]
    print(MaxRectangleAreaInHistogram(histogram)) #15


if __name__ == "__main__":
    main()


#credits
#https://www.youtube.com/watch?v=ZmnqCZp9bBs
# video has for loop implemented without i++ at the end. Which is equivalent of while loop as in here
# http://cs-technotes.blogspot.com/2010/12/largest-rectangle-of-histogram.html