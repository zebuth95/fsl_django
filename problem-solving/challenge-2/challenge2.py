def dice_faces_calculator(dice1: int, dice2: int, dice3: int) -> int:
    aux_list = [dice1, dice2, dice3]
    if len(list(filter(lambda x: 1 <= x <= 6, aux_list))) != 3:
        raise Exception("Dice out of number range")
    aux_set = {dice1, dice2, dice3}
    if len(aux_set) == 1:
        return list(aux_set)[0] * 3
    elif len(aux_set) == 3:
        return max(aux_set)
    else:
        for i in aux_set:
            if aux_list.count(i) == 2:
                return i * 2
    return 0
