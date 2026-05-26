from patient import Patient
from doctor import Doctor
from prescription import Prescription 

class MedicalRecord:
    def __init__(self, record_id, patient, doctor, diagnosis, treatments, prescription=None):
        self.record_id = record_id
        self.patient = patient
        self.doctor = doctor 
        self.diagnosis = diagnosis
        self.treatments = treatments 
        self.prescription = prescription

    def display_record(self):
        print(f"=== Medical Record {self.record_id} ===")
        print(f"Patient: {self.patient.name} ({self.patient.patient_id})")
        print(f"Doctor: {self.doctor.name}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Treatments: {self.treatments}")
        if self.prescription:
            print(f"Associated Medicine: {self.prescription.medicine_name}")
        print("=================================\n")

class MedicalRecordManager:
    def __init__(self):
        self.records = {} 

    def create_record(self, patient: Patient, doctor: Doctor, diagnosis: str, treatments: str, prescription=None) -> MedicalRecord:
    record_id = f"REC{len(self.records) + 1:04d}" 
    new_record = MedicalRecord(record_id, patient, doctor, diagnosis, treatments, prescription)
    self.records[record_id] = new_record
    return new_record

    def get_patient_history(self, patient_id: str) -> list:
        return [rec for rec in self.records.values() if rec.patient.patient_id == patient_id]

# Test
if __name__ == "__main__":
    patient1 = Patient(101, "Amy", "123456778", "1991-03-02", "Female")
    doctor1 = Doctor(201, "Bob", "Cardiology", "Room 301")

    p1 = Prescription(1, patient1, doctor1, "Paracetamol", "500mg", "3 times a day", 5, "2026-06-01")

    record1 = MedicalRecord(
        record_id="REC-2026-001",
        patient=patient1,
        doctor=doctor1,
        diagnosis="Common Cold",
        treatments="Rest and hydration",
        prescription=p1
    )
    record1.display_record()
