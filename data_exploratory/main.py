import logging
import pandas as pd

from os import path
from pandas import DataFrame
from zipfile import ZipFile


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataExploratory:
    INPUT_FILE = 'COVID-19_Case_Surveillance_Public_Use_Data.csv'

    def run(self) -> None:
        """
        Runs the COVID-19 data exploratory.
        """
        dataframe = self._load_data()

        # TODO: Clean that `dataframe`

    def _load_data(self) -> DataFrame:
        """
        Extracts the COVID-19 zip file and load it as a `DataFrame`.
        """
        # Find the project directory
        # by moves 1 directory up from the current path
        base_path = path.abspath(path.dirname(__name__))

        input_path = f'{base_path}/inputs'
        input_file = f'{input_path}/{self.INPUT_FILE}'

        # Extracts the zip file if it doesn't exists
        logger.info('Extracting input file...')

        if not path.exists(input_file):
            with ZipFile(f'{input_file}.zip', 'r') as zip:
                zip.extractall(input_path)

        if not path.exists(input_file):
            raise FileNotFoundError(
                f'{self.INPUT_FILE} is not found in the zip file!'
            )

        # Load the CSV input file as a `DataFrame`
        logger.info('Loads the input file into a `DataFrame`...')

        dataframe = pd.read_csv(
            input_file,
            dtype={
                'cdc_report_dt': str,                   # The date when CDC reported
                'pos_spec_dt': str,                     # The date of the first positive specimen collection
                'onset_dt': str,                        # The onset date of the symptoms
                'current_status': str,                  # Current status of the person
                'sex': str,                             # Gender of the person
                'age_group': str,                       # Age group categories
                'Race and ethnicity (combined)': str,   # Race and Ethnicity (combined) / Case demographic
                'hosp_yn': str,                         # Was the patient hospitalized?
                'icu_yn': str,                          # Was the patient admitted to an intensive care unit (ICU)?
                'death_yn': str,                        # Did the patient die as a result of this illness?
                'medcond_yn': str,                      # Did they have any underlying medical conditions and/or risk behaviors?
            }
        )

        # Renames particular column name to make it more concise
        dataframe = dataframe.rename(columns={'Race and ethnicity (combined)': 'race_and_ethnicity'})

        return dataframe


if __name__ == '__main__':
    DataExploratory().run()
