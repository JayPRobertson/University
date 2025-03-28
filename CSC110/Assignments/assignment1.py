import doctest
SPACE = ' '
PI = 3.14

def print_mouse():
   '''
   prints an ascii image of a mouse
   
   credit to Hayley Jane Wakenshaw for art
   asciiart.eu/animals/rodents/mice
   '''
   print((2 * SPACE) + 'O~O')
   print(' (\\"/)')
   print('(\\"o"/)')
   print(' m`-\'m\'`---.')      

def print_aardvark():
      '''
      prints an ascii image of an aardvark
      
      credit to Veronica Karlsson for art
      asciiart.eu/animals/aardvarks
      '''
      print((7 * SPACE) + '_.---._' + (4 * SPACE) + '/\\\\')
      print((4 * SPACE) + './\'' + (7 * SPACE) + '"--`\//')
      print((2 * SPACE) + './' + (14 * SPACE) + 'o \\')
      print(' /./\  )______' + (3 * SPACE) + '\__ \\')
      print('./' + (2 * SPACE) + '/ /\ \\' + (3 * SPACE) + '| \ \  \ \\')
      print((3 * SPACE) + '/ /  \ \  | |\ \  \\' + '7')

def print_logo():
   '''
   prints alternating ascii mouse and aardvark images with spacer lines
   
   credit to Veronica Karlsson and Hayley Jane Wakenshaw for art
   asciiart.eu/animals/rodents/mice
   asciiart.eu/animals/aardvarks
   '''
   spacer_line = '/~~~~~~~~\\'
   print(spacer_line)
   print_mouse()
   print_aardvark()
   print(spacer_line)
   print_mouse()
   print_aardvark()
   print(spacer_line)
   print_mouse()
   print_aardvark()
   print(spacer_line)
   print_mouse()
   print_aardvark()
   print(spacer_line)   
   
      
def calculate_surface_area(height: float, diameter: float):
   '''
   calculates and prints a cyclinder's surface area for a given height and diameter
   >>> calculate_surface_area(1.5, 9)
   cyclinder area: 169.6
   >>> calculate_surface_area(13.1, 2.4)
   cyclinder area: 107.8
   '''
   number_of_circles = 2
   circumfrence = PI * diameter
   circle_area = circumfrence**2 / (4 * PI)
   cylinder_walls_area = circumfrence * height
   total_surface_area =  number_of_circles * circle_area + cylinder_walls_area
   print(f'cyclinder area:{total_surface_area: 0.1f}') 