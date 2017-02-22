
# 2^n -1 moves needed where n = number of discs
numberOfSteps = 0

def Tower(n, SourceRod, DestinationRod,AuxiliaryRod):

    if n == 0:
        global numberOfSteps
        numberOfSteps += 1
        return
    Tower(n - 1, SourceRod, AuxiliaryRod, DestinationRod)
    print("Move the disk "+ str(n)+ " from " + str(SourceRod) + " to " + str(DestinationRod)
          + "current move number: " + str(numberOfSteps) )
    Tower(n - 1, AuxiliaryRod, DestinationRod, SourceRod)


print(Tower(5, 'S', 'D', 'A'))
print(numberOfSteps)