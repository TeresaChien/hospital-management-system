from patient import Patient
from doctor import Doctor

class Prescription:
    def __init__(self, prescription_id, patient, doctor, medicine_name, dosage, frequency, duration, date):
        self.prescription_id = prescription_id
        self.patient = patient      
        self.doctor = doctor          
        self.medicine_name = medicine_name
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        self.date = date

    def issue_prescription(self):
        if self.duration <= 0:
            print("錯誤：天數必須大於0")
            return
        print("=== Prescription Information ===")
        print(f"Prescription ID: {self.prescription_id}")
        print(f"Patient ID: {self.patient.patient_id}")   
        print(f"Patient Name: {self.patient.name}")
        print(f"Doctor ID: {self.doctor.doctor_id}")      
        print(f"Doctor Name: {self.doctor.name}")
        print(f"Medicine: {self.medicine_name}")
        print(f"Dosage: {self.dosage}")
        print(f"Frequency: {self.frequency}")
        print(f"Duration: {self.duration} days")
        print(f"Date: {self.date}")
        print("------------------------------")

    def get_prescription(self):
        return {
            "prescription_id": self.prescription_id,
            "patient_id": self.patient.patient_id,
            "doctor_id": self.doctor.doctor_id,
            "medicine_name": self.medicine_name,
            "dosage": self.dosage,
            "frequency": self.frequency,
            "duration": self.duration,
            "date": self.date
        }

    def get_total_med_cost(self):
        cost_per_day = 50
        return cost_per_day * self.duration

    def cancel_prescription(self):
        print(f"Prescription {self.prescription_id} has been cancelled.")

# Test
if __name__ == "__main__":
    patient1 = Patient(101, "Amy", "123456778", "1991-03-02", "Female")
    doctor1 = Doctor(201, "Bob", "Cardiology", "Room 301")

    p = Prescription(
        prescription_id=1,
        patient=patient1,
        doctor=doctor1,
        medicine_name="Paracetamol",
        dosage="500mg",
        frequency="3 times a day",
        duration=5,
        date="2026-06-01"
    )

    p.issue_prescription()
    print(f"Medicine Cost: {p.get_medicine_cost()}")
