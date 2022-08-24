# __MP4/M4A Tagger__

- This program is to tag __MP4/M4A__ media files using __Mutagen__.
- __Mutagen__ is a Python module to handle audio metadata and tags.

## __Installation__

1) First clone the repo.
```shell
git clone https://github.com/dropcreations/MP4_Tagger.git && cd MP4_Tagger
```
2) Install `mutagenMP4`.
```shell
pip install --editable .
```

## __Usage__

- You can add one MP4/M4A file at once.

```shell
mutagenMP4 [MP4/M4A_path]
```

## __Explanation__

- You can add multiple values to a tag by seperating it with a comma and a space (', ').

    `eg : Tag_Value_01, Tag_Value_02, Tag_Value_03,...`

- When you are adding lyrics, first save lyrics to a text file.
- Then add that text file's path when it asked.
- You can add more custom tags.
- Save all custom tags to text file or type one by one while running.
- If you are using a text file to add custom tags, text file's format must be as below.

    `Tag_Name_01: Tag_Value_01, Tag_Value_02, Tag_Value_03,...`<br>
    `Tag_Name_02: Tag_Value_01, Tag_Value_02, Tag_Value_03,...`

    eg:

    ![CustomTagsPreview](https://raw.githubusercontent.com/dropcreations/MP4_Tagger/main/CustomTags_Preview.png)

- You can add covers/albumarts. (PNG and JPG/JPEG are supported)
