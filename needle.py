junk = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
needle = "needle"
found = ""

def findNeedle():
    if needle in junk:
        found = f"found the needle at position {junk.index(needle)+1}"
        print(found)
        return found
findNeedle()