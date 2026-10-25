# -*- coding: utf-8 -*-
import json
import random

# Load or define Tourism IT questions from generate_quiz.py
from generate_quiz import questions as tourism_questions

mobile_questions = [
    # ==========================================
    # หมวดที่ 1: สถาปัตยกรรมการทำงานของ Flutter และ Build System (15 ข้อ: ข้อ 1 - 15)
    # ==========================================
    {
        "id": 1,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "สถาปัตยกรรมของ Flutter Framework แตกต่างจาก Cross-platform Framework แบบดั้งเดิม (เช่น React Native) อย่างไรในด้านการ Render หน้าจอ?",
        "choices": [
            "Flutter วาด UI ทั้งหมดลงบน Canvas ด้วยเอนจินกราฟิกของตนเอง (Impeller / Skia) โดยไม่ต้องพึ่งพา Native OEM Widgets หรือ JavaScript Bridge",
            "Flutter แปลงโค้ด Dart เป็นภาษา HTML5 และ CSS3 แล้วรันบน WebView ของระบบปฏิบัติการ",
            "Flutter ใช้ JavaScript Bridge แปลงคำสั่งไปเรียกใช้ Native UI ของ Android และ iOS ตลอดเวลา",
            "Flutter ต้องแปลงโค้ดเป็นภาษา Java สำหรับ Android และ Objective-C สำหรับ iOS ก่อนทำงานเสมอ"
        ],
        "correctAnswer": 0,
        "explanation": "Flutter โดดเด่นด้วยการใช้ Engine กราฟิกประสิทธิภาพสูง (Impeller หรือ Skia เขียนด้วย C++) วาดทุกพิกเซลลงบนผืนผ้าใบ (Canvas) โดยตรง ทำให้การแสดงผลคงที่ ลื่นไหล 60-120 FPS และไม่ต้องเสีย overhead ให้กับ JavaScript Bridge"
    },
    {
        "id": 2,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "ในการทำงานเบื้องหลังของ Flutter เมื่อโครงสร้าง UI มีการเปลี่ยนแปลง ระบบจะจัดการต้นไม้ข้อมูล 3 ชั้น (Three Trees) ตามลำดับใด?",
        "choices": [
            "Widget Tree (การกำหนดค่า) -> Element Tree (การเชื่อมโยงสถานะ) -> RenderObject Tree (การวาดภาพและจัด Layout)",
            "RenderObject Tree -> Element Tree -> Widget Tree",
            "Element Tree -> Widget Tree -> RenderObject Tree",
            "Widget Tree -> RenderObject Tree -> Element Tree"
        ],
        "correctAnswer": 0,
        "explanation": "Flutter แบ่งต้นไม้ข้อมูลเป็น 3 ชั้น: 1. Widget Tree (พิมพ์เขียว/Configuration ที่ถูกสร้างและทำลายได้ง่าย) 2. Element Tree (ตัวจัดการวงจรชีวิตและจับคู่ Widget กับ RenderObject) 3. RenderObject Tree (จัดการ Layout และคำนวณการวาดภาพจริงบนจอ)"
    },
    {
        "id": 3,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "ฟีเจอร์ 'Hot Reload' ใน Flutter ทำงานอย่างไร และมีข้อดีอย่างไรต่อนักพัฒนา?",
        "choices": [
            "ทำการ Inject โค้ดที่แก้ไขเข้าไปใน Dart Virtual Machine (DVM) ทันที โดยยังคงรักษาตัวแปรและสถานะ (State) เดิมของแอปไว้",
            "ทำการ Restart แอปพลิเคชันใหม่ทั้งหมด และล้างข้อมูล State ในหน่วยความจำทิ้ง",
            "ทำการ Build ไฟล์ APK ใหม่และติดตั้งลงในเครื่องจริงทุกครั้งที่กด Save",
            "ทำการคอมไพล์โค้ดเป็น WebAssembly แล้วรันผ่านเบราว์เซอร์"
        ],
        "correctAnswer": 0,
        "explanation": "Hot Reload อาศัยฟีเจอร์ JIT (Just-In-Time) ของ Dart VM ในการโหลดเฉพาะโค้ดที่มีการเปลี่ยนแปลงเข้าไปในระบบ โดยยังคงรักษา Application State ปัจจุบันไว้ ทำให้นักพัฒนาเห็นผลลัพธ์บนหน้าจอได้ในเวลาไม่ถึง 1 วินาที"
    },
    {
        "id": 4,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "สถานการณ์ใดที่การกด 'Hot Reload' จะไม่เกิดผลลัพธ์ และจำเป็นต้องใช้ 'Hot Restart' หรือ Full Restart?",
        "choices": [
            "เมื่อมีการแก้ไขฟังก์ชัน main() หรือเปลี่ยนโครงสร้างใน initState() หรือเปลี่ยนชนิดตัวแปร Global",
            "เมื่อแก้ไขสีพื้นหลังของ Container หรือ Text",
            "เมื่อแก้ไขค่า Padding หรือ Margin ของ Widget",
            "เมื่อเปลี่ยนข้อความใน Text Widget จากภาษาไทยเป็นภาษาอังกฤษ"
        ],
        "correctAnswer": 0,
        "explanation": "Hot Reload จะเรียกเฉพาะฟังก์ชัน build() ใหม่เท่านั้น หากมีการแก้ไขฟังก์ชัน main(), การเปลี่ยนแปลงใน initState() (ซึ่งทำงานครั้งเดียวตอนสร้าง State), หรือการเปลี่ยนแปลงชนิดตัวแปร static/global จะต้องใช้ Hot Restart เพื่อให้ State ถูกรีเซ็ตและสร้างใหม่"
    },
    {
        "id": 5,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "ไฟล์ใดในโปรเจกต์ Flutter ที่ทำหน้าที่เป็นศูนย์กลางในการกำหนดค่า Dependency (แพ็กเกจภายนอก), กำหนด Asset รูปภาพ, ฟอนต์ และเวอร์ชันของแอปพลิเคชัน?",
        "code": "name: my_app\ndescription: A new Flutter project.\nversion: 1.0.0+1\n\ndependencies:\n  flutter:\n    sdk: flutter\n  http: ^1.2.0",
        "choices": [
            "pubspec.yaml",
            "package.json",
            "AndroidManifest.xml",
            "build.gradle"
        ],
        "correctAnswer": 0,
        "explanation": "pubspec.yaml คือไฟล์ Configuration หลักของโปรเจกต์ Flutter/Dart ใช้กำหนด Metadata, รายชื่อ External Packages (Dependencies), ไฟล์ Assets (รูปภาพ, ไอคอน), และฟอนต์ โดยต้องระมัดระวังการเว้นวรรค (Indentation) แบบ YAML"
    },
    {
        "id": 6,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "หลังจากเพิ่มชื่อไลบรารี เช่น 'http: ^1.2.0' ลงใน pubspec.yaml แล้ว จะต้องใช้คำสั่งใดผ่าน Command Line เพื่อดาวน์โหลดแพ็กเกจมาติดตั้งในโปรเจกต์?",
        "choices": [
            "flutter pub get",
            "npm install flutter-http",
            "dart package download",
            "flutter build packages"
        ],
        "correctAnswer": 0,
        "explanation": "คำสั่ง 'flutter pub get' ทำหน้าที่อ่านไฟล์ pubspec.yaml แล้วดาวน์โหลด External Libraries ที่ระบุจากแหล่งรวมแพ็กเกจทางการ (pub.dev) พร้อมทั้งสร้างและอัปเดตไฟล์ pubspec.lock เพื่อล็อกเวอร์ชันของแพ็กเกจ"
    },
    {
        "id": 7,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "คลังจัดเก็บและแบ่งปันแพ็กเกจ/ไลบรารีแบบโอเพนซอร์สของชุมชนนักพัฒนา Dart & Flutter อย่างเป็นทางการคือเว็บไซต์ใด?",
        "choices": [
            "pub.dev",
            "npmjs.com",
            "pypi.org",
            "maven.org"
        ],
        "correctAnswer": 0,
        "explanation": "pub.dev คือ Official Package Repository สำหรับภาษา Dart และ Flutter ที่เปิดให้นักพัฒนาทั่วโลกค้นหา ดาวน์โหลด และเผยแพร่ Package/Plugin ต่างๆ"
    },
    {
        "id": 8,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "คำว่า 'APK' ในบริบทของการพัฒนาแอปพลิเคชันบนระบบปฏิบัติการ Android ย่อมาจากอะไร?",
        "choices": [
            "Android Package (หรือ Android Package Kit)",
            "Apple Programming Kit",
            "Application Process Kernel",
            "Advanced Programming Knowledge"
        ],
        "correctAnswer": 0,
        "explanation": "APK ย่อมาจาก Android Package (หรือ Android Package Kit) เป็นรูปแบบไฟล์แพ็กเกจมาตรฐานที่ระบบปฏิบัติการ Android ใช้สำหรับการแจกจ่ายและติดตั้งแอปพลิเคชัน"
    },
    {
        "id": 9,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "เมื่อต้องการสร้างไฟล์ APK ที่พร้อมสำหรับการนำไปใช้งานจริง (Production) โดยมีการบีบอัดขนาดไฟล์ และตัดโค้ดส่วน Debug ออก ควรใช้คำสั่งใด?",
        "choices": [
            "flutter build apk --release",
            "flutter run --debug-apk",
            "flutter create apk --production",
            "flutter test --export-apk"
        ],
        "correctAnswer": 0,
        "explanation": "คำสั่ง 'flutter build apk --release' (หรือการระบุ split-per-abi) จะคอมไพล์โค้ดแบบ AOT (Ahead-Of-Time) ปรับปรุงประสิทธิภาพ (Minification, Tree-shaking) เพื่อตัดโค้ดที่ไม่ได้ใช้ออก ทำให้ไฟล์มีขนาดเล็กและทำงานได้รวดเร็วสูงสุด"
    },
    {
        "id": 10,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "ความแตกต่างสำคัญระหว่างการคอมไพล์แบบ JIT (Just-In-Time) ในโหมด Debug และ AOT (Ahead-Of-Time) ในโหมด Release ของ Flutter คือข้อใด?",
        "choices": [
            "JIT คอมไพล์โค้ดขณะแอปกำลังรันเพื่อรองรับ Hot Reload ส่วน AOT คอมไพล์โค้ด Dart เป็น Machine Code ของอุปกรณ์ล่วงหน้าเพื่อประสิทธิภาพสูงสุด",
            "JIT ใช้เฉพาะบน iOS ส่วน AOT ใช้เฉพาะบน Android",
            "JIT ทำให้แอปทำงานเร็วกว่า AOT ในการใช้งานจริง",
            "JIT ใช้สำหรับการ Build APK เพื่อขึ้น Google Play Store"
        ],
        "correctAnswer": 0,
        "explanation": "Dart มีความยืดหยุ่นสูง: ใน Development Mode จะใช้ JIT คอมไพล์ทีละคำสั่งเพื่อให้นักพัฒนาใช้ Hot Reload ได้อย่างรวดเร็ว ส่วนใน Release Mode จะใช้ AOT คอมไพล์โค้ดเป็น Native Machine Code (ARM/x86) ล่วงหน้าเพื่อความเร็วและลื่นไหลสูงสุด"
    },
    {
        "id": 11,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "ข้อใดอธิบายแนวคิด 'Everything is a Widget' ใน Flutter ได้ถูกต้องที่สุด?",
        "choices": [
            "ทุกองค์ประกอบบนหน้าจอ ตั้งแต่ปุ่ม ข้อความ การจัดระยะห่าง (Padding) ไปจนถึงโครงสร้างหน้า (Scaffold) ล้วนถูกสร้างขึ้นในรูปแบบของ Widget ทั้งสิ้น",
            "Widget หมายถึงเฉพาะปุ่มกดที่สามารถคลิกได้เท่านั้น",
            "Widget คือชื่อฐานข้อมูลที่ใช้เก็บข้อมูลภายในแอปพลิเคชัน",
            "Widget ใช้สำหรับจัดการเครือข่ายอินเทอร์เน็ตเท่านั้น"
        ],
        "correctAnswer": 0,
        "explanation": "ปรัชญาการออกแบบของ Flutter คือ 'Everything is a Widget' ไม่เพียงแค่องค์ประกอบเชิงภาพ (Structural) เช่น Text, Image, Button แต่รวมถึงองค์ประกอบเชิงผังงาน (Layout) เช่น Row, Column, Padding, Center ก็ล้วนเป็น Widget ที่นำมาประกอบกัน (Composition)"
    },
    {
        "id": 12,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "ในการสร้างไฟล์ APK ขนาดเล็กแยกตามสถาปัตยกรรม CPU ของสมาร์ตโฟน (เช่น armeabi-v7a, arm64-v8a) ควรเพิ่ม Flag ใดในคำสั่ง build?",
        "choices": [
            "flutter build apk --split-per-abi",
            "flutter build apk --mini-size",
            "flutter build apk --cpu-all",
            "flutter build apk --clean-architecture"
        ],
        "correctAnswer": 0,
        "explanation": "การใช้ 'flutter build apk --split-per-abi' จะแยกสร้างไฟล์ APK สำหรับสถาปัตยกรรม CPU แต่ละประเภท แทนที่จะรวม Native Libraries ของทุกสถาปัตยกรรมไว้ในไฟล์เดียว ทำให้ขนาดไฟล์ APK สำหรับผู้ใช้แต่ละเครื่องลดลงอย่างมาก"
    },
    {
        "id": 13,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "เอนจินการเรนเดอร์กราฟิกรุ่นใหม่ที่ทีม Flutter พัฒนาขึ้นมาแทนที่ Skia บนระบบปฏิบัติการ iOS และ Android เพื่อแก้ปัญหา Shader Compilation Jank (อาการกระตุกตอนแสดงผลครั้งแรก) มีชื่อว่าอะไร?",
        "choices": [
            "Impeller",
            "V8",
            "WebKit",
            "Blink"
        ],
        "correctAnswer": 0,
        "explanation": "Impeller คือ Rendering Engine รุ่นใหม่ของ Flutter ที่ออกแบบมาเพื่อคอมไพล์ Shaders ล่วงหน้า (Pre-compilation) ทั้งหมด ขจัดปัญหา UI กระตุกตอนโหลดแอนิเมชันครั้งแรก (Shader Jank) ได้อย่างสมบูรณ์"
    },
    {
        "id": 14,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "ในไฟล์ pubspec.yaml หากต้องการระบุเวอร์ชันของแพ็กเกจด้วยสัญลักษณ์แคร์เร็ต เช่น '^2.1.0' มีความหมายอย่างไรตามหลัก Semantic Versioning?",
        "choices": [
            "ยินยอมให้อัปเดตเวอร์ชันใหม่ได้ตราบใดที่ไม่ใช่ Major Release (คือตั้งแต่ 2.1.0 ถึงก่อน 3.0.0)",
            "ยอมรับเฉพาะเวอร์ชัน 2.1.0 เท่านั้น ห้ามอัปเดตเด็ดขาด",
            "อนุญาตให้อัปเดตเป็นเวอร์ชัน 3.0.0 ได้โดยอัตโนมัติ",
            "เป็นการบังคับให้ Downgrade เวอร์ชันลงไปที่ 1.0.0"
        ],
        "correctAnswer": 0,
        "explanation": "สัญลักษณ์ ^ (Caret syntax) ใน pubspec.yaml หมายถึงสามารถอัปเดตเป็นเวอร์ชันที่เข้ากันได้ (Compatible version) คือเวอร์ชันที่มีการแก้ไขบั๊กหรือเพิ่มฟีเจอร์ย่อย (Minor/Patch) แต่จะไม่ข้ามไป Major Version ถัดไปที่มี Breaking Changes"
    },
    {
        "id": 15,
        "section": "สถาปัตยกรรมการทำงานของ Flutter และ Build System",
        "question": "เมื่อรันคำสั่ง 'flutter create my_app' โฟลเดอร์ใดที่เป็นจุดเริ่มต้นหลักในการเขียนโค้ดภาษา Dart ของนักพัฒนา?",
        "choices": [
            "lib/",
            "android/",
            "ios/",
            "test/"
        ],
        "correctAnswer": 0,
        "explanation": "โฟลเดอร์ lib/ คือที่อยู่ของซอร์สโค้ดภาษา Dart ทั้งหมดของโปรเจกต์ Flutter โดยมีไฟล์ lib/main.dart เป็น Entry Point หลักที่มีฟังก์ชัน main() สำหรับเริ่มต้นแอป"
    },

    # ==========================================
    # หมวดที่ 2: ภาษา Dart และหลักการ Object-Oriented Programming (15 ข้อ: ข้อ 16 - 30)
    # ==========================================
    {
        "id": 16,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "ในระบบ Sound Null Safety ของภาษา Dart คีย์เวิร์ด 'late' มีหน้าที่และความสำคัญอย่างไร?",
        "code": "class ProfileScreen extends StatefulWidget {\n  // ...\n}\nclass _ProfileScreenState extends State<ProfileScreen> {\n  late String username;\n  \n  @override\n  void initState() {\n    super.initState();\n    username = 'Somchai';\n  }\n}",
        "choices": [
            "เป็นการบอกคอมไพเลอร์ว่าตัวแปรประเภท Non-nullable นี้จะยังไม่มีค่าเริ่มต้นทันทีตอนประกาศ แต่สัญญาว่าจะถูกกำหนดค่าอย่างแน่นอนก่อนถูกนำไปใช้งาน",
            "ใช้กำหนดให้ตัวแปรนั้นสามารถเก็บค่า null ได้ตลอดอายุการใช้งาน",
            "ใช้สำหรับหน่วงเวลาให้ฟังก์ชันทำงานช้าลง 3 วินาที",
            "ใช้สำหรับประกาศตัวแปรค่าคงที่ที่ไม่มีวันเปลี่ยนแปลง"
        ],
        "correctAnswer": 0,
        "explanation": "คีย์เวิร์ด 'late' ใช้เมื่อเราต้องการประกาศตัวแปรที่เป็น Non-nullable (ห้ามเป็น null) แต่ยังไม่สามารถกำหนดค่าเริ่มต้นในทันทีที่ประกาศได้ (เช่น ต้องรอกำหนดค่าใน initState) หากพยายามเรียกใช้ตัวแปรก่อนกำหนดค่า ระบบจะโยน LateInitializationError"
    },
    {
        "id": 17,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "การใส่คีย์เวิร์ด 'const' หน้า Constructor ของ Widget ใน Flutter เช่น 'const Text(\"Hello\")' มีผลดีอย่างไรต่อประสิทธิภาพของแอปพลิเคชัน?",
        "choices": [
            "สร้างอินสแตนซ์เป็น Compile-time Constant (Canonicalized) ในหน่วยความจำ ทำให้ Flutter ไม่ต้อง Rebuild Widget ตัวนี้ใหม่เมื่อ Parent Widget ทำการ Rebuild",
            "ทำให้ข้อความนั้นสามารถแก้ไขค่าได้แบบ Real-time",
            "ทำให้ Widget นั้นกลายสภาพเป็น StatefulWidget",
            "ช่วยให้แอปพลิเคชันสามารถเชื่อมต่ออินเทอร์เน็ตได้เร็วขึ้น"
        ],
        "correctAnswer": 0,
        "explanation": "การใช้ 'const' Constructor จะสร้างออบเจกต์ในหน่วยความจำตั้งแต่ขั้นตอน Compile-time และนำมาใช้ซ้ำ (Canonicalization) เมื่อ Parent Widget ทำการ Rebuild วิดเจ็ตที่เป็น const จะไม่ถูกสร้างใหม่ ช่วยลดภาระการจัดสรรหน่วยความจำและเพิ่มความลื่นไหล"
    },
    {
        "id": 18,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "ความแตกต่างสำคัญระหว่างคีย์เวิร์ด 'final' และ 'const' ในภาษา Dart คือข้อใด?",
        "choices": [
            "const ต้องทราบค่าที่แน่นอนตั้งแต่ตอนคอมไพล์ (Compile-time Constant) ส่วน final กำหนดค่าได้ครั้งเดียวตอนรันไทม์ (Runtime Constant)",
            "final เปลี่ยนแปลงค่าได้ตลอดเวลา ส่วน const เปลี่ยนแปลงค่าไม่ได้",
            "const ใช้ได้เฉพาะกับตัวเลข ส่วน final ใช้ได้เฉพาะกับข้อความ",
            "final ใช้เฉพาะในภาษา Dart 1.0 ส่วน const ใช้ในภาษา Dart 3.0"
        ],
        "correctAnswer": 0,
        "explanation": "ทั้ง final และ const กำหนดค่าได้เพียงครั้งเดียว (Immutable) แต่ 'const' เป็น Compile-time constant ต้องรู้ค่าล่วงหน้าก่อนรัน (เช่น const pi = 3.14) ส่วน 'final' เป็น Runtime constant สามารถรับค่าจากการคำนวณหรือฟังก์ชันตอนรันได้ (เช่น final now = DateTime.now())"
    },
    {
        "id": 19,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "การสืบทอดคุณสมบัติในภาษา Dart หากต้องการให้คลาสลูกสืบทอดความสามารถและโครงสร้างจากคลาสแม่เพียงคลาสเดียว (Single Inheritance) ต้องใช้คีย์เวิร์ดใด?",
        "code": "class Car extends Vehicle {\n  int numberOfDoors = 4;\n}",
        "choices": [
            "extends",
            "implements",
            "with",
            "abstract"
        ],
        "correctAnswer": 0,
        "explanation": "Dart ใช้คีย์เวิร์ด 'extends' ในการสืบทอดคลาส (Inheritance) ทำให้คลาสลูกได้รับคุณสมบัติ (Properties) และเมธอด (Methods) ทั้งหมดของคลาสแม่"
    },
    {
        "id": 20,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "หากต้องการนำฟังก์ชันการทำงานจากหลายๆ คลาสมาใช้งานร่วมกันโดยไม่ต้องสร้างความสัมพันธ์ทางสายเลือดแบบลำดับขั้น (Multiple Mixins) ใน Dart ต้องใช้คีย์เวิร์ดใด?",
        "code": "class Dog extends Animal with Swimmer, Runner {\n  // ...\n}",
        "choices": [
            "with",
            "implements",
            "super",
            "interface"
        ],
        "correctAnswer": 0,
        "explanation": "Dart ไม่รองรับ Multiple Class Inheritance ทางตรง แต่ใช้แนวคิด 'Mixin' ผ่านคีย์เวิร์ด 'with' เพื่อนำโค้ดและพฤติกรรมจากหลายแหล่งมาผนวกเข้าด้วยกันได้อย่างยืดหยุ่น เช่น การใส่ SingleTickerProviderStateMixin เพื่อทำ Animation"
    },
    {
        "id": 21,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "ไลบรารี 'dart:convert' ในภาษา Dart มีคลาสหรือฟังก์ชันใดที่ใช้แปลงข้อความสตริงรูปแบบ JSON ให้กลายเป็น Map หรือ List ของภาษา Dart?",
        "code": "import 'dart:convert';\n\nString jsonString = '{\"name\": \"Somchai\", \"age\": 22}';\nMap<String, dynamic> user = jsonDecode(jsonString);",
        "choices": [
            "jsonDecode()",
            "jsonEncode()",
            "json.stringify()",
            "JSON.parse()"
        ],
        "correctAnswer": 0,
        "explanation": "ในไลบรารี dart:convert ฟังก์ชัน 'jsonDecode()' (หรือ json.decode()) ใช้สำหรับ Deserialize ข้อความสตริง JSON ให้กลายเป็นโครงสร้างข้อมูลในภาษา Dart (Map<String, dynamic> หรือ List<dynamic>)"
    },
    {
        "id": 22,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "หากต้องการแปลงข้อมูลชนิด Map ของภาษา Dart ให้กลายเป็นข้อความสตริง JSON (Serialization) เพื่อส่งผ่าน API จะต้องใช้ฟังก์ชันใดใน 'dart:convert'?",
        "code": "Map<String, dynamic> data = {'item': 'Laptop', 'price': 25000};\nString payload = jsonEncode(data);",
        "choices": [
            "jsonEncode()",
            "jsonDecode()",
            "toMap()",
            "toPayload()"
        ],
        "correctAnswer": 0,
        "explanation": "ฟังก์ชัน 'jsonEncode()' (หรือ json.encode()) ทำหน้าที่ Serialize อ็อบเจกต์ใน Dart (เช่น Map หรือ List) ให้กลายเป็นข้อความสตริง JSON เพื่อส่งผ่าน Network หรือบันทึกลงไฟล์"
    },
    {
        "id": 23,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "โค้ดภาษา Dart ต่อไปนี้ ผลลัพธ์จากการทำงานคือข้อใด?",
        "code": "void main() {\n  String? nickname;\n  print(nickname ?? 'Guest');\n}",
        "choices": [
            "พิมพ์คำว่า 'Guest'",
            "เกิดข้อผิดพลาด NullPointerException",
            "พิมพ์คำว่า 'null'",
            "พิมพ์คำว่า 'nickname'"
        ],
        "correctAnswer": 0,
        "explanation": "เครื่องหมาย '??' คือ If-null Operator ในภาษา Dart โดยหากนิพจน์ทางซ้ายมีค่าเป็น null ระบบจะเลือกใช้ค่าทางขวาแทน ในที่นี้ nickname เป็น null จึงแสดงผลลัพธ์เป็น 'Guest'"
    },
    {
        "id": 24,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "สัญลักษณ์ '?' ที่ต่อท้ายชนิดข้อมูล เช่น 'int? score;' ในภาษา Dart หมายถึงอะไร?",
        "choices": [
            "ตัวแปร score เป็นตัวแปรประเภท Nullable ซึ่งสามารถเก็บค่าตัวเลขจำนวนเต็ม หรือเก็บค่า null ก็ได้",
            "เป็นการตรวจสอบว่า score มีค่ามากกว่า 0 หรือไม่",
            "หมายถึงตัวแปร score เป็นตัวแปรประเภทสุ่มตัวเลข",
            "เป็นไวยากรณ์ที่ผิดพลาด คอมไพเลอร์จะแจ้ง Error"
        ],
        "correctAnswer": 0,
        "explanation": "ใน Dart Sound Null Safety ตัวแปรทุกตัวเริ่มต้นจะเป็น Non-nullable (ห้ามเป็น null) หากต้องการอนุญาตให้ตัวแปรนั้นสามารถถือครองค่า null ได้ จะต้องเติมเครื่องหมาย '?' ต่อท้ายชนิดข้อมูล เช่น String?, int?, Widget?"
    },
    {
        "id": 25,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "การใช้งานเครื่องหมาย '!' (Null Assertion Operator) เช่น 'String name = input!;' มีความหมายและข้อควรระวังอย่างไร?",
        "choices": [
            "เป็นการยืนยันกับคอมไพเลอร์อย่างเด็ดขาดว่าค่าไม่เป็น null แน่นอน แต่หากค่าเป็น null จริงจะเกิดรันไทม์แคช (TypeError / Exception)",
            "เป็นการสั่งให้ลบค่าในตัวแปรทิ้ง",
            "เป็นการตรวจสอบว่าค่าเป็นสตริงว่างหรือไม่",
            "ช่วยป้องกันไม่ให้เกิด Error ทุกกรณีโดยอัตโนมัติ"
        ],
        "correctAnswer": 0,
        "explanation": "เครื่องหมาย '!' (Bang Operator / Null Assertion) เป็นการบังคับ Cast ค่า Nullable เป็น Non-nullable ซึ่งควรใช้ด้วยความระมัดระวังสูงสุด เพราะหากรันไทม์แล้วค่านั้นเป็น null จริง แอปพลิเคชันจะแครชทันที"
    },
    {
        "id": 26,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "การประกาศ Named Constructor ในภาษา Dart มีรูปแบบที่ถูกต้องตามข้อใด?",
        "code": "class Point {\n  final double x, y;\n  Point(this.x, this.y);\n  Point.origin() : x = 0, y = 0; // บรรทัดนี้เรียกว่าอะไร?\n}",
        "choices": [
            "Named Constructor เพื่อเพิ่มทางเลือกในการสร้างอ็อบเจกต์ด้วยชื่อที่สื่อความหมาย",
            "Factory Pattern เท่านั้น",
            "Method Overloading แบบภาษา Java",
            "การประกาศตัวแปร Pointer"
        ],
        "correctAnswer": 0,
        "explanation": "Dart ไม่รองรับ Method Overloading แต่มีฟีเจอร์ 'Named Constructor' (เช่น ClassName.identifier()) ช่วยให้นักพัฒนาสร้าง Constructor หลายตัวที่มีชื่อระบุจุดประสงค์การทำงานได้อย่างชัดเจน"
    },
    {
        "id": 27,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "ฟังก์ชันประเภท 'Arrow Syntax' (=>) ในภาษา Dart เหมาะสำหรับใช้งานในกรณีใด?",
        "code": "int add(int a, int b) => a + b;",
        "choices": [
            "ฟังก์ชันที่มีคำสั่งส่งค่ากลับเพียงบรรทัดเดียว (One-line expression)",
            "ฟังก์ชันที่มีลูปการทำงานซับซ้อนหลายขั้นตอน",
            "ฟังก์ชันประเภท Asynchronous ที่ต้องรอรับข้อมูล",
            "ฟังก์ชันที่ไม่ต้องการให้ส่งค่าใดๆ กลับมา"
        ],
        "correctAnswer": 0,
        "explanation": "สัญลักษณ์ '=>' (Fat Arrow Syntax) ใน Dart เป็นไวยากรณ์ย่อ (Shorthand) สำหรับฟังก์ชันที่มี Expression เพียงนิพจน์เดียว โดยมีค่าเทียบเท่ากับการเขียน { return expression; }"
    },
    {
        "id": 28,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "คีย์เวิร์ด 'super' ในภาษา Dart มีวัตถุประสงค์หลักเพื่อสิ่งใด?",
        "choices": [
            "ใช้อ้างอิงหรือเรียกใช้ Constructor, เมธอด หรือคุณสมบัติของคลาสแม่ (Superclass)",
            "ใช้เพิ่มสิทธิ์ผู้ดูแลระบบ (Admin) ในการรันโค้ด",
            "ใช้ประกาศตัวแปรที่มีประสิทธิภาพสูงกว่าปกติ",
            "ใช้ยกเลิกการสืบทอดคุณสมบัติของคลาส"
        ],
        "correctAnswer": 0,
        "explanation": "คีย์เวิร์ด 'super' ใช้สำหรับอ้างอิงถึงคลาสแม่ เช่น การเรียก 'super.initState()' ใน State class หรือการส่งค่าพารามิเตอร์ขึ้นไปยังคลาสแม่ผ่าน 'super(key: key)' ใน Constructor"
    },
    {
        "id": 29,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "การทำ 'Cascade Notation' (..) ในภาษา Dart ให้ประโยชน์อย่างไร?",
        "code": "var paint = Paint()\n  ..color = Colors.blue\n  ..strokeWidth = 5.0\n  ..style = PaintingStyle.stroke;",
        "choices": [
            "ช่วยให้สามารถเรียกใช้เมธอดหรือกำหนดค่า Property ต่อเนื่องหลายๆ รายการบนอ็อบเจกต์เดียวกันได้โดยไม่ต้องพิมพ์ชื่อตัวแปรซ้ำ",
            "ใช้สำหรับลบอ็อบเจกต์ออกจากหน่วยความจำ",
            "ใช้เชื่อมต่ออินเทอร์เน็ตแบบ 2 ทิศทาง",
            "ใช้สำหรับการแปลงชนิดข้อมูลแบบบังคับ (Type Casting)"
        ],
        "correctAnswer": 0,
        "explanation": "Cascade Operator (..) อนุญาตให้นักพัฒนาทำการดำเนินการต่อเนื่องหลายรายการบนสมาชิกของอ็อบเจกต์เดียวกัน ทำให้โค้ดกระชับ สะอาด และอ่านเข้าใจง่ายขึ้น"
    },
    {
        "id": 30,
        "section": "ภาษา Dart และหลักการ Object-Oriented Programming",
        "question": "ในภาษา Dart คลาสทุกคลาสจะสืบทอดคุณสมบัติมาจากคลาสรากฐาน (Root Class) สูงสุดตัวใดโดยอัตโนมัติ?",
        "choices": [
            "Object",
            "Widget",
            "Base",
            "Class"
        ],
        "correctAnswer": 0,
        "explanation": "ในระบบ Type Hierarchy ของภาษา Dart ทุกคลาสที่ไม่เป็น Nullable จะสืบทอดคุณสมบัติพื้นฐานมาจากคลาส 'Object' ซึ่งบรรจุเมธอดพื้นฐานเช่น toString(), hashCode, และ noSuchMethod()"
    },

    # ==========================================
    # หมวดที่ 3: Widgets พื้นฐานและการจัดวาง Layout (20 ข้อ: ข้อ 31 - 50)
    # ==========================================
    {
        "id": 31,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "ความแตกต่างสำคัญที่สุดระหว่าง 'StatelessWidget' และ 'StatefulWidget' คือข้อใด?",
        "choices": [
            "StatelessWidget เป็นวิดเจ็ตที่สถานะและข้อมูลภายในคงที่ ไม่สามารถเปลี่ยนแปลงค่าได้หลังสร้างขึ้น ส่วน StatefulWidget สามารถเปลี่ยนแปลงข้อมูลภายในและสั่ง Rebuild UI ใหม่ได้ผ่าน setState()",
            "StatelessWidget ใช้สำหรับหน้าจอที่มีปุ่มกด ส่วน StatefulWidget ใช้สำหรับหน้าจอแสดงข้อความตัวอักษรอย่างเดียว",
            "StatelessWidget ใช้แสดงผลบน Android ส่วน StatefulWidget ใช้แสดงผลบน iOS",
            "StatelessWidget ประมวลผลช้ากว่า StatefulWidget เสมอ"
        ],
        "correctAnswer": 0,
        "explanation": "StatelessWidget คือ Immutable Widget (ไม่มี State ภายในที่เปลี่ยนแปลงได้ตามเวลา) เหมาะสำหรับ UI นิ่งๆ เช่น ป้ายข้อความ ไอคอน ส่วน StatefulWidget จะสร้าง State Object แยกออกมาเพื่อเก็บสถานะที่สามารถอัปเดตและสั่งวาดใหม่ได้ผ่าน setState()"
    },
    {
        "id": 32,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "ในการจัดวาง Layout ด้วยวิดเจ็ต 'Row' แกนหลัก (Main Axis) และแกนตัดขวาง (Cross Axis) คือทิศทางใด?",
        "choices": [
            "แกนหลัก (Main Axis) คือแนวนอน (แนวนอนซ้ายไปขวา) และแกนตัดขวาง (Cross Axis) คือแนวตั้ง (บนลงล่าง)",
            "แกนหลักคือแนวตั้ง และแกนตัดขวางคือแนวนอน",
            "ทั้งสองแกนเป็นแนวตั้งทั้งคู่",
            "ทั้งสองแกนเป็นแนวนอนทั้งคู่"
        ],
        "correctAnswer": 0,
        "explanation": "สำหรับ 'Row' องค์ประกอบจะเรียงตัวในแนวนอน ดังนั้น แกนหลัก (Main Axis) คือแนวนอน ส่วนแกนตัดขวาง (Cross Axis) คือแนวตั้ง ในทางกลับกัน สำหรับ 'Column' แกนหลักคือแนวตั้ง และแกนตัดขวางคือแนวนอน"
    },
    {
        "id": 33,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "หากต้องการให้ Children ภายใน 'Row' กระจายตัวออกจากกันโดยมีระยะห่างระหว่างแต่ละชิ้นเท่ากันทั้งหมด และมีช่องว่างเว้นขอบหัวท้ายด้วย ควรตั้งค่า 'mainAxisAlignment' อย่างไร?",
        "choices": [
            "MainAxisAlignment.spaceEvenly",
            "MainAxisAlignment.spaceBetween",
            "MainAxisAlignment.start",
            "MainAxisAlignment.center"
        ],
        "correctAnswer": 0,
        "explanation": "MainAxisAlignment.spaceEvenly จะแบ่งพื้นที่ว่างทั้งหมดให้มีขนาดเท่ากันเป๊ะระหว่างทุกองค์ประกอบและขอบหัวท้าย ส่วน spaceBetween จะเว้นว่างเฉพาะระหว่างไอเทมโดยชิดขอบหัวท้าย และ spaceAround จะแบ่งช่องว่างรอบๆ ไอเทม"
    },
    {
        "id": 34,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "วิดเจ็ต 'Positioned' ต้องใช้งานเป็นบุตร (Child) ภายใต้วิดเจ็ตแม่ตัวใดเสมอ จึงจะสามารถกำหนดพิกัดตำแหน่ง เช่น top, left, right, bottom ได้?",
        "code": "Stack(\n  children: [\n    Container(color: Colors.red),\n    Positioned(\n      top: 20,\n      right: 20,\n      child: Icon(Icons.close),\n    ),\n  ],\n)",
        "choices": [
            "Stack",
            "Row",
            "Column",
            "ListView"
        ],
        "correctAnswer": 0,
        "explanation": "วิดเจ็ต 'Positioned' ถูกออกแบบมาให้ใช้งานอยู่ภายใต้ 'Stack' เท่านั้น เพื่อทำหน้าที่ควบคุมตำแหน่งพิกัดเฉพาะเจาะจง (Absolute Positioning) ของชิ้นส่วนที่ซ้อนทับกันอยู่บนหน้าจอ"
    },
    {
        "id": 35,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "การกำหนดระยะขอบภายในด้วยคำสั่ง 'EdgeInsets.symmetric(vertical: 16.0, horizontal: 24.0)' มีความหมายอย่างไร?",
        "choices": [
            "เว้นระยะขอบ ด้านบนและด้านล่าง 16.0 พิกเซล และเว้นระยะขอบ ด้านซ้ายและด้านขวา 24.0 พิกเซล",
            "เว้นระยะขอบรอบทิศทาง 16.0 พิกเซลเท่ากันทั้งหมด",
            "เว้นระยะขอบเฉพาะด้านบน 16.0 และด้านซ้าย 24.0 เท่านั้น",
            "เว้นระยะขอบด้านนอก (Margin) อย่างเดียวโดยไม่เกี่ยวกับ Padding"
        ],
        "correctAnswer": 0,
        "explanation": "EdgeInsets.symmetric() รับพารามิเตอร์ 2 ตัวคือ 'vertical' (มีผลต่อขอบบนและล่างพร้อมกัน) และ 'horizontal' (มีผลต่อขอบซ้ายและขวาพร้อมกัน)"
    },
    {
        "id": 36,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "ข้อผิดพลาด 'A RenderFlex overflowed by ... pixels' ที่ปรากฏเป็นแถบคาดลายสีเหลืองสลับดำบนหน้าจอ เกิดจากสาเหตุใด?",
        "choices": [
            "ขนาดรวมของ Children ภายใน Row หรือ Column มีความกว้างหรือสูงเกินกว่าพื้นที่ว่างที่มีอยู่จริงบนหน้าจอ",
            "ลืมเชื่อมต่อฐานข้อมูล Firebase",
            "ความเร็วอินเทอร์เน็ตของเครื่องไม่เพียงพอ",
            "การสะกดชื่อตัวแปรผิดในไฟล์ pubspec.yaml"
        ],
        "correctAnswer": 0,
        "explanation": "RenderFlex Overflow เกิดเมื่อขนาดของ Widget ลูก (เช่น ข้อความยาวเกินไป หรือหลาย Widget รวมกัน) มีขนาดมิติเกินกว่าขอบเขตหน้าจอหรือพื้นที่ที่ Parent (Row/Column) จะรองรับได้ ทำให้เนื้อหาล้นทะลุขอบจอ"
    },
    {
        "id": 37,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "แนวทางการแก้ไขข้อผิดพลาด 'A RenderFlex overflowed' ในกรณีที่ข้อความยาวเกินไปใน Row หรือรายการยาวล้น Column ข้อใดถูกต้อง?",
        "choices": [
            "ครอบ Child ด้วย 'Expanded' หรือ 'Flexible' ภายใน Row หรือครอบ Column ด้วย 'SingleChildScrollView'",
            "เปลี่ยนชื่อโปรเจกต์ใหม่",
            "ปิดหน้าจอแล้วเปิดใหม่",
            "ลบโฟลเดอร์ android/ ทิ้งแล้วสร้างใหม่"
        ],
        "correctAnswer": 0,
        "explanation": "หากเกิด Overflow ใน Row มักแก้ด้วยการครอบ Widget ลูกด้วย 'Expanded' หรือ 'Flexible' เพื่อจำกัดขนาดไม่ให้เกินพื้นที่ที่เหลือ หรือหากเนื้อหาใน Column ยาวเกินจอแนวตั้ง ให้ครอบด้วย 'SingleChildScrollView' หรือใช้ 'ListView' เพื่อให้เลื่อนหน้าจอได้"
    },
    {
        "id": 38,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "ในการสร้างตารางกริด 2 มิติด้วยคำสั่ง 'GridView.count' คุณสมบัติ (Property) ใดใช้กำหนดจำนวนคอลัมน์ในแต่ละแถว?",
        "code": "GridView.count(\n  crossAxisCount: 2,\n  children: List.generate(10, (index) => Card()),\n)",
        "choices": [
            "crossAxisCount",
            "mainAxisCount",
            "rowCount",
            "columnLength"
        ],
        "correctAnswer": 0,
        "explanation": "ใน GridView.count คุณสมบัติ 'crossAxisCount' เป็นพารามิเตอร์บังคับ (Required) ใช้กำหนดจำนวนช่องหรือคอลัมน์ในแนวตัดขวาง (แนวนอน) เช่น crossAxisCount: 2 จะแสดงแถวละ 2 ช่อง"
    },
    {
        "id": 39,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "วิดเจ็ต 'Expanded' เมื่อนำไปครอบ Widget ลูกภายใน Row หรือ Column มีพฤติกรรมการทำงานอย่างไร?",
        "choices": [
            "ขยายขนาดของ Widget ลูกตัวนั้นให้ครอบครองพื้นที่ว่างที่เหลืออยู่ทั้งหมดตามแนวแกนหลัก",
            "ทำให้ Widget ลูกตัวนั้นหายไปจากหน้าจอ",
            "บีบขนาดของ Widget ลูกให้มีขนาดเล็กลงครึ่งหนึ่งเสมอ",
            "เปลี่ยนสีพื้นหลังของ Widget ลูกเป็นสีโปร่งใส"
        ],
        "correctAnswer": 0,
        "explanation": "Expanded จะบังคับให้ Child ขยายขนาดเต็มพื้นที่ว่างที่เหลืออยู่ (Available Space) ตามแนวแกนหลัก (Main Axis) โดยสามารถกำหนดสัดส่วนการแบ่งพื้นที่ระหว่างกันได้ด้วยพารามิเตอร์ 'flex'"
    },
    {
        "id": 40,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "วิดเจ็ตพื้นฐานที่เปรียบเสมือนโครงสร้างหลักของหน้าจอใน Material Design ซึ่งมีพื้นที่สำหรับ AppBar, Drawer, Body, และ FloatingActionButton คือวิดเจ็ตใด?",
        "choices": [
            "Scaffold",
            "Container",
            "Card",
            "SizedBox"
        ],
        "correctAnswer": 0,
        "explanation": "Scaffold คือวิดเจ็ตโครงสร้างสถาปัตยกรรมภาพพื้นฐานตามมาตรฐาน Material Design ที่เตรียมช่องทางติดตั้งองค์ประกอบต่างๆ ของหน้าจอ เช่น appBar, body, floatingActionButton, drawer, bottomNavigationBar"
    },
    {
        "id": 41,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "หากต้องการสร้างระยะห่างแบบว่างเปล่าระหว่าง Widget สองชิ้นอย่างง่ายและมีประสิทธิภาพสูงสุด ควรเลือกใช้วิดเจ็ตใด?",
        "code": "Column(\n  children: [\n    Text('Header'),\n    const SizedBox(height: 20),\n    Text('Subheader'),\n  ],\n)",
        "choices": [
            "const SizedBox(height: 20)",
            "Container(color: Colors.white, width: 0, height: 20)",
            "Padding(padding: EdgeInsets.zero)",
            "Opacity(opacity: 0, child: Text(''))"
        ],
        "correctAnswer": 0,
        "explanation": "const SizedBox(width/height) คือแนวทางที่กระชับและมีประสิทธิภาพสูงสุด (High Performance) สำหรับการสร้างช่องว่าง เพราะเป็น lightweight widget ที่ไม่มี overhead ด้านตกแต่ง และสามารถประกาศเป็น const ได้"
    },
    {
        "id": 42,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "วิดเจ็ตใดที่ช่วยตรวจจับท่าทางและเหตุการณ์การสัมผัสของผู้ใช้ (เช่น การแตะ一次, ดับเบิ้ลคลิก, แตะค้าง, ลากนิ้ว) ให้แก่วิดเจ็ตใดๆ ที่ไม่มีระบบสัมผัสในตัว?",
        "choices": [
            "GestureDetector (หรือ InkWell)",
            "TouchListener",
            "ClickController",
            "MotionEvent"
        ],
        "correctAnswer": 0,
        "explanation": "GestureDetector ใช้ครอบวิดเจ็ตใดๆ เพื่อดักจับท่าทางการสัมผัส เช่น onTap, onDoubleTap, onLongPress, onPanUpdate ส่วน 'InkWell' จะทำงานคล้ายกันแต่เพิ่มเอฟเฟกต์ระลอกคลื่นน้ำ (Ripple Effect) ตามสไตล์ Material"
    },
    {
        "id": 43,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "ความแตกต่างสำคัญระหว่าง 'ListView' ธรรมดา และ 'ListView.builder' คือข้อใด?",
        "choices": [
            "ListView.builder ทำงานแบบ Lazy Loading สร้างเฉพาะไอเทมที่กำลังจะปรากฏบนจอ ช่วยประหยัดหน่วยความจำอย่างมากเมื่อแสดงรายการข้อมูลจำนวนมาก",
            "ListView ธรรมดาสามารถเลื่อนหน้าจอได้ แต่ ListView.builder เลื่อนไม่ได้",
            "ListView.builder ใช้สำหรับตารางกริดเท่านั้น",
            "ListView ธรรมดาสร้างไอเทมได้รวดเร็วกว่า ListView.builder เสมอ"
        ],
        "correctAnswer": 0,
        "explanation": "ListView(children: [...]) จะสร้างและจัดสรรหน่วยความจำให้ทุก Widget พร้อมกันตั้งแต่เริ่มต้น จึงเหมาะกับรายการสั้นๆ ส่วน ListView.builder จะสร้างเฉพาะไอเทมที่มองเห็นบนจอ (On-demand / Virtualized) เหมาะสำหรับข้อมูลนับร้อยหรือพันแถว"
    },
    {
        "id": 44,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "วิดเจ็ต 'Stack' มีรูปแบบการจัดวางเรียงซ้อนของ Child Widgets อย่างไร?",
        "choices": [
            "ซ้อนทับกันเป็นเลเยอร์ตามมิติแกน Z (จากชิ้นแรกอยู่ล่างสุด ชิ้นถัดไปทับขึ้นมาเรื่อยๆ)",
            "เรียงต่อกันในแนวนอน",
            "เรียงต่อกันในแนวตั้ง",
            "สลับตำแหน่งแบบสุ่มอัตโนมัติ"
        ],
        "correctAnswer": 0,
        "explanation": "Stack ทำหน้าที่วาง Widget ซ้อนทับกันตามแนวลึก (Z-axis) โดยวิดเจ็ตลูกชิ้นแรกจะอยู่ล่างสุด และวิดเจ็ตลูกตัวถัดไปในลิสต์จะถูกวาดทับด้านบนขึ้นมาตามลำดับ"
    },
    {
        "id": 45,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "คุณสมบัติ 'decoration' ในวิดเจ็ต 'Container' นิยมใช้คลาสใดในการกำหนดสีพื้นหลัง ขอบโค้งมน เงาตกกระทบ และเส้นขอบ?",
        "code": "Container(\n  decoration: BoxDecoration(\n    color: Colors.white,\n    borderRadius: BorderRadius.circular(12),\n    boxShadow: [BoxShadow(blurRadius: 4)],\n  ),\n)",
        "choices": [
            "BoxDecoration",
            "CardDecoration",
            "StyleDecoration",
            "PaintDecoration"
        ],
        "correctAnswer": 0,
        "explanation": "BoxDecoration คือคลาสหลักที่ใช้กำหนดคุณสมบัติการตกแต่งกล่องใน Container เช่น สีพื้นหลัง (color/gradient), ขอบมน (borderRadius), เส้นขอบ (border), เงา (boxShadow), และรูปภาพพื้นหลัง (image)"
    },
    {
        "id": 46,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "ข้อควรระวังสำคัญที่สุดเมื่อกำหนดสีพื้นหลังใน 'Container' ที่มี 'BoxDecoration' คือข้อใด?",
        "choices": [
            "หากมีการใช้งาน BoxDecoration จะต้องระบุสีใน BoxDecoration(color: ...) ห้ามระบุ color ที่ตัว Container โดยตรง มิฉะนั้นจะเกิด Runtime Error",
            "ห้ามใช้สีเขียวหรือสีฟ้าเด็ดขาด",
            "ต้องกำหนดสีเป็นเลขฐานสิบหกเสมอ",
            "ต้องกำหนดรูปภาพประกอบด้วยทุกครั้ง"
        ],
        "correctAnswer": 0,
        "explanation": "Flutter มีข้อกำหนดว่า: หากมีการระบุคุณสมบัติ decoration ใน Container จะต้องย้ายการกำหนด color เข้าไปไว้ใน BoxDecoration เท่านั้น หากใส่ color ที่ Container ซ้ำซ้อน ระบบจะแจ้ง Assertion failure: 'cannot provide both a color and a decoration'"
    },
    {
        "id": 47,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "หากต้องการตัดขอบของรูปภาพหรือวิดเจ็ตให้มีมุมโค้งมน (Rounded Corners) อย่างง่าย ควรใช้วิดเจ็ตใดครอบ?",
        "choices": [
            "ClipRRect (Clip Rounded Rectangle)",
            "OvalClipper",
            "CutCornerWidget",
            "BorderRadiusBox"
        ],
        "correctAnswer": 0,
        "explanation": "ClipRRect ย่อมาจาก Clip Rounded Rectangle เป็นวิดเจ็ตที่ใช้สำหรับตัดขอบ (Clip) วิดเจ็ตลูก (เช่น Image.network) ให้มีมุมโค้งมนตามรัศมีที่ระบุในคุณสมบัติ 'borderRadius'"
    },
    {
        "id": 48,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "ในวิดเจ็ต 'Column' การตั้งค่า 'crossAxisAlignment: CrossAxisAlignment.stretch' จะส่งผลอย่างไรต่อ Children ทั้งหมด?",
        "choices": [
            "บังคับให้ Children ทุกชิ้นขยายความกว้างเต็มขนาดของ Column ในแนวนอน",
            "ทำให้ Children ทุกชิ้นขยายความสูงเต็มหน้าจอ",
            "จัดวาง Children ให้อยู่กึ่งกลางหน้าจอ",
            "บีบ Children ให้มีขนาดเล็กที่สุดเท่าที่จะทำได้"
        ],
        "correctAnswer": 0,
        "explanation": "ใน Column แกนตัดขวางคือแนวนอน ค่า CrossAxisAlignment.stretch จะสั่งให้วิดเจ็ตลูกทุกตัวขยายขนาดความกว้างจนเต็มพื้นที่แนวนอนของ Column"
    },
    {
        "id": 49,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "วิดเจ็ต 'SafeArea' มีประโยชน์สำคัญอย่างไรในการออกแบบ UI ของแอปพลิเคชันยุคใหม่?",
        "choices": [
            "ช่วยเพิ่มระยะห่างอัตโนมัติ เพื่อป้องกันไม่ให้ UI ไปทับซ้อนกับรอยบาก (Notch), กล้องหน้าเจาะรู, แถบสถานะ (Status Bar) หรือแถบโฮมของอุปกรณ์",
            "ช่วยป้องกันการถูกแฮ็กข้อมูลทางไซเบอร์",
            "ช่วยตรวจสอบว่าผู้ใช้เชื่อมต่อ Wi-Fi ที่ปลอดภัยหรือไม่",
            "ใช้สำหรับซ่อนรหัสผ่านในช่องกรอกข้อมูล"
        ],
        "correctAnswer": 0,
        "explanation": "SafeArea จะตรวจวัดขนาดของสิ่งกีดขวางบนหน้าจอของระบบปฏิบัติการ (เช่น รอยบากกล้อง, Dynamic Island, แถบ Navigation ด้านล่าง) แล้วแทรก Padding ให้โดยอัตโนมัติ ทำให้เนื้อหาแสดงผลในจุดที่ปลอดภัยสายตา"
    },
    {
        "id": 50,
        "section": "Widgets พื้นฐานและการจัดวาง Layout",
        "question": "วิดเจ็ตใดที่ใช้สำหรับแสดงภาพจาก URL บนอินเทอร์เน็ตได้อย่างรวดเร็วใน Flutter?",
        "choices": [
            "Image.network('https://example.com/pic.jpg')",
            "Image.asset('images/pic.jpg')",
            "Image.file(File('pic.jpg'))",
            "Image.memory(bytes)"
        ],
        "correctAnswer": 0,
        "explanation": "Image.network() เป็น Constructor แบบ Named ของคลาส Image ที่เตรียมระบบดาวน์โหลด แคช และเรนเดอร์รูปภาพจากที่อยู่อินเทอร์เน็ต (URL) ให้โดยอัตโนมัติ"
    },

    # ==========================================
    # หมวดที่ 4: Responsive Design และการจัดการฟอร์มรับข้อมูล (15 ข้อ: ข้อ 51 - 65)
    # ==========================================
    {
        "id": 51,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "การหาความกว้างของหน้าจออุปกรณ์ปัจจุบันเพื่อนำมาออกแบบ Responsive Layout ใน Flutter สามารถทำได้อย่างไร?",
        "code": "double screenWidth = MediaQuery.of(context).size.width;",
        "choices": [
            "MediaQuery.of(context).size.width",
            "Screen.getWidth(context)",
            "Window.current.width",
            "Device.size.horizontal"
        ],
        "correctAnswer": 0,
        "explanation": "MediaQuery.of(context) เป็นเครื่องมือหลักในการดึงข้อมูลมิติทางกายภาพ สัดส่วนหน้าจอ (Orientation), ข้อมูลการซูมฟอนต์, และ Insets ของอุปกรณ์ โดย .size.width จะให้ความกว้างเป็นพิกเซลตรรกะ (Logical Pixels)"
    },
    {
        "id": 52,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "ในการสร้างช่องกรอกข้อมูลประเภท 'รหัสผ่าน' (Password) ด้วยวิดเจ็ต TextField หรือ TextFormField คุณสมบัติใดที่ใช้ซ่อนตัวอักษรเป็นจุดกลมดำหรือดอกจัน?",
        "code": "TextField(\n  obscureText: true,\n  decoration: InputDecoration(labelText: 'Password'),\n)",
        "choices": [
            "obscureText: true",
            "hideCharacters: true",
            "isPassword: true",
            "secureField: true"
        ],
        "correctAnswer": 0,
        "explanation": "คุณสมบัติ 'obscureText: true' ใน TextField หรือ TextFormField ทำหน้าที่ซ่อนตัวอักษรที่พิมพ์ไม่ให้บุคคลภายนอกมองเห็น เหมาะอย่างยิ่งสำหรับช่องป้อนข้อมูลที่เป็นความลับ เช่น รหัสผ่าน หรือ PIN"
    },
    {
        "id": 53,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "ตัวควบคุม (Controller) ชนิดใดที่ใช้สำหรับอ่านค่าที่ผู้ใช้พิมพ์ ตรวจจับการเปลี่ยนแปลงข้อความ หรือกำหนดข้อความเริ่มต้นให้แก่ TextField?",
        "code": "final TextEditingController _nameController = TextEditingController();",
        "choices": [
            "TextEditingController",
            "InputFormController",
            "StringFieldController",
            "TextFieldHandler"
        ],
        "correctAnswer": 0,
        "explanation": "TextEditingController ใช้ผูกเข้ากับ TextField ผ่านพารามิเตอร์ 'controller' เพื่อช่วยให้อ่านค่าข้อความ (.text), ล้างค่า (.clear()), หรือดักฟังสตรีมการพิมพ์ (.addListener) ได้อย่างสมบูรณ์"
    },
    {
        "id": 54,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "เมื่อใช้งาน 'TextEditingController' ใน State class ข้อปฏิบัติสำคัญตามหลัก Memory Management คือข้อใด?",
        "choices": [
            "ต้องเรียกใช้งานคำสั่ง controller.dispose() ภายในเมธอด dispose() เสมอ เพื่อคืนหน่วยความจำและป้องกัน Memory Leak",
            "ต้องประกาศตัวแปรให้เป็น const",
            "ต้องห้ามใช้กับวิดเจ็ตประเภท Form",
            "ไม่ต้องทำอะไรเลย ระบบจัดการขยะ (GC) จะดูแลได้ 100%"
        ],
        "correctAnswer": 0,
        "explanation": "Controller และ Animation Objects ใน Flutter มีการผูก Event Listener ภายใน หากไม่สั่ง .dispose() เมื่อ Widget นั้นถูกทำลายออกไป จะเกิดปัญหา Memory Leak ทำให้แอปพลิเคชันกินแรมเพิ่มขึ้นเรื่อยๆ"
    },
    {
        "id": 55,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "หากต้องการตรวจสอบความถูกต้องของข้อมูลในแบบฟอร์ม (Form Validation) ควบคู่กับ GlobalKey<FormState> วิดเจ็ตช่องป้อนข้อมูลใดที่ควรเลือกใช้แทน TextField ธรรมดา?",
        "choices": [
            "TextFormField",
            "SimpleInput",
            "CheckedTextField",
            "ValidatedBox"
        ],
        "correctAnswer": 0,
        "explanation": "TextFormField เป็นวิดเจ็ตระดับสูงที่ครอบ TextField และผูกเข้ากับระบบ Form โดยมีพารามิเตอร์ 'validator' ให้เราเขียนฟังก์ชันตรวจสอบเงื่อนไขความถูกต้อง (เช่น ตรวจสอบอีเมล, ตรวจความยาวรหัสผ่าน) ร่วมกับ FormState.validate()"
    },
    {
        "id": 56,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "ในการตรวจสอบความถูกต้องของฟอร์มด้วยคำสั่ง '_formKey.currentState!.validate()' จะทราบได้อย่างไรว่าข้อมูลในทุกช่องผ่านเกณฑ์ถูกต้องทั้งหมด?",
        "choices": [
            "เมธอด validate() จะส่งคืนค่าบูลีนกลับมาเป็น true",
            "เมธอด validate() จะส่งค่า null",
            "ระบบจะสั่งปิดแอปพลิเคชันทันที",
            "หน้าจอจะเปลี่ยนเป็นสีเขียวทั้งหมด"
        ],
        "correctAnswer": 0,
        "explanation": "เมธอด validate() จะวนลูปเรียก validator ของ TextFormField ทุกตัวในฟอร์ม หากทุกช่องคืนค่า null (ไม่มีข้อผิดพลาด) เมธอดจะส่งคืนค่า 'true' บ่งบอกว่าฟอร์มผ่านเกณฑ์ พร้อมส่งข้อมูลต่อไปได้"
    },
    {
        "id": 57,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "คุณสมบัติใดใน TextField ที่ใช้กำหนดประเภทของคีย์บอร์ดเสมือนบนหน้าจอ (เช่น คีย์บอร์ดตัวเลข, คีย์บอร์ดสำหรับกรอกอีเมล)?",
        "code": "TextField(\n  keyboardType: TextInputType.emailAddress,\n)",
        "choices": [
            "keyboardType",
            "inputKeyboard",
            "textFormat",
            "keypadStyle"
        ],
        "correctAnswer": 0,
        "explanation": "พารามิเตอร์ 'keyboardType' รับค่าเป็น TextInputType (เช่น .number, .emailAddress, .phone, .multiline) เพื่อบอกระบบปฏิบัติการให้เปิดคีย์บอร์ดที่เหมาะสมกับข้อมูลที่ผู้ใช้ต้องกรอก"
    },
    {
        "id": 58,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "วิดเจ็ต 'LayoutBuilder' มีความแตกต่างและจุดเด่นอย่างไรเมื่อเทียบกับการใช้ 'MediaQuery' ในการทำ Responsive Layout?",
        "choices": [
            "LayoutBuilder จะส่งมอบค่า BoxConstraints ของพื้นที่ของ Parent Widget ที่ตำแหน่งนั้นๆ ต่างจาก MediaQuery ที่ส่งมอบขนาดหน้าจอรวมทั้งหมดของอุปกรณ์",
            "LayoutBuilder ใช้เฉพาะบนแท็บเล็ตเท่านั้น",
            "LayoutBuilder ไม่สามารถทราบขนาดพื้นที่ใดๆ ได้",
            "LayoutBuilder ใช้สำหรับเปลี่ยนภาษาของระบบ"
        ],
        "correctAnswer": 0,
        "explanation": "MediaQuery ให้ขนาดรวมของหน้าจออุปกรณ์ทั้งหมด แต่ 'LayoutBuilder' ให้ค่าขนาดความกว้าง/ความสูงสูงสุดที่ Parent อนุญาตให้วิดเจ็ตนั้นวาดได้ (BoxConstraints) เหมาะสำหรับการสร้าง Reusable Responsive Component ที่วางในจุดใดของจอก็ได้"
    },
    {
        "id": 59,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "การตรวจสอบว่าผู้ใช้กำลังถืออุปกรณ์ใน 'แนวตั้ง' หรือ 'แนวนอน' ผ่าน MediaQuery สามารถเขียนเงื่อนไขได้อย่างไร?",
        "choices": [
            "MediaQuery.of(context).orientation == Orientation.portrait",
            "Device.isVertical() == true",
            "Screen.direction == 'up'",
            "Window.isRotated == false"
        ],
        "correctAnswer": 0,
        "explanation": "สามารถตรวจสอบผ่าน MediaQuery.of(context).orientation ซึ่งจะคืนค่า Enum เป็น Orientation.portrait (แนวตั้ง) หรือ Orientation.landscape (แนวนอน) เพื่อสลับการแสดงผล Layout ให้เหมาะสม"
    },
    {
        "id": 60,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "เมื่อผู้ใช้แตะที่ช่อง TextField แล้วคีย์บอร์ดเสมือนเลื่อนขึ้นมาบดบังปุ่มกดด้านล่าง ปัญหานี้สามารถป้องกันและแก้ไขได้อย่างมีประสิทธิภาพด้วยวิธีใด?",
        "choices": [
            "ครอบโครงสร้าง Body ทั้งหมดด้วย SingleChildScrollView เพื่อให้หน้าจอเลื่อนหลบคีย์บอร์ดได้โดยอัตโนมัติ",
            "ห้ามไม่ให้อุปกรณ์เปิดคีย์บอร์ด",
            "ลดขนาดของฟอนต์ตัวหนังสือให้เหลือ 1 พิกเซล",
            "ลบช่อง TextField ออกจากหน้าจอ"
        ],
        "correctAnswer": 0,
        "explanation": "การครอบด้วย 'SingleChildScrollView' ทำให้ Viewport สามารถขยายตัวและเลื่อนเนื้อหา (Auto-scroll) ขึ้นด้านบนเมื่อคีย์บอร์ดเสมือนถูกเปิดขึ้นมา ช่วยขจัดปัญหา Bottom Overflow เมื่อพิมพ์ข้อความ"
    },
    {
        "id": 61,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "ในวิดเจ็ต 'InputDecoration' หากต้องการแสดงข้อความใบ้สีเทาจางๆ ในช่องพิมพ์ที่จะหายไปเมื่อผู้ใช้เริ่มพิมพ์ตัวอักษร ควรระบุที่พารามิเตอร์ใด?",
        "choices": [
            "hintText",
            "labelText",
            "helperText",
            "errorText"
        ],
        "correctAnswer": 0,
        "explanation": "พารามิเตอร์ 'hintText' ใช้สำหรับแสดงข้อความแนะแนวทาง (Placeholder) ที่จะปรากฏเมื่อช่องนั้นยังว่างเปล่า ส่วน 'labelText' คือข้อความกำกับที่จะลอยขึ้นไปอยู่ขอบบนเมื่อมีโฟกัส (Floating Label)"
    },
    {
        "id": 62,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "การสั่งปิดคีย์บอร์ดเสมือนลง (Dismiss Keyboard) เมื่อผู้ใช้แตะที่พื้นที่ว่างบนหน้าจอ สามารถทำได้อย่างไรใน Flutter?",
        "choices": [
            "FocusScope.of(context).unfocus();",
            "Keyboard.close();",
            "System.hideInput();",
            "InputMethodManager.hide();"
        ],
        "correctAnswer": 0,
        "explanation": "การเรียกคำสั่ง 'FocusScope.of(context).unfocus()' จะสั่งปลดโฟกัส (Focus) ออกจากช่องป้อนข้อมูลปัจจุบัน ส่งผลให้ระบบปฏิบัติการหุบคีย์บอร์ดเสมือนลงทันที"
    },
    {
        "id": 63,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "วิดเจ็ต 'DropdownButton<T>' ใน Flutter ใช้สำหรับวัตถุประสงค์ใดในแบบฟอร์ม?",
        "choices": [
            "สร้างเมนูตัวเลือกแบบดรอปดาวน์ให้ผู้ใช้คลิกเลือกค่าหนึ่งค่าจากรายการที่กำหนดไว้ล่วงหน้า",
            "ใช้สำหรับอัปโหลดไฟล์ขนาดใหญ่ไปยังเซิร์ฟเวอร์",
            "ใช้สำหรับดาวน์โหลดข้อมูลแบบ Real-time",
            "ใช้สำหรับควบคุมระดับเสียงของตัวเครื่อง"
        ],
        "correctAnswer": 0,
        "explanation": "DropdownButton<T> เป็นวิดเจ็ตมาตรฐานสำหรับสร้างเมนูตัวเลือก โดยรับค่า items ในรูปของ List<DropdownMenuItem<T>> และรับฟังก์ชัน onChanged เพื่ออัปเดตค่าเมื่อผู้ใช้เลือกตัวเลือกใหม่"
    },
    {
        "id": 64,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "หากต้องการสร้างปุ่มเปิด/ปิดสถานะแบบสวิตช์เลื่อน (Toggle Switch) ในแบบฟอร์มการตั้งค่า ควรเลือกใช้วิดเจ็ตใด?",
        "choices": [
            "Switch (หรือ SwitchListTile)",
            "Checkbox",
            "Radio",
            "Slider"
        ],
        "correctAnswer": 0,
        "explanation": "วิดเจ็ต 'Switch' (หรือ SwitchListTile ที่มีข้อความและไอคอนประกอบ) ใช้สำหรับแสดงและสลับสถานะเปิด/ปิด (Boolean: true/false) ในลักษณะของสวิตช์เลื่อนสไตล์โมเดิร์น"
    },
    {
        "id": 65,
        "section": "Responsive Design และการจัดการฟอร์มรับข้อมูล",
        "question": "คุณสมบัติ 'autofocus: true' ในวิดเจ็ต TextField ส่งผลอย่างไรเมื่อหน้าจอนั้นถูกเปิดขึ้นมา?",
        "choices": [
            "ช่องข้อความนั้นจะถูกเลือกและเปิดคีย์บอร์ดเสมือนขึ้นมาโดยอัตโนมัติทันทีที่หน้าจอแสดงผล",
            "ทำให้กล้องถ่ายภาพทำการโฟกัสภาพอัตโนมัติ",
            "ทำการพิมพ์ข้อความอัตโนมัติโดยที่ผู้ใช้ไม่ต้องแตะ",
            "ทำการตรวจสอบไวยากรณ์ภาษาไทยแบบอัตโนมัติ"
        ],
        "correctAnswer": 0,
        "explanation": "'autofocus: true' จะสั่งให้ Focus Node จับจ้องไปที่ช่องข้อความดังกล่าวทันทีที่วิดเจ็ตถูกประกอบลงในหน้าจอ ทำให้คีย์บอร์ดเด้งขึ้นมาพร้อมให้ผู้ใช้พิมพ์ได้ทันทีโดยไม่ต้องเอานิ้วไปแตะซ้ำ"
    },

    # ==========================================
    # หมวดที่ 5: วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส (15 ข้อ: ข้อ 66 - 80)
    # ==========================================
    {
        "id": 66,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "ในวงจรชีวิต (Lifecycle) ของ 'StatefulWidget' เมธอดใดที่จะถูกเรียกใช้งานเพียง 'ครั้งเดียวเท่านั้น' เมื่อ State Object ถูกสร้างขึ้นและแทรกลงใน Element Tree?",
        "code": "@override\nvoid initState() {\n  super.initState();\n  // จุดนี้ทำงานเมื่อใด?\n}",
        "choices": [
            "initState()",
            "build()",
            "dispose()",
            "didUpdateWidget()"
        ],
        "correctAnswer": 0,
        "explanation": "'initState()' คือเมธอดแรกในวงจรชีวิตของ State ที่จะถูกเรียกเพียงครั้งเดียวตลอดอายุของวิดเจ็ตนั้น เหมาะสำหรับการกำหนดค่าเริ่มต้น การเริ่มต้น Controller หรือการดึงข้อมูลจาก API ครั้งแรก"
    },
    {
        "id": 67,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "เมธอดใดในวงจรชีวิตของ StatefulWidget ที่จะถูกเรียกใช้งานเป็นลำดับสุดท้ายเมื่อวิดเจ็ตถูกถอดถอนออกจาก Widget Tree อย่างถาวร?",
        "choices": [
            "dispose()",
            "deactivate()",
            "initState()",
            "build()"
        ],
        "correctAnswer": 0,
        "explanation": "'dispose()' คือเมธอดสุดท้ายที่จะทำงานเมื่อ State Object ถูกทำลายทิ้งอย่างถาวร (เช่น การกด Back ออกจากหน้านั้น) โดยใช้สำหรับยกเลิก StreamSubscription, ปิด Controller, หรือปลด Animation ทิ้ง"
    },
    {
        "id": 68,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "การสืบทอดคลาส 'ChangeNotifier' ในกระบวนการทำ State Management ร่วมกับ Provider หรือ ListenableBuilder ให้ความสามารถสำคัญใด?",
        "code": "class CounterModel extends ChangeNotifier {\n  int _count = 0;\n  int get count => _count;\n  \n  void increment() {\n    _count++;\n    notifyListeners(); // ทำหน้าที่อะไร?\n  }\n}",
        "choices": [
            "ทำให้คลาสนั้นสามารถกระจายสัญญาณแจ้งเตือนไปยังวิดเจ็ตต่างๆ ที่กำลังดักฟังอยู่ให้ Rebuild หน้าจอใหม่ได้ผ่านคำสั่ง notifyListeners()",
            "ทำให้คลาสนั้นสามารถเก็บข้อมูลลง SQLite ได้อัตโนมัติ",
            "ใช้สำหรับเปลี่ยนภาษาของระบบปฏิบัติการ",
            "ป้องกันไม่ให้ข้อมูลในคลาสถูกเปลี่ยนแปลง"
        ],
        "correctAnswer": 0,
        "explanation": "ChangeNotifier คือคลาสใน Flutter Foundation ที่ทำหน้าที่ตาม Observer Pattern เมื่อข้อมูลภายในโมเดลมีการเปลี่ยนแปลง การเรียก 'notifyListeners()' จะแจ้งไปยังทุก Consumer/Widget ที่กำลังฟังโมเดลนี้อยู่ ให้สั่ง build ใหม่อัตโนมัติ"
    },
    {
        "id": 69,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "ฟังก์ชัน Asynchronous ต่อไปนี้ ข้อใดอธิบายการทำงานได้ถูกต้องสมบูรณ์ที่สุด?",
        "code": "Future<String> fetchName() async {\n  await Future.delayed(const Duration(seconds: 2));\n  return 'Somchai';\n}",
        "choices": [
            "ฟังก์ชันนี้จะทำงานแบบอะซิงโครนัส โดยไม่บล็อก UI Thread และจะส่งคืนอ็อบเจกต์ Future ที่เมื่อเวลาผ่านไป 2 วินาทีแล้ว จะส่งมอบผลลัพธ์เป็นสตริง 'Somchai'",
            "ฟังก์ชันนี้ทำให้หน้าจอค้างไม่สามารถกดปุ่มใดๆ ได้เป็นเวลา 2 วินาที",
            "ฟังก์ชันนี้จะส่งคืนข้อความ 'Somchai' ทันทีโดยไม่มีการรอคอยใดๆ",
            "เป็นฟังก์ชันที่ผิดไวยากรณ์ คอมไพเลอร์จะไม่ยอมให้รัน"
        ],
        "correctAnswer": 0,
        "explanation": "ฟังก์ชันที่มีคีย์เวิร์ด 'async' จะคืนค่าผลลัพธ์เป็น 'Future<T>' เสมอ โดยคำสั่ง 'await' จะหยุดรอผลลัพธ์ของ Operation นั้นโดยไม่บล็อก Main Thread (UI ไม่ค้าง) เมื่อเสร็จสิ้นจะคืนค่าตามประเภทที่ระบุ"
    },
    {
        "id": 70,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "วิดเจ็ตใดที่นิยมใช้มากที่สุดในการรอรับข้อมูลจากฟังก์ชัน Asynchronous (Future) แล้วสลับแสดง UI ระหว่าง 'กำลังโหลด' (Loading) และ 'แสดงข้อมูลเสร็จสมบูรณ์'?",
        "code": "FutureBuilder<String>(\n  future: fetchName(),\n  builder: (context, snapshot) {\n    if (snapshot.connectionState == ConnectionState.waiting) {\n      return CircularProgressIndicator();\n    }\n    return Text(snapshot.data ?? '');\n  },\n)",
        "choices": [
            "FutureBuilder",
            "StreamBuilder",
            "AsyncWidget",
            "ThreadWatcher"
        ],
        "correctAnswer": 0,
        "explanation": "'FutureBuilder' ออกแบบมาเพื่อผูกเข้ากับ Future โดยมี 'builder' ที่ได้รับ AsyncSnapshot เพื่อให้นักพัฒนาสามารถตรวจเช็ค ConnectionState (waiting, done) หรือ snapshot.hasError เพื่อเรนเดอร์ UI ตามสถานะได้อย่างสวยงาม"
    },
    {
        "id": 71,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "หากต้องการอัปเดตตัวแปรภายใน State ของ StatefulWidget และต้องการให้หน้าจอแสดงผลค่าใหม่บนจอทันที ต้องเรียกใช้คำสั่งใด?",
        "code": "void _increase() {\n  setState(() {\n    _counter++;\n  });\n}",
        "choices": [
            "setState(() { ... })",
            "updateScreen()",
            "refreshUI()",
            "rebuild()"
        ],
        "correctAnswer": 0,
        "explanation": "การเรียก 'setState()' เป็นการส่งสัญญาณบอก Flutter Framework ว่าสถานะภายในของอ็อบเจกต์นี้เปลี่ยนไปแล้ว ทำให้ระบบกำหนดตารางเวลา (Schedule) ให้เรียกเมธอด build() ใหม่เพื่อวาด UI ล่าสุด"
    },
    {
        "id": 72,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "ข้อใดเป็นข้อห้ามสำคัญที่ไม่ควรทำอย่างเด็ดขาดภายในเมธอด 'build(BuildContext context)' ใน Flutter?",
        "choices": [
            "ห้ามเรียกใช้คำสั่ง setState() หรือสั่งรันคำสั่ง HTTP Request โดยตรงใน build() เพราะจะทำให้เกิด Infinite Rebuild Loop",
            "ห้ามประกาศตัวแปรชนิด String หรือ int",
            "ห้ามส่งคืนค่าเป็นวิดเจ็ต Scaffold",
            "ห้ามใช้งานวิดเจ็ต Text เกิน 1 ตัว"
        ],
        "correctAnswer": 0,
        "explanation": "เมธอด build() มีหน้าที่ส่งคืนโครงสร้าง Widget Tree เท่านั้น และอาจถูกเรียกซ้ำบ่อยครั้งตามรอบการเรนเดอร์ การใส่ setState() หรือการยิง API ใน build() จะทำให้เกิดการเรียกซ้ำไม่สิ้นสุด (Infinite Loop) และทำให้แอปพัง"
    },
    {
        "id": 73,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "เมื่อใช้งานคำสั่ง 'await' ในฟังก์ชัน Asynchronous ข้อบังคับสำคัญทางไวยากรณ์ของภาษา Dart คือข้อใด?",
        "choices": [
            "คำสั่ง await จะสามารถใช้งานได้เฉพาะภายในฟังก์ชันที่มีการกำกับคีย์เวิร์ด 'async' ไว้เท่านั้น",
            "ฟังก์ชันนั้นต้องส่งคืนค่าเป็น void เสมอ",
            "ต้องประกาศตัวแปรทั้งหมดให้เป็น static",
            "ต้องรันผ่านโทรศัพท์เครื่องจริงเท่านั้น"
        ],
        "correctAnswer": 0,
        "explanation": "ในภาษา Dart คีย์เวิร์ด 'await' ต้องอยู่ภายในฟังก์ชันที่ถูกประกาศว่าเป็น 'async' เสมอ เพื่อให้คอมไพเลอร์ทราบว่าโครงสร้างฟังก์ชันนี้จะถูกแปลงเป็นการประมวลผลแบบต่อเนื่องตามลำดับของ Future"
    },
    {
        "id": 74,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "หากต้องการรับส่งข้อมูลที่ไหลเข้ามาอย่างต่อเนื่องตามเวลา (Continuous Stream of Data) เช่น ข้อมูล Real-time Chat หรือพิกัด GPS ควรเลือกใช้วิดเจ็ตใดในการแสดงผล?",
        "choices": [
            "StreamBuilder",
            "FutureBuilder",
            "SingleChildScrollView",
            "StatefulBuilder"
        ],
        "correctAnswer": 0,
        "explanation": "'StreamBuilder' เหมาะสำหรับข้อมูลที่ไหลมาเป็นกระแสอย่างต่อเนื่องหลายๆ ครั้ง (Stream) ต่างจาก 'FutureBuilder' ที่รอรับข้อมูลเพียงครั้งเดียวแล้วสิ้นสุดลง"
    },
    {
        "id": 75,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "การจัดการข้อผิดพลาด (Error Handling) สำหรับโค้ดที่มีการเรียกใช้คำสั่ง 'await' นิยมใช้บล็อกคำสั่งใด?",
        "code": "try {\n  var result = await fetchName();\n} catch (e) {\n  print('Error: $e');\n}",
        "choices": [
            "try { ... } catch (e) { ... }",
            "if ... else ...",
            "switch ... case ...",
            "assert( ... )"
        ],
        "correctAnswer": 0,
        "explanation": "เมื่อเขียนโค้ดแบบ async/await เราสามารถจัดการข้อผิดพลาด (Exception) ได้เหมือนกับการเขียนโค้ด Synchronous ทั่วไป โดยครอบด้วยบล็อก 'try - catch' เพื่อดักจับและจัดการปัญหาได้อย่างปลอดภัย"
    },
    {
        "id": 76,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "ในการทำ Navigation เพื่อเปลี่ยนหน้าจอไปยังหน้าใหม่และสามารถกดปุ่มย้อนกลับได้ นิยมใช้คำสั่งใดของคลาส Navigator?",
        "choices": [
            "Navigator.push(context, MaterialPageRoute(builder: (context) => DetailScreen()))",
            "Navigator.replace(context, DetailScreen())",
            "Navigator.kill(context)",
            "System.changeScreen(DetailScreen())"
        ],
        "correctAnswer": 0,
        "explanation": "Navigator.push() ทำหน้าที่ดัน (Push) Route หน้าใหม่ขึ้นไปวางทับบน Navigation Stack โดยมีแอนิเมชันเลื่อนหน้าจอตามสไตล์ของ OS และจะสร้างปุ่มลูกศรย้อนกลับ (Back Arrow) ที่ AppBar ให้อัตโนมัติ"
    },
    {
        "id": 77,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "หากต้องการปิดหน้าจอปัจจุบันและส่งผลลัพธ์กลับไปยังหน้าที่เปิดมา ควรใช้คำสั่งใด?",
        "choices": [
            "Navigator.pop(context, result);",
            "Navigator.push(context);",
            "Navigator.destroy();",
            "Navigator.closeAll();"
        ],
        "correctAnswer": 0,
        "explanation": "Navigator.pop(context, [result]) จะทำการดึง (Pop) หน้าจอปัจจุบันออกจาก Stack เพื่อกลับไปยังหน้าจอก่อนหน้า พร้อมทั้งสามารถส่งอาร์กิวเมนต์ผลลัพธ์กลับไปให้หน้าที่รออยู่ได้"
    },
    {
        "id": 78,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "การใช้งาน 'mounted' property ใน State class มีประโยชน์สำคัญอย่างไรในการป้องกันข้อผิดพลาด?",
        "code": "var data = await fetchName();\nif (!mounted) return;\nsetState(() {\n  _name = data;\n});",
        "choices": [
            "ใช้ตรวจสอบว่าวิดเจ็ตนี้ยังคงอยู่ในหน้าจอหรือไม่ หากผู้ใช้กดออกจากหน้าไปแล้วระหว่างรอโหลดข้อมูล จะไม่สั่ง setState() ซึ่งช่วยป้องกันไม่ให้แอปแครช",
            "ใช้ตรวจสอบว่าโทรศัพท์ติดตั้งอยู่บนขาตั้งหรือไม่",
            "ใช้ตรวจสอบว่ามีการเสียบสายชาร์จแบตเตอรี่หรือไม่",
            "ใช้ตรวจสอบว่ามีการใส่ซิมการ์ดหรือไม่"
        ],
        "correctAnswer": 0,
        "explanation": "หลังจากการทำงานของ async Operation ที่ต้องใช้เวลา หากผู้ใช้กดปิดหน้านั้นไปก่อน State จะถูก unmounted หากเราสั่ง setState() ในขณะที่ !mounted ระบบจะแจ้ง Error ทันที การตรวจสอบ 'if (!mounted) return;' จึงเป็น Best Practice สำคัญ"
    },
    {
        "id": 79,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "วงจรชีวิต 'didUpdateWidget(covariant T oldWidget)' ใน State class จะทำงานในสถานการณ์ใด?",
        "choices": [
            "เมื่อ Parent Widget ทำการ Rebuild และส่ง Configuration (Arguments/Parameters) ชุดใหม่มาให้ Widget เดิมตัวนี้",
            "เมื่อแอปพลิเคชันถูกดาวน์โหลดเสร็จสิ้นจาก Play Store",
            "เมื่อเครื่องโทรศัพท์ถูกปิดเครื่อง",
            "ทำงานเฉพาะตอนเปิดแอปครั้งแรกครั้งเดียวเท่านั้น"
        ],
        "correctAnswer": 0,
        "explanation": "'didUpdateWidget' จะทำงานเมื่อ Parent Widget Rebuild แล้วส่งข้อมูลชุดใหม่มาให้ Child Widget เดิมตัวเดิม เพื่อให้ State มีโอกาสเปรียบเทียบค่าระหว่าง widget (ใหม่) กับ oldWidget (เก่า) และปรับปรุงสถานะภายใน"
    },
    {
        "id": 80,
        "section": "วงจรชีวิต Widget, State Management & การโปรแกรมแบบอะซิงโครนัส",
        "question": "เหตุใดการจัดการ State ระดับแอปพลิเคชัน (App-wide State Management) ด้วยเครื่องมือเช่น Provider, Riverpod, หรือ Bloc จึงได้รับความนิยมมากกว่าการพึ่งพา setState() เพียงอย่างเดียวในแอปขนาดใหญ่?",
        "choices": [
            "ช่วยแยก Business Logic ออกจาก UI อย่างชัดเจน (Separation of Concerns), แก้ปัญหาการส่งข้อมูลข้ามหลายชั้น (Prop Drilling), และลดการ Rebuild ที่ไม่จำเป็น",
            "เพราะ setState() ถูกยกเลิกไปแล้วใน Flutter เวอร์ชันล่าสุด",
            "เพราะช่วยให้แอปไม่ต้องใช้อินเทอร์เน็ตในการทำงาน",
            "เพราะทำให้แอปมีขนาดไม่เกิน 1 เมกะไบต์เสมอ"
        ],
        "correctAnswer": 0,
        "explanation": "ในแอปพลิเคชันระดับองค์กร การใช้เพียง setState() จะทำให้เกิด Spaghetti Code และปัญหา Prop Drilling (ส่งข้อมูลผ่าน Constructor ต่อกันหลายสิบชั้น) การใช้ State Management ช่วยให้แชร์ข้อมูลระหว่างหน้าจอได้ง่าย ควบคุมการ Rebuild เฉพาะจุด และเขียน Unit Test ได้ง่ายขึ้นอย่างมาก"
    }
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

# Process both subjects
balanced_tourism = balance_and_shuffle_choices(tourism_questions, seed=101)
balanced_mobile = balance_and_shuffle_choices(mobile_questions, seed=202)

print("Tourism questions count:", len(balanced_tourism))
print("Mobile questions count:", len(balanced_mobile))

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

# Subject metadata
subjects = {
    "tourism": {
        "id": "tourism",
        "title": "การจัดการเทคโนโลยีสารสนเทศในอุตสาหกรรมการท่องเที่ยวและบริการ",
        "badge": "สาขาวิชาการท่องเที่ยวและบริการดิจิทัล",
        "description": "คลังข้อสอบมาตรฐานจำนวน 80 ข้อ ครอบคลุมคุณลักษณะของการบริการ, E-commerce 8 ประการ, แผนธุรกิจบริการ, กรณีศึกษา IT ทัวร์ไทย และกรณีศึกษา Velia Rental Store",
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
      max-width: 900px;
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
      background: linear-gradient(90deg, #2563eb, #38bdf8, #10b981);
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
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 20px;
      margin: 24px 0 12px 0;
    }}

    .subject-card {{
      background: #ffffff;
      border: 2px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 24px;
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
      width: 52px;
      height: 52px;
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

    .subject-card-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
      line-height: 1.4;
    }}

    .subject-card-desc {{
      font-size: 0.88rem;
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
      font-size: 0.82rem;
      font-weight: 700;
      padding: 3px 12px;
      border-radius: 20px;
      background: #f1f5f9;
      color: var(--text-main);
    }}

    .btn-select {{
      font-size: 0.9rem;
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
    @media (max-width: 640px) {{
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
                <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h2 class="subject-card-title">การจัดการเทคโนโลยีสารสนเทศในอุตสาหกรรมการท่องเที่ยวและบริการ</h2>
              <p class="subject-card-desc">ทฤษฎีลักษณะบริการ (Characteristics of Services), E-commerce 8 คุณลักษณะ, โครงสร้างแผนธุรกิจ, กรณีศึกษา IT ท่องเที่ยวไทย และกรณีศึกษา Velia Rental Store</p>
            </div>
            <div class="subject-footer">
              <span class="subject-pill">จำนวน 80 ข้อ</span>
              <span class="btn-select">
                เลือกวิชานี้
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
              </span>
            </div>
          </div>

          <!-- Card Subject 2 -->
          <div class="subject-card" onclick="selectSubject('mobile')">
            <div>
              <div class="subject-icon-box indigo">
                <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
              </div>
              <h2 class="subject-card-title">การพัฒนา Mobile Application (Flutter & Dart)</h2>
              <p class="subject-card-desc">ข้อสอบระดับปริญญาตรีพร้อมโค้ดสั้นๆ: Flutter Architecture, pubspec.yaml, Hot Reload, initState, APK, late, const, Layouts, RenderFlex overflow, ChangeNotifier, async/Future</p>
            </div>
            <div class="subject-footer">
              <span class="subject-pill">จำนวน 80 ข้อ</span>
              <span class="btn-select">
                เลือกวิชานี้
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
              </span>
            </div>
          </div>
        </div>
      </section>

      <!-- ================= 1. START / OVERVIEW SCREEN ================= -->
      <section id="startScreen" class="screen">
        <div style="margin-bottom: 16px;">
          <button class="btn btn-secondary" onclick="backToPortal()" style="padding: 8px 16px; font-size: 0.9rem;">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            เลือกวิชาอื่น
          </button>
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

      switchScreen(startScreen);
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

      // Handle optional code snippet
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

print(f"Generated successfully at: {output_path}")
