"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    collection_of_neo = []
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for elem in reader:

            if elem['pha'] == "Y":
                elem['pha'] = True
            else:
                elem['pha'] = False

            if elem['name'] == '':
                elem['name'] = None

            if elem['diameter'] == '':
                elem['diameter'] = float('nan')

            collection_of_neo.append(elem)

    return [NearEarthObject(designation=neo['pdes'], name=neo['name'], diameter=float(neo['diameter']), hazardous=neo['pha']) for neo in collection_of_neo]

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as f:
        content = json.load(f)
        fields = content["fields"]
        collection_of_ca_objects = []
        collection_of_ca = [dict(zip(fields,ca)) for ca in content["data"]]

    return [CloseApproach(time=ca['cd'], distance=float(ca['dist']), velocity=float(ca['v_rel']), designation=ca['des'],
    neo=None) for ca in collection_of_ca]
