
import time
import sys
import win32pipe, win32file, pywintypes


from random import randrange

def pipe_server():
    pipe = win32pipe.CreateNamedPipe(
        r'\\.\pipe\CoorinatePipe',
        win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
        1, 11, 11,
        0,
        None)
    try:
        print("waiting for client")
        win32pipe.ConnectNamedPipe(pipe, None)
        print("got client")

        while True:
            
            
            x = randrange(10) / 10 
            y = randrange(10) / 10
            z = randrange(10) / 10

            coord_data = str.encode(f"{x},{y},{z}",'utf8')
            print(len(f"{x},{y},{z}".encode('utf8')))
            win32file.WriteFile(pipe, coord_data)
            #win32file.SetFilePointer(pipe,0,win32file.FILE_BEGIN)

        print("finished now")
    except Exception as e:
        print(e)
    finally:
        win32file.CloseHandle(pipe)

pipe_server()