"""
This experiment processes the "bbbp" dataset which is a small of organic molecules
which are divided into the two classes "pass" and "non-pass" in respect to the human blood brain barrier

CHANGELOG

0.1.0 - 23.02.23 - initial version

0.2.0 - 08.05.23 - moved to the pycomex functional API
"""
import os
import json
import pathlib
import typing as t

from pycomex.functional.experiment import Experiment
from pycomex.util import folder_path, file_namespace

PATH = pathlib.Path(__file__).parent.absolute()
ASSETS_PATH = os.path.join(PATH, 'assets')

# The vgd file share provider from which to download the CSV file to be used as the source for the VGD
# conversion.
FILE_SHARE_PROVIDER: str = 'main'
# This may be one of the following two things:
# 1. A valid absolute file path on the local system pointing to a CSV file to be used as the source for
#    the VGD conversion
# 2. A valid relative path to a CSV file stashed on the given vgd file share provider which will be
#    downloaded first and then processed.
CSV_FILE_NAME: str = os.path.join(ASSETS_PATH, 'tadf.csv')
# Optionally, this may define the string name of the CSV column which contains the integer index
# associated with each dataset element. If this is not given, then integer indices will be randomly
# generated for each element in the final VGD
INDEX_COLUMN_NAME: t.Optional[str] = None
# This has to be the string name of the CSV column which contains the SMILES string representation of
# the molecule.
SMILES_COLUMN_NAME: str = 'smiles'
# This has to be the string name of the CSV column which contains the target value
TARGET_TYPE: str = 'regression'
TARGET_COLUMN_NAMES: t.List[str] = ['splitting_energy', 'oscillator_strength', 'tadf_rate']

# == DATASET PARAMETERS ==
# These parameters control aspects of the visual graph dataset creation process

# The name given to the visual graph dataset folder which will be created.
DATASET_NAME: str = 'tadf'
# The width and height of the molecule visualization PNGs in pixels.
IMAGE_WIDTH: int = 1000
IMAGE_HEIGHT: int = 1000
# This dict will be converted into the .meta.yml file which will be added to the final visual graph dataset
# folder. This is an optional file, which can add additional meta information about the entire dataset
# itself. Such as documentation in the form of a description of the dataset etc.
DATASET_META: t.Optional[dict] = {
    'version': '0.1.0',
    # A list of strings where each element is a description about the changes introduced in a newer
    # version of the dataset.
    'changelog': [
        '0.1.0 - 29.01.2023 - initial version'
    ],
    # A general description about the dataset, which gives a general overview about where the data was
    # sampled from, what the input features look like, what the prediction target is etc...
    'description': (
        'A large dataset consisting of roughly half a million molecules annotated with properties '
        'relevant to their thermally activated delayed fluorescent (TADF) behavior. The dataset was '
        'created in a large scale virtual screening application using DFT calculations.'
    ),
    # A list of informative strings (best case containing URLS) which are used as references for the
    # dataset. This could for example be a reference to a paper where the dataset was first introduced
    # or a link to site where the raw data can be downloaded etc.
    'references': [
        'Library used for the processing and visualization of molecules. https://www.rdkit.org/',
    ],
    # A small description about how to interpret the visualizations which were created by this dataset.
    'visualization_description': (
        'Molecular graphs generated by RDKit based on the SMILES representation of the molecule.'
    ),
    # A dictionary, where the keys should be the integer indices of the target value vector for the dataset
    # and the values should be string descriptions of what the corresponding target value is about.
    'target_descriptions': {
        0: 'The singlet-triplet splitting energy of the molecule in eV',
        1: 'The oscillator strength of the molecule',
        2: 'The k_TADF rate'
    }
}

experiment = Experiment.extend(
    'generate_molecule_dataset_from_csv.py',
    base_path=folder_path(__file__),
    namespace=file_namespace(__file__),
    glob=globals(),
)

experiment.run_if_main()