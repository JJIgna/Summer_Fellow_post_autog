"""
Query Parse:
    function for parsing an .sql containing multiple queries into separate queries
parameters : path - path to .sql file to be parsed
returns : this function is a generator. calling .__next__() will give the next query 
"""


def query_parse(path):
    # buffer to hold queries as they are built
    buf = []


    # booleans
    seen_dash = False
    seen_slash = False
    seen_star = False
    ignore = False #used when encountering a comment
    in_multiline = False

    # parser
    with open(path) as q:
        while c := q.read(1):

            # identify if inside comment
            if ignore:
                if in_multiline:
                    if c == "*":
                        seen_star = True
                        continue
                    if c == "/":
                        if seen_star:
                            ignore = False
                            in_multiline = False
                            continue
                    continue
                if c == "\n":
                    ignore = False
                    buf.append(c)
                continue

            # identify single line comment
            if c == "-":
                if seen_dash:
                    buf.pop()
                    ignore = True
                    continue
                seen_dash = True
                buf.append(c)
                continue

            # identify multiline comment
            if c == "/":
                seen_slash = True
                buf.append(c)
                continue
            if c == "*":
                if seen_slash:
                    buf.pop()
                    in_multiline = True
                    ignore = True
                    continue
                buf.append(c)
                continue

            # identify query end
            if c == ";":
                buf.append(c)
                yield ''.join(buf)
                buf.clear()
                continue

            # if no identifiers trigger, good to append and clear booleans
            buf.append(c)
            seen_dash = False
            seen_slash = False
            seen_star = False