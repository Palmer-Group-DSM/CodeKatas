# Medicine Clash

## Background
Prescription drugs are given as treatment for patients by doctors. There are many different types of prescriptions used to treat a variety of things. Not all prescription drugs can be taken at the same time because of interactions that may result in a bad outcome for the patient. Healthcare providers may be unaware of the medicine clash when prescribing the medication because it can take years to identify interactions between medications.

A Health Insurance company has recently discovered a medicine clash and needs to identify any patients who may be impacted by this problem. In order to find these patients,the company needs access to the database of patient medicine and prescription records. 

Once they have this information, they can notify the patient's healthcare provider. The provider can get the medication changed and keep the patient on the best course of treatment. Create a "Patient" class with a "Clash" method. The method takes a list of medications and how many days before today to consider (default to the previous 90 days), as arguments. A collection of days on which all of the medications were being taken during that period of time should be returned. 

___
Starter code is provided [here](http://github.com/emilybache/KataMedicineClash/blob/master/README.md) by the original author of Medicine Clash, Emily Bache.



## User Story

> As a Health Insurer,
> 
> I want to be able to search for patients who have a medicine clash,
> 
> So that I can alert their healthcare provider and get their medications changed.

## Data Format

Assume the data you need is in a database. This database can accessed in the code via an object oriented domain model. You only need focus on the following three entities and their attributes:

```
Patient
 - medicine

Medicine
- name
- prescriptions

Prescription
- dispense date
- days supply
```
## Assumptions

- Dispense date = medication start date.
- Days supply = number of days patient continues to take medication after the dispense date.
- If the patient has 2 overlapping prescriptions for the same medication assume they stop taking the earlier one.