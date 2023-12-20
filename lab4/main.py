import threading

from cube import start_cube
from user_interface import start_interface
class CubeState:
    X_Y = 1
    X_Z = 0
    Y_Z = 0
    Color = "All"
    FPS = 30


if __name__ =="__main__":
    cube_state = CubeState()

    t1 = threading.Thread(target=start_cube, args=(cube_state,))
    t2 = threading.Thread(target=start_interface, args=(cube_state,))
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
 
    print("Done!")