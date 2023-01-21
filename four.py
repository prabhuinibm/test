element_list = [10,20,31,56,78]
for i in element_list:
    print(i)
#if odd is double and even is square
    if (i %2 ==0):
        print(i*i)
    else:
        print(i*2)
# div 3 should mul by 9 , if div by 4 mul by 16
for i in element_list:
    if i % 3 == 0:
        print(f"{i} {i*9}, CSP your answer")
    elif i % 4 == 0:
        print(f"{i} {i*16}, There you go CSP")
    