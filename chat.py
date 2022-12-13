import win32pipe
import win32file

# Create a named pipe server
pipe = win32pipe.CreateNamedPipe(
    "\\\\.\\pipe\\my_pipe",
    win32pipe.PIPE_ACCESS_DUPLEX,
    win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_WAIT,
    1, 65536, 65536,
    0,
    None
)

# Wait for a client to connect
win32pipe.ConnectNamedPipe(pipe, None)

# Send a message to the client  
message = "Hello from Python!".encode()
win32file.WriteFile(pipe, message)

# Read a response from