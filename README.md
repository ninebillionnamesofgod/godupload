# Configuration
Copy conf.yaml.example to conf.yaml. Open the file and edit the server, username, password, master, count

The index.html should contain the latest version of the ninebillionnamesofgod homepage. If the page does not contain a marker add "<!--- clip -->" to the file as shown in index.html

# Run
This will update the index.html file and upload the master.mp3 and index file to the ftp server mentioned in the conf.yaml file

    $ python main.py
