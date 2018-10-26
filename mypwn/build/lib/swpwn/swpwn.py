#!/usr/bin/env python
# encoding: utf-8

from pwn import *
import os
from optparse import OptionParser


ru = lambda x : io.recvuntil(x)
sn = lambda x : io.send(x)
rl = lambda : io.recvline()
sl = lambda x : io.sendline(x)
rv = lambda x : io.recv(x)
sa = lambda a,b : io.sendafter(a,b)
sla = lambda a,b : io.sendlineafter(a,b)

def lg(s,addr):
    """
    use red color show addr
    usage: s - > text ,addr -> whant to show 
    """
    print('\033[1;31;40m%20s-->0x%x\033[0m'%(s,addr))


def raddr(a=6):
    """
    do infoleak
    recvn() -- > to  read addr
    usage: size of addr
    """
    if(a==6):
        return u64(rv(a).ljust(8,'\x00'))
    else:
        return u64(rl().strip('\n').ljust(8,'\x00'))

def get_base_addr(pid):
    """
    get base :
    usage :PID Number
    """
    pid = int(pid)
    vmmap = os.popen("pmap %d | awk '{print $1}'"%(pid)).read()
    ba = vmmap.split("\n")[1]
    return int(ba,16)



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



def init_parser():
    """
    init parser
    debug or remote
    """
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage=usage)

    parser.add_option("-l", "--local", dest="local", action="store_true",
                      help="pwn for local bin", default=False)
    parser.add_option("-r", "--remote", dest="remote",  action="store_true",
                      help="pwn for remote bin", default=False)

    (options, args) = parser.parse_args()

    if options.remote:
        options.local = True
        options.remote = False
    elif options.remote:
        options.local = False
        options.remote = True
    return options


opt = init_parser()


def init_pwn(BIN_FILE = '',LIBC_FILE='',remote_detail=('127.0.0.1',23333),is_env = False):
    """
    init pwn infomation
    usage: binary ,libc.so ,remote ip and port and  if use libc to debug
    
    return io,elf,libc
    """
    elf = ELF(BIN_FILE)
    if LIBC_FILE:
        libc = ELF(LIBC_FILE)
    else:
        libc = elf.libc
    # io = process(binary,env = {'LD_PRELOAD': './libc.so.6'})
    env = {'LD_PRELOAD':os.getcwd() + '/' +  LIBC_FILE}
    if opt.local:
        if is_env:
            io = process(BIN_FILE,env=env)
        else:
            io = process(BIN_FILE)
    else:
        io = remote(remote_detail[0],remote_detail[1],timeout=5)


    return io,elf,libc



