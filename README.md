# Data Exploration of COVID-19 in 2020

This repository is used for a research project to get insight into the COVID-19 cases that occurred in 2020 based on the public dataset available on [Kaggle](https://www.kaggle.com/datasets/arashnic/covid19-case-surveillance-public-use-dataset).

To run the project, you need to:
- Ensure `python3` is installed on your computer.
- Open a terminal and navigate to the directory where this project is located.
- Activate python virtual environment on your computer. Read [this one](https://docs.python.org/3/library/venv.html#creating-virtual-environments) if you are not familiar with it.
- Install python dependencies by running this command `$ pip3 install -r requirements.txt`
- Run command `$ ./run.sh`

## Questions
1. I want to see the comparison case between a person that is positive for COVID-19 and a person that probably infected by COVID-19.
2. I want to see the case of demographic COVID-19.
3. I want to see how many patients were hospitalized when COVID-19 occurred.
4. I want to see how many patients admitted to an ICU when COVID-19 occurred.
5. I want to see how many patients died due to COVID-19.
6. I want to see how many patients have underlying medical conditions/risk behaviors.
7. I want to see the comparison case between a person that is positive for COVID-19 and a person that probably infected by COVID-19 by their gender.
8. I want to see how many patients died due to COVID-19 with underlying medical conditions/risk behaviors.
9. I want to see the case of COVID-19 based on the person age groups.
10. I want to see how many patients were hospitalized when COVID-19 occurred based on the person age groups.
11. I want to see how many patients were admitted to an ICU based on the person age groups.

## Answers
1. Here is the comparison between a person that is positive for COVID-19 and a person that probably infected by COVID-19.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Infected%20COVID-19.png"/>
2. Here is the case of demographic COVID-19.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Demographic%20COVID-19.png"/>
3. Here is the hospitalized patient when COVID-19 occurred.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Hospitalized%20Patient.png"/>
4. Here is the patient who was admitted to an ICU when COVID-19 occurred.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Patient%20Admitted%20to%20an%20ICU.png"/>
5. Here is the patient who died due to COVID-19.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Death%20due%20to%20COVID-19.png"/>
6. Here is the patient who have underlying medical conditions/risk behaviors.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Underlying%20Medical%20Conditions%20or%20Risk%20Behavior.png"/>
7. Here is the comparison between a person that is positive for COVID-19 and a person that probably infected by COVID-19 by their gender.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Infected%20COVID-19%20by%20Gender.png"/>
8. Here is the patients who died due to COVID-19 with underlying medical conditions/risk behaviors.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Death%20due%20to%20COVID-19%20with%20underlying%20medical%20conditions%20or%20risk%20behavior.png"/>
9. Here is the case of COVID-19 based on the person age groups.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Infected%20COVID-19%20by%20Age%20Groups.png"/>
10. Here is the hospitalized patients based on the person age groups.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Hospitalized%20Patient%20by%20Age%20Groups.png"/>
11. Here is the case of patients admitted to an ICU based on the person age groups.<br/><br/><br/><img src="https://github.com/panjiyudasetya/data-exploratory-covid19/blob/main/outputs/Case%20of%20Patient%20Admitted%20to%20an%20ICU%20by%20Age%20Groups.png"/>

## Conclusion
- The dataset contains too many "Missing" information for us to make some conclusions.
- However, if we remove them, the dataset becomes would be significantly reduced to be explored.
- Hence, all the answers above are built while we consider all the missing parts.
