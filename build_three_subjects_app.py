# -*- coding: utf-8 -*-
import json
import random

# 1. Load Tourism questions
from generate_quiz import questions as tourism_questions
# 2. Load Mobile questions
from build_full_app import mobile_questions
# 3. Load IoT questions
from generate_iot_questions import iot_questions
# 4. Load Business Intelligence questions
from generate_bi_questions import bi_questions, bi_guidelines_20
from bi_written_exam_data import bi_written_questions_20

# 25 Original Guideline Questions for Reference Modal
iot_guidelines_25 = [
    "1. ในระบบ IoT ที่มี ESP32 ตรวจวัดอุณหภูมิและส่งข้อมูลผ่านเครือข่าย Wi-Fi ไปยัง MQTT Broker จงอธิบายลำดับการทำงานตั้งแต่การอ่านค่าจากเซ็นเซอร์จนกระทั่งผู้ใช้งานสามารถดูข้อมูลผ่านแอปพลิเคชันบนโทรศัพท์มือถือได้",
    "2. นักศึกษาต้องการจัดเก็บข้อมูลอุณหภูมิจาก ESP32 ลงในฐานข้อมูล SQLite บน Raspberry Pi จงยกตัวอย่างข้อมูลที่ควรบันทึกในแต่ละรายการอย่างน้อย 3 รายการ พร้อมอธิบายเหตุผลที่ต้องจัดเก็บข้อมูลเหล่านั้น",
    "3. ในการสื่อสารผ่าน MQTT จงอธิบายความแตกต่างระหว่างอุปกรณ์ที่ทำหน้าที่ส่งข้อมูล อุปกรณ์ที่ทำหน้าที่รับข้อมูล และตัวกลางที่จัดการการส่งต่อข้อความ พร้อมยกตัวอย่างการใช้งานในระบบ IoT",
    "4. นักศึกษาต้องการสร้างระบบตรวจวัดอุณหภูมิที่สามารถแสดงค่าปัจจุบันและดูข้อมูลย้อนหลังได้ จงอธิบายว่าระบบควรจัดเก็บข้อมูลทั้งสองประเภทอย่างไร และข้อมูลแต่ละประเภทเหมาะกับการนำไปใช้งานลักษณะใด",
    "5. Raspberry Pi สามารถทำหน้าที่เป็นเครื่องแม่ข่ายสำหรับระบบ IoT ได้ จงอธิบายข้อดีของการใช้ Raspberry Pi เป็นเครื่องแม่ข่ายภายในเครือข่าย เมื่อเปรียบเทียบกับการส่งข้อมูลจาก ESP32 ไปยังบริการบนอินเทอร์เน็ตโดยตรง",
    "6. ระบบ IoT มี ESP32 หลายตัวส่งข้อมูลอุณหภูมิและความชื้นไปยัง MQTT Broker เดียวกัน จงอธิบายหลักการออกแบบ MQTT Topic เพื่อให้สามารถระบุอุปกรณ์และประเภทข้อมูลได้อย่างชัดเจน พร้อมยกตัวอย่าง Topic อย่างน้อย 3 รายการ",
    "7. นักศึกษาใช้ Node-RED รับข้อมูลอุณหภูมิจาก ESP32 ผ่าน MQTT และต้องการแสดงค่าบน Dashboard จงอธิบายว่า Flow ควรประกอบด้วย Node ประเภทใดบ้าง และข้อมูลจะไหลผ่าน Node เหล่านั้นอย่างไร",
    "8. นักศึกษาต้องการพัฒนาเว็บไซต์แสดงข้อมูลจาก Firebase Realtime Database จงอธิบายแนวทางการเชื่อมต่อเว็บไซต์กับฐานข้อมูล และวิธีนำข้อมูลที่ได้รับมาแสดงเป็นตัวเลขบนหน้าเว็บไซต์",
    "9. หาก ESP32 ไม่สามารถเชื่อมต่อ MQTT Broker ได้ จงยกตัวอย่างสาเหตุที่เป็นไปได้อย่างน้อย 3 สาเหตุ พร้อมอธิบายวิธีตรวจสอบปัญหาเบื้องต้น",
    "10. นักศึกษาต้องการควบคุมหลอดไฟผ่าน Relay ที่เชื่อมต่อกับ ESP32 โดยใช้แอปพลิเคชัน IoT MQTT Panel จงอธิบายหลักการส่งคำสั่งควบคุมผ่าน MQTT และวิธีที่ ESP32 นำคำสั่งไปใช้เปิดหรือปิด Relay",
    "11. Raspberry Pi ติดตั้ง Nginx เพื่อให้บริการเว็บไซต์ภายในห้องปฏิบัติการ จงอธิบายขั้นตอนโดยสังเขปที่คอมพิวเตอร์เครื่องอื่นจะใช้เปิดเว็บไซต์ดังกล่าวผ่าน Web Browser และปัจจัยที่อาจทำให้ไม่สามารถเข้าถึงเว็บไซต์ได้",
    "12. นักศึกษาต้องการใช้ Firebase Realtime Database จัดเก็บข้อมูลจากเซ็นเซอร์หลายตัว จงเสนอแนวทางจัดโครงสร้างข้อมูลเพื่อแยกข้อมูลตามอุปกรณ์ พร้อมอธิบายประโยชน์ของการจัดโครงสร้างข้อมูลอย่างเป็นระบบ",
    "13. ในระบบ MQTT นักศึกษาสามารถใช้คำสั่ง mosquitto_pub และ mosquitto_sub เพื่อทดสอบการสื่อสารได้ จงอธิบายแนวทางการทดสอบส่งข้อความจากเครื่องหนึ่งไปยังอีกเครื่องหนึ่ง และวิธีตรวจสอบว่าการรับส่งข้อมูลทำงานถูกต้อง",
    "14. นักศึกษาต้องการสร้าง Dashboard แสดงอุณหภูมิ ความชื้น และสถานะการทำงานของ Relay จงเสนอรูปแบบการแสดงผลที่เหมาะสมสำหรับข้อมูลแต่ละประเภท พร้อมอธิบายเหตุผลในการเลือกใช้",
    "15. ระบบ IoT ใช้ ESP32 ส่งข้อมูลผ่าน MQTT ไปยัง Raspberry Pi ซึ่งมี Mosquitto, Node-RED และ SQLite จงอธิบายความสัมพันธ์ขององค์ประกอบทั้งสาม และลำดับการทำงานตั้งแต่ Raspberry Pi ได้รับข้อความจนกระทั่งข้อมูลถูกบันทึกลงฐานข้อมูล",
    "16. หากนักศึกษาต้องการตรวจสอบข้อมูลอุณหภูมิย้อนหลังในช่วงเวลาที่กำหนด จงอธิบายว่าการจัดเก็บข้อมูลในฐานข้อมูลมีประโยชน์อย่างไร และสามารถนำข้อมูลย้อนหลังไปใช้วิเคราะห์เรื่องใดได้บ้าง",
    "17. นักศึกษาต้องการให้ Node-RED ตรวจสอบค่าความชื้นที่ได้รับจาก MQTT และแสดงข้อความเตือนเมื่อความชื้นต่ำกว่า 40% จงอธิบายแนวทางออกแบบ Flow ตั้งแต่รับข้อมูลจนถึงการแจ้งเตือน",
    "18. ในระบบ IoT ที่ใช้ MQTT หาก Publisher ส่งข้อมูลไปยัง Topic ที่ไม่มี Subscriber ติดตามอยู่ จงอธิบายว่าจะเกิดอะไรขึ้นกับข้อความดังกล่าวภายใต้การส่งข้อความแบบปกติที่ไม่ได้ตั้งค่า Retain และไม่ได้ใช้กลไกเก็บข้อความสำหรับผู้รับที่ออฟไลน์",
    "19. นักศึกษาต้องการใช้ IoT MQTT Panel ควบคุม Relay จำนวน 2 ช่องที่เชื่อมต่อกับ ESP32 จงอธิบายวิธีออกแบบปุ่มควบคุมและการกำหนดข้อความคำสั่ง เพื่อให้สามารถควบคุม Relay แต่ละช่องได้อย่างอิสระ",
    "20. หาก Firebase Realtime Database ถูกกำหนดสิทธิ์ให้บุคคลทั่วไปสามารถอ่านและเขียนข้อมูลได้โดยไม่ต้องยืนยันตัวตน จงวิเคราะห์ผลกระทบที่อาจเกิดขึ้นกับความถูกต้องของข้อมูลและความปลอดภัยของระบบ พร้อมเสนอแนวทางลดความเสี่ยง",
    "21. นักศึกษาต้องการให้ ESP32 ส่งข้อมูลอุณหภูมิทุก 10 วินาที จงอธิบายว่าการกำหนดความถี่ในการส่งข้อมูลมีผลต่อปริมาณข้อมูลที่ส่งผ่านเครือข่ายอย่างไร และควรพิจารณาปัจจัยใดบ้างในการเลือกช่วงเวลาส่งข้อมูล",
    "22. นักศึกษาต้องการสร้างระบบ IoT ที่สามารถดูค่าอุณหภูมิจากโทรศัพท์มือถือและสั่งเปิด–ปิดพัดลมได้ จงอธิบายว่าแอปพลิเคชันควรมีส่วนแสดงผลและส่วนควบคุมอะไรบ้าง และแต่ละส่วนทำงานร่วมกับ MQTT อย่างไร",
    "23. หาก Raspberry Pi ได้รับข้อมูลอุณหภูมิจาก ESP32 ผ่าน MQTT แล้วต้องการบันทึกข้อมูลลง SQLite โดยใช้ Node-RED จงอธิบายขั้นตอนการประมวลผลข้อมูลที่จำเป็นก่อนนำข้อมูลไปจัดเก็บในฐานข้อมูล",
    "24. นักศึกษาต้องการตรวจสอบว่า MQTT Broker บน Raspberry Pi ทำงานได้ตามปกติหรือไม่ โดยใช้คอมพิวเตอร์อีกเครื่องหนึ่งในเครือข่ายเดียวกัน จงอธิบายวิธีทดสอบการเชื่อมต่อและการรับส่งข้อความ พร้อมระบุสิ่งที่ต้องตรวจสอบหากการทดสอบไม่สำเร็จ",
    "25. จงออกแบบระบบ IoT สำหรับตรวจวัดอุณหภูมิในห้องเรียน โดยใช้ ESP32, MQTT Broker, Node-RED และ Dashboard พร้อมอธิบายหน้าที่ของแต่ละองค์ประกอบ และลำดับการทำงานของระบบตั้งแต่ตรวจวัดข้อมูลจนถึงการแสดงผลให้ผู้ใช้งานเห็น"
]

