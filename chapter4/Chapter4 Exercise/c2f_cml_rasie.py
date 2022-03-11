import sys
def read_C():
    
    try:
        C = float(sys.argv[1])
    except IndexError:
        raise IndexError("No command arguments for C!")
        
    except ValueError:
        raise ValueError("C must be pure number , not%s!" % sys.argv[1])
        
    if C < -273.15:
        raise ValueError("C=%g is non physical number" % C)
        
    return C

try:
    C = read_C()
    
except (IndexError,ValueError) as e:
    print(e)
    sys.exit(1)
    
F = 9/5*C + 32
print("%gC is %.1f F"%(C,F))
        
        
      