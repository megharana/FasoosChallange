name1 = "rebel"
name2 = "reebeel"


def solution(name1, name2):
    """
    func description: operates on given arguments depending on the possibility of operations
    Return value description : N/A (prints the resultant strings after operations)
    """
    if (check_feasibility(name1, name2)):
        dict_name1 = get_op_possiblity(name1)
        dict_name2 = get_op_possiblity(name2)
        while (name1 != name2 and check_possibility(name1, name2)):
            limit = min(len(name1), len(name2))
            for x in range(0, 5):
                print(x)
                if (name1[x] != name2[x]):
                    if (dict_name1[x][1]):
                        name1 = name1[:x] + name1[x + 1:len(name1)]
                    elif (dict_name2[x][1]):
                        name2 = name2[:x] + name2[x + 1:len(name2)]

    print(name1, name2)


def check_possibility(name1, name2):
    """
    func description: checks whether any one input strings are having adjacent repeatative characters
    Return value description : Boolean
    """
    if (checks_rep_adjacent(name1) or checks_rep_adjacent(name2)):
        return True
    else:
        return False


def check_feasibility(name1, name2):
    """
    func description: checks whether input strings are sharing same set of characters
    Return value description : Boolean

    param name1: 'name1'  --> string's distinct characters are matched with other argument's character set
    type name1: string

    param name1: 'name2'  --> string's distinct characters are matched with other argument's character set
    type name1: string
    """
    return set(name1).symmetric_difference(set(name2)) == set()


def get_op_possiblity(name):
    """
    func description: returns dictionary with index as key and operations list as value  
    Return value description : dict{ int : [boolean] }

    param name1: 'name'  --> operates on the string and returns dictionary
    type name1: string

    """
    name_dict = {}
    list_op = []
    list_op.append(True)
    if (name[1] == name[0]):
        list_op.append(True)
    else:
        list_op.append(False)
    name_dict.update({0: list_op})

    for x in range(1, len(name) - 1):
        list_op = []
        list_op.append(True)
        if (name[x] == name[x - 1] or name[x] == name[x + 1]):
            list_op.append(True)
        else:
            list_op.append(False)

        name_dict.update({x: list_op})
    list_op = []
    list_op.append(True)

    if (name[len(name) - 1] == name[len(name) - 2]):
        list_op.append(True)
    else:
        list_op.append(False)

    name_dict.update({len(name) - 1: list_op})
    return name_dict


def checks_rep_adjacent(check_string):
    """
    func description: checks whether input string is having adjacently repeatative characters
    Return value description : Boolean

    param name1: 'check_string'  --> string to check ajacent repeatative characters
    type name1: string

    """
    count = {}

    for s in check_string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    list_diff_adjacent_index = []
    for key in count:
        if count[key] > 1:
            # Start with this value.
            location = -1
            index = 0

            while True:
                # Advance location by 1.
                location = check_string.find(key, location + 1)

                # Break if not found.
                if location == -1: break

                # Display result.
                if (index != 0):
                    list_diff_adjacent_index.append(location - index)

                index = location
    if (list_diff_adjacent_index.__contains__(1)):
        return True
    else:
        return False


solution(name1, name2)