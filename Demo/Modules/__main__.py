
from Demo.Modules.utils import log, add

def main():
    log("Hello, World!")
    log(add(2,4))

# Is this module/file being used as the main module?
if __name__ == "__main__":
    main()  # yes, so call the main function