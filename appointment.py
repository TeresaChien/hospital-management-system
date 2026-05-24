from abc import ABC, abstractmethod
from datetime import date
from typing import List, Dict, Optional

from team_module import Patient, Doctor

class IAppointmentService(ABC):
    @abstractmethod
    def set_doctor_available_slots(self, doctor_id: int, appt_date: date, slots: List[str]):
        pass

    @abstractmethod
    def create_appointment(self, patient: Patient, doctor: Doctor, appt_date: date, time_str: str) -> Optional['Appointment']:
        pass

class Appointment:
    def __init__(self, appointment_id: str, patient: Patient, doctor: Doctor, appointment_date: date, time_str: str):
        self.appointment_id = appointment_id
        self.patient = patient   
        self.doctor = doctor     
        self.appointment_date = appointment_date
        self.time_str = time_str
        self.status = "Scheduled"

    def __str__(self):
        return f"[預約成功] 單號: {self.appointment_id} | 病人: {self.patient.name} -> 醫生: {self.doctor.name} ({self.doctor.specialization}) | 時間: {self.appointment_date} {self.time_str}"

class AppointmentManager(IAppointmentService):
    def __init__(self):
        self.appointments: Dict[str, Appointment] = {}
        self.doctor_schedules: Dict[int, Dict[date, List[str]]] = {}
        self._counter = 100

    def set_doctor_available_slots(self, doctor_id: int, appt_date: date, slots: List[str]):
        if doctor_id not in self.doctor_schedules:
            self.doctor_schedules[doctor_id] = {}
        self.doctor_schedules[doctor_id][appt_date] = slots

    def create_appointment(self, patient: Patient, doctor: Doctor, appt_date: date, time_str: str) -> Optional[Appointment]:
        doc_id = doctor.get_doctor_id() 
        
        if doc_id in self.doctor_schedules and appt_date in self.doctor_schedules[doc_id]:
            available_slots = self.doctor_schedules[doc_id][appt_date]
            
            if time_str in available_slots:
                available_slots.remove(time_str)
                self._counter += 1
                appt_id = f"APP{self._counter}"
                new_appt = Appointment(appt_id, patient, doctor, appt_date, time_str)
                self.appointments[appt_id] = new_appt
                return new_appt
                
        print(f"❌ 預約失敗：{doctor.name} 醫生在 {appt_date} {time_str} 沒有可預約的空位。")
        return None
