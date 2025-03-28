#!/usr/bin/env python
"""Assignment 4 Part 1 Version 3 template"""
print(__doc__)

from typing import IO
from typing import Union
import random as ran

class Shape:
    '''Shape class: represents a shape object'''
    
    def __init__(self, col:tuple, info:tuple) -> None:
        '''__init__ method: initializes an instance of a Shape object
               Parameters:
                   col (tuple) - colour specifications of the ellipse in form 
                                 (red, green, blue)
                    info (tuple) - information about the shape needed for an HTMl
                                   tag in the form (tag, attributes, spaces)
               Returns: NONE
        '''        
        self.red:int = col[0]
        self.green:int = col[1]
        self.blue:int = col[2]
        self.op:float = col[3]
        
        infoDict:dict = info[1]
        infoDict["fill"] = f'rgb({self.red}, {self.green}, {self.blue})'
        infoDict["fill-opacity"] = self.op
        self.htmlComp:HtmlComponent = HtmlComponent(info[0], infoDict, info[2])
        
    def drawShape(self, file:IO[str]) -> None:
        '''drawShape method: writes the SVG representation of a shape to file
               Parameters:
                   file (IO[str]) - a file to write to
               Returns: NONE
        '''
        file.write(self.htmlComp.render())
        
class CircleShape(Shape):
    '''CircleShape class: represents a circle shape object'''
    
    def __init__(self, shape:tuple, col:tuple) -> None:
        '''__init__ method: initializes an instance of a CircleShape object
               Parameters:
                   shape (tuple)- specifications of rect shape in the form 
                                  (x centre coord, y centre coord, radius),
                   col (tuple) - colour specifications of the ellipse in form 
                                 (red, green, blue)
               Returns: NONE
        '''         
        self.cx:int = shape[0]
        self.cy:int = shape[1]
        self.rad:int = shape[2]
        
        circleInfo:tuple = ("circle", {"cx":self.cx, "cy":self.cy, "r":self.rad}, 2)
        super().__init__(col, circleInfo)
        
class RectangleShape(Shape):
    '''RectangleShape class: represents a rectangle shape object'''
    
    def __init__(self, shape:tuple, col:tuple) -> None:
        '''__init__ method: initializes an instance of a RectangleShape object
               Parameters:
                   shape (tuple)- specifications of rect shape in the form 
                                  (width, height, x top-left coord, y top-left coord),
                   col (tuple) - colour specifications of the ellipse in form 
                                 (red, green, blue)
               Returns: NONE
        '''        
        self.width:int = shape[0]
        self.height:int = shape[1]
        self.xpos:int = shape[2]
        self.ypos:int = shape[3]
        
        rectInfo:tuple = ("rect", {"width":self.width, "height":self.height, "x":self.xpos, "y":self.ypos}, 2)
        super().__init__(col, rectInfo)        

class EllipseShape(Shape):
    '''EllipseShape class: represents an ellipse shape object'''
    
    def __init__(self, shape:tuple, col:tuple) -> None:
        '''__init__ method: initializes an instance of an EllipseShape object
               Parameters:
                   shape (tuple)- specifications of ellipse shape in the form 
                                  (x radius, y radius, x centre coord, y centre coord),
                   col (tuple) - colour specifications of the ellipse in form 
                                 (red, green, blue)
               Returns: NONE
        '''            
        self.rx:int = shape[0] #x radius of ellipse
        self.ry:int = shape[1] #y radius of ellipse
        self.cx:int = shape[2] #cx x-axis center of ellipse
        self.cy:int = shape[3] #cy y-axis center of ellipse
        
        ellipseInfo:tuple = ("ellipse", {"rx":self.rx, "ry":self.ry, "cx":self.cx, "cy":self.cy}, 2)
        super().__init__(col, ellipseInfo)           

