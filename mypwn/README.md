## Outline



### about swpwn



wrapper for pwtools， Debug and exploit for CTF .

A pwn framework(based on `pwntools`) aiming at eliminating dull work while scripting and debugging.





### Install 

`python setup.py install` 

or copy the **swpwn.py** to your directory

### usage

#### 0x01 init pwn

```python
from swpwn import *

io,elf,libc = init_pwn(BIN_FILE = 'bin',LIBC_FILE='libc.so.6',remote_detail=('127.0.0.1',23333),is_env = False)
```



fecture:

```python
def init_pwn(BIN_FILE = '',LIBC_FILE='',remote_detail=('127.0.0.1',23333),is_env = False):
    """
    init pwn infomation
    usage: binary ,libc.so ,remote ip and port and  if use libc to debug
    
    return io,elf,libc
    """
    global io
    elf = ELF(BIN_FILE)
    
#    if LIBC_FILE:
#        libc = ELF(LIBC_FILE)
#    else:
#        libc = elf.libc
    # io = process(binary,env = {'LD_PRELOAD': './libc.so.6'})
    env = {'LD_PRELOAD':os.getcwd() + '/' +  LIBC_FILE}
    if opt.local:
        if is_env:
            io = process(BIN_FILE,env=env)
            libc = ELF(LIBC_FILE)
        else:
            io = process(BIN_FILE)
            libc = elf.libc
    else:
        io = remote(remote_detail[0],remote_detail[1],timeout=5)
        libc = ELF(LIBC_FILE)

    return io,elf,libc
```







#### 0x02 init debug

call init_debug(io,breakpoint=['0x1234','0xdeadbeef'],pie = False)

```python
def init_debug(io,breakpint=[],pie = False):
    """
    init debug
    usage: io, breakpoint ,pie if open
    return breakpoint and get gdb attach PID
    """
    if pie:
        base_addr = get_base_addr(proc.pidof(io)[0])
        bp = ''.join(['b *0x%x\n'%(b+base_addr) for b in breakpint])
    else:
        bp = ''.join(['b *0x%x\n'% b for b in breakpint])

    gdb.attach(proc.pidof(io)[0],bp)
    return bp
```



if your binary open pie, you can set pie is true ,than the program will auto find the code base by **get_base_addrt** function.

#### 0x03  quick script



```python
ru = lambda x : io.recvuntil(x)
sn = lambda x : io.send(x)
rl = lambda : io.recvline()
sl = lambda x : io.sendline(x)
rv = lambda x : io.recv(x)
sa = lambda a,b : io.sendafter(a,b)
sla = lambda a,b : io.sendlineafter(a,b)
```



we can use the simple word to call IO Function. 



### TODO

quick find magic function add, like main_arean,malloc_hook...

- [ ] malloc_hook

- [ ] Free_hook

- [ ] main_arean

- [ ] system

- [ ] onegadget

  .....