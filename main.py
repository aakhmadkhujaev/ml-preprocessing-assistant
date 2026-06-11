from pathlib import Path

from numpy.random import choice
import preprocessing
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
            # Load dataset
            df = utils.load_data(filepath)

            # Original dataset analysis
            info = utils.show_dataset_info(df)
            print(info)

            missing_info = utils.analyze_missing_values(df)
            print(missing_info)

            duplicate_info = utils.analyze_duplicates(df)
            print(duplicate_info)

            # Clean dataset
            cleaned_df = preprocessing.clean_dataset(df)

            print("\nDataset cleaned successfully!")

            utils.save_dataset(
            cleaned_df,
            "output/cleaned_data.csv"
            )

            # Cleaned dataset analysis
            missing_info = utils.analyze_missing_values(cleaned_df)
            print(missing_info)

            duplicate_info = utils.analyze_duplicates(cleaned_df)
            print(duplicate_info)

            print("\nChoose encoding method:")
            print("1. One-Hot Encoding")
            print("2. Label Encoding")
            print("3. Skip Encoding")

            choice = input("Enter choice: ")

            if choice == "1":
                encoding_method = "onehot"

            elif choice == "2":
                encoding_method = "label"

            elif choice == "3":
                encoding_method = "skip"

            else:
                raise ValueError("Invalid choice.")
            
            encoded_df = preprocessing.encode_dataset(
                cleaned_df,
                encoding_method
            )


            print("\nChoose scaling method:")
            print("1. StandardScaler")
            print("2. MinMaxScaler")
            print("3. Skip Scaling")

            choice = input("Enter choice: ")

            if choice == "1":
                scaling_method = "standard"

            elif choice == "2":
                scaling_method = "minmax"

            elif choice == "3":
                scaling_method = "skip"

            else:
                raise ValueError("Invalid choice.")

            scaled_df = preprocessing.scale_dataset(
                encoded_df,
                scaling_method
            )

            if scaling_method == "skip":
                print("\nScaling skipped.")
            else:
                print(f"\nScaling applied using {scaling_method}.")

            utils.save_dataset(
                scaled_df,
                "output/processed_data.csv"
            )

            print("Dataset processed successfully!")
        


                        

        except FileNotFoundError as e:
            print(f"\nError: {e}")

        except Exception as e:
            print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
    main()