class PyArtConfig:
    '''PyArtConfig class: represents a set of ranges for for the different 
                          parameters of generated random art
    '''
    DEFAULT_SHA:tuple = (0, 2) #shape range
    DEFAULT_RAD:tuple = (0, 100) #circle radius w/small range
    DEFAULT_RX:tuple = (10, 30) #ellipse x radius
    DEFAULT_RY:tuple = (10, 30) #ellipse y radius
    DEFAULT_W:tuple = (10, 100) #rect width w/small range
    DEFAULT_H:tuple = (10, 100) #rect height w/small range
    DEFAULT_R:tuple = (0, 255) #red colour of RGB
    DEFAULT_G:tuple = (0, 255) #green colour of RGB
    DEFAULT_B:tuple = (0, 255) #blue colour of RGB
    DEFAULT_OP:tuple = (0.0, 1.0) #shape opacity
    
    def __init__(self, viewport:tuple, sha:tuple=DEFAULT_SHA, rad:tuple=DEFAULT_RAD, 
                     rx:tuple=DEFAULT_RX, ry:tuple=DEFAULT_RY, w:tuple=DEFAULT_W,
                          h:tuple=DEFAULT_H, r:tuple=DEFAULT_R, g:tuple=DEFAULT_G,
                               b:tuple=DEFAULT_B, op:tuple=DEFAULT_OP) -> None:
        '''__init__ method: initializes an instance of a PyArtConfig object. 
               Parameters: (all ranges are inclusive)
                   viewport (tuple) - the dimensions of the canvas to generate in;
                                      given as (x px, y px)
                   sha (tuple) - range of possible shapes, where 0=circle, 1=rect, 2=ellipse
                   rad (tuple) - range of circle radii given as (min r, max r)
                   rx (tuple) - range of ellipse radii in x given as (min r, max r)
                   ry (tuple) - range of ellipse radii in y given as (min r, max r)
                   w (tuple) - range of rect widths given as (min x, max x)
                   h (tuple) - range of rect heights given as (min y, max y)
                   r (tuple) - range of red amounts in RGB given as (min r, max r)
                   g (tuple) - range of green amounts in RGB given as (min g, max g)
                   b (tuple) - range of blue amounts in RGB given as (min b, max b)
                   op (tuple) - range of shape opacities (min op, max op)
               Returns: NONE
        '''           
        self.x:tuple = (0, viewport[0]) #x-coordinate of shape
        self.y:tuple = (0, viewport[1]) #y-coordinate of shape
        self.sha:tuple = sha 
        self.rad:tuple = rad 
        self.rx:tuple = rx 
        self.ry:tuple = ry 
        self.w:tuple = w 
        self.h:tuple = h 
        self.r:tuple = r
        self.g:tuple = g
        self.b:tuple = b
        self.op:tuple = op
    
class RandomShape:
    '''RandomShape class: represents a random shape generated according to an art style'''
    
    def __init__(self, artStyle:PyArtConfig) -> None:
        '''__init__ method: initializes an instance of an RandomShape object;
                            randomly generates attributes in ranges given by artStyle
               Parameters:
                   artStyle (PyArtConfig) - the artsyle to generate according to
               Returns: NONE
        '''          
        self.artStyle:PyArtConfig = artStyle
        self.x:int = ran.randint(artStyle.x[0], artStyle.x[1])
        self.y:int = ran.randint(artStyle.y[0], artStyle.y[1])
        
        self.sha:int = ran.randint(self.artStyle.sha[0], self.artStyle.sha[1])
        self.rad:int = ran.randint(self.artStyle.rad[0], self.artStyle.rad[1])
        self.rx:int = ran.randint(artStyle.rx[0], artStyle.rx[1])
        self.ry:int = ran.randint(artStyle.ry[0], artStyle.ry[1])
        self.w:int = ran.randint(artStyle.w[0], artStyle.w[1])
        self.h:int = ran.randint(artStyle.h[0], artStyle.h[1])
        self.r:int = ran.randint(artStyle.r[0], artStyle.r[1])
        self.g:int = ran.randint(artStyle.g[0], artStyle.g[1])
        self.b:int = ran.randint(artStyle.b[0], artStyle.b[1])
        self.op:float = round(ran.uniform(artStyle.op[0], artStyle.op[1]), 1)
    
    def getShape(self) -> Union[CircleShape, RectangleShape, EllipseShape]:
        '''getShape method: creates a Shape instance of the random shape
               Parameters: NONE
               Returns:
                   shape (CircleShape, RectangleShape, or EllipseShape) - 
                         a Shape instance created from the random values
        '''
        col = (self.r, self.g, self.b, self.op)
        
        if self.sha == 0:
            shape:CircleShape = CircleShape((self.x, self.y, self.rad), col)
        elif self.sha == 1:
            shape:RectangleShape = RectangleShape((self.w, self.h, self.x, self.y), col)
        else:
            shape:EllipseShape = EllipseShape((self.rx, self.ry, self.x, self.y), col)         
        
        return shape

