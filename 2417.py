cv, ce, cs, fv, fe, fs = map(int, input().split())

cp = cv*3 + ce
fp = fv*3 + fe

if cp > fp or (cp == fp and cs > fs):
    print ("C")
elif fp > cp or (cp == fp and cs < fs):
    print ("F")
else:
    print  ("=")