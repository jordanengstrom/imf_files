from dotenv import load_dotenv
import concurrent.futures
import os
import pandas as pd
import requests
import time


# Set environment variables:
print("[*] Loading environment...")
load_dotenv()
IMF_LINKS_DOCUMENT_PATH = os.getenv("IMF_LINKS_DOCUMENT_PATH")
DROPBOX_FOLDER_PATH = os.getenv("DROPBOX_FOLDER_PATH")


def save_pdf_file(request_url, destination_path: str):
    print(f"[*] Downloading file: {destination_path}")
    http_response = requests.get(request_url)

    print(f"[*] Writing file to disk: {destination_path}")
    with open(destination_path, "wb") as file:
        file.write(http_response.content)

    print(f"[*] Successfully downloaded file: {destination_path}")
    return True


def main():
    print("[*] Importing document...")
    df = pd.read_csv(IMF_LINKS_DOCUMENT_PATH)

    total_rows = len(df.index)

    print("Launching concurrent file downloads...")
    futures = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Iterate through the df:
        for i in range(0, total_rows):
            # Determine the download path based on os:
            if os.name == "posix":
                new_file_name = (
                    DROPBOX_FOLDER_PATH
                    + "/"
                    + str(df.at[i, "Dropbox folder"])
                    + "/"
                    + str(df.at[i, "File name"] + ".pdf")
                )
            else:
                new_file_name = (
                    DROPBOX_FOLDER_PATH
                    + "\\"
                    + str(df.at[i, "Dropbox folder"])
                    + "\\"
                    + str(df.at[i, "File name"] + ".pdf")
                )

            pdf_url = str(df.at[i, "Link"])
            fn_args = [pdf_url, new_file_name]
            futures.append(executor.submit(save_pdf_file, *fn_args))

        for future in concurrent.futures.as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- Execution time: %s seconds ---" % (time.time() - start_time))
