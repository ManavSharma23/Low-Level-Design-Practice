# Create a simple hospital management system with these classes:
#   - Person
#   - Doctor
#   - Patient
#   - Appointment
#   - Hospital
# Requirements:
#   1. Person should contain common attributes such as name and age.
#   2. Doctor and Patient should inherit from Person.
#   3. Doctor should additionally have:
#       - Doctor ID
#       - Specialization
#       - Consultation fee
#   4. Patient should additionally have:
#       - Patient ID
#       - Medical history
#   5. Appointment should contain:
#       - Doctor
#       - Patient
#       - Appointment date
#       - Appointment status
#   6. Hospital should:
#       - Maintain a list of doctors and appointments.
#       - Allow patients to book appointments.
#       - Allow appointments to be cancelled.
#       - Display appointments for a particular doctor.
#   7. A doctor cannot have two appointments at the same date and time.




class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Doctor(Person):

    def __init__(self, name, age, doctor_id, specialization, consultancy_fee):
        super().__init__(name, age)
        self.__doctor_id = doctor_id
        self.__specialization = specialization
        self.__consultancy_fee = consultancy_fee

    def get_doctorID(self):
        return self.__doctor_id

    def get_specialization(self):
        return self.__specialization

    def get_consultancy_fee(self):
        return self.__consultancy_fee


class Patient(Person):

    def __init__(self, name, age, patient_id, medical_history):
        super().__init__(name, age)
        self.__patientID = patient_id
        self.__medical_history = medical_history

    def get_patientID(self):
        return self.__patientID

    def get_medicalHistory(self):
        return self.__medical_history


class Appointment:

    def __init__(self, doctor, patient, date, status):
        self.__doctor = doctor
        self.__patient = patient
        self.__date = date
        self.__status = status

    def get_doctor(self):
        return self.__doctor

    def get_patient(self):
        return self.__patient

    def get_date(self):
        return self.__date

    def get_status(self):
        return self.__status

    def cancel_appointment(self):
        self.__status = "Cancelled"


class Hospital:

    def __init__(self):
        self.__doctors = []
        self.__appointments = []

    def add_doctors(self, doctor):
        if doctor not in self.__doctors:
            self.__doctors.append(doctor)
            print("Doctor added successfully")
        else:
            print("Doctor already exists")

    def book_appointment(self, doctor, patient, date):

        if doctor not in self.__doctors:
            print("Doctor does not belong to this hospital")
            return

        for appointment in self.__appointments:

            if (appointment.get_doctor() == doctor
                and appointment.get_date() == date
                and appointment.get_status() == "Scheduled"):

                print("Doctor is already booked at this time")
                return

        new_appointment = Appointment(
            doctor, patient, date, "Scheduled"
        )

        self.__appointments.append(new_appointment)

        print("Appointment booked successfully")

    def cancel_appointment(self, appointment):

        if appointment in self.__appointments:

            if appointment.get_status() == "Scheduled":
                appointment.cancel_appointment()
                print("Appointment cancelled successfully")
            else:
                print("Appointment is already cancelled")

        else:
            print("Appointment not found")

    def display_appointments(self):

        if not self.__appointments:
            print("No appointments available")
            return

        for appointment in self.__appointments:

            print("------------------------")
            print("Doctor:", appointment.get_doctor().get_name())
            print("Patient:", appointment.get_patient().get_name())
            print("Date:", appointment.get_date())
            print("Status:", appointment.get_status())


    