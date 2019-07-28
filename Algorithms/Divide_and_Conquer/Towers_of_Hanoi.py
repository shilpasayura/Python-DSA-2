from_peg = 'S'
to_peg = 'D'
aux_peg = 'T'

n = int(raw_input("Enter Number of disks: "))


def TowersofHanoi(n, from_peg, to_peg, aux_peg):
    if n==1:
        print "Move peg from %s peg to %s peg" % (from_peg,  to_peg)
        return
    TowersofHanoi(n-1, from_peg, aux_peg, to_peg)
    print "Move peg from %s peg to %s peg" % (from_peg, to_peg)
    TowersofHanoi(n-1, aux_peg, to_peg, from_peg)


TowersofHanoi(n, from_peg, to_peg, aux_peg)