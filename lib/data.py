import base64

class Data(bytearray):
    # Operator Overloads
    def __xor__(self, other):
        if type(other) is not Data:
            return self.__xor__( Data(other) )
        ret = Data( len(self) )
        for i in range( len(self) ):
            ret[i] = self[i]^other[i%len(other)]
        return ret
    def __and__(self, other):
        if type(other) is not Data:
            return self.__xor__( Data(other) )
        ret = Data( len(self) )
        for i in range( len(self) ):
            ret[i] = self[i]&other[i%len(other)]
        return ret
    def __or__(self, other):
        if type(other) is not Data:
            return self.__xor__( Data(other) )
        ret = Data( len(self) )
        for i in range( len(self) ):
            ret[i] = self[i]|other[i%len(other)]
        return ret

    # General Functions
    def split(self, other):
        if type(other) is not Data:
            return self.split( Data(other) )
        return [ Data(x) for x in bytearray.split(self, other) ]
    def chunk(self, bs):
        return [ Data(self[i:i+bs]) for i in range(0, len(self), bs) ]
    def transpose(self, bs):
        ret = [ Data() for i in range(bs) ]
        for i in range( len(self) ):
            ret[i%bs].append( self[i] )
        return ret
    def hammingbytes(self, other):
        if type(other) is not Data:
            return self.hammingbytes( Data(other) )
        assert(len(self)==len(other))
        diff = 0
        for c1, c2 in zip(self, other):
            if c1 != c2:
                diff += 1
        return diff
    def hammingbits(self, other):
        if type(other) is not Data:
            return self.hammingbits( Data(other) )
        assert(len(self)==len(other))
        diff = 0
        for c1, c2 in zip(self, other):
            diff += popcount( c1^c2 )
        return diff

    # General representations
    def __str__(self):
        return str( bytearray(self) )[9:]
    def __repr__(self):
        return "Data"+str(self)

    # Creation
    def fromhex(self):
        ret = Data()
        for i in range( len(self)//2 ):
            ret.append(
                    ( undhex(self[2*i+1]) ) |
                    ( undhex(self[2*i  ]) <<4 )
                    )
        return ret
    def fromb64(self):
        return Data( base64.b64decode(self) )
    def fromascii(st):
        return Data( st, "ascii" )

    # Conversion
    def tohex(self):
        ret = Data()
        for x in self:
            ret.append(gethex(x>>4))
            ret.append(gethex(x&15))
        return ret
    def tob64(self):
        return Data(base64.b64encode( self ))
    def toascii(self):
        return self.decode("ascii")

def gethex(x):
    if x > 15 or x < 0:
        raise Expception("Wrong size to hex")
    return x+55 if x>9 else x+48
def undhex(x):
    if x < 48:
        raise Exception("Wrong size to undo hex")
    if x < 58:
        return x-48
    if x < 65:
        raise Exception("Wrong size to undo hex")
    if x < 71:
        return x-55
    if x < 97:
        raise Exception("Wrong size to undo hex")
    if x < 103:
        return x-87
    raise Exception("Wrong size to undo hex")
def popcount( x ):
    c = 0
    b = 1
    while b<=x:
        if x&b:
            c += 1
        b *= 2
    return c

def fromfile(fname):
    o = None
    with open(fname, "rb") as f:
        o = f.read()
    return Data(o)
