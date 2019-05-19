#Create Dataset

Expect the following file structure:
```
|-images directory
  |-image files (filename format: *.jpg)
|-annotations directory
  |-xmls directory
    |-annotation files (filename format: *.xml)
  |-trimaps directory
    |-image files (filename format: *.jpg)
label_map.pbtxt
```

```
mkdir -p annotations/trimaps
```

```
python3 
```

python3 create_tf_record.py --label_map_path=label_map.pbtxt --data_dir=. --output_dir=. --num_shards=1