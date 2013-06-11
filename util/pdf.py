# not an encapsulation of the pdf, just the util-y parts

import sympy as s

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

_rt3 = s.sqrt(3).evalf()

def get_letter_canvas( filename ):
    '''sets up the standard configuration of one face panel
    centered on a letter-sized landscape, clipping included'''
    
    # get canvas object
    c = canvas.Canvas( filename, pagesize=( 11 * inch, 8.5 * inch ) )
    
    # set scale
    c.setLineWidth( 2/(9*inch) )
    delta_y = (17 - 3*_rt3)/4
    c.translate( 5.5 * inch, delta_y * inch )
    c.scale( 9*inch, 9*inch )

    # create/draw clipping triangle
    c.setStrokeColor( (0.5, 0.5, 1) )
    p = c.beginPath()
    p.moveTo( -0.5, -_rt3/6 )
    p.lineTo( 0, _rt3/3)
    p.lineTo( 0.5, -_rt3/6 )
    p.lineTo( -0.5, -_rt3/6 )
    p.close()
    c.clipPath( p )
    
    # return our canvas object
    return c
    

def draw_hexes( c, hexes = 5 ):
    '''Presumes we have an equilateral triangle, with origin
    at centroid and edge length of 1; draws hex grid within it,
    where hexes determines the number of complete hexagons
    along the edge.'''
    
    pass
    
