def trend (xlist,ylist):
    n = len(xlist)-1
    xAverage = sum(xlist)/n
    yAverage = sum(ylist)/n
    
    aTop = sum([((xlist[i]-xAverage)*(ylist[i]-yAverage)) for i in range(0,n)])
    aBot = sum([(xlist[i]-xAverage)**2 for i in range(0,n)])
    a = aTop/aBot
    b = yAverage-a*xAverage
    
    return [a,b]