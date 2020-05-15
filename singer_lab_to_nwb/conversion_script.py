# This is a conversion script for running Intan to NWB conversion on Singer Lab data
# ALP 5/15/2020

# import libraries
import numpy as np
import yaml
import os
from singer_lab_to_nwb.simple_conversion_module import simple_conversion_function

# set file directories -
base_path = 'C:\\Users\\apaulson3\\Desktop\\testingNWB\\'  # raw data filename
source_paths = dict(
    dir_ecephys_rhd=dict(
        type='dir',
        path=os.path.join(base_path, 'rawData\\A25_200317')
    ),
    # file_electrodes=dict(
    #     type='file',
    #     path=os.path.join(base_path,'impedances_example.csv')
    # )
)

f_nwb = os.path.join(base_path, 'my_experiment_test.nwb')  # output filename

# load metafile
metafile = 'template_metafile.yml'
with open(metafile, 'r') as f:
    metadata = yaml.safe_load(f)

# run conversion function
simple_conversion_function(source_paths=source_paths,
                           f_nwb=f_nwb,
                           metadata=metadata,
                           add_rhd=True,
                           )
