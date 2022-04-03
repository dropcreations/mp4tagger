# **MP4/M4A Tagger**

- This **python script** is to tag **MP4/M4A** media files using **Mutagen**.
- ***Mutagen*** is a Python module to handle audio metadata.

## **Install Mutagen**

- Read mutagen docs [here](https://mutagen.readthedocs.io/en/latest/index.html).

**`python3 -m pip install mutagen`**

or

**`sudo apt-get install python3-mutagen`**

## **Usage**

- If you want, add **`mutagen_MP4.py`** file to **System Variables**.
- Open **Terminal** and type below command.
- You can add one MP4/M4A media file at once.

**`python mutagen_MP4.py [mp4_or_m4a_file_path]`**

## **Explanation**

- You can add multiple values to a tag by seperating it with a comma and a space (', ').<br>
`eg : tag value 1, tag value 2, tag value 3,......`
- When you are adding lyrics, first save lyrics to a text file.
- Then add that text file's path when it ask.
- You can add more custom tags.
- Save all custom tags to a text file or type one by one while running the script.
- If you are using a text file to add custom tags, text file's format must be as below.<br>
`Tag name: tag value, tag value, tag value,....`<br>
`Tag name: tag value, tag value, tag value,....`<br>
 eg:<br>
`Director: Jon Watts`<br>
`Original Music Composer: Michael Giacchino`<br>
`Distribution: Columbia Pictures, Sony Pictures Releasing`<br>
`Cast: Tom Holland, Zendaya, Andrew Garfield, Tobey Maguire, Marisa Tomei`<br>
- You can add covers/albumarts. (PNG and JPG/JPEG are supported)

### **NOTE**
- This is completely tested on **Windows**.
