import sympy as s

class Circle( object ):

    def __init__( self, x0 = 0, y0 = 0, radius = 1 ):
        self.x0 = x0
        self.y0 = y0
        self.radius = radius
        
def three_point_circle( x1, y1, x2, y2, x3, y3 ):
        
        a = x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2
        d = -x1**2*y2 + x1**2*y3 + x2**2*y1 - x2**2*y3 - x3**2*y1 + \
               x3**2*y2 - y1**2*y2 + y1**2*y3 + y1*y2**2 - y1*y3**2 - \
                y2**2*y3 + y2*y3**2
        e = x1**2*x2 - x1**2*x3 - x1*x2**2 + x1*x3**2 - x1*y2**2 + \
                x1*y3**2 + x2**2*x3 - x2*x3**2 + x2*y1**2 - x2*y3**2 - \
                x3*y1**2 + x3*y2**2
        x0 = -d/(2*a)
        y0 = -e/(2*a)
        return Circle( x0, y0, s.sqrt( (x1-x0)**2+(y1-y0)**2 ) )
    
