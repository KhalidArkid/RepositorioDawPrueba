def son_oposats(s1, s2):
    # Si ambdues cadenes estan buides, retorna False
    if not s1 and not s2:
        return False
    
    # Comprova la longitud de les cadenes
    if len(s1) != len(s2):
        return False
    
    for c1, c2 in zip(s1, s2):
        # Si les lletres són iguals en majúscula o minúscula, no són oposades
        if c1.lower() == c2.lower():
            if c1.islower() == c2.isupper() or c1.isupper() == c2.islower():
                continue
            else:
                return False
        else:
            return False
    
    # Si ha passat totes les comprovacions, les cadenes són oposades
    return True

# Proves amb els exemples donats
print(son_oposats("ab", "AB"))        # true
print(son_oposats("aB", "Ab"))        # true
print(son_oposats("aBcd", "AbCD"))   # true
print(son_oposats("AB", "Ab"))       # false
print(son_oposats("", ""))                 # false
