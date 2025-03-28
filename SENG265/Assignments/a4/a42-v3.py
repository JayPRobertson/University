#!/usr/bin/env python
"""Assignment 4 Part 2 Version 3"""
print(__doc__)

from typing import IO
import random as ran

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
    
    def __init__(self, viewport:tuple, sha:tuple=DEFAULT_SHA,rad:tuple=DEFAULT_RAD, 
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
        self.sha:tuple = sha #shape range
        self.rad:tuple = rad #circle radius w/small range
        self.rx:tuple = rx #ellipse x radius
        self.ry:tuple = ry #ellipse y radius
        self.w:tuple = w #rect width w/small range
        self.h:tuple = h #rect height w/small range
        self.r:tuple = r #red colour of RGB
        self.g:tuple = g #green colour of RGB
        self.b:tuple = b #blue colour of RGB
        self.op:tuple = op #shape opacity
    
class RandomShape:
    '''RandomShape class: represents a random shape generated according to an art style'''
    __obj_count:int = 0
    
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
        
        RandomShape.__obj_count += 1
        
        self.data:list = [RandomShape.__obj_count-1, self.sha, self.x, self.y, self.rad, self.rx, self.ry, self.w, self.h, self.r, self.g, self.b, self.op]
        
    def __str__(self) -> str:
        '''__str__ method: returns a str of object data nicely formatted over 
                           multiple lines
               Parameters: NONE
               Returns:
                   (str) - a formatted str of object data
        '''
        return f'Shape: {self.sha} (where 0=circle, 1=rectangle, 2=ellipse)\n' +\
               f'Located at: (x={self.x}, y={self.y})\nCircle radius: {self.rad}\n' +\
               f'Ellipse radius: {self.rx} (in x) and {self.ry} (in y)\n' +\
               f'Rectangle size: {self.w} (width) and {self.h} (height)\n' +\
               f'RGB: (red={self.r}, green={self.g}, blue={self.b})\nOpacity: {self.op}\n'       
    
    def as_Part2_line(self) -> str:
        '''as_Part2_line method: returns a str of object data in the form of 
                                 a line of numbers
               Parameters: NONE
               Returns:
                   lineStr (str) - a formatted str of object data          
        '''
        lineStr:str = ''
        for val in self.data:
            lineStr += f'{val:>5}'
            
        return lineStr
    
    def as_svg(self) -> str:
        '''as_svg method: returns a str of object data in the form of SVG commands
               Parameters: NONE
               Returns:
                   (str) - a formatted str of object data
        '''
        shape:str = ''
        attStr:str = ''
        
        if self.sha == 0:
            shape = "circle"
            attStr = f'cx="{self.x}" cy="{self.y}" r="{self.rad}"'
        elif self.sha == 1:
            shape = "rect"
            attStr = f'width="{self.w}" height="{self.h}" x="{self.x}" y="{self.y}"'
        else:
            shape = "ellipse"
            attStr = f'rx="{self.rx}" ry="{self.ry}" cx="{self.x}" cy="{self.y}"'           
        
        return f'<{shape} {attStr} fill="rgb({self.r},{self.g},{self.b})" ' +\
               f'opacity="{self.op}"></{shape}>'
    
def main() -> None:
    '''main method'''
    
    print("  CNT  SHA    X    Y  RAD   RX   RY    W    H    R    G    B   OP")
    for i in range(11):
        artStyle:PyArtConfig = PyArtConfig((500,300))
        shape:RandomShape = RandomShape(artStyle)
        print(shape.as_Part2_line())
    

if __name__ == "__main__":
    main()
