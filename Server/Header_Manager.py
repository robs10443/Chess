def convertData(header_data):
    flag = int(header_data[0])
    starting_row = int(header_data[1])
    starting_col = int(header_data[2])
    ending_row = int(header_data[3])
    ending_col = int(header_data[4])

    move = header_data[5]

    promotion = ""
    if(len(header_data) > 6):
        promotion = header_data[6:]

    return flag,starting_row,starting_col,ending_row,ending_col,move,promotion

def convertDataToHeader(flag,starting_row,starting_col,ending_row,ending_col,move,promotion):
    return str(flag) + str(starting_row) + str(starting_col) + str(ending_row) + str(ending_col) + move + promotion
