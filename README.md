# Web Application แบบทดสอบ: การจัดการเทคโนโลยีสารสนเทศในอุตสาหกรรมการท่องเที่ยวและบริการ

เว็บแอปพลิเคชันระบบทดสอบความรู้และติวข้อสอบ (Interactive Quiz Web App) จำนวน 80 ข้อ ครอบคลุมเนื้อหาสำคัญตามหลักสูตรวิชา **"การจัดการเทคโนโลยีสารสนเทศในอุตสาหกรรมการท่องเที่ยวและบริการ"** พัฒนาขึ้นด้วยเทคโนโลยี HTML5, CSS3 และ Modern JavaScript แบบ Standalone Single-file พร้อมใช้งานได้ทันทีบนทุกอุปกรณ์ (Responsive Web Design)

🌐 **เข้าใช้งานออนไลน์ผ่าน GitHub Pages**: [https://wiwatpromwihan.github.io/tourism-it-quiz-app/](https://wiwatpromwihan.github.io/tourism-it-quiz-app/)

---

## 🎯 ฟังก์ชันการทำงานของระบบ (Key Features)

1. **หน้าแรก (Welcome Screen)**
   - สรุปรายละเอียดและโครงสร้างแบบทดสอบทั้ง 5 หมวดวิชา รวม 80 ข้อ
   - สวิตช์เปิด/ปิด **"โหมดสุ่มคำถาม (Shuffle Mode)"** สำหรับการฝึกซ้อมซ้ำ
   - ปุ่ม **"เริ่มทำแบบทดสอบ (80 ข้อ)"**

2. **ระบบการทำแบบทดสอบ (Interactive Quiz Screen)**
   - แสดงคำถามทีละ 1 ข้อ พร้อมตัวเลือก 4 ตัวเลือก (ก, ข, ค, ง)
   - แถบความคืบหน้า (Progress Bar) และตัวระบุหมวดหมู่วิชา
   - **ระบบ Interactive เฉลยทันที**: ไฮไลท์ **สีเขียว** ที่ข้อถูก และ **สีแดง** ที่ข้อผิดเมื่อผู้ใช้คลิกเลือก
   - **กล่องคำอธิบายเฉลยทางวิชาการ**: อธิบายเหตุผลและทฤษฎีอ้างอิงอย่างละเอียดใต้คำถาม
   - **ปุ่ม "ข้อถัดไป"**: ให้ผู้ใช้มีเวลาอ่านและทำความเข้าใจคำอธิบายเฉลยได้ตามต้องการ ก่อนก้าวสู่ข้อถัดไป

3. **หน้าสรุปผลการประเมิน (Comprehensive Result Screen)**
   - แสดงคะแนนรวมสุทธิ (Total Score / 80) และร้อยละ (%)
   - ป้ายระดับผลการประเมิน (ยอดเยี่ยม / ผ่านเกณฑ์มาตรฐาน / ควรทบทวนเพิ่มเติม)
   - **Section Breakdown**: กราฟแท่งจำแนกคะแนนตามรายหมวดทั้ง 5 ส่วน เพื่อวิเคราะห์จุดแข็ง-จุดอ่อน
   - **โหมดทบทวนข้อสอบ (Review Mode)**: แสดงรายการข้อสอบทั้ง 80 ข้อ พร้อมเปรียบเทียบคำตอบของผู้ใช้ เฉลยที่ถูกต้อง และคำอธิบาย
   - ปุ่ม **"ทำแบบทดสอบอีกครั้ง"** เพื่อเริ่มทำใหม่

---

## 📚 โครงสร้างคลังข้อสอบ 80 ข้อ (Question Bank Distribution)

| ส่วนที่ | หมวดหมู่เนื้อหา | จำนวนข้อ | ขอบเขตเนื้อหาหลัก |
| :---: | :--- | :---: | :--- |
| **1** | ความรู้เบื้องต้นเกี่ยวกับการบริการ | **10 ข้อ** | ทฤษฎีคุณลักษณะของการบริการ (Characteristics of Services: Intangibility, Inseparability, Variability, Perishability), Service Blueprint, Moment of Truth, GAP Model |
| **2** | คุณลักษณะเฉพาะทั้ง 8 ประการของ E-commerce | **20 ข้อ** | Ubiquity, Global Reach, Universal Standards, Richness, Interactivity, Information Density, Personalization/Customization, Social Technology |
| **3** | องค์ประกอบขององค์กรตามแผนธุรกิจ | **15 ข้อ** | โครงสร้าง Business Plan: Executive Summary, Value Proposition, 7Ps Marketing Mix, Operations Plan, Financial Plan, IT/Technology Plan, Risk Management |
| **4** | กรณีศึกษา IT ท่องเที่ยวและบริการในไทย | **20 ข้อ** | Happy Together, Facebook/LINE OA, การใช้ QR Code, การสร้าง Trust (ใบอนุญาตนำเที่ยว) & Utility, พฤติกรรมผู้บริโภค (ROPO, Showrooming, Webrooming, Browsers vs Buyers) |
| **5** | กรณีศึกษา IT ร้านเช่าชุดออนไลน์ Velia Rental Store | **15 ข้อ** | Instagram Marketing, การจัดการสต็อกคิวชุดและกล้อง, ปัญหา Double Booking และการแก้ด้วยระบบ Online Booking System, Time-based Reservation, การจัดการเงินประกัน |

---

## 💻 วิธีการเปิดใช้งานในเครื่อง (Local Usage)

สามารถเปิดใช้งานได้โดยตรงโดยไม่ต้องติดตั้งเซิร์ฟเวอร์หรือไลบรารีภายนอก:
1. ดาวน์โหลดหรือเปิดไฟล์ `index.html`
2. ดับเบิ้ลคลิกเพื่อเปิดผ่านเบราว์เซอร์ใดก็ได้ เช่น Google Chrome, Safari, Microsoft Edge หรือ Firefox
