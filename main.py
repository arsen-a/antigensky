from helpers import init_dirs
from services import collect_inputs_and_store_data, generate_report


def main():
    init_dirs()
    antigensky = collect_inputs_and_store_data()
    antigensky.generate_qr()
    generate_report(antigensky)


if __name__ == "__main__":
    main()
