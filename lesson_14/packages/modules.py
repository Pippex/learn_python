def position_string(string, item_searched, only_item=False):
    item_positions = []
    for i in range(len(string)):
        if string[i] == item_searched:
            if only_item and i == len(string) - 1 and string[i-1] == " ":
                item_positions.append(i)
            elif only_item and i == 0 and string[i+1] == " ":
                item_positions.append(i)
            elif only_item and string[i-1] == string[i+1] == " ":
                item_positions.append(i)
            elif not only_item:
                item_positions.append(i)
    
    return item_positions
