import bin.interface.menu as mn
import bin.akibo as ak

if __name__ == "__main__":
    menu = mn.MainMenu()
    mode = menu.mode
    args = menu.args
    ak.run(mode, args)
