## autoinfo_account_move_link_payment_number (Odoo 15)

โมดูลเพิ่มฟิลด์ `Payment Number` บน Vendor Bill (account.move) เพื่อแสดงเลขที่เอกสาร Payment ที่ถูก reconcile กับบิลนั้น ช่วยให้ทีมบัญชีตรวจสอบการจ่ายได้สะดวกขึ้นทั้งในหน้าฟอร์มและรายการบิล

### Dependencies
- account

### Installation
ดูรายละเอียดใน [INSTALL.md](INSTALL.md)

### Usage (สรุป)
1. ไปที่ Vendor Bills
2. เปิดบิลที่มีการ Register Payment และ reconcile แล้ว
3. ระบบจะแสดงฟิลด์ `Payment Number` เป็นรายการเลขที่ Payment (คั่นด้วยเครื่องหมาย ,)

### Task Summary (รายการที่ทำในงานนี้)
- ตรวจสอบโครงสร้างโมดูลและข้อมูลใน `__manifest__.py`
- เพิ่มคู่มือการใช้งาน/ติดตั้ง: `README.md`, `INSTALL.md`
- ปรับแพ็กเกจสำหรับปล่อยงานให้เป็นโมดูลเดียว (1 module) และจัดโครงสร้าง zip ให้ถูกต้อง
- อัปโหลดซอร์สขึ้น GitHub repository

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).
