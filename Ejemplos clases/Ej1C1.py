import os   

def main():
    print(f"Proceso padre PID: {os.getpid()}")
    #Process ID (pid)
    pid = os.fork()
    if pid == 0:
        # Codigo ejecutado por el proceso hijo
        print(f"Este es el proceso hijo, PID: {os.getpid()}")
    elif pid > 0:
        # Codigo ejecutado por el proceso padre
        print(f"Este es el proceso padre, PID todavia: {os.getpid()}")
        os.wait() # El padre espera a que el hijo termine
    else:
        # fork fallo
        print("fork fallo")

if __name__ == "__main__":
    main()