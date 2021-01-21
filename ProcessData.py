# Converting given data to format, src: {[[dest, cost]]} and returning the dictionary
# Reference https://stackoverflow.com/a/3199256/5990108
def prepareData(data):
    dic = {}
    for line in data:
        if line == 'END OF INPUT':
            return dic

        else:
            # Splitting the input by keeping a blank space as the splitting criteria
            d = line.split(' ')

            # If the src is not in dictionary create the entry and add the cost and destination
            if d[0] not in dic:
                dic[d[0]] = [[d[1], float(d[2])]]
            else:
                # If the entry already exists then append to the list associated with the key
                dic[d[0]].append([d[1], float(d[2])])
            if d[1] not in dic:
                # Here we do the same as above for the situation, A -> B is also B -> A
                dic[d[1]] = [[d[0], float(d[2])]]
            else:
                # If the entry already exists then append the list associated with the key
                dic[d[1]].append([d[0], float(d[2])])


# Converting heuristic data to format, state: cost and returning the dictionary
def prepareHeuristicData(data):
    dic = {}
    for line in data:
        if line == 'END OF INPUT':
            return dic
        else:
            d = line.split(' ')
            dic[d[0]] = float(d[1])
