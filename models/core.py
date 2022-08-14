from libharness import ffi, lib

def ffi_str(s):
    return ffi.string(s).decode('utf-8')

@ffi.def_extern()
def decode(msg):
    string = "hello, world!"
    print("decode reached")
    return ffi.from_buffer("char *", string.encode('utf-8'))