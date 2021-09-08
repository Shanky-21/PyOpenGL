import glfw
from OpenGL.GL import *
import numpy as np

glfw.init()

window = glfw.create_window(800,600, "PyOpenGL Trianlge", None, None)
glfw.set_window_pos(window,400, 200)
glfw.make_context_current(window)

vertices = [-0.5,-0.5, 0.0,
            0.5,-0.5,0.0,
            0.0, 0.5,0.0]

#list of colors

colors = [1.0, 0, 0,
          0, 1.0, 0,
          0, 0, 1.0]

v = np.array(vertices, dtype = np.float32)
c = np.array(colors, dtype = np.float32)

# for drawing colorless triangle
glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3,GL_FLOAT, 0, v)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, c)

# setting color for the background

glClearColor(1,1,1,0)
while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    #ADDING ANIMATION
    glRotatef(0.1,0, 1, 0)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(window)

glfw.terminate()
