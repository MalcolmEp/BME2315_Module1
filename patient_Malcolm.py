import csv

class Patient_Objects:  # Create the class

    all_patients = [] # Initialize the list of all patients

    def __init__(self, years_of_education: int, tTau_pg_ug: float, highest_level_education: str = "n/a", sex: str = "n/a"): # Constructors for every variable of interest
        self.years_of_education = years_of_education
        self.tTau_pg_ug = tTau_pg_ug
        self.highest_level_education = highest_level_education
        self.sex = sex
        Patient_Objects.all_patients.append(self)

    def __repr__(self):  # Return all attributes of a patient as a convenient string
            return f"({self.years_of_education} | {self.tTau_pg_ug} | {self.highest_level_education} | {self.sex})" 

    def years_of_education(self):
        return self.years_of_education

    def get_tTau_pg_ug(self):
        return self.tTau_pg_ug

    def highest_level_education(self):
        return self.highest_level_education

    def get_sex(self):
        return self.sex


    @classmethod 
    def instantiate_from_csv(cls, filename: str): # Instantiating patients from the data csv file
        cls.all_patients.clear() # Clears any existing list of patients
            
        with open(filename, encoding="utf8") as f: # Opening the data file and reading each line
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
        
             
            for row in rows_of_patients: # Assigning data table values to class defined variables
                    Patient_Objects(
                    years_of_education = (int(row["Years of education"])),
                    tTau_pg_ug = (float(row["tTAU pg/ug"])),
                    highest_level_education = row["Highest level of education"],
                    sex = row["Sex"]
                    )


    @classmethod
    def filter(cls, list, years_of_education = "any", tTau_pg_ug = "any", highest_level_education = "any", sex = "any"): # Filters the patient data by a given attribute
            all_patients = list
            remove_list = []
            attr_list = (
                        years_of_education,
                        tTau_pg_ug,
                        highest_level_education,
                        sex
                        )
            attr_name = (
                        "years_of_education",
                        "tTau_pg_ug",
                        "highest_level_education",
                        "sex"
                        )
            
            for attr in range(len(attr_list)):  
                if attr_list[attr] != "any":
                    for patient in all_patients:
                        if getattr(patient,attr_name[attr]) != attr_list[attr]:
                            remove_list.append(patient)
                    all_patients = [patient for patient in all_patients if patient not in remove_list]
                    remove_list.clear()

            return all_patients