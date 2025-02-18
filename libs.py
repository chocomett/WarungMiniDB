from program import warung

def opening():
    message = "selamat datang di Warung DB"
    decor = "*" * (len(message) + 6)
    
    print(decor)
    print(f"** {message} **")
    print(decor)

def menu():
    menus = int(input(f"\n1. Warung DB\n2. Comming Soon\n\nSilahkan pilih program: "))
    
    if menus == 1:
        warung.start()
    else:
        print("pilihan tak tersedia")
        exit()


if __name__ == "__main__":
    opening()
    menu()