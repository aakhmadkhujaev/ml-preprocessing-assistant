from pathlib import Path
import utils


def main():
    while True:

        filename = input(
            "\nEnter CSV filename (or type 'exit' to quit): "
        )

        if filename.lower() == "exit":
            print("Goodbye!")
            break

        filepath = Path("data") / filename

        try:
            df = utils.load_data(filepath)

            info = utils.show_dataset_info(df)

            print(info)

        except FileNotFoundError as e:
            print(f"\nError: {e}")

        except Exception as e:
            print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()