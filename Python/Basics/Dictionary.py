def sw(ar):
    sr = {
        0: "Zero",
        1: "one",
        2: "Two",
        3: "Three",
        4: "Foure",
        5: "Five",
        6: "Six",
        7: "SEVEN",
        8: "Eight",
        9: "Nine",
    }
    return sr.get(ar, "nothing")


if __name__=="__main__":
    ar=8
    print(sw(ar))