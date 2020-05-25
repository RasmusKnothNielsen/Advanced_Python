# schedule1.py

import warnings

import osconfeed


DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn(f'loading {DB_NAME}')
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1] # remove plural s
        for record in rec_list:
            key = f'{record_type}.{record["serial"]}' # build key
            record['serial'] = key # update the record with the full key
            db[key] = Record(**record)
