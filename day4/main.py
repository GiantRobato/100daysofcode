from __future__ import print_function

import struct
import zlib

with open('./whitePixel.png','rb') as f:
    PNGheader = f.read(8)
    while True:
        chunk = f.read(4)
        if not chunk: break
        chunkType = f.read(4)        
        numBytes = int.from_bytes(chunk, byteorder='big')
        data = f.read(numBytes)
        crc = f.read(4)
        try:
            chunkType = bytes(chunkType).decode('utf-8')
            if chunkType == 'IDAT':
                deflated = zlib.decompress(data)
                (a,r,g,b) = struct.unpack('<BBBB',deflated)
                print('argb value is: [{},{},{},{}]'.format(a,r,g,b))
        except Exception as e:
            print(e)
