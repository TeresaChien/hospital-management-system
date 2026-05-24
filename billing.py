class Billing:
    # 類別變數 (Class variable)，用來自動生成不重複的帳單 ID
    _bill_id_counter = 1000 

    def __init__(self, patient, appointment=None, prescription=None):
        """
        Initialize a Bill object.
        :param patient: Patient object (包含病人基本資訊)
        :param appointment: Appointment object (用來獲取醫生看診費)
        :param prescription: Prescription object (用來獲取藥品費用)
        """
        Billing._bill_id_counter += 1
        # 自動生成唯一的帳單編號，例如 BILL-1001
        self.bill_id = f"BILL-{Billing._bill_id_counter}"
        self.patient = patient
        self.appointment = appointment
        self.prescription = prescription
        
        # 財務相關屬性初始化
        self.consultation_fee = 0.0
        self.medication_fee = 0.0
        self.tax_rate = 0.05  # 假設 5% 的標準營業稅
        self.total_amount = 0.0
        self.is_paid = False

        # 在物件初始化時，自動呼叫方法計算總金額
        self.calculate_total()

    def calculate_total(self):
        """Calculates the breakdown and total amount of the bill."""
        # 1. 從 Appointment 模組獲取看診費
        if self.appointment and hasattr(self.appointment, 'doctor'):
            # 使用 getattr 安全讀取醫生設定的費用，若組員沒寫則預設 500.0
            self.consultation_fee = getattr(self.appointment.doctor, 'consultation_fee', 500.0)
        else:
            self.consultation_fee = 500.0

        # 2. 從 Prescription 模組獲取藥品總費用
        if self.prescription and hasattr(self.prescription, 'get_total_med_cost'):
            self.medication_fee = self.prescription.get_total_med_cost()
        else:
            self.medication_fee = 0.0

        # 3. 計算包含稅金的總金額
        subtotal = self.consultation_fee + self.medication_fee
        self.total_amount = subtotal * (1 + self.tax_rate)

    def pay_bill(self, payment_method):
        """Processes the payment for the bill."""
        # 防呆機制：若已經付過錢，則不重複扣款
        if self.is_paid:
            print(f"[Notice] Bill {self.bill_id} has already been paid.")
            return
        
        # 變更付款狀態
        self.is_paid = True
        print(f"[Success] Payment of ${self.total_amount:.2f} processed via 【{payment_method}】.")

    def print_invoice(self):
        """Prints a structured financial invoice."""
        # 根據付款狀態顯示文字
        status = "PAID" if self.is_paid else "UNPAID"
        
        # 格式化輸出精美的英文收據
        print("\n" + "="*45)
        print(f"{'HOSPITAL MANAGEMENT SYSTEM - INVOICE':^45}")
        print("="*45)
        print(f" Bill ID       : {self.bill_id}")
        print(f" Patient Name  : {self.patient.name} (ID: {self.patient.patient_id})")
        print(f" Payment Status: {status}")
        print("-"*45)
        print(f" Consultation Fee :   ${self.consultation_fee:>10.2f}")
        print(f" Medication Fee   :   ${self.medication_fee:>10.2f}")
        print(f" Tax (5%)         :   ${(self.consultation_fee + self.medication_fee) * self.tax_rate:>10.2f}")
        print("-"*45)
        print(f" Total Amount Due :   ${self.total_amount:>10.2f}")
        print("="*45 + "\n")
