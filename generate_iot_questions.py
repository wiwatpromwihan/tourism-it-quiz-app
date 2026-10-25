# -*- coding: utf-8 -*-

iot_questions = [
    # ==========================================
    # หมวดที่ 1: สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT (16 ข้อ: ข้อ 1 - 16)
    # ==========================================
    {
        "id": 1,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "ในระบบ IoT ลำดับการทำงานตั้งแต่ ESP32 ตรวจวัดอุณหภูมิจนกระทั่งผู้ใช้เห็นข้อมูลบนแอปพลิเคชันมือถือ ข้อใดเรียงลำดับได้ถูกต้องที่สุด?",
        "choices": [
            "Sensor วัดค่า -> แปลงเป็นสัญญาณดิจิทัล -> ESP32 ประมวลผลและต่อ Wi-Fi -> Publish ข้อความไปยัง MQTT Broker -> Broker ส่งต่อ (Forward) ให้แอปพลิเคชันที่ Subscribe ไว้ -> แอปแสดงผลบนหน้าจอ",
            "แอปพลิเคชันส่งคำขอไปยัง Sensor โดยตรง -> Sensor ส่งข้อมูลกลับมายังมือถือ -> บันทึกลง MQTT Broker",
            "ESP32 บันทึกข้อมูลลงใน SD Card -> ส่งข้อมูลผ่านบลูทูธไปยังโทรศัพท์ -> โทรศัพท์ส่งข้อมูลไปที่ MQTT Broker",
            "MQTT Broker ดึงข้อมูลจาก Sensor อัตโนมัติ -> แปลงเป็นไฟล์ภาพ -> ส่งไปยังอีเมลของผู้ใช้งาน"
        ],
        "correctAnswer": 0,
        "explanation": "ลำดับการทำงานที่ถูกต้องในสถาปัตยกรรม Publish/Subscribe: 1. เซ็นเซอร์ (เช่น DHT22) อ่านค่าอุณหภูมิ 2. ESP32 รับค่ามาแปลงเป็นตัวเลข/JSON 3. ESP32 เชื่อมต่อ Wi-Fi แล้ว Publish ข้อความไปยัง MQTT Broker ผ่าน Topic ที่กำหนด 4. Broker ตรวจสอบและส่งต่อข้อความไปยัง Clients ที่กด Subscribe Topic นั้นไว้ 5. แอปพลิเคชันบนมือถือได้รับ Payload และอัปเดต UI ทันที"
    },
    {
        "id": 2,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "ข้อใดอธิบายบทบาทหน้าที่ขององค์ประกอบในโปรโตคอล MQTT ได้ถูกต้องตามหลักการ Publish/Subscribe?",
        "choices": [
            "Publisher คือผู้ส่งข้อมูล, Subscriber คือผู้รอรับข้อมูล, และ Broker คือเซิร์ฟเวอร์ตัวกลางทำหน้าที่รับ คัดกรอง และกระจายข้อความตาม Topic",
            "Publisher คือผู้รับข้อมูล, Subscriber คือผู้ส่งข้อมูล, และ Broker คือสายเคเบิลเชื่อมต่อ",
            "Broker คือเซ็นเซอร์, Publisher คือฐานข้อมูล, และ Subscriber คือเราเตอร์ Wi-Fi",
            "ทั้ง Publisher และ Subscriber ติดต่อสื่อสารกันโดยตรงโดยไม่ต้องมี Broker เป็นตัวกลาง"
        ],
        "correctAnswer": 0,
        "explanation": "โปรโตคอล MQTT อาศัย Broker เป็นศูนย์กลาง (Decoupled Architecture) โดย Publisher (เช่น ESP32) จะส่งข้อความไปยัง Topic ที่ต้องการ ส่วน Subscriber (เช่น Node-RED, Mobile App) จะลงทะเบียนรอรับข้อมูลใน Topic นั้น โดยที่ทั้งสองฝ่ายไม่จำเป็นต้องรู้จัก IP Address ของกันและกัน"
    },
    {
        "id": 3,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "หลักการออกแบบชื่อ MQTT Topic ที่มีประสิทธิภาพและเป็นระบบสำหรับองค์กรที่มีอุปกรณ์หลายตัวควรมีลักษณะอย่างไร?",
        "choices": [
            "จัดโครงสร้างแบบลำดับชั้นจากใหญ่ไปเล็ก โดยคั่นด้วยเครื่องหมาย Slash (/) เช่น สถานที่/ห้อง/อุปกรณ์/ชนิดข้อมูล",
            "ตั้งชื่อเป็นข้อความยาวติดต่อกันโดยไม่เว้นวรรคและไม่ใช้เครื่องหมายใดๆ",
            "ใช้เฉพาะตัวเลข IP Address ของอุปกรณ์เป็นชื่อ Topic เสมอ",
            "ตั้งชื่อเหมือนกันทุกอุปกรณ์เพื่อความสะดวกในการส่งข้อมูลรวมกัน"
        ],
        "correctAnswer": 0,
        "explanation": "การออกแบบ Topic Hierarchy ที่ดีต้องแบ่งระดับจากกว้างไปแคบโดยใช้ '/' เช่น 'building1/room101/esp32_01/temperature' ทำให้ระบุตำแหน่ง อุปกรณ์ และชนิดข้อมูลได้อย่างชัดเจน และรองรับการใช้ Wildcards (+ และ #) ในการ Subscribe"
    },
    {
        "id": 4,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "ข้อใดเป็นตัวอย่างการตั้งชื่อ MQTT Topic ที่ถูกต้องและชัดเจนที่สุดตามหลัก Topic Hierarchy ในระบบตรวจวัดสภาพแวดล้อม?",
        "choices": [
            "pkru/building3/room301/dht22/temperature",
            "temperature_room301_building3_pkru_now",
            "192.168.1.100:1883/temp",
            "C:\\Users\\IoT\\Temperature.txt"
        ],
        "correctAnswer": 0,
        "explanation": "'pkru/building3/room301/dht22/temperature' เป็นตัวอย่างที่สมบูรณ์แบบ เพราะระบุสถาบัน (pkru) -> อาคาร (building3) -> ห้อง (room301) -> อุปกรณ์เซ็นเซอร์ (dht22) -> ชนิดข้อมูล (temperature) อย่างเป็นลำดับขั้น"
    },
    {
        "id": 5,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "ในระบบ MQTT หาก Publisher ส่งข้อความไปยัง Topic หนึ่งซึ่งในขณะนั้น 'ไม่มี Subscriber ใดๆ ติดตามอยู่' และไม่ได้ตั้งค่า Retain ข้อความนั้นจะเป็นอย่างไร?",
        "choices": [
            "Broker จะทิ้งข้อความนั้นไปทันที (Message Dropped) และจะไม่มี Client ใดได้รับข้อความย้อนหลัง",
            "Broker จะเก็บข้อความไว้ในหน่วยความจำถาวรตลอดไปจนกว่าจะมีคนมาเปิดดู",
            "Broker จะส่งข้อความแจ้งเตือนกลับไปยัง Publisher ว่าส่งไม่สำเร็จ",
            "ระบบจะสั่งปิดการทำงานของ Broker โดยอัตโนมัติ"
        ],
        "correctAnswer": 0,
        "explanation": "ตามพฤติกรรมปกติของ MQTT หากข้อความไม่ได้กำหนด Retained Flag (retain = false) Broker จะทำหน้าที่ส่งต่อให้ Subscriber ที่เชื่อมต่ออยู่ ณ เวลานั้นเท่านั้น หากไม่มีใคร Subscribe อยู่ ข้อความจะถูกทิ้งทันที (Discarded) ไม่ถูกเก็บไว้"
    },
    {
        "id": 6,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "การตั้งค่า 'Retain Flag' (retain = true) ในการ Publish ข้อความ MQTT มีประโยชน์สำคัญอย่างไร?",
        "choices": [
            "Broker จะเก็บบันทึกข้อความล่าสุดของ Topic นั้นไว้ และส่งให้แก่ Subscriber รายใหม่ทันทีที่เข้ามา Subscribe แม้จะเพิ่งเชื่อมต่อทีหลัง",
            "ช่วยเพิ่มความเร็วของสัญญาณ Wi-Fi ของ ESP32",
            "ป้องกันไม่ให้ผู้อื่นสามารถ Subscribe Topic นี้ได้",
            "ช่วยแปลงข้อความภาษาไทยให้เป็นภาษาอังกฤษอัตโนมัติ"
        ],
        "correctAnswer": 0,
        "explanation": "Retained Message คือฟังก์ชันที่สั่งให้ Broker เก็บข้อความล่าสุด (Last Known Good Value) ไว้ใน Topic นั้น เมื่อมี Client ใหม่เข้ามา Subscribe จะได้รับค่านี้ทันทีโดยไม่ต้องรอให้อุปกรณ์ส่งข้อมูลรอบถัดไป เหมาะสำหรับค่าสถานะ เช่น สถานะ Relay หรือค่าพารามิเตอร์ระบบ"
    },
    {
        "id": 7,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "สัญลักษณ์ Wildcard เครื่องหมายบวก (+) ในการ Subscribe MQTT Topic มีหน้าที่และความหมายอย่างไร?",
        "code": "mosquitto_sub -t 'home/+/temperature'",
        "choices": [
            "ใช้แทนที่ชื่อระดับใดระดับหนึ่งเพียงระดับเดียว (Single-level Wildcard) เช่น รับอุณหภูมิจากทุกห้องใน home",
            "ใช้แทนที่ทุกระดับขั้นตั้งแต่ตำแหน่งนั้นเป็นต้นไปจนจบ (Multi-level Wildcard)",
            "ใช้สำหรับการบวกค่าตัวเลขอุณหภูมิให้เพิ่มขึ้น 1 องศา",
            "ใช้แทนเฉพาะตัวเลขจำนวนเต็มเท่านั้น"
        ],
        "correctAnswer": 0,
        "explanation": "เครื่องหมาย '+' คือ Single-level Wildcard ใช้แทนระดับชั้นเดียว เช่น 'home/+/temperature' จะรับข้อมูลจาก 'home/kitchen/temperature' และ 'home/bedroom/temperature' แต่จะไม่รับ 'home/floor2/bedroom/temperature'"
    },
    {
        "id": 8,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "สัญลักษณ์ Wildcard เครื่องหมายชาร์ป (#) ในการ Subscribe MQTT Topic มีหน้าที่และความหมายอย่างไร?",
        "code": "mosquitto_sub -t 'factory/machine1/#'",
        "choices": [
            "ใช้แทนที่ทุกระดับขั้นตั้งแต่จุดนั้นเป็นต้นไปจนถึงระดับลึกสุด (Multi-level Wildcard) และต้องอยู่ท้ายสุดของ Topic เสมอ",
            "ใช้แทนอักขระตัวเดียวเท่านั้น",
            "ใช้สำหรับซ่อนชื่อ Topic ไม่ให้คนอื่นมองเห็น",
            "ใช้สำหรับตรวจสอบข้อผิดพลาดของข้อมูล"
        ],
        "correctAnswer": 0,
        "explanation": "เครื่องหมาย '#' คือ Multi-level Wildcard สามารถจับคู่กับทุก Topic ย่อยที่อยู่ใต้ระดับนั้นทั้งหมด เช่น 'factory/machine1/#' จะได้รับทั้ง temperature, humidity, vibration, status ฯลฯ โดยต้องวางไว้ที่ตำแหน่งท้ายสุดเสมอ"
    },
    {
        "id": 9,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "คำสั่ง Command Line ใดที่ใช้สำหรับ 'รอรับข้อมูล' (Subscribe) จาก MQTT Broker เพื่อทดสอบการสื่อสาร?",
        "code": "mosquitto_sub -h 192.168.1.50 -t 'classroom/temp' -v",
        "choices": [
            "mosquitto_sub",
            "mosquitto_pub",
            "mqtt_listen",
            "broker_fetch"
        ],
        "correctAnswer": 0,
        "explanation": "'mosquitto_sub' คือ CLI Tool สำหรับทำหน้าที่เป็น Subscriber โดยพารามิเตอร์ -h คือ IP ของ Broker, -t คือชื่อ Topic, และ -v (verbose) คือให้แสดงชื่อ Topic กำกับพร้อมกับข้อมูลที่ได้รับ"
    },
    {
        "id": 10,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "คำสั่ง Command Line ใดที่ใช้สำหรับ 'ส่งข้อความ' (Publish) ไปยัง MQTT Broker เพื่อทดสอบ?",
        "code": "mosquitto_pub -h 192.168.1.50 -t 'classroom/temp' -m '28.5'",
        "choices": [
            "mosquitto_pub",
            "mosquitto_sub",
            "mqtt_send",
            "broker_push"
        ],
        "correctAnswer": 0,
        "explanation": "'mosquitto_pub' ใช้ส่งข้อความ (Publish) โดยใช้พารามิเตอร์ -h ระบุโฮสต์, -t ระบุ Topic และ -m (message) ระบุข้อความ Payload ที่ต้องการส่ง"
    },
    {
        "id": 11,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "พอร์ตมาตรฐาน (Default Port) สำหรับการเชื่อมต่อสื่อสารผ่านโปรโตคอล MQTT แบบปกติที่ไม่มีการเข้ารหัสข้อมูล (Unencrypted) คือพอร์ตหมายเลขใด?",
        "choices": [
            "1883",
            "8883",
            "80",
            "3306"
        ],
        "correctAnswer": 0,
        "explanation": "พอร์ตมาตรฐานของ MQTT คือ 1883 สำหรับการเชื่อมต่อแบบ TCP ปกติ (Plaintext) ส่วนพอร์ต 8883 ใช้สำหรับ MQTT over TLS/SSL (เข้ารหัสความปลอดภัย)"
    },
    {
        "id": 12,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "ในการทดสอบว่าเครื่องคอมพิวเตอร์สามารถติดต่อกับ MQTT Broker บน Raspberry Pi ผ่านพอร์ต 1883 ได้หรือไม่ ควรใช้คำสั่งใดในการตรวจสอบเครือข่าย?",
        "choices": [
            "nc -zv <IP_RaspberryPi> 1883 หรือ telnet <IP_RaspberryPi> 1883",
            "ping <IP_RaspberryPi>:1883",
            "ssh -p 1883 <IP_RaspberryPi>",
            "curl http://<IP_RaspberryPi>:1883"
        ],
        "correctAnswer": 0,
        "explanation": "คำสั่ง 'ping' ตรวจสอบได้เฉพาะระดับ ICMP ไม่สามารถระบุหมายเลขพอร์ตได้ การตรวจสอบว่าพอร์ต 1883 เปิดและพร้อมรับการเชื่อมต่อหรือไม่ ต้องใช้คำสั่งอย่าง 'nc' (Netcat) หรือ 'telnet' ระบุ IP และ Port 1883"
    },
    {
        "id": 13,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "เหตุใดการกำหนด 'Client ID' ของอุปกรณ์แต่ละตัวในระบบ MQTT จึงห้ามซ้ำกันโดยเด็ดขาด?",
        "choices": [
            "หากมี Client ID ซ้ำกันเชื่อมต่อเข้ามา Broker จะตัดการเชื่อมต่อของ Client ตัวเดิมออกทันที ทำให้เกิดปัญหาเชื่อมต่อหลุดสลับกันไปมา",
            "เพราะ Broker จะระเบิดและฮาร์ดแวร์เสียหาย",
            "เพราะจะทำให้อุณหภูมิที่วัดได้มีความคลาดเคลื่อน",
            "เพราะโปรโตคอล Wi-Fi จะบล็อกหมายเลข MAC Address ทันที"
        ],
        "correctAnswer": 0,
        "explanation": "ตามมาตรฐาน MQTT ข้อกำหนดคือ Client ID ต้องไม่ซ้ำกัน (Unique) หากมีอุปกรณ์ที่ใช้ Client ID เดียวกันพยายามเชื่อมต่อเข้ามา Broker จะถือว่าเป็นเซสชันใหม่และเตะ (Disconnect) ไคลเอนต์ตัวก่อนหน้าออก ส่งผลให้เกิดอาการหลุดและต่อใหม่วนลูป"
    },
    {
        "id": 14,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "ระดับการรับประกันการส่งข้อมูล QoS (Quality of Service) ระดับใดใน MQTT ที่ส่งข้อมูลเพียงครั้งเดียวโดยไม่รอการตอบรับ (Fire and Forget) ซึ่งประหยัดพลังงานที่สุด?",
        "choices": [
            "QoS 0 (At most once)",
            "QoS 1 (At least once)",
            "QoS 2 (Exactly once)",
            "QoS 3 (Never lost)"
        ],
        "correctAnswer": 0,
        "explanation": "QoS 0 (At most once) คือการส่งแบบ 'Fire and Forget' ไม่มีการยืนยันการรับส่ง (Handshake ต่ำสุด) ใช้แบนด์วิดท์และพลังงานน้อยที่สุด เหมาะกับข้อมูลเซ็นเซอร์ที่ส่งอย่างต่อเนื่องและยอมให้ข้อมูลสูญหายได้บ้าง"
    },
    {
        "id": 15,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "หากต้องการตรวจสอบว่า Service ของ Mosquitto MQTT Broker บน Raspberry Pi กำลังทำงานอยู่หรือไม่ ควรใช้คำสั่งใด?",
        "choices": [
            "sudo systemctl status mosquitto",
            "sudo apt-get install mosquitto",
            "mosquitto --check-all",
            "service restart wifi"
        ],
        "correctAnswer": 0,
        "explanation": "บนระบบปฏิบัติการ Linux / Raspberry Pi OS คำสั่ง 'sudo systemctl status mosquitto' ใช้ตรวจสอบสถานะการทำงาน (Active/Running) ดูข้อความ Log ล่าสุด และตรวจสอบข้อผิดพลาดในการเริ่มต้นเซอร์วิส"
    },
    {
        "id": 16,
        "section": "สถาปัตยกรรมระบบ IoT และโปรโตคอล MQTT",
        "question": "ไฟล์คอนฟิกูเรชันหลักของ Mosquitto Broker บน Raspberry Pi ที่ใช้กำหนด Port, Listener และการอนุญาต Anonymous Clients คือไฟล์ใด?",
        "choices": [
            "/etc/mosquitto/mosquitto.conf",
            "/var/log/mosquitto.log",
            "/etc/network/interfaces",
            "/home/pi/mqtt.json"
        ],
        "correctAnswer": 0,
        "explanation": "ไฟล์ '/etc/mosquitto/mosquitto.conf' คือ Configuration File หลัก ใน Mosquitto v2.0+ จำเป็นต้องระบุ 'listener 1883' และ 'allow_anonymous true' หากต้องการให้อุปกรณ์อื่นภายนอกเครื่องสามารถเชื่อมต่อเข้ามาได้โดยไม่ต้องใช้รหัสผ่าน"
    },

    # ==========================================
    # หมวดที่ 2: การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED (16 ข้อ: ข้อ 17 - 32)
    # ==========================================
    {
        "id": 17,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "ในการสร้าง Flow บน Node-RED เพื่อรับข้อมูลอุณหภูมิจาก MQTT แล้วนำไปแสดงผลบน Dashboard ควรใช้โหนดประเภทใดเป็นตัวเริ่มต้นและตัวแสดงผล?",
        "choices": [
            "โหนด 'mqtt in' รับข้อมูล -> โหนดประมวลผล (function/json) -> โหนด 'ui_gauge' หรือ 'ui_text' แสดงผล",
            "โหนด 'http request' -> โหนด 'debug' -> โหนด 'inject'",
            "โหนด 'tcp in' -> โหนด 'file write' -> โหนด 'email'",
            "โหนด 'ui_button' -> โหนด 'delay' -> โหนด 'mqtt out'"
        ],
        "correctAnswer": 0,
        "explanation": "โครงสร้าง Flow การรับและแสดงผลข้อมูลมาตรฐานใน Node-RED: เริ่มจากโหนด 'mqtt in' (ดักฟังสัญญาณตาม Topic) -> ส่ง payload ต่อไปยังโหนดแปลงค่า (เช่น json หรือ function) -> ส่งต่อไปยังโหนด Dashboard UI (เช่น ui_gauge หรือ ui_chart)"
    },
    {
        "id": 18,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "ข้อมูลที่ไหลระหว่างโหนดต่างๆ ใน Node-RED จะถูกห่อหุ้มและส่งต่อในรูปแบบของอ็อบเจกต์ใดเป็นหลัก?",
        "choices": [
            "msg (โดยมี msg.payload เก็บเนื้อหาของข้อมูล และ msg.topic เก็บชื่อหัวข้อ)",
            "data.json เท่านั้น",
            "xml_packet",
            "global_variable"
        ],
        "correctAnswer": 0,
        "explanation": "Node-RED ทำงานด้วยการส่ง Message Object หรือ 'msg' โดยเนื้อหาหรือค่าที่ได้รับจะถูกจัดเก็บไว้ใน Property ที่ชื่อ 'msg.payload' และสามารถมี Metadata อื่นๆ เช่น 'msg.topic' ประกอบมาด้วยเสมอ"
    },
    {
        "id": 19,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "หากต้องการตรวจสอบเงื่อนไขว่า 'ความชื้นต่ำกว่า 40% หรือไม่' เพื่อแยกเส้นทางข้อมูลไปสั่งแจ้งเตือน ใน Node-RED ควรใช้โหนดชนิดใดที่สะดวกและมีประสิทธิภาพที่สุด?",
        "choices": [
            "โหนด 'switch' (กำหนดกฎ: msg.payload < 40)",
            "โหนด 'delay'",
            "โหนด 'catch'",
            "โหนด 'link out'"
        ],
        "correctAnswer": 0,
        "explanation": "โหนด 'switch' ทำหน้าที่เป็นตัวแยกเงื่อนไข (Routing Node) เปรียบเหมือนคำสั่ง if-else ในการเขียนโปรแกรม โดยสามารถกำหนดเงื่อนไข เช่น 'is less than 40' เพื่อส่งต่อไปยัง Output พอร์ตที่กำหนดเมื่อตรงตามเงื่อนไข"
    },
    {
        "id": 20,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "รูปแบบการแสดงผล (Widget) ใดบน Node-RED Dashboard ที่เหมาะสมที่สุดสำหรับการแสดงค่า 'อุณหภูมิและความชื้นปัจจุบัน' เพื่อให้ผู้ใช้มองเห็นระดับความปลอดภัยได้อย่างชัดเจนในทันที?",
        "choices": [
            "Gauge (มาตรวัดรูปเข็ม/แถบโค้ง) แบ่งแถบสีเขียว-เหลือง-แดง",
            "Dropdown Menu",
            "Form Input",
            "Password Box"
        ],
        "correctAnswer": 0,
        "explanation": "Gauge (เกจวัด) เหมาะสมที่สุดสำหรับค่าตัวเลขทางฟิสิกส์แบบ Real-time เช่น อุณหภูมิหรือความดัน เพราะมองเห็นระดับค่าได้ทันที และสามารถกำหนดแถบสี (Sectors) เพื่อเตือนเมื่อค่าขึ้นสูงเกินเกณฑ์ปกติได้ง่าย"
    },
    {
        "id": 21,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "รูปแบบการแสดงผลใดบน Dashboard ที่เหมาะสมที่สุดสำหรับการแสดง 'แนวโน้มการเปลี่ยนแปลงของอุณหภูมิตลอด 24 ชั่วโมง'?",
        "choices": [
            "Chart (กราฟเส้นแสดงแนวโน้มตามแกนเวลา Time Series)",
            "Switch ปุ่มเปิดปิด",
            "Text ข้อความสั้น",
            "Slider แถบเลื่อน"
        ],
        "correctAnswer": 0,
        "explanation": "Chart (กราฟเส้นแสดงข้อมูลตามแกนเวลา) เป็นเครื่องมือที่เหมาะสมที่สุดในการดูข้อมูลย้อนหลังและวิเคราะห์แนวโน้ม (Trends) ทำให้เห็นจุดสูงสุด จุดต่ำสุด และช่วงเวลาที่มีการเปลี่ยนแปลงของอุณหภูมิได้อย่างชัดเจน"
    },
    {
        "id": 22,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "เมื่อข้อความที่ได้รับจาก MQTT อยู่ในรูปแบบ JSON String เช่น '{\"temp\": 28.5, \"hum\": 65}' โหนดใดใน Node-RED ที่ใช้แปลงให้กลายเป็น JavaScript Object โดยอัตโนมัติ?",
        "choices": [
            "โหนด 'json'",
            "โหนด 'template'",
            "โหนด 'split'",
            "โหนด 'csv'"
        ],
        "correctAnswer": 0,
        "explanation": "โหนด 'json' ใน Node-RED ทำหน้าที่เป็นตัวแปลงสองทาง (Bi-directional converter): หากรับ JSON String เข้ามาจะแปลงเป็น JavaScript Object และหากรับ Object เข้ามาจะแปลงเป็น JSON String ให้โดยอัตโนมัติ"
    },
    {
        "id": 23,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "ในโหนด 'function' ของ Node-RED หากต้องการเขียนโค้ด JavaScript ดึงเฉพาะค่าอุณหภูมิและส่งค่าออกไป ควรเขียนอย่างไร?",
        "code": "msg.payload = msg.payload.temp;\nreturn msg;",
        "choices": [
            "msg.payload = msg.payload.temp; return msg;",
            "print(msg.payload.temp);",
            "response.send(temp);",
            "return temp;"
        ],
        "correctAnswer": 0,
        "explanation": "ในโหนด function ของ Node-RED ต้องเขียนด้วยไวยากรณ์ JavaScript โดยดึงค่าจาก Property ที่ต้องการมาเก็บไว้ใน msg.payload แล้วจบคำสั่งด้วย 'return msg;' เพื่อส่งอ็อบเจกต์ไปยังโหนดถัดไป"
    },
    {
        "id": 24,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "โหนดใดที่นิยมใช้ในการจำลองส่งข้อมูลทดสอบเข้าไปใน Flow หรือสั่งให้ระบบเริ่มทำงานตามรอบเวลาที่กำหนด (เช่น ทุก 5 วินาที)?",
        "choices": [
            "โหนด 'inject'",
            "โหนด 'debug'",
            "โหนด 'exec'",
            "โหนด 'comment'"
        ],
        "correctAnswer": 0,
        "explanation": "โหนด 'inject' ใช้สำหรับสร้างสัญญาณทดสอบ โดยสามารถคลิกปุ่มซ้ายของโหนดเพื่อส่งค่า (Timestamp, String, Number, JSON) เข้าสู่ Flow ด้วยตนเอง หรือตั้งเวลาให้ส่งอัตโนมัติเป็นรอบ (Repeat interval) ได้"
    },
    {
        "id": 25,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "โหนด 'debug' ใน Node-RED มีประโยชน์หลักในการพัฒนาอย่างไร และข้อมูลผลลัพธ์จะไปปรากฏที่ใด?",
        "choices": [
            "ใช้แสดงโครงสร้างและค่าของ msg ในแถบแท็บ Debug (สัญลักษณ์รูปแมลง) ทางขวามือ เพื่อช่วยตรวจสอบความถูกต้องของการไหลของข้อมูล",
            "ใช้สำหรับลบโค้ดที่มีข้อผิดพลาดทิ้งอัตโนมัติ",
            "ใช้สำหรับควบคุมความเร็วของพัดลมระบายความร้อน",
            "ผลลัพธ์จะถูกส่งเป็นข้อความ SMS เข้าโทรศัพท์ของนักพัฒนา"
        ],
        "correctAnswer": 0,
        "explanation": "โหนด debug เป็นเครื่องมือตรวจสอบหลักของนักพัฒนา Node-RED ช่วยให้สามารถดูโครงสร้างและข้อมูลของตัวแปร msg ได้ในหน้าต่าง Debug Panel ทางขวามือ ช่วยให้วิเคราะห์จุดที่เกิดบั๊กได้อย่างแม่นยำ"
    },
    {
        "id": 26,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "พอร์ตเริ่มต้นและ URL ในการเปิดใช้งานหน้าจอแก้ไข Flow (Editor) ของ Node-RED บน Web Browser คือข้อใด?",
        "choices": [
            "http://<IP_Address>:1880",
            "http://<IP_Address>:8080",
            "http://<IP_Address>:1883",
            "http://<IP_Address>:3000"
        ],
        "correctAnswer": 0,
        "explanation": "Node-RED ทำงานบนพอร์ตเริ่มต้นหมายเลข 1880 ดังนั้นการเข้าใช้งานจึงพิมพ์ 'http://<IP_Address>:1880' และสามารถดูหน้า Dashboard ได้ที่ 'http://<IP_Address>:1880/ui'"
    },
    {
        "id": 27,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "ในการส่งคำสั่งเปิด/ปิด Relay ไปยัง ESP32 ผ่าน MQTT ด้วยการกดสวิตช์บน Dashboard ของ Node-RED ควรใช้โหนดคู่ใดทำงานร่วมกัน?",
        "choices": [
            "โหนด 'ui_switch' ต่อเข้ากับโหนด 'mqtt out'",
            "โหนด 'ui_chart' ต่อเข้ากับโหนด 'mqtt in'",
            "โหนด 'ui_text' ต่อเข้ากับโหนด 'http in'",
            "โหนด 'ui_gauge' ต่อเข้ากับโหนด 'debug'"
        ],
        "correctAnswer": 0,
        "explanation": "โหนด 'ui_switch' จะสร้างปุ่มสวิตช์เปิด-ปิดบนหน้าเว็บ เมื่อคลิกจะสร้าง payload (เช่น 'ON' หรือ 'OFF') แล้วส่งต่อไปยังโหนด 'mqtt out' เพื่อ Publish คำสั่งไปยัง Topic ที่ ESP32 กำลัง Subscribe รอรับอยู่"
    },
    {
        "id": 28,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "ปุ่ม 'Deploy' สีแดงมุมขวาบนของหน้าต่าง Node-RED มีหน้าที่อะไร?",
        "choices": [
            "บันทึกและนำการเปลี่ยนแปลงของ Flow ทั้งหมดขึ้นไปทำงานจริงบนเซิร์ฟเวอร์ (Runtime)",
            "ลบโปรเจกต์ทั้งหมดทิ้งเพื่อเริ่มสร้างใหม่",
            "สั่ง Restart เครื่องเซิร์ฟเวอร์ Raspberry Pi",
            "ดาวน์โหลดโค้ดลงในคอมพิวเตอร์เป็นไฟล์ PDF"
        ],
        "correctAnswer": 0,
        "explanation": "ปุ่ม 'Deploy' มีหน้าที่คอมไพล์และอัปเดต Flow ที่แก้ไขบนหน้าเว็บให้มีผลบังคับใช้จริงใน Node-RED Runtime Engine ทันที"
    },
    {
        "id": 29,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "หากต้องการติดตั้งแพ็กเกจ Dashboard เสริม (node-red-dashboard) บน Node-RED ต้องเข้าไปจัดการที่เมนูใด?",
        "choices": [
            "Manage palette -> แท็บ Install",
            "Export -> Download",
            "Settings -> Change Password",
            "Import -> Clipboard"
        ],
        "correctAnswer": 0,
        "explanation": "เมนู 'Manage palette' (จัดการชุดโหนด) ภายใน Node-RED ช่วยให้นักพัฒนาสามารถค้นหา ติดตั้ง อัปเดต หรือลบชุดโหนดเสริมภายนอก (Palette Modules) เช่น node-red-dashboard ได้โดยตรงผ่านหน้า UI"
    },
    {
        "id": 30,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "ขั้นตอนการประมวลผลข้อมูลใน Node-RED ก่อนจะนำข้อมูลอุณหภูมิบันทึกลงฐานข้อมูล SQLite ข้อใดระบุลำดับได้ถูกต้องที่สุด?",
        "choices": [
            "รับข้อความ MQTT -> แปลง JSON String เป็น Object -> ดึงค่าตัวเลข -> สร้างคำสั่ง SQL INSERT พร้อม Timestamp -> ส่งเข้าโหนด sqlite",
            "ส่งข้อความดิบเข้าโหนด sqlite ทันทีโดยไม่ต้องแปลงข้อมูล",
            "แปลงข้อมูลเป็นไฟล์รูปภาพ -> ส่งเข้า sqlite",
            "บันทึกลงกระดาษก่อนแล้วค่อยพิมพ์เข้า sqlite ด้วยมือ"
        ],
        "correctAnswer": 0,
        "explanation": "ข้อมูลที่ได้จาก MQTT มักเป็นสตริง ต้องผ่านการแปลงเป็น Object (JSON Parsing), คัดแยกเฉพาะฟิลด์ที่ต้องการ, กำหนดเวลาบันทึก (Timestamp), และประกอบเป็นคำสั่ง SQL Statement เช่น 'INSERT INTO logs (temp, created_at) VALUES (?, ?)' ก่อนส่งเข้าโหนดฐานข้อมูล"
    },
    {
        "id": 31,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "โหนด 'ui_notification' หรือการส่งแจ้งเตือนผ่าน LINE Notify ใน Node-RED ทำงานเมื่อใดในระบบตรวจวัดอุณหภูมิ?",
        "choices": [
            "เมื่อข้อมูลที่ผ่านเข้ามาตรงตามเงื่อนไขความผิดปกติที่กำหนดไว้ เช่น อุณหภูมิสูงเกิน 35 องศาเซลเซียส",
            "ทำงานสุ่มเวลาทุกๆ 1 ชั่วโมงโดยไม่สนใจข้อมูล",
            "ทำงานเฉพาะตอนที่อินเทอร์เน็ตหลุดเท่านั้น",
            "ทำงานเมื่อผู้ใช้กดปิดแอปพลิเคชัน"
        ],
        "correctAnswer": 0,
        "explanation": "โหนดแจ้งเตือนจะถูกวางไว้หลังโหนดตรวจสอบเงื่อนไข (Switch Node) โดยจะทำงานเฉพาะเมื่อค่าเซ็นเซอร์ทะลุเกณฑ์วิกฤต (Threshold Exceeded) เช่น อุณหภูมิสูงผิดปกติ หรือความชื้นต่ำเกินเกณฑ์ เพื่อแจ้งเตือนผู้ดูแลระบบทันที"
    },
    {
        "id": 32,
        "section": "การพัฒนาโฟลว์ประมวลผลและ Dashboard ด้วย Node-RED",
        "question": "ข้อใดคือความสัมพันธ์ของทั้งสามระบบ: Mosquitto, Node-RED และ SQLite บน Raspberry Pi?",
        "choices": [
            "Mosquitto ทำหน้าที่เป็นทางผ่านรับส่งข้อมูล (Messaging), Node-RED ทำหน้าที่เป็นสมองประมวลผลและตัวเชื่อมโยง (Logic & Integration), และ SQLite ทำหน้าที่เป็นคลังจัดเก็บข้อมูลถาวร (Storage)",
            "ทั้งสามระบบคือโปรแกรมชนิดเดียวกันที่ทำหน้าที่เหมือนกันทุกประการ",
            "SQLite ส่งข้อมูลให้ Mosquitto แล้ว Mosquitto บันทึกลง Node-RED",
            "Node-RED เป็นระบบปฏิบัติการ ส่วน Mosquitto เป็นโปรแกรมตัดต่อภาพ"
        ],
        "correctAnswer": 0,
        "explanation": "ทั้งสามองค์ประกอบทำงานร่วมกันอย่างสมบูรณ์แบบบน Raspberry Pi: Mosquitto เป็นตัวกลางกระจายข่าวสาร (Broker), Node-RED ดักฟังข้อมูล ประมวลผล ทำ Automation และ Dashboard, จากนั้นส่งข้อมูลไปบันทึกลงฐานข้อมูล SQLite เพื่อเก็บประวัติย้อนหลัง"
    },

    # ==========================================
    # หมวดที่ 3: การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase (16 ข้อ: ข้อ 33 - 48)
    # ==========================================
    {
        "id": 33,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "ในการออกแบบตารางฐานข้อมูล SQLite เพื่อจัดเก็บข้อมูลอุณหภูมิจากเซ็นเซอร์ ESP32 ฟิลด์ข้อมูลใดที่ 'จำเป็นต้องมี' อย่างน้อย 3 รายการ?",
        "choices": [
            "id (รหัสรายการ), timestamp (วันเวลาที่บันทึก), และ temperature (ค่าอุณหภูมิที่วัดได้)",
            "ชื่อพนักงาน, เบอร์โทรศัพท์, และทะเบียนรถ",
            "สีของบอร์ด ESP32, ยี่ห้อปลั๊กไฟ, และความยาวสายไฟ",
            "ไฟล์ภาพถ่าย, ไฟล์เพลง, และไฟล์วิดีโอ"
        ],
        "correctAnswer": 0,
        "explanation": "ตารางข้อมูล Time-series IoT พื้นฐานต้องประกอบด้วย: 1. Primary Key (id) สำหรับอ้างอิงลำดับ 2. Timestamp เพื่อระบุว่าข้อมูลถูกบันทึกเมื่อใด (สำคัญที่สุดในการวิเคราะห์ย้อนหลัง) 3. Metric Value เช่น temperature (และอาจมี device_id เพิ่มเติมกรณีมีหลายโหนด)"
    },
    {
        "id": 34,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "เหตุใดฟิลด์ 'Timestamp' (วันและเวลาที่บันทึก) จึงมีความสำคัญสูงสุดในระบบจัดเก็บข้อมูล IoT?",
        "choices": [
            "เพราะทำให้สามารถนำข้อมูลไปพล็อตกราฟแนวโน้มตามเวลา (Time-series Analysis) และสืบค้นย้อนหลังได้ว่าเหตุการณ์ผิดปกติเกิดขึ้นเมื่อใด",
            "เพราะทำให้ไฟล์ฐานข้อมูลมีขนาดเล็กลง",
            "เพราะช่วยป้องกันไม่ให้ไวรัสคอมพิวเตอร์เข้าสู่ระบบ",
            "เพราะเป็นข้อบังคับที่ไม่สามารถรันโปรแกรมได้หากไม่มีฟิลด์นี้"
        ],
        "correctAnswer": 0,
        "explanation": "ข้อมูล IoT เกือบทั้งหมดเป็น Time-series Data การมี Timestamp ทำให้เราสามารถเรียงลำดับเหตุการณ์ วิเคราะห์แนวโน้มตามช่วงเวลา (เช่น เช้า/กลางวัน/เย็น), หาค่าเฉลี่ยรายวัน/รายเดือน และเปรียบเทียบข้อมูลย้อนหลังได้อย่างถูกต้อง"
    },
    {
        "id": 35,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "คำสั่งภาษา SQL ใดที่ถูกต้องในการสร้างตาราง 'temperature_logs' ในฐานข้อมูล SQLite?",
        "code": "CREATE TABLE temperature_logs (\n  id INTEGER PRIMARY KEY AUTOINCREMENT,\n  device_id TEXT NOT NULL,\n  temperature REAL NOT NULL,\n  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);",
        "choices": [
            "CREATE TABLE temperature_logs ( id INTEGER PRIMARY KEY AUTOINCREMENT, device_id TEXT, temperature REAL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );",
            "MAKE NEW DATABASE temperature_logs;",
            "INSERT INTO temperature_logs VALUES (1, 'ESP32', 25.5);",
            "SELECT * FROM temperature_logs;"
        ],
        "correctAnswer": 0,
        "explanation": "คำสั่ง 'CREATE TABLE' เป็นคำสั่ง DDL (Data Definition Language) ในการสร้างตาราง โดยระบุชื่อคอลัมน์ ชนิดข้อมูล (INTEGER, REAL, TEXT) และ Constraints เช่น PRIMARY KEY, AUTOINCREMENT, และ DEFAULT CURRENT_TIMESTAMP ได้อย่างถูกต้อง"
    },
    {
        "id": 36,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "ความแตกต่างในการนำไปใช้งานระหว่าง 'ข้อมูลค่าปัจจุบัน' (Real-time Value) และ 'ข้อมูลย้อนหลัง' (Historical Data) คือข้อใด?",
        "choices": [
            "ข้อมูลปัจจุบันเหมาะสำหรับการเฝ้าระวังและสั่งการแบบทันทีทันใด ส่วนข้อมูลย้อนหลังเหมาะสำหรับการวิเคราะห์แนวโน้ม คาดการณ์ และทำรายงานสถิติ",
            "ข้อมูลปัจจุบันเก็บไว้ในฮาร์ดดิสก์ถาวร ส่วนข้อมูลย้อนหลังเก็บไว้ใน RAM ชั่วคราว",
            "ข้อมูลปัจจุบันมีขนาดใหญ่กว่าข้อมูลย้อนหลังเสมอ",
            "ไม่มีความแตกต่างกัน ทั้งสองประเภทใช้ทดแทนกันได้ทุกประการ"
        ],
        "correctAnswer": 0,
        "explanation": "ข้อมูลปัจจุบัน (Current/Real-time) เช่น อุณหภูมิวินาทีนี้ ใช้สำหรับ Monitor บนหน้าจอ หรือทริกเกอร์เตือนภัยทันที ส่วนข้อมูลย้อนหลัง (Historical Data) ที่บันทึกลงฐานข้อมูล ใช้สำหรับดูพฤติกรรมระยะยาว เช่น วางแผนประหยัดแอร์ หรือดูว่าห้องไหนร้อนผิดปกติในแต่ละเดือน"
    },
    {
        "id": 37,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "เหตุใด 'SQLite' จึงเป็นตัวเลือกฐานข้อมูลที่นิยมใช้งานอย่างกว้างขวางบน Raspberry Pi สำหรับระบบ IoT ขนาดเล็กถึงปานกลาง?",
        "choices": [
            "เป็น Serverless Database ที่จัดเก็บข้อมูลทั้งหมดอยู่ในไฟล์เดี่ยว (.db) ไม่กินทรัพยากรเครื่อง และไม่ต้องติดตั้ง Service แยก",
            "เพราะทำงานเร็วกว่าระบบ Cloud ขนาดใหญ่ของ Google เสมอ",
            "เพราะไม่มีการใช้ภาษา SQL ในการสืบค้นข้อมูล",
            "เพราะสามารถรองรับผู้ใช้งานพร้อมกันได้หลายล้านคนพร้อมกัน"
        ],
        "correctAnswer": 0,
        "explanation": "SQLite เป็นฐานข้อมูลแบบฝังตัว (Embedded/Serverless) ที่เก็บข้อมูลทั้งหมดลงในไฟล์เดี่ยวบนดิสก์ มีน้ำหนักเบา (Lightweight) ใช้หน่วยความจำน้อยมาก และติดตั้งง่าย เหมาะกับระบบสมองกลฝังตัวอย่าง Raspberry Pi"
    },
    {
        "id": 38,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "ใน Firebase Realtime Database ข้อมูลทั้งหมดถูกจัดเก็บและจัดโครงสร้างในรูปแบบเอกสารชนิดใด?",
        "choices": [
            "JSON Tree (โครงสร้างต้นไม้แบบ JSON กิ่งก้านสาขา)",
            "ตารางตารางแบบ Relational (Table & Foreign Key)",
            "ไฟล์ Excel (.xlsx)",
            "ไฟล์ข้อความแบบ CSV"
        ],
        "correctAnswer": 0,
        "explanation": "Firebase Realtime Database เป็นฐานข้อมูลแบบ NoSQL ที่เก็บข้อมูลทั้งหมดเป็นอ็อบเจกต์ JSON ขนาดใหญ่ชิ้นเดียวในรูปแบบโครงสร้างต้นไม้ (JSON Tree) โดยไม่มีตาราง (Tables) หรือเรคอร์ด (Records) เหมือนฐานข้อมูล SQL แบบดั้งเดิม"
    },
    {
        "id": 39,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "การจัดโครงสร้างข้อมูลที่ดีใน Firebase Realtime Database สำหรับระบบที่มีเซ็นเซอร์หลายตัว (Multi-device) ควรออกแบบอย่างไร?",
        "choices": [
            "แยกโหนดตามรหัสอุปกรณ์ เช่น devices/{deviceId}/readings/{timestamp}/...",
            "นำข้อมูลของทุกอุปกรณ์มากองรวมกันในฟิลด์เดียวโดยไม่ระบุชื่อเครื่อง",
            "สร้างโปรเจกต์ Firebase ใหม่สำหรับเซ็นเซอร์ทุกๆ 1 ตัว",
            "บันทึกข้อมูลทุกตัวทับลงที่ Root Node เสมอ"
        ],
        "correctAnswer": 0,
        "explanation": "การแบ่งหมวดหมู่โดยใช้ Unique Device ID เป็นโหนดย่อย เช่น `devices/esp32_room101/temperature` ช่วยให้โครงสร้างแบน (Shallow Data Structure) ดึงข้อมูลง่าย และประหยัด Bandwidth เพราะสามารถ Listen เฉพาะอุปกรณ์ที่ต้องการได้โดยไม่ต้องดาวน์โหลดข้อมูลทั้งหมด"
    },
    {
        "id": 40,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "การดึงข้อมูลจาก Firebase Realtime Database มาแสดงผลบนหน้าเว็บไซต์แบบ Real-time นิยมใช้ฟังก์ชัน Listener ใดของ Firebase JavaScript SDK?",
        "code": "import { ref, onValue } from 'firebase/database';\n\nconst tempRef = ref(db, 'sensors/temperature');\nonValue(tempRef, (snapshot) => {\n  const data = snapshot.val();\n  document.getElementById('tempDisplay').innerText = data;\n});",
        "choices": [
            "onValue()",
            "fetchOnce()",
            "setInterval()",
            "queryAll()"
        ],
        "correctAnswer": 0,
        "explanation": "ฟังก์ชัน 'onValue()' ของ Firebase SDK ทำหน้าที่เป็น Real-time Event Listener เมื่อข้อมูลที่จุดอ้างอิง (ref) ในฐานข้อมูลมีการเปลี่ยนแปลง เซิร์ฟเวอร์จะผลักดัน (Push) ข้อมูลใหม่มายัง Callback Function ทันที ทำให้หน้าเว็บอัปเดตตัวเลขอัตโนมัติโดยไม่ต้อง Refresh หน้าจอ"
    },
    {
        "id": 41,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "หากกฎความปลอดภัย (Security Rules) ของ Firebase Realtime Database ถูกกำหนดไว้ดังนี้ จะเกิดผลกระทบอย่างไร?",
        "code": "{\n  \"rules\": {\n    \".read\": true,\n    \".write\": true\n  }\n}",
        "choices": [
            "เกิดช่องโหว่ความปลอดภัยร้ายแรง ใครก็ตามที่มี URL ของฐานข้อมูลสามารถเข้ามาอ่าน แก้ไข หรือลบข้อมูลทิ้งทั้งหมดได้โดยไม่ต้องล็อกอิน",
            "ทำให้ฐานข้อมูลทำงานเร็วขึ้นและปลอดภัยสูงสุด",
            "ระบบจะอนุญาตให้เฉพาะแอดมินเท่านั้นที่เข้าถึงได้",
            "ระบบจะเข้ารหัสข้อมูลทั้งหมดด้วยมาตรฐานระดับกองทัพ"
        ],
        "correctAnswer": 0,
        "explanation": "กฎ `\".read\": true, \".write\": true` (Public Access) เป็นอันตรายอย่างยิ่งต่อระบบ Production เพราะเปิดโอกาสให้บุคคลภายนอกเข้าถึงและดัดแปลงแก้ไข หรือสั่งลบ (Data Tampering / Data Loss) ได้อย่างอิสระ จึงควรจำกัดสิทธิ์โดยผูกกับ Firebase Authentication"
    },
    {
        "id": 42,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "แนวทางการกำหนด Firebase Security Rules ที่ปลอดภัยสำหรับการใช้งานระบบ IoT จริงควรทำอย่างไร?",
        "choices": [
            "กำหนดให้เขียนและอ่านข้อมูลได้เฉพาะ Client ที่ผ่านการยืนยันตัวตน (auth != null) หรือมี Secret Key ประจำอุปกรณ์ที่ถูกต้อง",
            "เปิดสิทธิ์สาธารณะตลอดไปเพื่อไม่ให้ระบบสะดุด",
            "ห้ามไม่ให้อุปกรณ์ใดๆ เขียนข้อมูลลงฐานข้อมูล",
            "ปิดการทำงานของฐานข้อมูลในเวลากลางคืน"
        ],
        "correctAnswer": 0,
        "explanation": "แนวทางที่ถูกต้องคือการใช้ Authentication เช่น ตรวจสอบ `auth != null` หรือการใช้ Database Secrets / Service Accounts สำหรับไมโครคอนโทรลเลอร์ เพื่อป้องกันไม่ให้ผู้ไม่หวังดีแอบส่งข้อมูลปลอมเข้ามาทำลายความถูกต้องของระบบ"
    },
    {
        "id": 43,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "คำสั่ง SQL ใดที่ใช้สำหรับดึงข้อมูลอุณหภูมิย้อนหลังเฉพาะช่วงวันที่ต้องการเพื่อนำมาวิเคราะห์?",
        "code": "SELECT * FROM temperature_logs WHERE created_at BETWEEN '2026-10-01' AND '2026-10-25';",
        "choices": [
            "SELECT * FROM temperature_logs WHERE created_at BETWEEN '2026-10-01' AND '2026-10-25';",
            "DELETE FROM temperature_logs WHERE date = '2026-10-01';",
            "UPDATE temperature_logs SET temp = 25;",
            "DROP TABLE temperature_logs;"
        ],
        "correctAnswer": 0,
        "explanation": "คำสั่ง 'SELECT ... WHERE created_at BETWEEN ... AND ...' เป็นคำสั่งมาตรฐานในการสืบค้นข้อมูลย้อนหลังตามช่วงเวลาที่กำหนด เพื่อนำชุดข้อมูล (Dataset) ไปคำนวณสถิติหรือสร้างกราฟสรุปผล"
    },
    {
        "id": 44,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "ข้อมูลอุณหภูมิและความชื้นย้อนหลังที่จัดเก็บในฐานข้อมูล สามารถนำไปใช้วิเคราะห์เพื่อประโยชน์ด้านใดในโรงเรียนหรือองค์กร?",
        "choices": [
            "วิเคราะห์ช่วงเวลาที่มีการใช้เครื่องปรับอากาศสูงสุดเพื่อวางแผนประหยัดพลังงาน และตรวจหาจุดที่เกิดความร้อนผิดปกติ",
            "ใช้คำนวณผลการเรียนเฉลี่ย (GPA) ของนักศึกษา",
            "ใช้เปลี่ยนสีผนังห้องเรียนโดยอัตโนมัติ",
            "ใช้แทนใบเสร็จรับเงินค่าลงทะเบียนเรียน"
        ],
        "correctAnswer": 0,
        "explanation": "ข้อมูลสภาพแวดล้อมย้อนหลังมีคุณค่าเชิงการจัดการ (Analytics) เช่น นำมาประเมินประสิทธิภาพการทำความเย็นของแอร์, ปรับเวลาเปิด-ปิดเครื่องปรับอากาศอัตโนมัติเพื่อลดค่าไฟ, และเฝ้าระวังความเสี่ยงของอุปกรณ์อิเล็กทรอนิกส์ในห้องปฏิบัติการ"
    },
    {
        "id": 45,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "ในการเชื่อมต่อเว็บแอปพลิเคชันเข้ากับ Firebase จำเป็นต้องใช้ข้อมูลการตั้งค่า (Firebase Config Object) ชุดใด?",
        "choices": [
            "apiKey, authDomain, databaseURL, projectId, storageBucket, appId",
            "username และ password ของอีเมลส่วนตัว",
            "หมายเลขบัตรประชาชนของอาจารย์ผู้สอน",
            "หมายเลขรหัสประจำตัวเครื่องคอมพิวเตอร์ Mac Address"
        ],
        "correctAnswer": 0,
        "explanation": "Firebase Config Object เป็นพารามิเตอร์ที่ได้รับจาก Firebase Console ประกอบด้วย apiKey, authDomain, databaseURL, projectId ฯลฯ เพื่อให้ Firebase SDK ของหน้าเว็บสามารถระบุตัวตนและเชื่อมต่อไปยังฐานข้อมูลของโปรเจกต์ได้อย่างถูกต้อง"
    },
    {
        "id": 46,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "ในกรณีที่เซ็นเซอร์ ESP32 ส่งข้อมูลมาถี่มาก (เช่น ทุก 1 วินาที) การจัดเก็บข้อมูลลง SD Card หรือ Flash Memory ของ Raspberry Pi โดยตรงอาจส่งผลเสียอย่างไร?",
        "choices": [
            "ทำให้ Flash Memory ของ SD Card เสื่อมสภาพและพังอย่างรวดเร็วจากจำนวนรอบการเขียน (Write Cycles) ที่มากเกินไป",
            "ทำให้อุปกรณ์มีน้ำหนักตัวเครื่องเพิ่มขึ้น",
            "ทำให้ไฟฟ้าลัดวงจรทันที",
            "ทำให้สัญญาณ Wi-Fi ถูกเปลี่ยนเป็นคลื่นวิทยุ AM"
        ],
        "correctAnswer": 0,
        "explanation": "SD Card มีขีดจำกัดในการเขียนซ้ำ (Write Endurance) การเขียนข้อมูลลงฐานข้อมูลบน SD Card ถี่เกินไปโดยไม่มีการทำ In-memory Buffering หรือการรวม Batch จะทำให้พื้นที่จัดเก็บบวมเร็วและ SD Card เสียหาย (Corrupted) ได้ในเวลาไม่กี่เดือน"
    },
    {
        "id": 47,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "การใช้คำสั่ง 'AVG(temperature)' ในคำสั่ง SQL มีประโยชน์อย่างไรในการทำรายงานสรุปผล?",
        "choices": [
            "คำนวณหาค่าเฉลี่ยของอุณหภูมิตามเงื่อนไขหรือช่วงเวลาที่กำหนด",
            "หาค่าอุณหภูมิที่สูงที่สุด",
            "หาค่าอุณหภูมิที่ต่ำที่สุด",
            "นับจำนวนครั้งที่เซ็นเซอร์หยุดทำงาน"
        ],
        "correctAnswer": 0,
        "explanation": "ฟังก์ชัน Aggregate 'AVG()' ในภาษา SQL ใช้คำนวณหาค่าเฉลี่ยทางสถิติของคอลัมน์ตัวเลข เช่น คำนวณอุณหภูมิเฉลี่ยประจำวัน (Daily Average Temperature)"
    },
    {
        "id": 48,
        "section": "การจัดเก็บข้อมูลและการจัดการฐานข้อมูล SQLite & Firebase",
        "question": "ข้อใดเป็นข้อดีของการเลือกใช้ Firebase Realtime Database เมื่อเทียบกับการจัดเก็บใน SQLite บนเครื่องตนเอง?",
        "choices": [
            "สามารถเข้าถึงและอัปเดตข้อมูลได้จากทุกที่ทั่วโลกผ่านอินเทอร์เน็ตโดยไม่ต้องตั้งค่า Forward Port หรือ Dynamic DNS ที่เราเตอร์",
            "สามารถใช้งานได้โดยไม่ต้องมีสัญญาณอินเทอร์เน็ตตลอดไป",
            "ไม่มีค่าใช้จ่ายใดๆ ทั้งสิ้นไม่ว่าจะใช้งานมากเท่าใด",
            "เป็นฐานข้อมูลที่เขียนโค้ดด้วยภาษา Assembly"
        ],
        "correctAnswer": 0,
        "explanation": "Firebase เป็น Cloud-hosted Database ทำให้แอปพลิเคชันหรือผู้ใช้งานจากที่ใดก็ได้ในโลกสามารถเข้าถึงข้อมูล Real-time ได้ทันทีผ่านอินเทอร์เน็ต โดยที่ผู้พัฒนาไม่ต้องกังวลเรื่องการเปิด Port Forwarding, การขอ Public IP หรือการดูแลฮาร์ดแวร์เซิร์ฟเวอร์"
    },

    # ==========================================
    # หมวดที่ 4: การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ (16 ข้อ: ข้อ 49 - 64)
    # ==========================================
    {
        "id": 49,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ในการควบคุมเปิด-ปิดหลอดไฟ 220V ผ่านโมดูล Relay ด้วย ESP32 ข้อใดอธิบายการทำงานของขาควบคุมและวงจรได้อย่างถูกต้อง?",
        "choices": [
            "ESP32 ส่งสัญญาณลอจิกดิจิทัล (HIGH/LOW 3.3V) ไปทริกเกอร์วงจรออปโต้คัปเปลอร์ของ Relay เพื่อดูดหน้าสัมผัสสวิตช์ให้วงจรไฟฟ้า 220V ครบวงจร",
            "ESP32 จ่ายกระแสไฟฟ้า 220V ออกจากขา GPIO โดยตรงไปยังหลอดไฟ",
            "Relay ทำหน้าที่เป็นตัวแปลงสัญญาณ Wi-Fi ให้เป็นคลื่นความร้อน",
            "หลอดไฟต้องเชื่อมต่อเข้ากับขาเสาอากาศของ ESP32 เสมอ"
        ],
        "correctAnswer": 0,
        "explanation": "Relay ทำหน้าที่เป็นสวิตช์กลไกไฟฟ้าที่ใช้สัญญาณไฟฟ้าแรงดันต่ำ (3.3V/5V) จากขา GPIO ของไมโครคอนโทรลเลอร์ มาสั่งการขดลวดแม่เหล็กเพื่อตัดหรือต่อวงจรไฟฟ้าแรงดันสูง (220VAC) โดยมีการแยกทางกายภาพ (Galvanic Isolation ผ่าน Optocoupler) เพื่อความปลอดภัยของบอร์ดไมโครคอนโทรลเลอร์"
    },
    {
        "id": 50,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ความแตกต่างระหว่างโมดูล Relay แบบ 'Active Low' และ 'Active High' คือข้อใด?",
        "choices": [
            "Active Low จะสั่งให้ Relay ทำงานเมื่อจ่ายสัญญาณลอจิก LOW (0V) ส่วน Active High จะทำงานเมื่อจ่ายสัญญาณ HIGH (3.3V/5V)",
            "Active Low ใช้กับไฟกระแสสลับ ส่วน Active High ใช้กับไฟกระแสตรง",
            "Active Low เปิดปิดช้ากว่า Active High 10 เท่า",
            "Active Low ไม่ต้องต่อสายไฟกราวด์ (GND)"
        ],
        "correctAnswer": 0,
        "explanation": "โมดูล Relay ส่วนใหญ่ในท้องตลาดมักเป็น 'Active Low' คือหน้าสัมผัสจะทำงาน (สวิตช์เปิด) เมื่อขา IN ได้รับสัญญาณดิจิทัล '0' หรือ LOW และจะตัดวงจรเมื่อได้รับสัญญาณ '1' หรือ HIGH นักพัฒนาจึงต้องตรวจสอบสเปกของโมดูลให้ชัดเจน"
    },
    {
        "id": 51,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "เมื่อใช้งานแอปพลิเคชัน 'IoT MQTT Panel' บนมือถือเพื่อควบคุม Relay 2 ช่องอย่างเป็นอิสระต่อกัน ควรออกแบบ Topic และ Payload อย่างไร?",
        "choices": [
            "แยก Topic ให้ชัดเจน เช่น 'home/relay1/set' และ 'home/relay2/set' โดยส่ง Payload เป็น 'ON' หรือ 'OFF'",
            "ใช้ Topic เดียวกันและส่งข้อความเหมือนกันทั้ง 2 ตัวตลอดเวลา",
            "ให้ผู้ใช้พิมพ์เลขโทรศัพท์ของบอร์ด ESP32 ทุกครั้งที่จะสั่งงาน",
            "ใช้การสั่นโทรศัพท์เพื่อสลับการทำงานของ Relay"
        ],
        "correctAnswer": 0,
        "explanation": "การแยก Topic เช่น `home/relay1/set` และ `home/relay2/set` เป็นวิธีที่เรียบง่ายและเป็นอิสระที่สุด ทำให้ ESP32 สามารถเขียนฟังก์ชัน Callback ดักจับ Topic เพื่อสั่ง `digitalWrite(RELAY1_PIN, ...)` และ `digitalWrite(RELAY2_PIN, ...)` แยกจากกันได้อย่างเด็ดขาด"
    },
    {
        "id": 52,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ในโค้ด Arduino C++ บน ESP32 ฟังก์ชันใดของไลบรารี PubSubClient ที่ทำหน้าที่รับข้อความคำสั่งที่ส่งมาจาก MQTT Broker?",
        "code": "void callback(char* topic, byte* payload, unsigned int length) {\n  // ฟังก์ชันนี้ทำงานเมื่อใด?\n}",
        "choices": [
            "Callback function (ฟังก์ชันตอบรับข้อความที่ลงทะเบียนไว้กับ client.setCallback())",
            "setup() function",
            "loop() function",
            "WiFi.begin() function"
        ],
        "correctAnswer": 0,
        "explanation": "ในไลบรารี PubSubClient ฟังก์ชัน 'callback' จะถูกเรียกทำงานโดยอัตโนมัติเมื่อมีข้อความใหม่ส่งเข้ามายัง Topic ที่ ESP32 ได้กด Subscribe ไว้ โดยมีพารามิเตอร์ส่ง topic, ข้อความ payload, และความยาวข้อมูลมาให้เพื่อนำไปประมวลผลต่อ"
    },
    {
        "id": 53,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "หากบอร์ด ESP32 ไม่สามารถเชื่อมต่อกับ MQTT Broker ได้ สาเหตุที่เป็นไปได้มากที่สุดในทางปฏิบัติคือข้อใด?",
        "choices": [
            "ESP32 ยังไม่ได้เชื่อมต่อ Wi-Fi หรือระบุหมายเลข IP / Port ของ Broker ผิดพลาด หรือมี Firewall บล็อกพอร์ต 1883 ไว้",
            "ความสว่างของหลอดไฟในห้องสว่างเกินไป",
            "ไม่ได้เสียบสายหูฟังเข้ากับบอร์ด ESP32",
            "เซ็นเซอร์วัดอุณหภูมิมีราคาสูงเกินไป"
        ],
        "correctAnswer": 0,
        "explanation": "สาเหตุหลักที่พบบ่อยในการทำแล็บ: 1. Wi-Fi หลุดหรือเชื่อมต่อไม่สำเร็จ 2. ระบุ IP Address ของ Raspberry Pi ผิด (เช่น IP เปลี่ยนจาก DHCP) 3. ระบุ Port ผิด หรือ Broker ไม่ได้เปิดเซอร์วิส 4. คอนฟิก mosquitto.conf ไม่ได้เปิด `listener 1883` และ `allow_anonymous true`"
    },
    {
        "id": 54,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ในการตรวจสอบเบื้องต้นเมื่อ ESP32 เชื่อมต่อ Wi-Fi หรือ MQTT ไม่สำเร็จ เครื่องมือใดในโปรแกรม Arduino IDE ที่สำคัญที่สุดในการดูข้อความ Error?",
        "choices": [
            "Serial Monitor (หน้าต่างมอนิเตอร์พอร์ตอนุกรมผ่าน Serial.println)",
            "Color Picker",
            "Font Size Manager",
            "Auto Format Code"
        ],
        "correctAnswer": 0,
        "explanation": "Serial Monitor คือเครื่องมือ Debug พื้นฐานที่สำคัญที่สุด นักพัฒนาจะใช้ `Serial.print()` เพื่อดู IP Address ที่ได้รับ, ดูสถานะการเชื่อมต่อ Wi-Fi (`WiFi.status()`) และดูรหัสข้อผิดพลาดของ MQTT (`client.state()` เช่น -2 = Connection Failed)"
    },
    {
        "id": 55,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ปัจจัยใดที่ควรนำมาพิจารณาในการกำหนด 'ความถี่ในการส่งข้อมูล' (Sampling & Publishing Rate) ของเซ็นเซอร์ เช่น การเลือกระหว่างส่งทุก 10 วินาที หรือส่งทุก 5 นาที?",
        "choices": [
            "ลักษณะการเปลี่ยนแปลงของข้อมูล, ปริมาณแบนด์วิดท์เครือข่าย, ปริมาณพื้นที่จัดเก็บข้อมูลในฐานข้อมูล, และอัตราการใช้พลังงานของอุปกรณ์",
            "สีของสายจัมเปอร์ที่ใช้เชื่อมต่อ",
            "ยี่ห้อของจอคอมพิวเตอร์ที่ใช้เขียนโค้ด",
            "ขนาดหน้าจอของโทรศัพท์มือถือ"
        ],
        "correctAnswer": 0,
        "explanation": "การกำหนดความถี่ต้องพิจารณาความเหมาะสม: อุณหภูมิห้องเปลี่ยนแปลงช้า การส่งทุก 1-5 นาทีก็เพียงพอ การส่งถี่เกินไป (เช่น ทุก 1-2 วินาที) จะทำให้เปลืองพลังงานแบตเตอรี่, เปลืองแบนด์วิดท์ Wi-Fi และทำให้ฐานข้อมูลมีขนาดบวมอย่างรวดเร็วโดยไม่จำเป็น"
    },
    {
        "id": 56,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "กลยุทธ์ 'Publish on Change' (ส่งข้อมูลเฉพาะเมื่อค่าเปลี่ยนแปลงเกินเกณฑ์ที่กำหนด) มีประโยชน์อย่างไรเมื่อเทียบกับการส่งตามช่วงเวลาคงที่ (Fixed Interval)?",
        "choices": [
            "ช่วยลดปริมาณข้อมูลที่ไม่จำเป็นได้อย่างมหาศาล ประหยัดพลังงาน และลดภาระของเครือข่ายและฐานข้อมูล",
            "ทำให้ค่าอุณหภูมิมีความแม่นยำสูงขึ้น 10 เท่า",
            "ช่วยให้เซ็นเซอร์ไม่ต้องใช้พลังงานไฟฟ้า",
            "ช่วยให้สามารถใช้งานได้โดยไม่ต้องมี Wi-Fi"
        ],
        "correctAnswer": 0,
        "explanation": "'Publish on Change' หรือ Deadband Reporting คือการตรวจสอบว่าถ้าค่าอุณหภูมิเปลี่ยนไปไม่ถึง 0.5 องศา จะไม่ส่งข้อมูลซ้ำ จะส่งเฉพาะเมื่อค่ามีการเปลี่ยนแปลงอย่างมีนัยสำคัญ ช่วยลด Traffic ในเครือข่ายลงได้มากกว่า 80%"
    },
    {
        "id": 57,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ในการออกแบบแอปพลิเคชันมือถือสำหรับ 'ดูอุณหภูมิและควบคุมพัดลม' สถาปัตยกรรมการสื่อสาร MQTT ควรทำงานร่วมกันอย่างไร?",
        "choices": [
            "แอปพลิเคชัน Subscribe รับข้อมูลจาก Topic อุณหภูมิ และ Publish คำสั่งควบคุมไปยัง Topic พัดลม",
            "แอปพลิเคชันทำหน้าที่เป็น Broker เสียเอง",
            "แอปพลิเคชันเชื่อมต่อไปยังสายไฟของพัดลมโดยตรง",
            "แอปพลิเคชันสั่งงานผ่านการโทรศัพท์อัตโนมัติ"
        ],
        "correctAnswer": 0,
        "explanation": "แอปพลิเคชันจะทำ 2 หน้าที่ในเวลาเดียวกัน: 1. ทำหน้าที่เป็น Subscriber รอรับข้อมูลอุณหภูมิจาก Topic (เช่น `room/temp`) เพื่อนำมาอัปเดตหน้าปัด 2. ทำหน้าที่เป็น Publisher ส่งข้อความ ('ON'/'OFF') ไปยัง Topic ควบคุม (เช่น `room/fan/set`) เมื่อผู้ใช้แตะปุ่ม"
    },
    {
        "id": 58,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "เพื่อความปลอดภัยและความถูกต้อง เมื่อแอปพลิเคชันส่งคำสั่งเปิดพัดลมไปยัง ESP32 ระบบที่ดีควรมีกลไกใดในการยืนยันสถานะกลับมาที่หน้าจอ (Feedback Loop)?",
        "choices": [
            "ให้ ESP32 Publish สถานะจริงของ Relay กลับมายัง Topic สถานะ (เช่น 'room/fan/status') เพื่อให้แอปปรับเปลี่ยนสีไอคอนปุ่มตามสถานะจริง",
            "ให้ผู้ใช้เดินไปดูพัดลมด้วยตนเองทุกครั้ง",
            "ให้ระบบส่งเสียงบี๊บดัง 10 ครั้ง",
            "ให้แอปพลิเคชันเดาสุ่มสถานะเองโดยไม่ต้องรับการยืนยัน"
        ],
        "correctAnswer": 0,
        "explanation": "หลักการควบคุมที่ดีต้องมี Feedback Loop: เมื่อ ESP32 สับสวิตช์ Relay สำเร็จ จะต้อง Publish สถานะจริงกลับมายัง Status Topic เพื่อยืนยันว่าคำสั่งทำงานสำเร็จจริง ไม่ใช่แค่ส่งคำสั่งลอยๆ แล้วแอปคิดเอาเองว่าพัดลมเปิดแล้ว"
    },
    {
        "id": 59,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ขาเซ็นเซอร์วัดอุณหภูมิและความชื้น 'DHT22' ที่เชื่อมต่อกับบอร์ด ESP32 สายสัญญาณข้อมูล (Data Pin) มักจำเป็นต้องต่อตัวต้านทานแบบใดเพื่อเสถียรภาพของสัญญาณดิจิทัล?",
        "choices": [
            "Pull-up Resistor (ขนาดประมาณ 4.7kΩ - 10kΩ) เชื่อมต่อระหว่างขา Data กับไฟ VCC",
            "Pull-down Resistor ขนาด 1MΩ",
            "ตัวเก็บประจุขนาดใหญ่ต่ออนุกรม",
            "ไม่ต้องต่อตัวต้านทานใดๆ และห้ามใช้ตัวต้านทานเด็ดขาด"
        ],
        "correctAnswer": 0,
        "explanation": "โพรโทคอล 1-Wire แบบ Single-bus ของ DHT22 ต้องการตัวต้านทาน Pull-up ขนาด 4.7kΩ - 10kΩ ดึงสายสัญญาณเข้ากับไฟเลี้ยง (3.3V/5V) เพื่อรักษาระดับแรงดันในสภาวะว่าง (Idle High) ช่วยป้องกันสัญญาณรบกวน"
    },
    {
        "id": 60,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "เมื่อใช้งาน ESP32 ส่งข้อมูลผ่านเครือข่าย Wi-Fi การใช้คำสั่ง 'delay(10000)' ในฟังก์ชัน loop() ส่งผลเสียต่อการทำงานของระบบ MQTT อย่างไร?",
        "choices": [
            "คำสั่ง delay() จะบล็อกการทำงานของ CPU ทำให้ฟังก์ชัน 'client.loop()' ไม่ได้ทำงาน ส่งผลให้ ESP32 ไม่สามารถรับข้อความเข้าและอาจถูก Broker ตัดการเชื่อมต่อจาก Keep-alive Timeout",
            "ทำให้ค่าอุณหภูมิที่วัดได้ลดลง 10 องศา",
            "ทำให้บอร์ด ESP32 ร้อนจนไหม้",
            "ไม่มีผลเสียใดๆ เป็นวิธีที่แนะนำให้ใช้เสมอ"
        ],
        "correctAnswer": 0,
        "explanation": "การใช้ `delay()` ยาวๆ เป็นการบล็อก Thread หลัก ทำให้ฟังก์ชัน `client.loop()` ไม่ได้ทำงานตามรอบ ส่งผลให้ไม่สามารถส่ง Ping (Heartbeat) ไปยัง Broker ได้ทันเวลา ทำให้ Broker คิดว่า ESP32 ตายไปแล้วและตัดการเชื่อมต่อ ทางแก้คือการใช้ฟังก์ชัน `millis()` แบบ Non-blocking"
    },
    {
        "id": 61,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ในการเชื่อมต่อ Relay เข้ากับเครื่องใช้ไฟฟ้า หน้าสัมผัส 'NO' (Normally Open) และ 'NC' (Normally Closed) มีความแตกต่างกันอย่างไร?",
        "choices": [
            "NO คือวงจรเปิดในสภาวะปกติ (ไฟดับ) จะติดเมื่อสั่งงาน, ส่วน NC คือวงจรปิดในสภาวะปกติ (ไฟติด) จะดับเมื่อสั่งงาน",
            "NO ใช้กับกระแสตรง ส่วน NC ใช้กับกระแสสลับ",
            "NO ทนกระแสได้มากกว่า NC 100 เท่า",
            "ทั้งสองขามีการทำงานเหมือนกันทุกประการ"
        ],
        "correctAnswer": 0,
        "explanation": "ขั้วต่อ Relay: COM คือขากลางร่วม / NO (Normally Open) คือปกติวงจรเปิด (เครื่องใช้ไฟฟ้าดับ) จะทำงานเมื่อ Relay ถูกกระตุ้น / ส่วน NC (Normally Closed) คือปกติวงจรปิด (เครื่องใช้ไฟฟ้าเปิดอยู่ตลอด) จะตัดการทำงานเมื่อ Relay ถูกกระตุ้น"
    },
    {
        "id": 62,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "หากต้องการประหยัดพลังงานแบตเตอรี่ของ ESP32 ที่ติดตั้งในจุดที่ไม่มีปลั๊กไฟ ควรใช้โหมดการทำงานใดของ ESP32 ในช่วงระหว่างรอบการวัดค่า?",
        "choices": [
            "Deep Sleep Mode (ให้ตื่นขึ้นมาวัดค่า ส่ง MQTT แล้วกลับไปหลับลึกทันที)",
            "Overclocking Mode",
            "Bluetooth Classic Scanning Mode",
            "Full Wi-Fi AP Mode"
        ],
        "correctAnswer": 0,
        "explanation": "ESP32 มีฟังก์ชัน 'Deep Sleep Mode' ซึ่งจะปิดการทำงานของ CPU, Wi-Fi, และ Bluetooth เหลือไว้เพียงโมดูล ULP และ RTC Timer ที่กินกระแสไฟฟ้าเพียงไม่กี่ไมโครแอมป์ (uA) ทำให้สามารถใช้งานร่วมกับแบตเตอรี่ได้นานหลายเดือนถึงเป็นปี"
    },
    {
        "id": 63,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "เมื่อใช้งานแอปพลิเคชัน IoT MQTT Panel การตั้งค่าชนิดของวิดเจ็ตสำหรับควบคุม Relay ควรเลือกคอนโทรลเลอร์ชนิดใด?",
        "choices": [
            "Switch หรือ Toggle Button",
            "Progress Bar",
            "Line Graph",
            "Static Text Label"
        ],
        "correctAnswer": 0,
        "explanation": "การควบคุมสถานะเปิด-ปิดของอุปกรณ์ดิจิทัล 2 สถานะ (Binary State) ควรใช้วิดเจ็ตประเภท 'Switch' หรือ 'Toggle Button' ซึ่งสามารถกำหนดค่า Payload สำหรับสถานะ ON (เช่น '1' หรือ 'ON') และสถานะ OFF (เช่น '0' หรือ 'OFF') ได้อย่างสะดวก"
    },
    {
        "id": 64,
        "section": "การควบคุมอุปกรณ์และการประยุกต์ใช้งานเชิงปฏิบัติ",
        "question": "ในกรณีที่ ESP32 ต้องส่งทั้งค่าอุณหภูมิและความชื้นพร้อมกัน การจัดรูปแบบข้อมูลแบบใดที่ได้รับความนิยมสูงสุดในระบบ IoT ยุคปัจจุบัน?",
        "choices": [
            "JSON Format เช่น '{\"temp\": 28.5, \"humidity\": 65.2}'",
            "ส่งเป็นไฟล์ข้อความ Word Document",
            "ส่งเป็นตัวเลขติดกันโดยไม่มีตัวคั่น",
            "ส่งเป็นรหัส Morse Code"
        ],
        "correctAnswer": 0,
        "explanation": "รูปแบบ JSON (JavaScript Object Notation) เป็นมาตรฐานสากลในการแลกเปลี่ยนข้อมูล IoT เพราะมีโครงสร้างแบบ Key-Value ที่มนุษย์อ่านเข้าใจง่าย (Human-readable) และโปรแกรมต่างๆ (Node-RED, Python, Web) มีไลบรารีถอดรหัส (Parse) ได้สะดวกรวดเร็ว"
    },

    # ==========================================
    # หมวดที่ 5: การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม (16 ข้อ: ข้อ 65 - 80)
    # ==========================================
    {
        "id": 65,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "ข้อดีของการใช้ 'Raspberry Pi' เป็นเครื่องแม่ข่ายภายในเครือข่ายท้องถิ่น (Local Edge Server) เมื่อเปรียบเทียบกับการส่งข้อมูลขึ้น Cloud โดยตรงคือข้อใด?",
        "choices": [
            "ระบบยังคงทำงานและควบคุมได้แม้ไม่มีอินเทอร์เน็ตภายนอก (Offline Capability), ความหน่วงต่ำ (Low Latency), และรักษาความเป็นส่วนตัวของข้อมูลภายในองค์กร",
            "ไม่ต้องใช้ไฟฟ้าในการเปิดเครื่อง",
            "สามารถเพิ่มจำนวนขา GPIO ได้ไม่จำกัด",
            "ทำให้ไม่ต้องเขียนโค้ดในการควบคุมระบบ"
        ],
        "correctAnswer": 0,
        "explanation": "Local Edge Server (เช่น Raspberry Pi) มีจุดแข็งคือ: 1. ทำงานได้แม้เน็ตนอกล่ม 2. การตอบสนองรวดเร็วมาก (Low Latency ไม่ต้องส่งข้อมูลไปกลับต่างประเทศ) 3. Data Privacy ข้อมูลเซ็นเซอร์และภาพไม่หลุดออกนอกองค์กร 4. ไม่มีค่าบริการ Cloud รายเดือน"
    },
    {
        "id": 66,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "โปรแกรมเว็บเซิร์ฟเวอร์ 'Nginx' ที่ติดตั้งบน Raspberry Pi ทำหน้าที่อะไรในระบบ IoT ของห้องปฏิบัติการ?",
        "choices": [
            "ให้บริการไฟล์หน้าเว็บ (HTML, CSS, JavaScript) แก่คอมพิวเตอร์และมือถือเครื่องอื่นๆ ในเครือข่ายวงแลนเดียวกันผ่าน HTTP/HTTPS",
            "ทำหน้าที่เป็นเซ็นเซอร์ตรวจวัดความดันอากาศ",
            "ใช้สำหรับระบายความร้อนให้ซีพียู",
            "ทำหน้าที่แปลงสัญญาณดาวเทียม"
        ],
        "correctAnswer": 0,
        "explanation": "Nginx เป็น Web Server ประสิทธิภาพสูง น้ำหนักเบา ทำหน้าที่รับคำขอ (HTTP Request) จากเว็บเบราว์เซอร์ของไคลเอนต์ แล้วส่งไฟล์หน้าเว็บไซต์ (Web Dashboard, รายงานข้อมูล) กลับไปแสดงผลให้ผู้ใช้งานดู"
    },
    {
        "id": 67,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "ขั้นตอนโดยสังเขปที่คอมพิวเตอร์เครื่องอื่นในวงแลนจะใช้เปิดดูเว็บไซต์ที่โฮสต์บน Nginx ใน Raspberry Pi คือข้อใด?",
        "choices": [
            "เชื่อมต่อ Wi-Fi วงเดียวกัน -> เปิด Web Browser -> พิมพ์ URL เป็นหมายเลข IP ของ Raspberry Pi เช่น http://192.168.1.150",
            "เปิดโปรแกรม Notepad แล้วพิมพ์ IP ของ Raspberry Pi",
            "เสียบสาย USB เชื่อมตรงจาก Raspberry Pi เข้ากับจอภาพ",
            "ต้องส่งคำร้องขอเปิดเว็บผ่านไปรษณีย์ไปยังผู้ให้บริการ"
        ],
        "correctAnswer": 0,
        "explanation": "เครื่องคอมพิวเตอร์หรือสมาร์ตโฟนที่อยู่ในเครือข่าย Local Area Network เดียวกัน สามารถเปิดโปรแกรม Web Browser (Chrome, Safari) แล้วพิมพ์ `http://<IP_RaspberryPi>` (พอร์ต 80 เป็นพอร์ตดีฟอลต์ไม่ต้องพิมพ์ระบุก็ได้) เพื่อเข้าถึงเว็บไซต์ได้ทันที"
    },
    {
        "id": 68,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "หากคอมพิวเตอร์ในห้องปฏิบัติการไม่สามารถเปิดเว็บไซต์บน Raspberry Pi ได้ ปัจจัยที่อาจเป็นสาเหตุคือข้อใด?",
        "choices": [
            "คอมพิวเตอร์และ Raspberry Pi อยู่คนละวงเครือข่าย (คนละ Wi-Fi/Subnet), บริการ Nginx หยุดทำงาน, หรือพิมพ์ IP Address ผิดพลาด",
            "สีของเคส Raspberry Pi ไม่ตรงกับสีโต๊ะทำงาน",
            "คอมพิวเตอร์เครื่องนั้นไม่ได้ติดตั้งระบบปฏิบัติการ Linux",
            "เมาส์ของคอมพิวเตอร์ไม่มีไฟ LED"
        ],
        "correctAnswer": 0,
        "explanation": "สาเหตุหลักที่เข้าเว็บไม่ได้: 1. ปัญหาเครือข่าย (ไม่ได้ต่อ Wi-Fi เดียวกัน หรือมีระบบ Client Isolation ในเราเตอร์) 2. IP Address ของ Pi เปลี่ยนแปลง 3. เซอร์วิส Nginx ไม่ได้สตาร์ท (`sudo systemctl status nginx`) 4. ไฟร์วอลล์ (ufw) บล็อกพอร์ต 80"
    },
    {
        "id": 69,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "โฟลเดอร์เริ่มต้น (Default Document Root) ที่ Nginx ใช้จัดเก็บไฟล์เว็บไซต์ index.html บนระบบปฏิบัติการ Raspberry Pi OS คือไดเรกทอรีใด?",
        "choices": [
            "/var/www/html/",
            "/home/pi/desktop/",
            "/etc/nginx/sites-available/",
            "/usr/bin/web/"
        ],
        "correctAnswer": 0,
        "explanation": "โฟลเดอร์มาตรฐานของ Nginx ในการจัดเก็บไฟล์เว็บคือ `/var/www/html/` หากนำไฟล์ `index.html` ไปวางไว้ที่นี่ ผู้ใช้จะสามารถเข้าดูหน้าเว็บผ่าน Browser ได้ทันที"
    },
    {
        "id": 70,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "คำสั่งใดในระบบ Linux ที่ใช้สำหรับตรวจสอบหมายเลข IP Address ของ Raspberry Pi ในเครือข่ายปัจจุบัน?",
        "choices": [
            "hostname -I (หรือ ip addr show / ifconfig)",
            "show my ip",
            "ping google.com",
            "whoami"
        ],
        "correctAnswer": 0,
        "explanation": "คำสั่ง 'hostname -I' เป็นวิธีที่เร็วและง่ายที่สุดในการดูหมายเลข IP Address ของเครื่อง Raspberry Pi หรือสามารถใช้คำสั่ง 'ip a' เพื่อดูรายละเอียดของอินเทอร์เฟซ eth0 (สายแลน) และ wlan0 (ไวไฟ) อย่างละเอียด"
    },
    {
        "id": 71,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "ในการออกแบบระบบ IoT ตรวจวัดอุณหภูมิในห้องเรียนครบวงจร องค์ประกอบใดทำหน้าที่เป็น 'Data Producer' (ผู้ผลิตข้อมูล)?",
        "choices": [
            "ESP32 ร่วมกับเซ็นเซอร์วัดอุณหภูมิ (เช่น DHT22)",
            "หน้าจอ Dashboard",
            "MQTT Broker",
            "ฐานข้อมูล SQLite"
        ],
        "correctAnswer": 0,
        "explanation": "ESP32 และเซ็นเซอร์ทำหน้าที่เป็น Edge Node / Data Producer คอยเก็บเกี่ยวข้อมูลทางกายภาพ (อุณหภูมิ) แปลงเป็นสัญญาณดิจิทัล แล้วส่งต่อเข้าสู่ระบบเครือข่าย"
    },
    {
        "id": 72,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "ในการออกแบบระบบ IoT ตรวจวัดอุณหภูมิในห้องเรียน องค์ประกอบใดทำหน้าที่เป็น 'Data Broker' (ผู้จัดการกระจายข้อมูล)?",
        "choices": [
            "Mosquitto MQTT Broker บน Raspberry Pi",
            "เซ็นเซอร์วัดอุณหภูมิ",
            "หลอดไฟ LED",
            "หม้อแปลงไฟฟ้า"
        ],
        "correctAnswer": 0,
        "explanation": "Mosquitto ทำหน้าที่เป็น Message Broker คอยรับข้อมูลจากอุปกรณ์เซ็นเซอร์ และจัดส่งไปยังแอปพลิเคชันหรือระบบประมวลผลต่างๆ ตาม Topic ที่ลงทะเบียนไว้"
    },
    {
        "id": 73,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "ในการออกแบบระบบ IoT ตรวจวัดอุณหภูมิห้องเรียน องค์ประกอบใดทำหน้าที่เป็น 'Data Processor & Presentation' (ประมวลผลและนำเสนอข้อมูล)?",
        "choices": [
            "Node-RED ร่วมกับโหนด Dashboard",
            "สายไฟเบอร์ออปติก",
            "กล่องพลาสติกสำหรับใส่บอร์ด",
            "ถ่านไฟฉาย 9V"
        ],
        "correctAnswer": 0,
        "explanation": "Node-RED ทำหน้าที่ประมวลผล (Business Logic / Data Transformation / Threshold Checking) และโมดูล Dashboard ทำหน้าที่เรนเดอร์ UI (Gauges, Charts) ให้ผู้ใช้สามารถดูข้อมูลผ่านหน้าจอได้อย่างเข้าใจง่าย"
    },
    {
        "id": 74,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "หากต้องการตั้งค่าให้เซอร์วิสต่างๆ (เช่น Mosquitto, Node-RED, Nginx) เริ่มต้นทำงานโดยอัตโนมัติทุกครั้งที่เปิดเครื่อง Raspberry Pi (Auto-start on boot) ควรใช้คำสั่งใด?",
        "choices": [
            "sudo systemctl enable <service_name>",
            "sudo apt update",
            "sudo systemctl stop <service_name>",
            "reboot now"
        ],
        "correctAnswer": 0,
        "explanation": "คำสั่ง 'sudo systemctl enable <service_name>' จะสร้าง Symbolic Link ในระบบ systemd เพื่อสั่งให้โปรแกรมดังกล่าวเริ่มต้นทำงานโดยอัตโนมัติทันทีที่ระบบปฏิบัติการบูตเครื่องเสร็จสิ้น (Start on Boot) ทำให้ระบบ IoT ทำงานต่อเนื่องโดยไม่ต้องมีคนมาเปิดโปรแกรม"
    },
    {
        "id": 75,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "แนวคิดเรื่อง 'Edge Computing' ในระบบ IoT แตกต่างจาก 'Cloud Computing' แบบดั้งเดิมอย่างไร?",
        "choices": [
            "Edge Computing มุ่งเน้นการประมวลผลและวิเคราะห์ข้อมูลที่บริเวณใกล้กับแหล่งกำเนิดข้อมูล (เช่น บน Raspberry Pi ในอาคาร) เพื่อลดความหน่วงและลดการส่งข้อมูลปริมาณมากขึ้นสู่ Cloud",
            "Edge Computing หมายถึงการประมวลผลข้อมูลบนอวกาศ",
            "Edge Computing ต้องใช้เครื่องซูเปอร์คอมพิวเตอร์เท่านั้น",
            "Edge Computing ไม่มีการเชื่อมต่อกับเซ็นเซอร์ใดๆ"
        ],
        "correctAnswer": 0,
        "explanation": "Edge Computing คือการขยับการประมวลผลมาไว้ที่ริมขอบของเครือข่าย (Edge) ใกล้กับเซ็นเซอร์ เช่น ประมวลผลบน Gateway/Raspberry Pi ช่วยลดภาระการส่งข้อมูลขึ้น Cloud ประหยัดแบนด์วิดท์ และทำให้ตัดสินใจสั่งงานอุปกรณ์ได้แบบ Real-time แม้เน็ตหลุด"
    },
    {
        "id": 76,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "ข้อใดเป็นมาตรการป้องกันความปลอดภัยพื้นฐานที่ดีเมื่อนำ Raspberry Pi มาทำเป็นเซิร์ฟเวอร์ IoT ในเครือข่าย?",
        "choices": [
            "เปลี่ยนรหัสผ่านเริ่มต้นของระบบ (Default Password ของผู้ใช้ pi), อัปเดตแพ็กเกจระบบสม่ำเสมอ, และเปิดใช้งานเฉพาะพอร์ตที่จำเป็นผ่าน Firewall",
            "แชร์รหัสผ่านของเครื่องไว้บนกระดานดำในห้องเรียน",
            "ปิดการอัปเดตความปลอดภัยทั้งหมด",
            "เปิดพอร์ตทั้งหมดตั้งแต่ 1 ถึง 65535 ให้ทุกคนใช้งานได้อิสระ"
        ],
        "correctAnswer": 0,
        "explanation": "ความปลอดภัยของ IoT Edge Server ต้องเริ่มจาก: 1. เปลี่ยนรหัสผ่านตั้งต้น (เพื่อป้องกันการถูกโจมตีด้วย Botnet เช่น Mirai) 2. สั่ง `sudo apt update && sudo apt upgrade` สม่ำเสมอ 3. ตั้งค่า Firewall (UFW) ให้เปิดเฉพาะพอร์ตที่ใช้งาน เช่น 22 (SSH), 80 (HTTP), 1883 (MQTT)"
    },
    {
        "id": 77,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "ในการออกแบบระบบแจ้งเตือนอุณหภูมิห้องเรียน หากค่าอุณหภูมิเกิน 32 องศาเซลเซียส วิธีการแจ้งเตือนใดที่เหมาะสมในการส่งตรงถึงสมาร์ตโฟนของอาจารย์หรือผู้ดูแลห้อง?",
        "choices": [
            "ส่งข้อความแจ้งเตือนผ่าน LINE Notify API หรือ Telegram Bot ผ่านคำสั่ง HTTP Request ใน Node-RED",
            "ส่งสัญญาณควันไฟ",
            "ฉายแสงเลเซอร์ขึ้นไปบนท้องฟ้า",
            "เขียนจดหมายส่งทางไปรษณีย์"
        ],
        "correctAnswer": 0,
        "explanation": "LINE Notify หรือ Telegram Bot เป็นช่องทางแจ้งเตือนยอดนิยมในไทย โดย Node-RED สามารถยิง HTTP POST Request พร้อมแนบ Access Token และข้อความแจ้งเตือน เช่น '🚨 แจ้งเตือน: ห้อง 301 อุณหภูมิสูง 33.2°C กรุณาตรวจสอบ' ไปยังกลุ่มไลน์ของผู้ดูแลได้ทันทีแบบ Real-time"
    },
    {
        "id": 78,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "เมื่อต้องติดตั้งบอร์ด ESP32 วัดอุณหภูมิในห้องเรียนจริง ตำแหน่งการติดตั้งใดที่เหมาะสมและสะท้อนสภาพแวดล้อมที่แท้จริงได้ดีที่สุด?",
        "choices": [
            "ติดตั้งบริเวณระดับความสูงประมาณ 1.2 - 1.5 เมตรจากพื้น หลีกเลี่ยงแสงแดดส่องตรง และไม่อยู่ตรงช่องลมเป่าของแอร์โดยตรง",
            "วางไว้บนหลังคานอกอาคารที่มีแดดจัด",
            "วางไว้ชิดกับช่องลมร้อนด้านหลังตู้เย็น",
            "ซ่อนไว้ในกล่องโลหะปิดสนิทที่สัญญาณ Wi-Fi เข้าไม่ถึง"
        ],
        "correctAnswer": 0,
        "explanation": "ตำแหน่งติดตั้งเซ็นเซอร์ (Sensor Placement) ต้องสะท้อนอุณหภูมิของบริเวณที่มนุษย์ใช้งานจริง (Breathing Zone ระดับ 1.2-1.5 เมตร) ไม่อยู่ในจุดอับลม ไม่โดนแดดส่องโดยตรง และไม่อยู่ตรงทางลมแอร์เป่า เพื่อป้องกันค่าที่คลาดเคลื่อนจากความเป็นจริง"
    },
    {
        "id": 79,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "การใช้โปรโตคอล MQTT ในระบบ IoT เหมาะสมกว่าการใช้ HTTP สำหรับอุปกรณ์ไมโครคอนโทรลเลอร์ขนาดเล็ก (เช่น ESP32) เพราะเหตุใดเป็นสำคัญ?",
        "choices": [
            "MQTT มี Packet Header ขนาดเล็กมาก (เริ่มต้นเพียง 2 ไบต์), สื่อสารแบบ Lightweight, และรักษาการเชื่อมต่อแบบ Persistent TCP ทำให้ประหยัดพลังงานและแบนด์วิดท์อย่างยิ่ง",
            "เพราะ HTTP ไม่สามารถส่งข้อความตัวเลขได้",
            "เพราะ MQTT สามารถส่งกระแสไฟฟ้าผ่านอากาศได้",
            "เพราะ HTTP ถูกยกเลิกการใช้งานไปแล้วทั่วโลก"
        ],
        "correctAnswer": 0,
        "explanation": "HTTP มี Overhead สูงมาก (Headers ขนาดใหญ่เป็นร้อยๆ ไบต์ และต้องเปิด-ปิด TCP Connection ซ้ำๆ ในแบบ Request/Response) ขณะที่ MQTT ออกแบบมาเฉพาะสำหรับอุปกรณ์ IoT ที่มีทรัพยากรจำกัด โดยมี Header เริ่มต้นเพียง 2 Bytes และใช้โครงสร้าง Publish/Subscribe ที่เบาและรวดเร็วกว่าหลายเท่า"
    },
    {
        "id": 80,
        "section": "การติดตั้ง Edge Server Raspberry Pi & การออกแบบระบบภาพรวม",
        "question": "เมื่อออกแบบระบบ IoT ตรวจวัดและควบคุมอุณหภูมิในห้องเรียนจนเสร็จสมบูรณ์ ขั้นตอนสุดท้ายที่จำเป็นในการส่งมอบงานหรือนำไปใช้งานจริงคือข้อใด?",
        "choices": [
            "ทำการทดสอบระบบตั้งแต่ต้นจนจบ (End-to-End Testing), ตรวจสอบความถูกต้องของการแสดงผลบน Dashboard, จัดทำเอกสารคู่มือการใช้งาน และสำรองไฟล์คอนฟิกูเรชันของระบบ",
            "ลบโค้ดทั้งหมดออกจากบอร์ด ESP32 เพื่อป้องกันความลับรั่วไหล",
            "ปิดเครื่องแม่ข่าย Raspberry Pi และห้ามเปิดใช้งานอีก",
            "ทาสีทับเซ็นเซอร์เพื่อความสวยงาม"
        ],
        "correctAnswer": 0,
        "explanation": "ขั้นตอนปิดท้ายของการพัฒนาระบบ IoT คือการทำ End-to-End Testing ทดสอบตั้งแต่การอ่านค่าจากเซ็นเซอร์, การส่งผ่าน MQTT, การเก็บลงฐานข้อมูล, การตอบสนองของ Relay, การแจ้งเตือน, พร้อมทั้งจัดทำคู่มือและ Backup ระบบ เพื่อให้ผู้ใช้งานสามารถดูแลและบำรุงรักษาต่อได้อย่างยั่งยืน"
    }
]

print(f"Total IoT Questions: {len(iot_questions)}")
