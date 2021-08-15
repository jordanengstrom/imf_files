from dotenv import load_dotenv
import os
import pandas as pd
import requests
import time


# Set environment variables:
print("[*] Loading environment...")
load_dotenv()
IMF_LINKS_DOCUMENT_PATH = os.getenv("IMF_LINKS_DOCUMENT_PATH")
DROPBOX_FOLDER_PATH = os.getenv("DROPBOX_FOLDER_PATH")


def save_pdf_file(http_response, destination_path: str, index: int):
    print(f"[*] Writing file #{index} to disk: {destination_path}")
    with open(destination_path, "wb") as file:
        file.write(http_response.content)
    print(f"[*] Successfully downloaded file #{index}: {destination_path}")


def main():
    print("[*] Importing document...")
    df = pd.read_csv(IMF_LINKS_DOCUMENT_PATH)

    total_rows = df.index
    test_stop_index = 10

    # Iterate through the df:
    for i in range(0, test_stop_index):

        # Alias variables:
        new_directory_name = DROPBOX_FOLDER_PATH + "/" + str(df.at[1, "Dropbox folder"])
        new_file_name = new_directory_name + "/" + str(df.at[0, "File name"] + ".pdf")
        pdf_url = str(df.at[2, "Link"])

        print(f"[*] Downloading file #{i}: {new_file_name}")
        response = requests.get(pdf_url)

        print(f"[*] Saving file #{i}: {new_file_name}")
        if not os.path.exists(new_directory_name):
            os.makedirs(new_directory_name)
            save_pdf_file(response, new_file_name, i)
        else:
            save_pdf_file(response, new_file_name, i)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- Execution time: %s seconds ---" % (time.time() - start_time))
