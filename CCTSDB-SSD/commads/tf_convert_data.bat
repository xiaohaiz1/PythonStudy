::you can convert voc to tfrecord which type is train\test
SET DATASET_DIR=D:\CCTSDB-VOC2007
SET OUTPUT_DIR=D:\CCTSDB-TF
SET OUTPUT_NAME=voc_2007_train
python ../tf_convert_data.py^
    --dataset_name=pascalvoc^
    --dataset_dir=%DATASET_DIR%^
    --output_name=%OUTPUT_NAME%^
    --output_dir=%OUTPUT_DIR%