def remove_duplicates(num):
    result = []
    for item in num:
        if item not in result:
            result.append(item)
    return result