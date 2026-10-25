# E-Testing & Quiz Portal: ระบบแบบทดสอบวัดความรู้ทางวิชาการ (240 ข้อ)

เว็บแอปพลิเคชันระบบทดสอบความรู้และติวข้อสอบออนไลน์ (Interactive Quiz Portal) ครอบคลุม 3 รายวิชา รวม 240 ข้อ พัฒนาขึ้นด้วยเทคโนโลยี HTML5, CSS3 และ Modern JavaScript แบบ Standalone Single-file 100% สวยงาม ทันสมัย พร้อมระบบเฉลยละเอียดและวิเคราะห์คะแนน รองรับ Responsive บนทุกอุปกรณ์

🌐 **เข้าใช้งานออนไลน์ผ่าน GitHub Pages**: [https://wiwatpromwihan.github.io/tourism-it-quiz-app/](https://wiwatpromwihan.github.io/tourism-it-quiz-app/)

---

## 📚 รายวิชาที่มีในระบบ (Subject Modules)

### วิชาที่ 1: การจัดการเทคโนโลยีสารสนเทศในอุตสาหกรรมการท่องเที่ยวและบริการ (80 ข้อ)
- **ส่วนที่ 1 (10 ข้อ)**: ความรู้เบื้องต้นเกี่ยวกับการบริการ (Characteristics of Services: Intangibility, Inseparability, Variability, Perishability, Service Blueprint, Moment of Truth, GAP Model)
- **ส่วนที่ 2 (20 ข้อ)**: คุณลักษณะเฉพาะทั้ง 8 ประการของเทคโนโลยี E-commerce (Ubiquity, Global Reach, Universal Standards, Richness, Interactivity, Information Density, Personalization/Customization, Social Technology)
- **ส่วนที่ 3 (15 ข้อ)**: องค์ประกอบขององค์กรตามเเผนธุรกิจ (Business Plan: Executive Summary, 7Ps Service Marketing, Operations Plan, Financial Plan, IT Plan, Risk Management)
- **ส่วนที่ 4 (20 ข้อ)**: กรณีศึกษาการจัดการ IT ในธุรกิจท่องเที่ยวและบริการในไทย (Happy Together, Facebook/LINE OA, QR Code, Trust & Utility, ROPO, Showrooming, Browsers vs Buyers)
- **ส่วนที่ 5 (15 ข้อ)**: กรณีศึกษาการจัดการ IT ร้านเช่าชุดออนไลน์ Velia Rental Store (Instagram Marketing, สต็อกคิวชุดและกล้อง, ปัญหา Double Booking, Online Booking System, Time-based Reservation, Security Deposit)

### วิชาที่ 2: การพัฒนา Mobile Application ด้วย Flutter & Dart (80 ข้อ ระดับ ป.ตรี)
- **หมวดที่ 1 (15 ข้อ)**: สถาปัตยกรรมการทำงานของ Flutter และ Build System (Engine, Impeller/Skia, Widget/Element/RenderObject Tree, Hot Reload vs Hot Restart, pubspec.yaml, flutter pub get, pub.dev, APK Build debug vs release, split-per-abi)
- **หมวดที่ 2 (15 ข้อ)**: ภาษา Dart และหลักการ Object-Oriented Programming (Sound Null Safety, คีย์เวิร์ด `late`, `const` vs `final`, การสืบทอดคุณสมบัติ `extends`, `implements`, `with` mixin, `dart:convert`: `jsonDecode`, `jsonEncode`)
- **หมวดที่ 3 (20 ข้อ)**: Widgets พื้นฐานและการจัดวาง Layout (`StatelessWidget` vs `StatefulWidget`, `mainAxisAlignment`, `crossAxisAlignment`, `Positioned` inside Stack, `EdgeInsets.symmetric`, การแก้ปัญหา `A RenderFlex overflowed`, `GridView.count` กับ `crossAxisCount`, `Expanded`, `SizedBox`, `SafeArea`)
- **หมวดที่ 4 (15 ข้อ)**: Responsive Design และการจัดการฟอร์มรับข้อมูล (`MediaQuery.of(context).size.width`, `TextField` / `TextFormField`, `obscureText: true`, `TextEditingController`, Form Validation, `LayoutBuilder`, `SingleChildScrollView` แก้คีย์บอร์ดบัง)
- **หมวดที่ 5 (15 ข้อ)**: วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส (`initState()`, `dispose()`, `extends ChangeNotifier` กับ `notifyListeners()`, `Future<String> fetchName() async`, `FutureBuilder`, `StreamBuilder`, `Navigator.push/pop`, `if (!mounted) return`)

### วิชาที่ 3: อินเทอร์เน็ตของสรรพสิ่ง (IoT - 8312404) (80 ข้อ พร้อมแนวคำถามปลายภาค 25 ข้อ)
- **หมวดที่ 1 (16 ข้อ)**: สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT (ESP32, Publisher/Subscriber/Broker, Topic Hierarchy, Wildcards `+` และ `#`, `mosquitto_sub`/`mosquitto_pub`, Port 1883/8883, Retain flag, Client ID, QoS)
- **หมวดที่ 2 (16 ข้อ)**: การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED (Node-RED Architecture, `mqtt in`, `function` node, `switch` node, Gauges, Charts, UI Switches, Notification alerts, Port 1880)
- **หมวดที่ 3 (16 ข้อ)**: การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase (SQLite on Raspberry Pi, Timestamp, Relational schema, Firebase Realtime Database JSON Tree, `onValue` listener, Security Rules, Historical Data Analytics)
- **หมวดที่ 4 (16 ข้อ)**: การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ (การควบคุม Relay 220V ผ่าน ESP32, Active Low/High, IoT MQTT Panel, การแยก Topic ควบคุม 2 แชนแนล, Sampling rate vs Battery/Bandwidth, Feedback loop)
- **หมวดที่ 5 (16 ข้อ)**: การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม (Local Edge Server vs Cloud, Nginx Web Server, IP checking, Service auto-start `systemctl`, การออกแบบระบบ IoT ห้องเรียนครบวงจร)
- **ฟังก์ชันพิเศษ**: มีปุ่มกดดู **แนวทางข้อสอบปลายภาค 25 ข้อฉบับเต็ม** ในรูปแบบ Modal หน้าต่างอ่านทบทวน

---

## 🎯 ฟังก์ชันเด่นของระบบ (Key Features)

1. **หน้าแรก Subject Portal**: การ์ดแสดง 3 รายวิชาสไตล์ Dashboard สวยงาม สามารถคลิกเลือกวิชาหรือเปลี่ยนวิชาได้ตลอดเวลา
2. **ระบบสลับตัวเลือกเฉลยสมดุล (Balanced Distribution)**: คำตอบที่ถูกต้องถูกกระจายระหว่าง ก, ข, ค, ง เฉลี่ยเท่ากันอย่างเป็นธรรมชาติ (25.0% ต่อตัวเลือก) ทุกวิชา
3. **รองรับ Code Snippet Box**: ข้อสอบที่มีโค้ดโปรแกรม คำสั่ง CLI หรือคำสั่ง SQL จะถูกไฮไลท์ในกล่อง Monospace Dark Theme อ่านง่าย ชัดเจน
4. **ระบบตรวจคำตอบทันที (Instant Interactive Feedback)**: ไฮไลท์ **สีเขียว** ที่ข้อถูก และ **สีแดง** ที่ข้อผิดทันทีที่คลิก พร้อมกล่องคำอธิบายเฉลยทางวิชาการ
5. **ปุ่ม "ข้อถัดไป" (Manual Navigation)**: ควบคุมการเปลี่ยนข้อด้วยตนเอง ทำให้อ่านทำความเข้าใจเฉลยได้โดยไม่ต้องเร่งรีบ
6. **ระบบวิเคราะห์คะแนน (Section Breakdown)**: กราฟแท่งจำแนกคะแนนตาม 5 หมวดหมู่ย่อยของแต่ละวิชา ชี้ชัดจุดแข็ง-จุดอ่อน
7. **โหมดทบทวนข้อสอบ (Review Mode)**: แสดงรายการข้อสอบทั้ง 80 ข้อ พร้อมคำตอบที่เลือก เฉลยที่ถูกต้อง และคำอธิบาย
8. **โหมดสุ่มคำถาม (Shuffle Mode)**: สลับลำดับคำถามสำหรับใช้ฝึกซ้อมซ้ำ

---

## 💻 วิธีการเปิดใช้งานในเครื่อง (Local Usage)

เปิดไฟล์ `index.html` ผ่านเว็บเบราว์เซอร์ใดก็ได้ (Chrome, Safari, Edge, Firefox) โดยไม่ต้องติดตั้งโปรแกรมหรือเซิร์ฟเวอร์เสริม
