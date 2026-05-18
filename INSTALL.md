## Vendor Bill Payment Number (Odoo 15) — คู่มือติดตั้ง

### 1) สิ่งที่ต้องมี
- Odoo 15
- โมดูลที่ต้องติดตั้งก่อน
  - account

### 2) ติดตั้งโมดูล (กรณีวางไฟล์บน Server)
1. วางโฟลเดอร์โมดูล `account_move_payment_number` ไว้ใน addons path ของระบบ
2. ตรวจสอบว่า `addons_path` ในไฟล์ config ของ Odoo ชี้มาที่โฟลเดอร์ดังกล่าวแล้ว
3. Restart service ของ Odoo
4. เปิด Odoo → Apps
5. เปิด Developer Mode (ถ้ายังไม่เปิด)
6. กด “Update Apps List”
7. ค้นหา `Vendor Bill Payment Number` แล้วกด Install หรือ Upgrade (ถ้าติดตั้งไว้แล้ว)

### 3) ติดตั้ง/อัปเกรดผ่านคำสั่ง (ทางเลือก)
- Upgrade เฉพาะโมดูล:
  - `-u account_move_payment_number`

### 4) ตรวจสอบผลลัพธ์
- ไปที่ Vendor Bills (หรือ Bills) แล้วเปิดบิลที่มีการจ่ายเงินและ reconcile แล้ว
- จะเห็นฟิลด์ `Payment Number`
  - หน้า Form: อยู่ถัดจากฟิลด์ `Reference`
  - หน้า List: อยู่ถัดจากฟิลด์ `Due Date`

### 5) ไฟล์สำคัญในโมดูล
- Manifest: `__manifest__.py`
- Logic: `models/account_move.py`
- View: `views/account_move_view.xml`

