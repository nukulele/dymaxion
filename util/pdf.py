# not a full encapsulation of the pdf, just the util-y parts

import sympy as s

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

_rt3 = s.sqrt(3).evalf()

def get_letter_canvas( filename, clip = True ):
    '''sets up the standard configuration of one face panel
    centered on a letter-sized landscape, clipping included'''
    
    # get canvas object
    c = canvas.Canvas( filename, pagesize=( 11 * inch, 8.5 * inch ) )
    
    # set scale
    delta_y = (17 - 3*_rt3)/4
    c.translate( 5.5 * inch, delta_y * inch )
    c.scale( 9*inch, 9*inch )

    # create and draw clipping triangle
    c.setStrokeColor( (0.75, 0.75, 1) )
    c.setLineWidth( 0.005 )
    p = c.beginPath()
    p.moveTo( -0.5, -_rt3/6 )
    p.lineTo( 0, _rt3/3)
    p.lineTo( 0.5, -_rt3/6 )
    p.lineTo( -0.5, -_rt3/6 )
    p.close()
    
    # make it a clipping triangle if clip==True
    if clip:
        c.clipPath( p )
    else:
        c.drawPath( p )
    
    # return our canvas object
    return c
    

def draw_hexes( c, hexes = 5 ):
    '''Presumes we have an equilateral triangle, with origin
    at centroid and edge length of 1; draws hex grid within it,
    where hexes determines the number of complete hexagons
    along the edge.'''
    
    x_inc = 1./( 6 * hexes )
    y_inc = _rt3/( 6 * hexes )
    
    def _scale_x( x ):
        return x * x_inc - 0.5
        
    def _scale_y( y ):
        return y * y_inc - _rt3/6
    
    for x in range( 6 * hexes ):
        for y in range( 3 * hexes ):
            
            xmod = x % 6
            ymod = y % 2
            if xmod > 2:
                xmod -=3
                ymod = 1 - ymod

            if xmod == 0 and ymod == 1:
                c.line( _scale_x( x ), _scale_y( y ), _scale_x( x+1 ), _scale_y( y ) )
            if xmod == 1 and ymod == 0:
                c.line( _scale_x( x ), _scale_y( y+1 ), _scale_x( x+1 ), _scale_y( y ) )
            if xmod == 1 and ymod == 1:
                c.line( _scale_x( x ), _scale_y( y ), _scale_x( x+1 ), _scale_y( y+1 ) )
            if xmod == 2 and ymod == 0:
                c.line( _scale_x( x ), _scale_y( y ), _scale_x( x+1 ), _scale_y( y ) )