class HtmlComponent:
    '''HtmlComponent class: represents a single HTML component'''
    
    def __init__(self, tag:str='', attributes:dict={}, spaces:int=0, writeVar:str='') -> None:
        '''__init__ method: initializes an instance of an HtmlComponent object
               Parameters:
                   tag (str) - the component's HTML tag 
                   attributes (dict) - the HTML tag attributes formatted as:
                                       {attribute:attribute value} (ex. {"r":20})
                   spaces (int) - the number of spaces to indent the comment
                   writeVar (str) - the str written within the HTML tag 
                                    (ex. "MyArt" in <title>MyArt</title>
               Returns: NONE
        '''        
        self.tag:str = tag 
        self.attributes:dict = attributes
        self.writeVar:str = writeVar
        self.spaces:int = spaces
        
    def render(self) -> str:
        '''render method: renders the component as an HTML string of format:
                          spacing<tag attributes="attribute vals">writeVar</tag>
               Parameters: NONE
               Returns: NONE         
        '''
        attDict:dict = self.attributes
        ts:str = "   " * self.spaces
        attStr:str = "".join(f' {key}="{attDict[key]}"' for key in attDict)
        return f'{ts}<{self.tag}{attStr}>{self.writeVar}</{self.tag}>\n'
    
    def opener(self) -> str:
        '''opener method: renders the component as half an HTML string of format:
                          spacing<tag attributes="attribute vals">
               Parameters: NONE
               Returns: NONE
        '''
        attDict:dict = self.attributes
        ts:str = "   " * self.spaces
        attStr:str = "".join(f' {key}="{attDict[key]}"' for key in attDict)
        return f'{ts}<{self.tag}{attStr}>\n'
    
    def closer(self) -> str:
        '''closer method: renders the component as the second half of an HTML 
                          string of format: </tag>
               Parameters: NONE
               Returns: NONE
        '''
        ts:str = "   " * self.spaces
        return f'{ts}</{self.tag}>\n'
        
class HtmlDocument:
    '''HtmlDocument class: represents an HTML Document where HTML can be written'''
    
    def __init__(self, file:IO[str], title:str='') -> None:
        '''__init__ method: initializes an instance of an HtmlDocument object
               Parameters:
                   file (IO[str]) - an opened .html file to write to
                   title (str) - the titl of the document
               Returns: NONE
        '''        
        self.file:IO[str] = file
        self.title:str = title
        self.html:HtmlComponent = HtmlComponent("html")
        self.title:HtmlComponent = HtmlComponent("title", spaces=1, writeVar=title)
        self.header:HtmlComponent = HtmlComponent("head")
        self.body:HtmlComponent = HtmlComponent("body")        
      
    def writeHTMLline(self, toWrite:Union[HtmlComponent, str]) -> None:
        '''writeHTMLline method: writes an HTML line to file
               Parameters:
                   toWrite (HtmlComponent or str) - 
                           the component to write as an HTML line to file; 
                           if str, it is assumed to be formatted HTML-correct
               Returns: NONE
        '''
        if isinstance(toWrite, HtmlComponent):
            self.file.write(toWrite.render()) #if HtmlComponent
        else:
            self.file.write(toWrite) #if str
      
    def writeHTMLcomment(self, t:int, com:str) -> None:
        '''writeHTMLcomment method: writes an HTML comment to file
               Parameters:
                   t (int) - the number of spaces to indent the comment
                   com (str) - the comment to write to file
               Returns: NONE
        '''        
        ts:str = "   " * t
        self.file.write(f'{ts}<!--{com}-->\n')
        
    def startHTMLfile(self) -> None:
        '''startHTMLfile method: writes HTML to file of format:
        <html>
        <head>
           <title>title</title>
        </head>
        <body>
               Parameters: NONE
               Returns: NONE
        '''
        self.writeHTMLline(self.html.opener())
        self.writeHTMLline(self.header.opener())
        self.writeHTMLline(self.title)
        self.writeHTMLline(self.header.closer())
        self.writeHTMLline(self.body.opener())
    
    def endHTMLfile(self) -> None:
        '''endHTMLfile method: writes HTML to file of format:
        </body>
        </html>
               Parameters: NONE
               Returns: NONE
        '''
        self.writeHTMLline(self.body.closer())   
        self.writeHTMLline(self.html.closer())       