# Helper function to evenly balance correct answers across 0, 1, 2, 3
def balance_and_shuffle_choices(q_list, seed=42):
    random.seed(seed)
    target_assignments = [i % 4 for i in range(len(q_list))]
    random.shuffle(target_assignments)
    
    balanced_list = []
    for idx, q in enumerate(q_list):
        new_q = dict(q)
        original_choices = list(q["choices"])
        orig_correct_idx = q["correctAnswer"]
        correct_choice_text = original_choices[orig_correct_idx]
        wrong_choices = [c for i, c in enumerate(original_choices) if i != orig_correct_idx]
        random.shuffle(wrong_choices)
        
        target_correct_pos = target_assignments[idx]
        
        new_choices = []
        wrong_ptr = 0
        for pos in range(4):
            if pos == target_correct_pos:
                new_choices.append(correct_choice_text)
            else:
                new_choices.append(wrong_choices[wrong_ptr])
                wrong_ptr += 1
                
        new_q["choices"] = new_choices
        new_q["correctAnswer"] = target_correct_pos
        balanced_list.append(new_q)
        
    return balanced_list

balanced_tourism = balance_and_shuffle_choices(tourism_questions, seed=101)
balanced_mobile = balance_and_shuffle_choices(mobile_questions, seed=202)
balanced_iot = balance_and_shuffle_choices(iot_questions, seed=303)

# Print distribution of correct answers
def print_dist(name, q_list):
    dist = {0: 0, 1: 0, 2: 0, 3: 0}
    letters = ['ก', 'ข', 'ค', 'ง']
    for q in q_list:
        dist[q['correctAnswer']] += 1
    print(f"Distribution for {name}:")
    for k, v in dist.items():
        print(f"  {letters[k]} ({k}): {v} ข้อ ({v/len(q_list)*100:.1f}%)")

print_dist("Tourism IT", balanced_tourism)
print_dist("Mobile Application", balanced_mobile)
print_dist("Internet of Things", balanced_iot)
print_dist("Business Intelligence", bi_questions)

