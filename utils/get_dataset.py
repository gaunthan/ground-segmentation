#!/usr/bin/env python3

import os
import zipfile
from pathlib import Path
from google_drive_downloader import GoogleDriveDownloader as gdd
from tqdm import tqdm


def get_cmu_corridor_dataset(dataset_path='./dataset'):
    dataset_path = Path(dataset_path)
    dataset_zipfile = dataset_path / 'cmu_corridor_dataset.zip'
    output_dir = dataset_path

    # Download dataset from google drive
    if not os.path.exists(dataset_zipfile):
        print("Could not find dataset, downloading...")
        gdd.download_file_from_google_drive(file_id='16yHVv2HIV2pqJj-Z1k8gRSb31enJeMdm',
                                            dest_path=dataset_zipfile,
                                            unzip=False)

    # Uncompress dataset
    fz = zipfile.ZipFile(dataset_zipfile, 'r')
    fz_list = fz.namelist()
    for file in tqdm(fz_list, total=len(fz_list), desc="Compressing dataset"):
        fz.extract(file, output_dir)


if __name__ == '__main__':
    get_cmu_corridor_dataset('./dataset')