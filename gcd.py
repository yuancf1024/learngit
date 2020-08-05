def euclid(p, q):
    if q == 0:
        return p
    r = p % q
    return euclid(q, r)

if __name__ == "__main__":
    print(euclid(15,75))