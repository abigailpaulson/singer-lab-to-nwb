from singer_lab_to_nwb.ecephys import Intan2NWB
import os


def simple_conversion_function(source_paths, f_nwb, metadata, add_rhd=False):
    nwbfile = None

    # Adding ecephys
    if add_rhd:
        nwbfile = Intan2NWB(
            nwbfile=nwbfile,
            metadata=metadata,
            source_paths=source_paths
        )
        nwbfile.run_conversion()

    # save the file
    nwbfile.save(to_path=f_nwb)
    print('NWB file saved with size: ', os.stat(f_nwb).st_size / 1e6, ' mb')
