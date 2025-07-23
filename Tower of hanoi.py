def toh(n,src,dest,aux):
    if n == 1:
        print(f"Move disk {n} from {src} to {dest}")
        return
    toh(n-1,src,aux,dest)
    print(f"Move disk {n} from {src} to {dest}")
    toh(n-1,aux,dest,src)

n = int(input("Enter the number of disks: "))
toh(n,'A','C','B')