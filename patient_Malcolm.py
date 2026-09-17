import csv

class Patient_Objects:  # Create the class

    all_patients = [] # Initialize the list of all patients

    def __init__(self, age_at_death: int, brain_ph: float, tTau_pg_ug: float, donor_id: str = "n/a", sex: str = "n/a"): # Constructors for every variable of interest
        self.age_at_death = age_at_death
        self.brain_ph = brain_ph
        self.tTau_pg_ug = tTau_pg_ug
        self.donor_id = donor_id
        self.sex = sex
        Patient_Objects.all_patients.append(self)

    def __repr__(self):  # Return all attributes of a patient as a convenient string
            return f"({self.age_at_death} | ({self.brain_ph} | {self.tTau_pg_ug} | {self.donor_id} | {self.sex})" 

    def get_age_at_death(self):
        return self.age_at_death

    def get_brain_ph(self):
        return self.brain_ph

    def get_tTau_pg_ug(self):
        return self.tTau_pg_ug

    def get_donor_id(self):
        return self.donor_id

    def get_sex(self):
        return self.sex


    @classmethod
    def print_based_on_aad_sex(cls): # Checks if each patient is a female and has an age of death at or above 88. If so, it prints it
         for patient in Patient_Objects.all_patients:
              if patient.age_at_death >= 88 and patient.sex == "Female":
                   print(patient)


    @classmethod 
    def instantiate_from_csv(cls, filename: str): # Instantiating patients from the data csv file
            
        with open(filename, encoding="utf8") as f: # Opening the data file and reading each line
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
        
             
            for row in rows_of_patients: # Assigning data table values to class defined variables
                    Patient_Objects(
                    age_at_death = (int(row["Age at Death"])),
                    brain_ph = (float(row["Brain pH"])),
                    tTau_pg_ug = (float(row["tTAU pg/ug"])),
                    donor_id = row["Donor ID"],
                    sex = row["Sex"]
                    )


    @classmethod
    def get_age_at_death2(cls, age_at_death):  # Checks if the age at death of each patient equals the given age of death and prints the first one found
        for patient in Patient_Objects.all_patients:
            if age_at_death == patient.get_age_at_death(): 
                return patient


    @classmethod
    def filter(cls, list, age_at_death = "any", brain_ph = "any", tTau_pg_ug = "any", donor_id = "any", sex = "any"): # Filters the patient data by a given attribute
            all_patients = list
            remove_list = []
            attr_list = (
                        age_at_death,
                        brain_ph,
                        tTau_pg_ug,
                        donor_id,
                        sex
                        )
            attr_name = (
                        "age at death",
                        "brain ph",
                        "tTau pg ug",
                        "donor id",
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