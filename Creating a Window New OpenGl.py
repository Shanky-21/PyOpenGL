

"""
Creating a Simple Window - New OpenGL
author - @Pycasm
"""

import glfw
from OpenGL.GL import*

def framebuffer_size_callback(window, width, height):
    glViewport(0,0, width, height)

def processInput(window):
    if glfw.get_key(window,glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window,True)


if not glfw.init():
    print('Can\'t initialize glfw')
    exit()




window = glfw.create_window(1000,800,"Pycasm Window", None, None)
if not window:
    glfw.terminate()
    print("Glfw window can't be created")
    exit()

glfw.set_window_pos(window, 100,100)
glfw.make_context_current(window)
glfw.set_framebuffer_size_callback(window,framebuffer_size_callback)

while not glfw.window_should_close(window):
    #Input
    processInput(window)
    #Rendering Commands Here
    glClearColor(0.2,0.3,0.3,1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    #Check and Call events and swap the buffers
    glfw.poll_events()
    glfw.swap_buffers(window)
    

glfw.terminate()



