import glfw
from OpenGL.GL import*

def framebuffer_size_callback(window, width, height):
    glViewport(0,0, width, height)

if not glfw.init():
    print('Can\'t initialize glfw')
    exit()


window = glfw.create_window(1000,800,"Main Window", None, None)
if not window:
    glfw.terminate()
    print("Glfw window can't be created")
    exit()

glfw.set_window_pos(window, 100,100)
glfw.make_context_current(window)
glfw.set_framebuffer_size_callback(window,framebuffer_size_callback)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()



