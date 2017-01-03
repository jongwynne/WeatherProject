def calc_vat(inputprice, vatrate):
    """calculate the varying rate vatrate
    on a net price"""
    answer = inputprice * (vatrate + 1)
    return answer


def total_basket_value(*items):
    """calculate the total value of basket items"""
    total = sum(items)
    print items
    return total


def total_basket_items(**items):
    """from a dict calculate total quant"""
    totalqty = 0
    for prodid, qty in items.iteritems():
        totalqty += qty
    return totalqty


