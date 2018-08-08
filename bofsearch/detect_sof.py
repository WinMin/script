import re
import idaapi

dsn_functions = ['_memcpy']
ds_functions = ['strcpy']
fdn_functions = ['read']
ida_info = idaapi.get_inf_structure()
number_pattern = r'^\d+[h]*$'

def parse_callee_args_x86_stdcall(caller_ea, nums):
    res = []
    func_start = 0
    cur_ea = PrevHead(caller_ea)
    #look backward from calling address
    cur_count = 0
    while True:
        mnem = GetMnem(cur_ea)
        if mnem == 'push':
            #the first nums push's opnd is the nums args of function
            cur_op = GetOpnd(cur_ea, 0)
            if cur_op != '':
                cur_op = cur_op.replace('[', '')
                cur_op = cur_op.replace(']', '')
                res.append(cur_op)
                cur_count += 1
                if cur_count == nums:
                    break
        cur_ea = PrevHead(cur_ea)
    
    return res

def parse_callee_args_x64_stdcall(caller_ea, nums):
    res = []

    print '[-]parse_callee_args_x64_stdcall Under constructions'
    
    return res

def analyse_dsn_func(dirtypool, data_size, callee_args):
    if callee_args[0] in dirtypool:
        if re.findall(number_pattern, callee_args[2]) != []:
            cur_size = 0
            if callee_args[2][-1] == 'h':
                cur_size = int(cacallee_args[2][0:-1], 0x10)
            else :
                cur_size = int(cacallee_args[2], 0x10)
            if data_size < cur_size:
                return 'for write destnation by larger size than buffer'
        else:
            return 'for using variable as size'

        
    return ''
            

def function_check(caller_ea, func_name, dirtypool, data_size):
    global dsn_functions
    # like memcpy(dst, src, n)
    global ds_functions
    global fdn_functions
    global ida_info

    for dsn_func in dsn_functions:
        if func_name == dsn_func:
            callee_args = []
            if ida_info.is_32bit():
                callee_args = parse_callee_args_x86_stdcall(caller_ea, 3)
            if ida_info.is_64bit():
                callee_args = parse_callee_args_x64_stdcall(caller_ea, 3)
            reason = analyse_dsn_func(dirtypool, data_size, callee_args)
            if reason != '':
                print '%s is vul, %s'%(func_name, reason)
    #for dsn_func in dsn_functions:


def parse_stk(base):
    res = dict()
    stack = idc.GetFrame(base)
    size  = idc.GetStrucSize(stack)

    pre_name = ''

    for i in xrange(size):
        n = idc.GetMemberName(stack, i)
        if n != ' s' and n != ' r' and n != None:

            if n in res.keys():
                # pass the in dict variables
                continue
            if pre_name != '':
                res[pre_name] = i - res[pre_name]
                #size = end - start
            
            res[n] = i
            pre_name = n

    res[pre_name] = size - res[pre_name]
    #size = end - start
    
    return res

def check_name_usage(op, dirtypool):
    for name in dirtypool:
        #emun the sinks to check if the opnd is something about the tainted data
        res = re.findall(name, op)
        if res != []:
            return True
    return False

def ins_taint(ops, dirtypool):
    res = dirtypool

    if 2 <= len(ops):
        if check_name_usage(ops[0], dirtypool) and not check_name_usage(ops[1], dirtypool):
            if ops[0] in dirtypool:
                #if dst of instruction is in dirtypool but src not, it will get out of dirtypool
                res.remove(ops[0])
        if check_name_usage(ops[1], dirtypool):
            #print ops[0], ops[1]
            #if src of instruction is in dirtypool, dst should in dirtypool
            res.append(ops[0])
            if ops[1] not in dirtypool:
                #sometimes src is part of member in dirtypool. if it is not in dirtypool, put it in
                res.append(ops[1])

    return res

def do_taint(base, data_name = None, size = 0):
    dirtypool = [data_name]
    print 'dirtypool',dirtypool
    for head in Heads(base, find_func_end(base)):
        print 'head',hex(head)
        # head here is addr of instructions
        if isCode(GetFlags(head)):
            mnem = GetMnem(head)
            # mnem is mov, call or lea etc.
            if mnem == 'call':
                func_name = GetOpnd(head, 0)
                print "func_name",func_name
                # if the instruction is call, the first opnd of it is callee's name
                # "print hex(head), dirtypool" here to get what dirtypool is
                function_check(head, func_name, dirtypool, size)
            ops = []
            for i in range(3):
                cur_op = GetOpnd(head, i)
                if cur_op != '':
                    cur_op = cur_op.replace('[', '')
                    cur_op = cur_op.replace(']', '')
                    #strip the brankets of opnd, so that variable in instruction like [ebp + dest] can be detect as reference of dest
                    ops.append(cur_op)
            dirtypool = ins_taint(ops, dirtypool)
    return dirtypool

def analyse_stkof(func_base):
    datas = parse_stk(func_base)

    # parse_stk returns {name_of_variable: size, ...}
    for data_name, size in datas.iteritems():
        do_taint(func_base, data_name, size)


if __name__ == '__main__':
     analyse_stkof(0x804843b) 