# Build subjects dictionary
subjects = {
    "tourism": {
        "id": "tourism",
        "title": "การจัดการเทคโนโลยีสารสนเทศในอุตสาหกรรมการท่องเที่ยวและบริการ",
        "badge": "สาขาวิชาการท่องเที่ยวและบริการดิจิทัล",
        "description": "คลังข้อสอบมาตรฐานจำนวน 80 ข้อ ครอบคลุมคุณลักษณะของการบริการ, E-commerce 8 ประการ, โครงสร้างแผนธุรกิจ, กรณีศึกษา IT ทัวร์ไทย และกรณีศึกษา Velia Rental Store",
        "sections": [
            {"name": "ส่วนที่ 1: ความรู้เบื้องต้นเกี่ยวกับการบริการ", "count": 10},
            {"name": "ส่วนที่ 2: คุณลักษณะเฉพาะทั้ง 8 ประการของเทคโนโลยี E-commerce", "count": 20},
            {"name": "ส่วนที่ 3: องค์ประกอบขององค์กรตามเเผนธุรกิจ", "count": 15},
            {"name": "ส่วนที่ 4: กรณีศึกษาการจัดการ IT ในธุรกิจท่องเที่ยวและบริการในไทย", "count": 20},
            {"name": "ส่วนที่ 5: กรณีศึกษาการจัดการ IT ร้านเช่าชุดออนไลน์ Velia Rental Store", "count": 15}
        ],
        "questions": balanced_tourism
    },
    "mobile": {
        "id": "mobile",
        "title": "การพัฒนา Mobile Application (Flutter & Dart)",
        "badge": "สาขาวิทยาการคอมพิวเตอร์ / เทคโนโลยีสารสนเทศ",
        "description": "แนวข้อสอบมาตรฐานระดับปริญญาตรี 80 ข้อ พร้อมโค้ดตัวอย่าง ครอบคลุม Flutter Architecture, Dart OOP, Widgets & Layout, Responsive & Form, และ State Management & Async",
        "sections": [
            {"name": "สถาปัตยกรรมการทำงานของ Flutter และ Build System", "count": 15},
            {"name": "ภาษา Dart และหลักการ Object-Oriented Programming", "count": 15},
            {"name": "Widgets พื้นฐานและการจัดวาง Layout", "count": 20},
            {"name": "Responsive Design และการจัดการฟอร์มรับข้อมูล", "count": 15},
            {"name": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส", "count": 15}
        ],
        "questions": balanced_mobile
    },
    "iot": {
        "id": "iot",
        "title": "อินเทอร์เน็ตของสรรพสิ่ง (IoT - 8312404)",
        "badge": "วิชา: อินเทอร์เน็ตของสรรพสิ่ง (8312404)",
        "description": "แนวทางข้อสอบปลายภาค 80 ข้อ พร้อมเฉลยละเอียดทางวิชาการและแนวคิดเชิงระบบ ครอบคลุม ESP32, MQTT Broker, Node-RED, SQLite บน Raspberry Pi, Firebase Realtime Database, Nginx และการควบคุม Relay",
        "sections": [
            {"name": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT", "count": 16},
            {"name": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED", "count": 16},
            {"name": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase", "count": 16},
            {"name": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ", "count": 16},
            {"name": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม", "count": 16}
        ],
        "guidelines": iot_guidelines_25,
        "questions": balanced_iot
    },
    "bi": {
        "id": "bi",
        "title": "ธุรกิจอัจฉริยะ (Business Intelligence Blueprint)",
        "badge": "สาขาวิชาเทคโนโลยีสารสนเทศ / วิทยาการข้อมูล",
        "description": "แบบทดสอบมาตรฐานระดับปริญญาตรี 80 ข้อ ครอบคลุม Data Roles (DE, DA, DS), Data Quality 6 มิติ, การคลีนข้อมูลด้วย Power Query, Star Schema Data Modeling, Cardinality, DAX Measures และการเลือกวิชวลตอบคำถามธุรกิจ",
        "sections": [
            {"name": "หมวดที่ 1: บทบาทหน้าที่และสถาปัตยกรรมงานข้อมูล (Data Roles & Pipeline)", "count": 16},
            {"name": "หมวดที่ 2: คุณภาพข้อมูลและการทำความสะอาดข้อมูลด้วย Power Query", "count": 16},
            {"name": "หมวดที่ 3: การแปลงข้อมูลขั้นสูงและกฎเกณฑ์ความถูกต้อง (Transformation & Validation)", "count": 16},
            {"name": "หมวดที่ 4: การสร้างแบบจำลองข้อมูลและโครงสร้าง Star Schema", "count": 16},
            {"name": "หมวดที่ 5: การคำนวณด้วย DAX และการเลือกวิชวลตอบโจทย์ธุรกิจ (Data Visualization)", "count": 16}
        ],
        "guidelines": bi_guidelines_20,
        "written_exam": bi_written_questions_20,
        "questions": bi_questions
    }
}

subjects_json = json.dumps(subjects, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ระบบแบบทดสอบวัดความรู้ทางวิชาการ (Academic Quiz Portal)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Prompt:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #eff6ff;
      --primary-glow: rgba(37, 99, 235, 0.15);
      --success: #10b981;
      --success-light: #ecfdf5;
      --success-border: #a7f3d0;
      --danger: #ef4444;
      --danger-light: #fef2f2;
      --danger-border: #fecaca;
      --warning: #f59e0b;
      --bg-body: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-light: #94a3b8;
      --border-subtle: #e2e8f0;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -2px rgba(0,0,0,0.05);
      --shadow-lg: 0 10px 25px -5px rgba(0,0,0,0.08), 0 8px 10px -6px rgba(0,0,0,0.04);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --font-th: 'Prompt', sans-serif;
      --font-en: 'Plus Jakarta Sans', sans-serif;
      --font-code: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-th);
      background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding: 24px 16px;
      line-height: 1.6;
    }}

    .container {{
      width: 100%;
      max-width: 920px;
      margin: 0 auto;
    }}

    .card {{
      background: var(--card-bg);
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      box-shadow: var(--shadow-lg);
      border: 1px solid rgba(255, 255, 255, 0.8);
      position: relative;
      overflow: hidden;
      backdrop-filter: blur(10px);
    }}

    .card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 6px;
      background: linear-gradient(90deg, #2563eb, #0ea5e9, #10b981, #f59e0b);
    }}

    .app-header {{
      text-align: center;
      margin-bottom: 28px;
    }}

    .badge-course {{
      display: inline-block;
      padding: 6px 16px;
      background: var(--primary-light);
      color: var(--primary);
      font-size: 0.85rem;
      font-weight: 600;
      border-radius: 999px;
      border: 1px solid rgba(37, 99, 235, 0.2);
      margin-bottom: 12px;
      letter-spacing: 0.3px;
    }}

    .app-title {{
      font-size: 1.65rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 8px;
      line-height: 1.35;
    }}

    .app-subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
    }}

    .screen {{
      display: none;
    }}

    .screen.active {{
      display: block;
      animation: fadeIn 0.3s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(8px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* ================= PORTAL SCREEN ================= */
    .portal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
      gap: 20px;
      margin: 24px 0 12px 0;
    }}

    .subject-card {{
      background: #ffffff;
      border: 2px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 24px 20px;
      transition: all 0.25s ease;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      box-shadow: var(--shadow-sm);
    }}

    .subject-card:hover {{
      border-color: var(--primary);
      transform: translateY(-4px);
      box-shadow: 0 12px 24px -10px rgba(37, 99, 235, 0.2);
    }}

    .subject-icon-box {{
      width: 50px;
      height: 50px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;
    }}

    .subject-icon-box.blue {{
      background: #eff6ff;
      color: #2563eb;
    }}

    .subject-icon-box.indigo {{
      background: #e0e7ff;
      color: #4f46e5;
    }}

    .subject-icon-box.emerald {{
      background: #ecfdf5;
      color: #059669;
    }}

    .subject-card-title {{
      font-size: 1.12rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
      line-height: 1.4;
    }}

    .subject-card-desc {{
      font-size: 0.86rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 18px;
      flex-grow: 1;
    }}

    .subject-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 14px;
      border-top: 1px solid var(--border-subtle);
    }}

    .subject-pill {{
      font-size: 0.8rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 20px;
      background: #f1f5f9;
      color: var(--text-main);
    }}

    .btn-select {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* ================= SYLLABUS BOX ================= */
    .syllabus-box {{
      background: #f8fafc;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 20px 0;
    }}

    .syllabus-title {{
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 14px;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .syllabus-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .syllabus-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.92rem;
      padding: 10px 14px;
      background: white;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
    }}

    .syllabus-name {{
      font-weight: 500;
      color: var(--text-main);
    }}

    .syllabus-count {{
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-light);
      padding: 2px 10px;
      border-radius: 12px;
      font-size: 0.82rem;
      white-space: nowrap;
    }}

    /* Guidelines Banner Box */
    .guideline-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: var(--radius-md);
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .guideline-info {{
      font-size: 0.92rem;
      color: #166534;
      font-weight: 600;
    }}

    .btn-view-guidelines {{
      background: #16a34a;
      color: white;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: background 0.2s;
    }}

    .btn-view-guidelines:hover {{
      background: #15803d;
    }}

    /* Modal for Guidelines */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(15, 23, 42, 0.7);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 20px;
      backdrop-filter: blur(4px);
    }}

    .modal-overlay.active {{
      display: flex;
    }}

    .modal-card {{
      background: white;
      border-radius: var(--radius-lg);
      max-width: 800px;
      width: 100%;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }}

    .modal-header {{
      padding: 20px 24px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .modal-close {{
      background: none;
      border: none;
      font-size: 1.5rem;
      cursor: pointer;
      color: var(--text-muted);
      line-height: 1;
    }}

    .modal-body {{
      padding: 24px;
      overflow-y: auto;
      font-size: 0.92rem;
      line-height: 1.65;
    }}

    .guideline-item {{
      margin-bottom: 14px;
      padding: 12px 14px;
      background: #f8fafc;
      border-radius: var(--radius-sm);
      border-left: 4px solid #10b981;
    }}

    .options-box {{
      margin: 20px 0;
      padding: 16px 20px;
      background: #f1f5f9;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
    }}

    .options-box input[type="checkbox"] {{
      width: 20px;
      height: 20px;
      accent-color: var(--primary);
      cursor: pointer;
    }}

    .options-box label {{
      cursor: pointer;
      font-weight: 500;
      color: var(--text-main);
      font-size: 0.95rem;
    }}

    /* ================= QUIZ SCREEN ================= */
    .quiz-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .section-pill {{
      font-size: 0.8rem;
      font-weight: 600;
      background: #e0e7ff;
      color: #3730a3;
      padding: 4px 12px;
      border-radius: 20px;
    }}

    .progress-text {{
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
    }}

    .progress-bar-container {{
      height: 8px;
      background: var(--border-subtle);
      border-radius: 999px;
      overflow: hidden;
      margin-bottom: 24px;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #2563eb, #38bdf8);
      width: 0%;
      transition: width 0.3s ease;
    }}

    .question-box {{
      margin-bottom: 20px;
    }}

    .question-number {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 6px;
      letter-spacing: 0.5px;
    }}

    .question-text {{
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.55;
      margin-bottom: 12px;
    }}

    /* Code Snippet Box */
    .code-box {{
      background: #0f172a;
      color: #e2e8f0;
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      margin: 12px 0 16px 0;
      font-family: var(--font-code);
      font-size: 0.88rem;
      line-height: 1.5;
      overflow-x: auto;
      border-left: 4px solid #38bdf8;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
    }}

    /* Choices */
    .choices-grid {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 24px;
    }}

    .choice-btn {{
      width: 100%;
      text-align: left;
      padding: 16px 20px;
      border-radius: var(--radius-md);
      border: 2px solid var(--border-subtle);
      background: white;
      font-family: var(--font-th);
      font-size: 0.98rem;
      color: var(--text-main);
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }}

    .choice-btn:hover:not(:disabled) {{
      border-color: var(--primary);
      background: var(--primary-light);
      transform: translateY(-1px);
    }}

    .choice-letter {{
      min-width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #f1f5f9;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.85rem;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }}

    .choice-btn:hover:not(:disabled) .choice-letter {{
      background: var(--primary);
      color: white;
    }}

    .choice-btn.correct {{
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: #065f46 !important;
      font-weight: 600;
    }}
    .choice-btn.correct .choice-letter {{
      background: var(--success) !important;
      color: white !important;
    }}

    .choice-btn.wrong {{
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
      color: #991b1b !important;
      font-weight: 600;
    }}
    .choice-btn.wrong .choice-letter {{
      background: var(--danger) !important;
      color: white !important;
    }}

    .choice-btn:disabled {{
      cursor: default;
    }}

    /* Explanation */
    .explanation-card {{
      display: none;
      padding: 20px 24px;
      border-radius: var(--radius-md);
      margin-bottom: 24px;
      border: 1px solid;
      animation: fadeIn 0.3s ease;
    }}

    .explanation-card.is-correct {{
      background: var(--success-light);
      border-color: var(--success-border);
      color: #065f46;
    }}

    .explanation-card.is-wrong {{
      background: var(--danger-light);
      border-color: var(--danger-border);
      color: #991b1b;
    }}

    .explanation-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      font-size: 1rem;
      margin-bottom: 8px;
    }}

    .explanation-body {{
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    /* Action buttons */
    .quiz-action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-top: 12px;
    }}

    .btn {{
      padding: 14px 28px;
      border-radius: var(--radius-md);
      font-family: var(--font-th);
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      border: none;
      box-shadow: var(--shadow-md);
      text-decoration: none;
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: white;
    }}

    .btn-primary:hover {{
      background: linear-gradient(135deg, #1d4ed8, #1e40af);
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
    }}

    .btn-secondary {{
      background: #f1f5f9;
      color: var(--text-main);
      border: 1px solid var(--border-subtle);
    }}

    .btn-secondary:hover {{
      background: #e2e8f0;
    }}

    .btn-full {{
      width: 100%;
    }}

    /* ================= RESULT SCREEN ================= */
    .result-score-card {{
      text-align: center;
      padding: 32px 20px;
      background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 100%);
      border-radius: var(--radius-md);
      border: 1px solid #bfdbfe;
      margin-bottom: 28px;
    }}

    .score-big {{
      font-family: var(--font-en);
      font-size: 3.5rem;
      font-weight: 800;
      color: var(--primary);
      line-height: 1;
      margin-bottom: 8px;
    }}

    .score-total {{
      font-size: 1.5rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .score-percent {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 12px;
    }}

    .grade-badge {{
      display: inline-block;
      padding: 6px 20px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.95rem;
    }}

    .grade-badge.excellent {{
      background: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }}

    .grade-badge.good {{
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }}

    .grade-badge.needs-work {{
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fde68a;
    }}

    .section-breakdown-box {{
      margin-bottom: 28px;
    }}

    .section-breakdown-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 14px;
    }}

    .breakdown-row {{
      background: #f8fafc;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      margin-bottom: 10px;
    }}

    .breakdown-info {{
      display: flex;
      justify-content: space-between;
      margin-bottom: 6px;
      font-size: 0.9rem;
      font-weight: 600;
    }}

    .breakdown-bar-bg {{
      height: 8px;
      background: #e2e8f0;
      border-radius: 4px;
      overflow: hidden;
    }}

    .breakdown-bar-fill {{
      height: 100%;
      border-radius: 4px;
      transition: width 0.4s ease;
    }}

    .result-buttons {{
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
    }}

    /* ================= REVIEW SCREEN ================= */
    .review-container {{
      margin-top: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .review-item {{
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px;
      box-shadow: var(--shadow-sm);
    }}

    .review-item.was-correct {{
      border-left: 5px solid var(--success);
    }}

    .review-item.was-wrong {{
      border-left: 5px solid var(--danger);
    }}

    .review-q-num {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}

    .review-q-text {{
      font-weight: 600;
      margin-bottom: 10px;
      font-size: 0.98rem;
    }}

    .review-answers {{
      font-size: 0.9rem;
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 10px;
    }}

    .review-user-ans {{
      font-weight: 600;
    }}
    .review-user-ans.correct {{
      color: var(--success);
    }}
    .review-user-ans.wrong {{
      color: var(--danger);
    }}

    .review-correct-ans {{
      color: #065f46;
      font-weight: 600;
    }}

    .review-exp {{
      font-size: 0.88rem;
      color: var(--text-muted);
      background: #f8fafc;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border-left: 3px solid #cbd5e1;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .card {{
        padding: 24px 18px;
      }}
      .app-title {{
        font-size: 1.35rem;
      }}
      .portal-grid {{
        grid-template-columns: 1fr;
      }}
      .choice-btn {{
        padding: 12px 14px;
        font-size: 0.92rem;
      }}
      .score-big {{
        font-size: 2.8rem;
      }}
      .result-buttons {{
        flex-direction: column;
      }}
      .quiz-action-bar {{
        flex-direction: column;
        align-items: stretch;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <header class="app-header">
        <span class="badge-course" id="topBadge">ศูนย์การเรียนรู้และทดสอบวัดระดับมาตรฐาน (E-Testing Portal)</span>
        <h1 class="app-title" id="topTitle">ระบบแบบทดสอบวัดความรู้ความสามารถทางวิชาการ</h1>
        <p class="app-subtitle" id="topSubtitle">เลือกรายวิชาที่ต้องการทดสอบเพื่อเริ่มทำแบบทดสอบและประเมินผล</p>
      </header>

      <!-- ================= 0. PORTAL SCREEN (SUBJECT SELECTION) ================= -->
      <section id="portalScreen" class="screen active">
        <div class="portal-grid">
          <!-- Card Subject 1 -->
          <div class="subject-card" onclick="selectSubject('tourism')">
            <div>
              <div class="subject-icon-box blue">
                <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h2 class="subject-card-title">การจัดการ IT ในอุตสาหกรรมการท่องเที่ยวและบริการ</h2>
              <p class="subject-card-desc">ทฤษฎีลักษณะบริการ (Characteristics of Services), E-commerce 8 คุณลักษณะ, แผนธุรกิจบริการ, กรณีศึกษา IT ทัวร์ไทย และร้านเช่าชุด Velia Rental Store</p>
            </div>
            <div class="subject-footer">
              <span class="subject-pill">80 ข้อ</span>
              <span class="btn-select">
                เข้าทำข้อสอบ
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
              </span>
            </div>
          </div>

          <!-- Card Subject 2 -->
          <div class="subject-card" onclick="selectSubject('mobile')">
            <div>
              <div class="subject-icon-box indigo">
                <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
              </div>
              <h2 class="subject-card-title">การพัฒนา Mobile Application (Flutter & Dart)</h2>
              <p class="subject-card-desc">ข้อสอบระดับ ป.ตรี พร้อมโค้ด: Flutter Architecture, pubspec.yaml, Hot Reload, initState, APK, late, const, Widgets, RenderFlex overflow, ChangeNotifier, async/Future</p>
            </div>
            <div class="subject-footer">
              <span class="subject-pill">80 ข้อ</span>
              <span class="btn-select">
                เข้าทำข้อสอบ
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
              </span>
            </div>
          </div>

          <!-- Card Subject 3: IoT (8312404) -->
          <div class="subject-card" onclick="selectSubject('iot')">
            <div>
              <div class="subject-icon-box emerald">
                <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg>
              </div>
              <h2 class="subject-card-title">อินเทอร์เน็ตของสรรพสิ่ง (IoT - 8312404)</h2>
              <p class="subject-card-desc">แนวทางข้อสอบปลายภาค 80 ข้อ: ESP32, MQTT Broker, Node-RED, SQLite on Raspberry Pi, Firebase Realtime Database, Nginx Web Server, Relay & Telemetry</p>
            </div>
            <div class="subject-footer">
              <span class="subject-pill">80 ข้อ</span>
              <span class="btn-select">
                เข้าทำข้อสอบ
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
              </span>
            </div>
          </div>
        </div>
      </section>

      <!-- ================= 1. START / OVERVIEW SCREEN ================= -->
      <section id="startScreen" class="screen">
        <div style="margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
          <button class="btn btn-secondary" onclick="backToPortal()" style="padding: 8px 16px; font-size: 0.9rem;">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            เลือกวิชาอื่น
          </button>
          <div id="guidelinesBtnContainer" style="display: none;">
            <button class="btn-view-guidelines" onclick="openGuidelinesModal()">
              📋 ดูแนวทางข้อสอบปลายภาค 25 ข้อฉบับเต็ม
            </button>
          </div>
        </div>

        <div id="guidelinesBanner" class="guideline-box" style="display: none;">
          <span class="guideline-info">💡 ข้อสอบชุดนี้สร้างขึ้นตามแนวทางข้อสอบปลายภาค 25 ข้อ โดยเน้นหลักการทำงาน การวิเคราะห์สถานการณ์ และการประยุกต์ใช้จริง</span>
          <button class="btn-view-guidelines" onclick="openGuidelinesModal()">อ่านแนวคำถาม 25 ข้อ</button>
        </div>

        <div class="syllabus-box">
          <div class="syllabus-title">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
            โครงสร้างเนื้อหาข้อสอบ 80 ข้อ
          </div>
          <ul class="syllabus-list" id="syllabusListContainer">
            <!-- Injected by JS -->
          </ul>
        </div>

        <div class="options-box" onclick="document.getElementById('shuffleToggle').click()">
          <input type="checkbox" id="shuffleToggle" onclick="event.stopPropagation()">
          <label for="shuffleToggle">เปิดโหมดสุ่มลำดับคำถาม (Shuffle Mode) สำหรับฝึกซ้อมทบทวน</label>
        </div>

        <button class="btn btn-primary btn-full" id="startBtn" onclick="startQuiz()">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          เริ่มทำแบบทดสอบ (80 ข้อ)
        </button>
      </section>

      <!-- ================= 2. QUIZ SCREEN ================= -->
      <section id="quizScreen" class="screen">
        <div class="quiz-meta">
          <span class="section-pill" id="currentSectionPill">หมวดหมู่</span>
          <span class="progress-text" id="progressText">ข้อ 1 / 80</span>
        </div>

        <div class="progress-bar-container">
          <div class="progress-bar-fill" id="progressBarFill"></div>
        </div>

        <div class="question-box">
          <div class="question-number" id="questionNumber">คำถามข้อที่ 1</div>
          <h2 class="question-text" id="questionText">ข้อความคำถาม</h2>
          <div id="codeSnippetBox" class="code-box" style="display: none;"></div>
        </div>

        <div class="choices-grid" id="choicesGrid">
          <!-- Choices generated by JS -->
        </div>

        <div class="explanation-card" id="explanationCard">
          <div class="explanation-header" id="explanationHeader">
            <span id="explanationIcon"></span>
            <span id="explanationTitle">เฉลยคำตอบ</span>
          </div>
          <div class="explanation-body" id="explanationBody">
            คำอธิบายเฉลยทางวิชาการ
          </div>
        </div>

        <div class="quiz-action-bar">
          <button class="btn btn-secondary" onclick="confirmExitToPortal()" style="padding: 10px 18px; font-size: 0.9rem;">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            เปลี่ยนวิชา
          </button>
          <button class="btn btn-primary" id="nextBtn" onclick="nextQuestion()" style="display: none;">
            ข้อถัดไป
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"></path></svg>
          </button>
        </div>
      </section>

      <!-- ================= 3. RESULT SCREEN ================= -->
      <section id="resultScreen" class="screen">
        <div class="result-score-card">
          <p class="score-percent" id="resultPercentText">คะแนนที่ทำได้</p>
          <div class="score-big"><span id="finalScore">0</span><span class="score-total"> / 80</span></div>
          <p style="margin-bottom: 12px; font-weight: 600; color: var(--text-muted);" id="finalPercent">คิดเป็น 0.0%</p>
          <div class="grade-badge" id="gradeBadge">ผลการประเมิน</div>
        </div>

        <div class="section-breakdown-box">
          <h3 class="section-breakdown-title">ผลการทดสอบแยกตามหมวดหมู่ (Section Breakdown)</h3>
          <div id="sectionBreakdownContainer">
            <!-- Breakdown items injected by JS -->
          </div>
        </div>

        <div class="result-buttons">
          <button class="btn btn-primary" style="flex: 1;" onclick="restartQuiz()">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            ทำแบบทดสอบอีกครั้ง
          </button>
          <button class="btn btn-secondary" style="flex: 1;" id="toggleReviewBtn" onclick="toggleReviewMode()">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path></svg>
            ดูเฉลยและทบทวนทั้ง 80 ข้อ
          </button>
          <button class="btn btn-secondary" style="flex: 1;" onclick="backToPortal()">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
            เลือกวิชาอื่น
          </button>
        </div>

        <div id="reviewContainer" class="review-container" style="display: none;">
          <!-- Review questions injected by JS -->
        </div>
      </section>

    </div>
  </div>

  <!-- Modal for 25 Exam Guidelines -->
  <div id="guidelinesModal" class="modal-overlay" onclick="closeGuidelinesModal(event)">
    <div class="modal-card" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 class="modal-title">📋 แนวทางข้อสอบปลายภาค วิชา อินเทอร์เน็ตของสรรพสิ่ง (8312404)</h3>
        <button class="modal-close" onclick="closeGuidelinesModal()">&times;</button>
      </div>
      <div class="modal-body" id="modalGuidelinesList">
        <!-- Injected by JS -->
      </div>
    </div>
  </div>

  <script>
    const allSubjects = {subjects_json};

    let currentSubjectKey = null;
    let activeQuestions = [];
    let currentIndex = 0;
    let score = 0;
    let userAnswers = [];
    let hasAnsweredCurrent = false;

    // DOM Elements
    const portalScreen = document.getElementById('portalScreen');
    const startScreen = document.getElementById('startScreen');
    const quizScreen = document.getElementById('quizScreen');
    const resultScreen = document.getElementById('resultScreen');

    const topBadge = document.getElementById('topBadge');
    const topTitle = document.getElementById('topTitle');
    const topSubtitle = document.getElementById('topSubtitle');

    const syllabusListContainer = document.getElementById('syllabusListContainer');
    const guidelinesBanner = document.getElementById('guidelinesBanner');
    const guidelinesBtnContainer = document.getElementById('guidelinesBtnContainer');
    const guidelinesModal = document.getElementById('guidelinesModal');
    const modalGuidelinesList = document.getElementById('modalGuidelinesList');

    const currentSectionPill = document.getElementById('currentSectionPill');
    const progressText = document.getElementById('progressText');
    const progressBarFill = document.getElementById('progressBarFill');
    const questionNumber = document.getElementById('questionNumber');
    const questionText = document.getElementById('questionText');
    const codeSnippetBox = document.getElementById('codeSnippetBox');
    const choicesGrid = document.getElementById('choicesGrid');
    const explanationCard = document.getElementById('explanationCard');
    const explanationIcon = document.getElementById('explanationIcon');
    const explanationTitle = document.getElementById('explanationTitle');
    const explanationBody = document.getElementById('explanationBody');
    const nextBtn = document.getElementById('nextBtn');

    function switchScreen(screenToShow) {{
      [portalScreen, startScreen, quizScreen, resultScreen].forEach(s => s.classList.remove('active'));
      screenToShow.classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function selectSubject(subjKey) {{
      currentSubjectKey = subjKey;
      const subj = allSubjects[subjKey];

      topBadge.textContent = subj.badge;
      topTitle.textContent = subj.title;
      topSubtitle.textContent = subj.description;

      // Populate syllabus list
      syllabusListContainer.innerHTML = '';
      subj.sections.forEach(sec => {{
        const li = document.createElement('li');
        li.className = 'syllabus-item';
        li.innerHTML = `
          <span class="syllabus-name">${{sec.name}}</span>
          <span class="syllabus-count">${{sec.count}} ข้อ</span>
        `;
        syllabusListContainer.appendChild(li);
      }});

      // Handle guidelines if available (e.g. IoT)
      if (subj.guidelines && subj.guidelines.length > 0) {{
        guidelinesBanner.style.display = 'flex';
        guidelinesBtnContainer.style.display = 'block';
        modalGuidelinesList.innerHTML = '';
        subj.guidelines.forEach(item => {{
          const div = document.createElement('div');
          div.className = 'guideline-item';
          div.textContent = item;
          modalGuidelinesList.appendChild(div);
        }});
      }} else {{
        guidelinesBanner.style.display = 'none';
        guidelinesBtnContainer.style.display = 'none';
      }}

      switchScreen(startScreen);
    }}

    function openGuidelinesModal() {{
      guidelinesModal.classList.add('active');
    }}

    function closeGuidelinesModal() {{
      guidelinesModal.classList.remove('active');
    }}

    function backToPortal() {{
      topBadge.textContent = 'ศูนย์การเรียนรู้และทดสอบวัดระดับมาตรฐาน (E-Testing Portal)';
      topTitle.textContent = 'ระบบแบบทดสอบวัดความรู้ความสามารถทางวิชาการ';
      topSubtitle.textContent = 'เลือกรายวิชาที่ต้องการทดสอบเพื่อเริ่มทำแบบทดสอบและประเมินผล';
      document.getElementById('reviewContainer').style.display = 'none';
      switchScreen(portalScreen);
    }}

    function confirmExitToPortal() {{
      if (confirm('คุณต้องการออกจากการทำแบบทดสอบเพื่อเปลี่ยนวิชาใช่หรือไม่? (ความคืบหน้าปัจจุบันจะถูกรีเซ็ต)')) {{
        backToPortal();
      }}
    }}

    function shuffleArray(arr) {{
      const array = [...arr];
      for (let i = array.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }}
      return array;
    }}

    function startQuiz() {{
      const subj = allSubjects[currentSubjectKey];
      const shuffle = document.getElementById('shuffleToggle').checked;

      if (shuffle) {{
        activeQuestions = shuffleArray(subj.questions);
      }} else {{
        activeQuestions = JSON.parse(JSON.stringify(subj.questions));
      }}

      currentIndex = 0;
      score = 0;
      userAnswers = new Array(activeQuestions.length).fill(null);
      hasAnsweredCurrent = false;

      switchScreen(quizScreen);
      renderQuestion();
    }}

    function escapeHtml(text) {{
      return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    function renderQuestion() {{
      hasAnsweredCurrent = false;
      nextBtn.style.display = 'none';
      explanationCard.style.display = 'none';

      const q = activeQuestions[currentIndex];
      const total = activeQuestions.length;

      currentSectionPill.textContent = q.section;
      progressText.textContent = `ข้อ ${{currentIndex + 1}} / ${{total}}`;
      const progressPercent = ((currentIndex + 1) / total) * 100;
      progressBarFill.style.width = `${{progressPercent}}%`;

      questionNumber.textContent = `คำถามข้อที่ ${{currentIndex + 1}} จาก ${{total}}`;
      questionText.textContent = q.question;

      // Code snippet
      if (q.code && q.code.trim().length > 0) {{
        codeSnippetBox.innerHTML = `<pre><code>${{escapeHtml(q.code)}}</code></pre>`;
        codeSnippetBox.style.display = 'block';
      }} else {{
        codeSnippetBox.style.display = 'none';
      }}

      // Choices
      choicesGrid.innerHTML = '';
      const letters = ['ก', 'ข', 'ค', 'ง'];

      q.choices.forEach((choiceText, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'choice-btn';
        btn.innerHTML = `
          <span class="choice-letter">${{letters[idx]}}</span>
          <span class="choice-text">${{escapeHtml(choiceText)}}</span>
        `;
        btn.onclick = () => selectAnswer(idx);
        choicesGrid.appendChild(btn);
      }});
    }}

    function selectAnswer(selectedIndex) {{
      if (hasAnsweredCurrent) return;
      hasAnsweredCurrent = true;

      const q = activeQuestions[currentIndex];
      const isCorrect = selectedIndex === q.correctAnswer;
      userAnswers[currentIndex] = {{
        question: q.question,
        code: q.code || '',
        section: q.section,
        choices: q.choices,
        userAnswer: selectedIndex,
        correctAnswer: q.correctAnswer,
        explanation: q.explanation,
        isCorrect: isCorrect
      }};

      if (isCorrect) {{
        score++;
      }}

      // Highlight buttons
      const choiceButtons = choicesGrid.querySelectorAll('.choice-btn');
      choiceButtons.forEach((btn, idx) => {{
        btn.disabled = true;
        if (idx === q.correctAnswer) {{
          btn.classList.add('correct');
        }} else if (idx === selectedIndex && !isCorrect) {{
          btn.classList.add('wrong');
        }}
      }});

      // Show explanation
      explanationCard.className = 'explanation-card ' + (isCorrect ? 'is-correct' : 'is-wrong');
      explanationIcon.innerHTML = isCorrect
        ? '<svg width="22" height="22" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>'
        : '<svg width="22" height="22" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path></svg>';
      explanationTitle.textContent = isCorrect ? 'ตอบถูกต้อง!' : 'ตอบไม่ถูกต้อง';
      explanationBody.textContent = q.explanation;
      explanationCard.style.display = 'block';

      if (currentIndex < activeQuestions.length - 1) {{
        nextBtn.innerHTML = `ข้อถัดไป <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"></path></svg>`;
      }} else {{
        nextBtn.innerHTML = `ดูผลคะแนนรวม <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`;
      }}
      nextBtn.style.display = 'inline-flex';
    }}

    function nextQuestion() {{
      if (currentIndex < activeQuestions.length - 1) {{
        currentIndex++;
        renderQuestion();
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }} else {{
        showResult();
      }}
    }}

    function showResult() {{
      switchScreen(resultScreen);

      const total = activeQuestions.length;
      const percent = ((score / total) * 100).toFixed(1);

      document.getElementById('finalScore').textContent = score;
      document.getElementById('finalPercent').textContent = `คิดเป็น ${{percent}}% จากทั้งหมด ${{total}} ข้อ`;

      const gradeBadge = document.getElementById('gradeBadge');
      if (percent >= 80) {{
        gradeBadge.className = 'grade-badge excellent';
        gradeBadge.textContent = 'ระดับผลการทดสอบ: ยอดเยี่ยม (Excellent)';
      }} else if (percent >= 60) {{
        gradeBadge.className = 'grade-badge good';
        gradeBadge.textContent = 'ระดับผลการทดสอบ: ผ่านเกณฑ์มาตรฐาน (Good)';
      }} else {{
        gradeBadge.className = 'grade-badge needs-work';
        gradeBadge.textContent = 'ระดับผลการทดสอบ: ควรทบทวนเพิ่มเติม (Needs Review)';
      }}

      // Section breakdown
      const sectionStats = {{}};
      userAnswers.forEach(ans => {{
        const sec = ans.section;
        if (!sectionStats[sec]) {{
          sectionStats[sec] = {{ total: 0, correct: 0 }};
        }}
        sectionStats[sec].total++;
        if (ans.isCorrect) {{
          sectionStats[sec].correct++;
        }}
      }});

      const breakdownContainer = document.getElementById('sectionBreakdownContainer');
      breakdownContainer.innerHTML = '';

      for (const [secName, stats] of Object.entries(sectionStats)) {{
        const secPercent = ((stats.correct / stats.total) * 100).toFixed(0);
        let color = '#2563eb';
        if (secPercent >= 80) color = '#10b981';
        else if (secPercent < 50) color = '#ef4444';

        const row = document.createElement('div');
        row.className = 'breakdown-row';
        row.innerHTML = `
          <div class="breakdown-info">
            <span>${{secName}}</span>
            <span>${{stats.correct}} / ${{stats.total}} (${{secPercent}}%)</span>
          </div>
          <div class="breakdown-bar-bg">
            <div class="breakdown-bar-fill" style="width: ${{secPercent}}%; background: ${{color}};"></div>
          </div>
        `;
        breakdownContainer.appendChild(row);
      }}

      renderReview();
    }}

    function renderReview() {{
      const reviewContainer = document.getElementById('reviewContainer');
      reviewContainer.innerHTML = '';
      const letters = ['ก', 'ข', 'ค', 'ง'];

      userAnswers.forEach((ans, idx) => {{
        const item = document.createElement('div');
        item.className = 'review-item ' + (ans.isCorrect ? 'was-correct' : 'was-wrong');

        const userAnsText = ans.userAnswer !== null ? `${{letters[ans.userAnswer]}}. ${{escapeHtml(ans.choices[ans.userAnswer])}}` : 'ไม่ได้ตอบ';
        const correctAnsText = `${{letters[ans.correctAnswer]}}. ${{escapeHtml(ans.choices[ans.correctAnswer])}}`;

        let codeHtml = '';
        if (ans.code && ans.code.trim().length > 0) {{
          codeHtml = `<div class="code-box"><pre><code>${{escapeHtml(ans.code)}}</code></pre></div>`;
        }}

        item.innerHTML = `
          <div class="review-q-num">ข้อที่ ${{idx + 1}} [${{ans.section}}]</div>
          <div class="review-q-text">${{escapeHtml(ans.question)}}</div>
          ${{codeHtml}}
          <div class="review-answers">
            <div class="review-user-ans ${{ans.isCorrect ? 'correct' : 'wrong'}}">
              คำตอบของคุณ: ${{userAnsText}} ${{ans.isCorrect ? '✅' : '❌'}}
            </div>
            ${{!ans.isCorrect ? `<div class="review-correct-ans">คำตอบที่ถูกต้อง: ${{correctAnsText}}</div>` : ''}}
          </div>
          <div class="review-exp">
            <strong>คำอธิบาย:</strong> ${{escapeHtml(ans.explanation)}}
          </div>
        `;
        reviewContainer.appendChild(item);
      }});
    }}

    function toggleReviewMode() {{
      const container = document.getElementById('reviewContainer');
      const btn = document.getElementById('toggleReviewBtn');
      if (container.style.display === 'none') {{
        container.style.display = 'flex';
        btn.innerHTML = `<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7"></path></svg> ซ่อนหน้าเฉลยและทบทวน`;
        container.scrollIntoView({{ behavior: 'smooth' }});
      }} else {{
        container.style.display = 'none';
        btn.innerHTML = `<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path></svg> ดูเฉลยและทบทวนทั้ง 80 ข้อ`;
      }}
    }}

    function restartQuiz() {{
      document.getElementById('reviewContainer').style.display = 'none';
      switchScreen(startScreen);
    }}
  </script>
</body>
</html>
"""

output_path = "/Users/wiwi/PKRU/webapp ติวข้อสอบ/index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated 3-subject app successfully at: {output_path}")
