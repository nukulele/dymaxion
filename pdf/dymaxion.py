from reportlab.pdfgen import canvas
import sympy

def sx( x ):
    return 216 * x + 18

def sy( y ):
    return 216 * y + 144
    
th = (sympy.sqrt(3)/2).evalf()

c = canvas.Canvas( "output.pdf", pagesize=( 17 * 72, 11 * 72 ) )
c.setStrokeColorRGB( .75, .75, 1 )
c.line( sx(0), sy(2 * th), sx(1), sy(0) )
c.line( sx( 0.5 ), sy(3 * th), sx(2), sy(0) )
c.line( sx( 1.5 ), sy(3 * th), sx(3), sy(0) )
c.line( sx( 2.5 ), sy(3 * th), sx(4), sy(0) )
c.line( sx( 3.5 ), sy(3 * th), sx(5), sy(0) )
c.line( sx( 4.5 ), sy( 3*th ), sx( 5.5 ), sy( th ) )
c.line( sx(0.5), sy(3 * th), sx(0), sy(2*th) )
c.line( sx(1.5), sy(3 * th), sx(0.5), sy(th) )
c.line( sx(2.5), sy(3 * th), sx(1), sy(0) )
c.line( sx(3.5), sy(3 * th), sx(2), sy(0) )
c.line( sx(4.5), sy(3 * th), sx(3), sy(0) )
c.line( sx(5), sy(2 * th), sx(4), sy(0) )
c.line( sx(5.5), sy(th), sx(5), sy(0) )
c.line( sx(0), sy(2 * th), sx(5), sy( 2*th) )
c.line( sx(0.5), sy(th), sx(5.5), sy(th) )
c.drawString( 36, 36, "stereographic projection of a sphere onto an unfolded icosahedron by nukulele / 2013 / karmic rights reserved" )

c.showPage()
c.save()