## account_move_payment_number (Odoo 15)

โมดูลเพิ่มฟิลด์ `Payment Number` บน Vendor Bill (account.move) เพื่อแสดงเลขที่เอกสาร Payment ที่ถูก reconcile กับบิลนั้น ช่วยให้ทีมบัญชีตรวจสอบการจ่ายได้สะดวกขึ้นทั้งในหน้าฟอร์มและรายการบิล

### Dependencies
- account

### Installation
ดูรายละเอียดใน [INSTALL.md](INSTALL.md)

### Usage (สรุป)
1. ไปที่ Vendor Bills
2. เปิดบิลที่มีการ Register Payment และ reconcile แล้ว
3. ระบบจะแสดงฟิลด์ `Payment Number` เป็นรายการเลขที่ Payment (คั่นด้วยเครื่องหมาย ,)

