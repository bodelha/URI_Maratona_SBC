out = []
def remove_pair(seq):
    clean_seq = seq
    for pair in ["BS", "SB", "CF", "FC"]:
        clean_seq = clean_seq.replace(pair, "")
    if clean_seq == seq:
        return clean_seq
    else:
        return remove_pair(clean_seq)


while True:
    try:
        seq = input()
        res = remove_pair(seq)
        out.append((len(seq)-len(res))//2)    

    except EOFError:
        break
    
print (*out, sep="\n")