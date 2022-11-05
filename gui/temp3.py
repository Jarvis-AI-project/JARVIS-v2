
with SerialPort(Serial(port='<COM1 or /dev/ttyUSB0>', baudrate=9600 * 6, timeout=2)) as port:
   rq = RqCommand(port)
   rs = RsSimple(port)
   Handshake(rq, rs).make()
