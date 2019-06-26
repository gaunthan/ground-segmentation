#!/usr/bin/env python3

import os
import zipfile
from google_drive_downloader import GoogleDriveDownloader as gdd

DATASET_ZIPFILE = './cmu_corridor_dataset.zip'
OUTPUT_DIR = './dataset'

# Download dataset from google drive
if not os.path.exists(DATASET_ZIPFILE):
    gdd.download_file_from_google_drive(file_id='16yHVv2HIV2pqJj-Z1k8gRSb31enJeMdm',
                                        dest_path=DATASET_ZIPFILE,
                                        unzip=False)

# Uncompressed dataset
fz = zipfile.ZipFile(DATASET_ZIPFILE, 'r')
for file in fz.namelist():
    fz.extract(file, OUTPUT_DIR)
