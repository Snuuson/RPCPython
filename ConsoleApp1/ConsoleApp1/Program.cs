using System.IO.Pipes;
using System;
using System.Data;

using (var client = new NamedPipeClientStream("CoorinatePipe")) {
    client.Connect();
    
    while (true) {
        Byte[] buffer = new Byte[11];
        int b = client.Read(buffer,0,11);
        Console.WriteLine(System.Text.Encoding.Default.GetString(buffer));
    }
}
