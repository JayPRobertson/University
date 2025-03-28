#!/usr/bin/env python
"""Assignment 4 Part 1 Version 3 template"""
print(__doc__)

from typing import IO
from typing import Union

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
        self.isOpen:bool = False
        
    def openSVGcanvas(self) -> None:
        '''openSVGcanvas method: opens the SVG canvas
               Parameters: NONE
               Returns: NONE
        '''
        self.doc.writeHTMLcomment(self.t, "Define SVG drawing box")
        svg:HtmlComponent = HtmlComponent("svg", {"width":self.canvas[0], "height":self.canvas[1]}, self.t)
        self.doc.writeHTMLline(svg.opener()) 
        self.isOpen = True
        
    def closeSVGcanvas(self) -> None:
        '''closeSVGcanvas method': closes the SVG canvas
               Parameters: NONE
               Returns: NONE
        '''
        svg:HtmlComponent = HtmlComponent("svg", {"width":self.canvas[0], "height":self.canvas[1]}, self.t)
        self.doc.writeHTMLline(svg.closer())        
        
    def genArt(self) -> None:
        '''genArt method: generates a set number of coloured circles in the SVG canvas
                Parameters: NONE
                Returns: NONE       
        '''  
        if not self.isOpen:
            self.openSVGcanvas()
            
        CircleShape((50,50,50), (255,0,0,1.0)).drawShape(self.doc.file)
        CircleShape((150,50,50), (255,0,0,1.0)).drawShape(self.doc.file)
        CircleShape((250,50,50), (255,0,0,1.0)).drawShape(self.doc.file)
        CircleShape((350,50,50), (255,0,0,1.0)).drawShape(self.doc.file)
        CircleShape((450,50,50), (255,0,0,1.0)).drawShape(self.doc.file)
        CircleShape((50,250,50), (0,0,255,1.0)).drawShape(self.doc.file)
        CircleShape((150,250,50), (0,0,255,1.0)).drawShape(self.doc.file)
        CircleShape((250,250,50), (0,0,255,1.0)).drawShape(self.doc.file)
        CircleShape((350,250,50), (0,0,255,1.0)).drawShape(self.doc.file)
        CircleShape((450,250,50), (0,0,255,1.0)).drawShape(self.doc.file)

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
                                  (width, height)
                   col (tuple) - colour specifications of the ellipse in form 
                                 (red, green, blue)
               Returns: NONE
        '''        
        self.width:int = shape[0]
        self.height:int = shape[1]
        
        rectInfo:tuple = ("rect", {"width":self.width, "height":self.height}, 2)
        super().__init__(col, rectInfo)        

class EllipseShape(Shape):
    '''EllipseShape class: represents an ellipse shape object'''
    
    def __init__(self, shape:tuple, col:tuple) -> None:
        '''__init__ method: initializes an instance of an EllipseShape object
               Parameters:
                   shape (tuple)- specifications of ellipse shape in the form 
                                  (x radius, y radius)
                   col (tuple) - colour specifications of the ellipse in form 
                                 (red, green, blue)
               Returns: NONE
        '''        
        self.rx:int = shape[0]
        self.ry:int = shape[1]
        
        ellipseInfo:tuple = ("ellipse", {"rx":self.rx, "ry":self.ry}, 2)
        super().__init__(col, ellipseInfo)           

def writeHTMLfile() -> None:
    ''' writeHTMLfile method: generates art in an html file called "a41.html" 
            Parameters: NONE
            Returns: NONE
    '''
    fnam:str = "a41.html"
    title:str = "My Art"
    f:IO[str] = open(fnam, "w")
    doc:HtmlDocument = HtmlDocument(f, title)
    doc.startHTMLfile()
    canvas:SvgCanvas = SvgCanvas(doc, (500,300), 1)
    canvas.genArt()
    canvas.closeSVGcanvas()
    doc.endHTMLfile()
    f.close()        

def main() -> None:
    """main method"""
    writeHTMLfile()

if __name__ == "__main__":
    main()
