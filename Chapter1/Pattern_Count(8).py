def Pattern_Count(Text,Pattern):
    k = len(Pattern)
    num = 0
    for i in range(len(Text)-k+1):
        if Text[i:i+k] == Pattern:
            num+=1
    return num

Pattern_Count('ACAACTATGCATACTATCGGGAACTATCCT','ACTAT')
