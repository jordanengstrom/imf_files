# IMF Files Dropbox Download

## How to run:

1. To guarantee cross platform compatibility, export the Excel document to a CSV. If you don't feel like doing this, just change this method call from read_csv to read_excel: <br>
 `df = pd.read_csv(IMF_LINKS_DOCUMENT_PATH)` <br>
 `df = pd.read_excel(IMF_LINKS_DOCUMENT_PATH)`
2. Open an IDE like VS Code, and create a `.env` file. This is where your file paths will go. Make sure there are no spaces in the file paths. Paste in and edit the contents like so:

```
IMF_LINKS_DOCUMENT_PATH=/absolute_file_path/to/IMF_file_list.csv
DROPBOX_FOLDER_PATH=/absolute_file_path/to/your_name/Dropbox
```

3. Run: `pip install -r requirements.txt`
4. Run: `python -m main.py`

5. Once the script has finished running, trigger a sync to dropbox and you should be good to go!
