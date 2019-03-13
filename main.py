from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
print_matrix([[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]])
# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )
parse_file( 'script.txt', edges, transform, screen, color )
parse_file( 'script1.txt', edges, transform, screen, color )
