import argparse
parser = argparse.Argumentparser()

parser.add_argument('--v0','--intial_velocity',type= float, default = 0.0, help='intial_velocity')
parser.add_argument('--s0','--intial_location',type= float, default = 0.0, help='intial_location')
parser.add_argument('--a','--accelaration',type= float, default = 1.0 ,help='acceralation')
parser.add_argument('--v0','--time',type= float, default = 1.0, help='time')

args = parser.parse_args

v0 = args.v0
s0 = args.s0
a= args.a
t = args.t

s=s0 + v0*t +0.5*a*t*t

print("current location",s)