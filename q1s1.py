digit_arr = [0, 1, 2, 3, 4, 5, 6, 6, 7]
free_digits = digit_arr
isValid_dict = {
    "a": lambda a: a != 0 and a in free_digits,  # [isvalid, possval1, possval2 ... possvaln]
    "b": lambda b: b in free_digits,
    "c": lambda c: c != 0 and c in free_digits,
    "d": lambda d: d + currVals_dict["a"] < 10 and d != 0 and d in free_digits,
    "e": lambda e: e in free_digits,
    "f": lambda f: f + currVals_dict["c"] < 10 and f != 0 and f in free_digits,
    "g": lambda g: g != 0 and g in free_digits,
    "h": lambda h: h in free_digits,
    "i": lambda i: i != 0 and i in free_digits,
}  # important to loop through in order
defaultCurrVals_dict = {
    "a": -1,
    "b": -1,
    "c": -1,
    "d": -1,
    "e": -1,
    "f": -1,
    "g": -1,
    "h": -1,
    "i": -1,
}
currVals_dict = defaultCurrVals_dict
# rules:
# abc + def = ghi
# cba + fed = ihg
# ans = g * h * i
# a + d < 10
# c + f < 10
# a, c, d, f, i, g != 0


def findPossValues():
    possVals_dict = {
        "a": [],
        "b": [],
        "c": [],
        "d": [],
        "e": [],
        "f": [],
        "g": [],
        "h": [],
        "i": [],
    }
    for letter in possVals_dict.keys():
        for digit in free_digits:
            if isValid_dict[letter](digit):
                possVals_dict[letter].append(digit)
    return possVals_dict

def test():
    numabc = int(str(currVals_dict["a"])+str(currVals_dict["b"])+str(currVals_dict["c"]))
    numdef = int(str(currVals_dict["d"]) + str(currVals_dict["e"]) + str(currVals_dict["f"]))
    numghi = int(str(currVals_dict["g"]) + str(currVals_dict["h"]) + str(currVals_dict["i"]))
    numcba = int(str(currVals_dict["c"]) + str(currVals_dict["b"]) + str(currVals_dict["a"]))
    numfed = int(str(currVals_dict["f"]) + str(currVals_dict["e"]) + str(currVals_dict["d"]))
    numihg = int(str(currVals_dict["a"]) + str(currVals_dict["b"]) + str(currVals_dict["c"]))
    if numabc + numdef == numghi and numcba + numfed == numihg:
        return True
    return False

# while not test:
# reset currValues and freedigits
# starting with num with smallest poss values loop through poss values
# assign each to curr values and remove from free digits
# reassess poss for each,
# repeat until none = -1