class SvgCanvas:
    '''SvgCanvas class: represents an SVG canvas where shapes can be drawn'''
    
    def __init__(self, doc:HtmlDocument, canvas:tuple, t:int=1) -> None:
        '''__init__ method: initializes an instance of an SvgCanvas object
               Parameters:
                   doc (HtmlDocument) - an HTML document where the canvas is located
                   canvas (tuple) - the dimensions of the canvas in (x px, y px)
                   t (int) - the number of spaces to indent SVG formatting
               Returns: NONE
        '''
        self.canvas:tuple = canvas
        self.t:int = t
        self.doc:HtmlDocument = doc
        self.svg:HtmlComponent = HtmlComponent("svg", {"width":canvas[0], "height":canvas[1]}, t)
        self.isOpen:bool = False
        
    def openSVGcanvas(self) -> None:
        '''openSVGcanvas method: opens the SVG canvas
               Parameters: NONE
               Returns: NONE
        '''
        self.doc.writeHTMLcomment(self.t, "Define SVG drawing box")
        self.doc.writeHTMLline(self.svg.opener()) 
        self.isOpen = True
        
    def closeSVGcanvas(self) -> None:
        '''closeSVGcanvas method': closes the SVG canvas
               Parameters: NONE
               Returns: NONE
        '''
        self.doc.writeHTMLline(self.svg.closer()) 
        self.isOpen = False
        
    def genArt(self, config:PyArtConfig, numShapes:int) -> None:
        '''genArt method: generates numShapes random shapes in the SVG canvas
                          according to PyArtConfig configuration
                Parameters:
                    config (PyArtConfig) - configuration for shape 
                                           generation specifications       
                    numShapes (int) - number of shapes to generate
                Returns: NONE       
        '''
        if not self.isOpen:
            self.openSVGcanvas() #first open if closed
        
        #Draw a given number of shapes to the open canvas
        for i in range(numShapes): 
            shape = RandomShape(config)
            shape.getShape().drawShape(self.doc.file)

def writeHTMLfile() -> None:
    ''' writeHTMLfile method: generates art in an html file. 
            Parameters: NONE
            Returns: NONE
    
    a431Config:PyArtConfig = PyArtConfig((1000, 400), sha=(0, 0), rad=(20, 90), r=(200, 255), g=(50, 200), b=(50, 200), op=(0.5, 1.0))
    shapes:int = 80
    
    a432Config:PyArtConfig = PyArtConfig((800, 600), rad=(70, 100))
    shapes:int = 1000
    
    a433Config:PyArtConfig = PyArtConfig((300, 600), sha=(1,2), ry=(20, 100), w=(0, 200), h=(50, 90), r=(0, 150), g=(200, 255), op=(0.5, 1.0))
    shapes:int = 400
    '''
    fnam:str = "a434.html"
    title:str = "My Art"
    f:IO[str] = open(fnam, "w")
    doc:HtmlDocument = HtmlDocument(f, title)
    doc.startHTMLfile()
    canvas:SvgCanvas = SvgCanvas(doc, (500,300), 1)
    a433Config:PyArtConfig = PyArtConfig((500,300))
    shapes:int = 100
    canvas.genArt(a433Config, shapes)
    canvas.closeSVGcanvas()
    doc.endHTMLfile()
    f.close()        

def main() -> None:
    '''main method: main entry point of the program'''
    writeHTMLfile()

if __name__ == "__main__":
    main()
