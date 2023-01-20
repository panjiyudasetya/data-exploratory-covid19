import logging
import matplotlib.pyplot as plt
import pandas as pd

from os import path, makedirs
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
        dataframe = self._clean_data(dataframe)

        logger.info('Generating Pie Chart about the Case of Infected COVID-19...')
        self._get_pie_insight('current_status', dataframe, "Case of Infected COVID-19")

        logger.info('Generating Pie Chart about the Case of Demographic COVID-19...')
        self._get_pie_insight('race_and_ethnicity', dataframe, "Case of Demographic COVID-19")

        logger.info('Generating Pie Chart about the Case of Hospitalized Patient...')
        self._get_pie_insight('hosp_yn', dataframe, "Case of Hospitalized Patient")

    def _get_pie_insight(self, column_name: str, dataframe:DataFrame, title: str) -> None:
        """
        Get insight of the specific `column_name` in the given `dataframe`
        as the Pie Chart with a specific `title`.

        The method will also saves the generated Pie Chart
        into the output directory.
        """
        # Configures mathplot library
        plt.title(title, fontsize=18)

        # Converts the value counts of that `column_name` into Pie Chart
        pie_plot = dataframe[column_name].value_counts().plot.pie(autopct="%1.1f%%")
        pie_plot.yaxis.set_visible(False)

        # Create output directory if it doesn't exists
        base_path = path.abspath(path.dirname(__name__))
        outputs_path = f'{base_path}/outputs'

        if not path.exists(outputs_path):
            makedirs(outputs_path)

        # Saves the plot as PNG file
        plt.savefig(f'{outputs_path}/{title}.png', bbox_inches='tight')

        # Clear the current figure
        plt.close()

    def _clean_data(self, dataframe: DataFrame) -> DataFrame:
        """
        Cleans the COVID-19 `dataframe` and returns the clean one.
        """
        logger.info('Describing the COVID-19 dataframe...')
        logger.info(f'\n{dataframe.describe().T}\n')
        logger.info(f'Pair of rows and columns before cleaning {dataframe.shape}\n')

        logger.info('Cleaning null values...')
        # Based on the table description, we found that the table
        # has too many null values on the `pos_spec_dt` and `onset_dt` columns.
        # From 8405079 rows of data, we could see:
        # 1. The values of the `pos_spec_dt` column (approximately) 75% are null
        # 2. The values of the `onset_dt` column (approximately) 50% are null
        # Therefore, it's much better to ignore them.
        dataframe = dataframe.drop(
            ['pos_spec_dt','onset_dt'],
            axis=1  # 1 for dropping an entire column
        )

        # Removes the other null values across the columns
        dataframe = dataframe.dropna()

        logger.info('Describing the COVID-19 dataframe that has been cleaned...')
        logger.info(f'\n{dataframe.describe().T}\n')
        logger.info(f'Pair of rows and columns after cleaning {dataframe.shape}\n')

        return dataframe

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
