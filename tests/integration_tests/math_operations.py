def is_in_accuracy(number, accuracy):
    number_str = str(int(number))[::-1]
    accuracy_str = str(int(accuracy))[::-1]
    index = 0
    while accuracy_str[index] == '0':
        if index < len(number_str):
            if number_str[index] != '0':
                return False
        index += 1
    return True
