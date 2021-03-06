from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    a = 2 * math.pi / step
    b = float(0)
    while (b < float(10)):
     x0 = cx + r * (math.cos(b))
     y0 = cy + r * (math.sin(b))
     b+=a
     x1 = cx + r * (math.cos(b))
     y1 = cy + r * (math.sin(b))
     add_edge(points,x0,y0,cz,x1,y1,cz)
    pass

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if (curve_type == "bezier"):
        cx,cy = make_bezier(x0,y0,x1,y1,x2,y2,x3,y3)
        x = float(0)
        dx = float(1/step)
        while(x < float(1)):
            x_0 = (cx[0] * math.pow(x, 3)) + (cx[1] * math.pow(x, 2)) + (cx[2] * x) + cx[3]
            y_0 = (cy[0] * math.pow(x, 3)) + (cy[1] * math.pow(x, 2)) + (cy[2] * x) + cy[3]
            x += dx
            x_1 = (cx[0] * math.pow(x, 3)) + (cx[1] * math.pow(x, 2)) + (cx[2] * x) + cx[3]
            y_1 = (cy[0] * math.pow(x, 3)) + (cy[1] * math.pow(x, 2)) + (cy[2] * x) + cy[3]
            add_edge(points , x_0 , y_0 , 0 , x_1 , y_1 , 0)
    elif(curve_type == "hermite"):
        cx, cy = make_hermite(x0, y0, x1, y1, x2, y2, x3, y3)
        dx = float(1/step)
        x = float(0)
        while (x < float(1)):
            x_0 = (cx[0] * math.pow(x, 3)) + (cx[1] * math.pow(x, 2)) + (cx[2] * x) + cx[3]
            y_0 = (cy[0] * math.pow(x, 3)) + (cy[1] * math.pow(x, 2)) + (cy[2] * x) + cy[3]
            x += dx
            x_1 = (cx[0] * math.pow(x, 3)) + (cx[1] * math.pow(x, 2)) + (cx[2] * x) + cx[3]
            y_1 = (cy[0] * math.pow(x, 3)) + (cy[1] * math.pow(x, 2)) + (cy[2] * x) + cy[3]
            add_edge(points , x_0 , y_0 , 0 , x_1 , y_1 , 0)
    pass


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
