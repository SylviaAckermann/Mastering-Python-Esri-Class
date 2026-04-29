import logging

logging.basicConfig(
    filename="app_error.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

def main():

    try:
        # this is the code which could fail
        logging.debug("Starting the program")
        raise Exception("Something went wrong ...")
    
    except Exception:
        # handle the error/exception by logging
        logging.fatal("Unexpected error occured.", exc_info=True)

if __name__ == "__main__":
    main()

