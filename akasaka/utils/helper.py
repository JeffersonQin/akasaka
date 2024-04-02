def make_consecutive_pairs(lst):
    """Make consecutive pairs from a list

    Args:
        lst (list): list to make pairs from

    Returns:
        list: list of consecutive pairs
    """
    return list(zip(lst[:-1], lst[1:]))
