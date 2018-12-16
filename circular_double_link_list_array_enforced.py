link1 = []
link2 = []
link3 = []
link4 = []
link5 = []
link1.append(link5)
link2.append(link1)
link3.append(link2)
link4.append(link3)
link5.append(link4)
link1.append('val1')
link2.append('val2')
link3.append('val3')
link4.append('val4')
link5.append('val5')
link1.append(link2)
link2.append(link3)
link3.append(link4)
link4.append(link5)
link5.append(link1)

# print(link1[2][2][2][0][1])