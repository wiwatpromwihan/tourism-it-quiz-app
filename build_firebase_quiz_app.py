# -*- coding: utf-8 -*-
import json
import re

# Load subjects from build_three_subjects_app.py
from build_three_subjects_app import subjects

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
      --warning-light: #fffbeb;
      --warning-border: #fde68a;
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
      padding: 20px 16px;
      line-height: 1.6;
    }}

    .container {{
      width: 100%;
      max-width: 920px;
      margin: 0 auto;
    }}

    /* User Auth Header Bar */
    .user-auth-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(12px);
      padding: 10px 20px;
      border-radius: var(--radius-md);
      margin-bottom: 16px;
      border: 1px solid rgba(226, 232, 240, 0.8);
      box-shadow: var(--shadow-sm);
      flex-wrap: wrap;
      gap: 12px;
    }}

    .user-profile {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .user-avatar {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--primary);
    }}

    .user-avatar-placeholder {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: #e2e8f0;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.95rem;
    }}

    .user-details {{
      display: flex;
      flex-direction: column;
    }}

    .user-name {{
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--text-main);
      line-height: 1.2;
    }}

    .user-status-pill {{
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .user-status-pill.logged-in {{
      color: #059669;
    }}

    .user-status-pill .dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: currentColor;
    }}

    .btn-auth {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-family: var(--font-th);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid var(--border-subtle);
      background: white;
      color: var(--text-main);
      box-shadow: var(--shadow-sm);
    }}

    .btn-auth:hover {{
      background: #f8fafc;
      border-color: #cbd5e1;
      transform: translateY(-1px);
    }}

    .btn-auth.sign-out {{
      color: #dc2626;
      border-color: #fecaca;
      background: #fff5f5;
    }}

    .btn-auth.sign-out:hover {{
      background: #fee2e2;
    }}

    .google-icon {{
      width: 18px;
      height: 18px;
    }}

    /* Main Card */
    .card {{
      background: var(--card-bg);
      border-radius: var(--radius-lg);
      padding: 34px 30px;
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
      margin-bottom: 24px;
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
      font-size: 1.6rem;
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
      margin: 20px 0 12px 0;
    }}

    .subject-card {{
      background: #ffffff;
      border: 2px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 22px 20px;
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

    .subject-resume-tag {{
      position: absolute;
      top: 14px;
      right: 14px;
      background: #fef3c7;
      color: #b45309;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
      border: 1px solid #fde68a;
      display: flex;
      align-items: center;
      gap: 4px;
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.03); }}
    }}

    .subject-icon-box {{
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 14px;
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

    .subject-icon-box.purple {{
      background: #f3e8ff;
      color: #9333ea;
    }}

    .subject-card-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
      line-height: 1.4;
    }}

    .subject-card-desc {{
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 16px;
      flex-grow: 1;
    }}

    .subject-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 12px;
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

    /* ================= RESUME BOX ================= */
    .resume-card-box {{
      background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
      border: 2px solid #fde68a;
      border-radius: var(--radius-md);
      padding: 20px 22px;
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
      display: none;
    }}

    .resume-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      font-size: 1.05rem;
      color: #b45309;
      margin-bottom: 6px;
    }}

    .resume-desc {{
      font-size: 0.92rem;
      color: #78350f;
      margin-bottom: 16px;
      line-height: 1.5;
    }}

    .resume-actions {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .btn-resume {{
      background: #d97706;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: var(--radius-sm);
      font-family: var(--font-th);
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 2px 4px rgba(217, 119, 6, 0.25);
      transition: all 0.2s ease;
    }}

    .btn-resume:hover {{
      background: #b45309;
      transform: translateY(-1px);
    }}

    .btn-restart-saved {{
      background: white;
      color: #78350f;
      border: 1px solid #fcd34d;
      padding: 10px 18px;
      border-radius: var(--radius-sm);
      font-family: var(--font-th);
      font-weight: 600;
      font-size: 0.92rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .btn-restart-saved:hover {{
      background: #fef3c7;
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

    /* Mode Selector Box */
    .mode-selector-box {{
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
      background: #f1f5f9;
      padding: 6px;
      border-radius: var(--radius-md);
    }}

    .mode-tab-btn {{
      flex: 1;
      padding: 12px 16px;
      border: none;
      background: transparent;
      border-radius: var(--radius-sm);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}

    .mode-tab-btn:hover {{
      color: var(--primary);
    }}

    .mode-tab-btn.active {{
      background: #ffffff;
      color: var(--primary);
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }}

    /* Written Exam Screen */
    .written-header-card {{
      background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
      color: white;
      border-radius: var(--radius-md);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-md);
    }}

    .written-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.2);
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 600;
      margin-bottom: 10px;
      backdrop-filter: blur(4px);
    }}

    .written-main-title {{
      font-size: 1.4rem;
      font-weight: 800;
      margin-bottom: 8px;
      line-height: 1.3;
    }}

    .written-main-desc {{
      font-size: 0.95rem;
      opacity: 0.9;
      line-height: 1.6;
      margin-bottom: 16px;
    }}

    .written-stats-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .written-stat-pill {{
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 600;
    }}

    .written-part-divider {{
      background: #e2e8f0;
      color: #334155;
      font-weight: 700;
      padding: 10px 16px;
      border-radius: var(--radius-sm);
      margin: 24px 0 16px 0;
      font-size: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .written-q-card {{
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px;
      margin-bottom: 18px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }}

    .written-q-card:hover {{
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }}

    .written-q-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .written-q-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .written-q-badges {{
      display: flex;
      gap: 6px;
    }}

    .badge-score {{
      background: #eff6ff;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
    }}

    .badge-type {{
      background: #f1f5f9;
      color: #475569;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
    }}

    .written-q-text {{
      font-size: 0.98rem;
      color: #1e293b;
      line-height: 1.65;
      margin-bottom: 14px;
      white-space: pre-line;
      background: #f8fafc;
      padding: 14px;
      border-radius: var(--radius-sm);
      border-left: 4px solid var(--primary);
    }}

    .written-practice-box {{
      margin-top: 12px;
      margin-bottom: 14px;
    }}

    .written-practice-box textarea {{
      width: 100%;
      min-height: 90px;
      padding: 10px 14px;
      border: 1px solid #cbd5e1;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.92rem;
      line-height: 1.5;
      resize: vertical;
      box-sizing: border-box;
      transition: border-color 0.2s;
    }}

    .written-practice-box textarea:focus {{
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }}

    .btn-toggle-answer {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      color: #334155;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-toggle-answer:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    .written-answer-box {{
      display: none;
      margin-top: 14px;
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: var(--radius-sm);
      padding: 16px;
    }}

    .written-answer-box.active {{
      display: block;
    }}

    .ans-sec-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: #166534;
      margin-bottom: 4px;
      margin-top: 10px;
    }}

    .ans-sec-title:first-child {{
      margin-top: 0;
    }}

    .ans-sec-content {{
      font-size: 0.92rem;
      color: #14532d;
      line-height: 1.6;
      white-space: pre-line;
      background: #ffffff;
      padding: 10px 12px;
      border-radius: 6px;
      border: 1px solid #dcfce7;
      margin-bottom: 8px;
    }}

    .ans-code-block {{
      background: #0f172a;
      color: #e2e8f0;
      padding: 12px;
      border-radius: 6px;
      font-family: var(--font-code);
      font-size: 0.85rem;
      line-height: 1.5;
      overflow-x: auto;
      white-space: pre;
    }}

    /* Print view styles */
    @media print {{
      body {{
        background: white !important;
        color: black !important;
      }}
      .app-header, .portal-grid, #startScreen, #quizScreen, #resultScreen, #guidelinesModal, .btn, .btn-toggle-answer, .written-practice-box textarea, .mode-selector-box {{
        display: none !important;
      }}
      #writtenScreen {{
        display: block !important;
      }}
      .written-answer-box {{
        display: block !important;
      }}
      .written-q-card {{
        page-break-inside: avoid;
        border: 1px solid #000 !important;
        box-shadow: none !important;
        margin-bottom: 20px !important;
      }}
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

    .quiz-meta-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .section-pill {{
      font-size: 0.8rem;
      font-weight: 600;
      background: #e0e7ff;
      color: #3730a3;
      padding: 4px 12px;
      border-radius: 20px;
    }}

    .autosave-pill {{
      font-size: 0.78rem;
      font-weight: 600;
      color: #059669;
      background: #ecfdf5;
      padding: 3px 10px;
      border-radius: 12px;
      border: 1px solid #a7f3d0;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      opacity: 0;
      transition: opacity 0.3s ease;
    }}

    .autosave-pill.show {{
      opacity: 1;
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
      .user-auth-bar {{
        flex-direction: column;
        align-items: stretch;
      }}
      .user-profile {{
        justify-content: flex-start;
      }}
      .btn-auth {{
        justify-content: center;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    
    <!-- Top User Profile & Google Login Bar -->
    <div class="user-auth-bar">
      <div class="user-profile">
        <div id="userAvatarContainer">
          <div class="user-avatar-placeholder">👤</div>
        </div>
        <div class="user-details">
          <span class="user-name" id="userNameDisplay">ผู้ใช้งานทั่วไป (Guest)</span>
          <span class="user-status-pill" id="userStatusPill">
            <span class="dot"></span>
            <span id="userStatusText">บันทึกข้อมูลในอุปกรณ์นี้ (Local Storage)</span>
          </span>
        </div>
      </div>
      <div>
        <button class="btn-auth" id="loginBtn" onclick="handleGoogleSignIn()">
          <svg class="google-icon" viewBox="0 0 24 24">
            <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
            <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
            <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
            <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
          </svg>
          เข้าสู่ระบบด้วย Google
        </button>
        <button class="btn-auth sign-out" id="logoutBtn" onclick="handleSignOut()" style="display: none;">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          ออกจากระบบ
        </button>
      </div>
    </div>

    <!-- Main Card -->
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
            <div id="resumeTag_tourism" class="subject-resume-tag" style="display: none;">
              <span>📌 ทำค้างอยู่</span>
            </div>
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
            <div id="resumeTag_mobile" class="subject-resume-tag" style="display: none;">
              <span>📌 ทำค้างอยู่</span>
            </div>
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
            <div id="resumeTag_iot" class="subject-resume-tag" style="display: none;">
              <span>📌 ทำค้างอยู่</span>
            </div>
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

          <!-- Card Subject 4: Business Intelligence -->
          <div class="subject-card" onclick="selectSubject('bi')">
            <div id="resumeTag_bi" class="subject-resume-tag" style="display: none;">
              <span>📌 ทำค้างอยู่</span>
            </div>
            <div>
              <div class="subject-icon-box purple">
                <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              </div>
              <h2 class="subject-card-title">ธุรกิจอัจฉริยะ (Business Intelligence Blueprint)</h2>
              <p class="subject-card-desc">สถาปัตยกรรมข้อมูล 80 ข้อปรนัย + 20 ข้อเขียน: Data Roles (DE, DA, DS), Data Quality 6 มิติ, Power Query Cleansing, Star Schema (Fact/Dimension), Cardinality, DAX Measures และการเลือกวิชวลตอบโจทย์ธุรกิจ</p>
            </div>
            <div class="subject-footer">
              <span class="subject-pill" style="background: #f3e8ff; color: #7e22ce; font-weight: 700;">80 ปรนัย + 20 ข้อเขียน</span>
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
            <button id="viewGuidelinesBtn" class="btn-view-guidelines" onclick="openGuidelinesModal()">
              📋 ดูแนวทางข้อสอบฉบับเต็ม
            </button>
          </div>
        </div>

        <!-- Mode Switcher Tabs (For subjects with written exam like BI) -->
        <div id="subjectModeSelector" class="mode-selector-box" style="display: none;">
          <button id="modeQuizBtn" class="mode-tab-btn active" onclick="switchSubjectMode('quiz')">
            🔘 โหมดแบบทดสอบปรนัย (80 ข้อ)
          </button>
          <button id="modeWrittenBtn" class="mode-tab-btn" onclick="switchSubjectMode('written')">
            📝 โหมดคลังข้อสอบข้อเขียน (20 ข้อ อัตนัย 100 คะแนน)
          </button>
        </div>

        <!-- In-Progress Resume Alert Box -->
        <div id="resumeCardBox" class="resume-card-box">
          <div class="resume-header">
            <span>📌 ตรวจพบแบบทดสอบที่ทำค้างไว้!</span>
          </div>
          <p class="resume-desc" id="resumeDescText">
            คุณได้ทำแบบทดสอบค้างไว้ถึงข้อที่ 41 (ทำไปแล้ว 40 จาก 80 ข้อ) บันทึกอัตโนมัติล่าสุดเมื่อสักครู่
          </p>
          <div class="resume-actions">
            <button class="btn-resume" onclick="resumeSavedQuiz()">
              <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              <span id="resumeBtnText">▶️ ทำต่อจากจุดเดิม</span>
            </button>
            <button class="btn-restart-saved" onclick="discardSavedAndStartFresh()">
              🔄 ล้างข้อมูลและเริ่มทำใหม่ตั้งแต่ข้อ 1
            </button>
          </div>
        </div>

        <div id="guidelinesBanner" class="guideline-box" style="display: none;">
          <span id="guidelinesBannerText" class="guideline-info">💡 ข้อสอบชุดนี้มีเอกสารแนวทางและการวิเคราะห์เชิงลึก</span>
          <button id="bannerGuidelinesBtn" class="btn-view-guidelines" onclick="openGuidelinesModal()">อ่านแนวทาง</button>
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

        <button class="btn btn-primary btn-full" id="startBtn" onclick="startFreshQuiz()">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          เริ่มทำแบบทดสอบใหม่ (80 ข้อ)
        </button>
      </section>

      <!-- ================= 1.5 WRITTEN EXAM SCREEN ================= -->
      <section id="writtenScreen" class="screen">
        <div style="margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
          <button class="btn btn-secondary" onclick="backToSubjectOverview()" style="padding: 8px 16px; font-size: 0.9rem;">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            กลับหน้ารายวิชา
          </button>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <button class="btn btn-secondary" onclick="toggleAllWrittenAnswers()" id="toggleAllAnswersBtn" style="padding: 8px 14px; font-size: 0.85rem;">
              👁️ เปิด/ซ่อนเฉลยทั้งหมด
            </button>
            <button class="btn btn-primary" onclick="window.print()" style="padding: 8px 16px; font-size: 0.85rem;">
              🖨️ พิมพ์ / บันทึก PDF
            </button>
          </div>
        </div>

        <div class="written-header-card">
          <div class="written-badge">แบบทดสอบวัดความรู้ความสามารถทางวิชาการ (ข้อเขียน)</div>
          <h2 class="written-main-title" id="writtenMainTitle">คลังข้อสอบข้อเขียน วิชา ธุรกิจอัจฉริยะ (Business Intelligence)</h2>
          <p class="written-main-desc">ชุดข้อสอบอัตนัยระดับปริญญาตรี จำนวน 20 ข้อ รวม 100 คะแนนเต็ม สร้างตรงตามเอกสาร Business Intelligence Blueprint พร้อมคีย์เฉลย เกณฑ์การให้คะแนน และข้อความอ้างอิงตรงจากสไลด์</p>
          <div class="written-stats-row">
            <span class="written-stat-pill">📝 ข้อสอบ 20 ข้อ</span>
            <span class="written-stat-pill">💯 100 คะแนนเต็ม</span>
            <span class="written-stat-pill">🎯 50:50 ทฤษฎี & สถานการณ์</span>
            <span class="written-stat-pill">📊 มีข้อคำนวณและโค้ดตรวจผล</span>
          </div>
        </div>

        <div id="writtenQuestionsList">
          <!-- Injected by JS -->
        </div>
      </section>

      <!-- ================= 2. QUIZ SCREEN ================= -->
      <section id="quizScreen" class="screen">
        <div class="quiz-meta">
          <div class="quiz-meta-left">
            <span class="section-pill" id="currentSectionPill">หมวดหมู่</span>
            <span class="autosave-pill" id="autosavePill">
              <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
              บันทึกอัตโนมัติแล้ว
            </span>
          </div>
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
            พักการทำข้อสอบ / เปลี่ยนวิชา
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

  <!-- Modal for Exam Guidelines -->
  <div id="guidelinesModal" class="modal-overlay" onclick="closeGuidelinesModal(event)">
    <div class="modal-card" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 class="modal-title" id="guidelinesModalTitle">📋 เอกสารแนวทางข้อสอบ</h3>
        <button class="modal-close" onclick="closeGuidelinesModal()">&times;</button>
      </div>
      <div class="modal-body" id="modalGuidelinesList">
        <!-- Injected by JS -->
      </div>
    </div>
  </div>

  <!-- Firebase Modular SDK Scripts -->
  <script type="module">
    import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
    import {{ 
      getAuth, 
      signInWithPopup, 
      GoogleAuthProvider, 
      signOut, 
      onAuthStateChanged 
    }} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
    import {{ 
      getFirestore, 
      doc, 
      setDoc, 
      getDoc, 
      deleteDoc 
    }} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

    // Firebase Configuration from User Request
    const firebaseConfig = {{
      apiKey: "AIzaSyD-B_yHI9fssIL_sFLSiUGorgcJxSJTbFs",
      authDomain: "tourism-it-quiz-app.firebaseapp.com",
      projectId: "tourism-it-quiz-app",
      storageBucket: "tourism-it-quiz-app.firebasestorage.app",
      messagingSenderId: "409455174572",
      appId: "1:409455174572:web:d2779b52f6b414e3565009",
      measurementId: "G-BQEXGWV62D"
    }};

    // Initialize Firebase
    let app, auth, db, provider;
    try {{
      app = initializeApp(firebaseConfig);
      auth = getAuth(app);
      db = getFirestore(app);
      provider = new GoogleAuthProvider();
      provider.setCustomParameters({{ prompt: 'select_account' }});
    }} catch (err) {{
      console.warn("Firebase initialization warning:", err);
    }}

    // Make Firebase services available to window
    window.firebaseAuth = auth;
    window.firebaseDb = db;
    window.currentUser = null;

    // Elements
    const userAvatarContainer = document.getElementById('userAvatarContainer');
    const userNameDisplay = document.getElementById('userNameDisplay');
    const userStatusPill = document.getElementById('userStatusPill');
    const userStatusText = document.getElementById('userStatusText');
    const loginBtn = document.getElementById('loginBtn');
    const logoutBtn = document.getElementById('logoutBtn');

    // Auth State Observer
    if (auth) {{
      onAuthStateChanged(auth, async (user) => {{
        window.currentUser = user;
        if (user) {{
          // User is signed in
          userAvatarContainer.innerHTML = user.photoURL 
            ? `<img src="${{user.photoURL}}" alt="avatar" class="user-avatar" referrerpolicy="no-referrer">`
            : `<div class="user-avatar-placeholder">${{user.displayName ? user.displayName.charAt(0) : 'U'}}</div>`;
          userNameDisplay.textContent = user.displayName || user.email || 'ผู้ใช้งาน Google';
          userStatusPill.className = 'user-status-pill logged-in';
          userStatusText.textContent = 'ซิงค์ข้อมูลกับ Cloud Firebase อัตโนมัติ';
          loginBtn.style.display = 'none';
          logoutBtn.style.display = 'inline-flex';

          // Sync cloud progress into current state if available
          await syncCloudProgress(user.uid);
        }} else {{
          // User is signed out (Guest)
          userAvatarContainer.innerHTML = '<div class="user-avatar-placeholder">👤</div>';
          userNameDisplay.textContent = 'ผู้ใช้งานทั่วไป (Guest)';
          userStatusPill.className = 'user-status-pill';
          userStatusText.textContent = 'บันทึกข้อมูลในอุปกรณ์นี้ (Local Storage)';
          loginBtn.style.display = 'inline-flex';
          logoutBtn.style.display = 'none';
        }}
        // Refresh portal badges
        window.updatePortalResumeTags();
        if (window.currentSubjectKey) {{
          window.checkAndShowResumeCard(window.currentSubjectKey);
        }}
      }});
    }}

    // Google Sign-In Handler
    window.handleGoogleSignIn = async function() {{
      if (!auth) {{
        alert("ระบบ Firebase ยังไม่ได้เริ่มต้น กรุณาตรวจสอบการตั้งค่า");
        return;
      }}
      try {{
        const result = await signInWithPopup(auth, provider);
        const user = result.user;
        console.log("Logged in successfully:", user.displayName);
      }} catch (error) {{
        console.error("Sign-in error:", error);
        if (error.code === 'auth/unauthorized-domain') {{
          alert("แจ้งเตือน: โดเมนนี้ (" + window.location.hostname + ") ยังไม่ได้รับอนุญาตใน Firebase Console\\n\\nกรุณาไปที่ Firebase Console > Authentication > Settings > Authorized domains แล้วเพิ่ม '" + window.location.hostname + "'\\n\\n(ทั้งนี้ ท่านยังคงใช้งานและบันทึกข้อมูลอัตโนมัติในเครื่องได้ตามปกติ)");
        }} else if (error.code === 'auth/configuration-not-found') {{
          alert("แจ้งเตือน: ยังไม่ได้เปิดใช้งาน Google Sign-In ใน Firebase Console\\n\\nวิธีแก้ไขง่ายๆ:\\n1. เข้า Firebase Console (tourism-it-quiz-app)\\n2. เมนูซ้ายเลือก Authentication > แท็บ Sign-in method\\n3. คลิกเลือก 'Google' สับสวิตช์เปิดใช้งาน (Enable) และเลือกอีเมล Support Email จากนั้นกด Save\\n4. กลับมารีเฟรชหน้านี้แล้วล็อกอินได้ทันทีครับ!");
        }} else if (error.code !== 'auth/popup-closed-by-user') {{
          alert("ไม่สามารถเข้าสู่ระบบด้วย Google ได้: " + error.message);
        }}
      }}
    }};

    // Sign-Out Handler
    window.handleSignOut = async function() {{
      if (!auth) return;
      if (confirm("คุณต้องการออกจากระบบหรือไม่? (ข้อมูลในเครื่องจะยังคงได้รับการบันทึก)")) {{
        await signOut(auth);
        console.log("Signed out successfully");
      }}
    }};

    // Cloud Firestore Sync Function
    async function syncCloudProgress(uid) {{
      if (!db) return;
      try {{
        for (const subjKey of ['tourism', 'mobile', 'iot']) {{
          const docRef = doc(db, "users", uid, "progress", subjKey);
          const docSnap = await getDoc(docRef);
          if (docSnap.exists()) {{
            const cloudData = docSnap.data();
            const localRaw = localStorage.getItem('quiz_progress_' + subjKey);
            const localData = localRaw ? JSON.parse(localRaw) : null;

            // Use the newer one
            if (!localData || (cloudData.lastUpdated && cloudData.lastUpdated > (localData.lastUpdated || 0))) {{
              localStorage.setItem('quiz_progress_' + subjKey, JSON.stringify(cloudData));
            }} else if (localData && (!cloudData.lastUpdated || localData.lastUpdated > cloudData.lastUpdated)) {{
              // Sync local to cloud
              await setDoc(docRef, localData, {{ merge: true }});
            }}
          }} else {{
            // Upload local to cloud if exists
            const localRaw = localStorage.getItem('quiz_progress_' + subjKey);
            if (localRaw) {{
              await setDoc(docRef, JSON.parse(localRaw), {{ merge: true }});
            }}
          }}
        }}
      }} catch (e) {{
        console.warn("Could not sync with Firestore (check Security Rules):", e);
      }}
    }}

    // Export save to cloud helper
    window.saveToFirestore = async function(subjKey, data) {{
      if (!db || !window.currentUser) return;
      try {{
        const docRef = doc(db, "users", window.currentUser.uid, "progress", subjKey);
        await setDoc(docRef, data, {{ merge: true }});
      }} catch (err) {{
        console.warn("Firestore save error:", err);
      }}
    }};

    // Export delete from cloud helper
    window.deleteFromFirestore = async function(subjKey) {{
      if (!db || !window.currentUser) return;
      try {{
        const docRef = doc(db, "users", window.currentUser.uid, "progress", subjKey);
        await deleteDoc(docRef);
      }} catch (err) {{
        console.warn("Firestore delete error:", err);
      }}
    }};
  </script>

  <!-- Application Logic Script -->
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
    const writtenScreen = document.getElementById('writtenScreen');
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

    const resumeCardBox = document.getElementById('resumeCardBox');
    const resumeDescText = document.getElementById('resumeDescText');
    const resumeBtnText = document.getElementById('resumeBtnText');
    const autosavePill = document.getElementById('autosavePill');

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
      [portalScreen, startScreen, writtenScreen, quizScreen, resultScreen].forEach(s => s.classList.remove('active'));
      screenToShow.classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function switchSubjectMode(mode) {{
      const quizBtn = document.getElementById('modeQuizBtn');
      const writtenBtn = document.getElementById('modeWrittenBtn');
      if (mode === 'written') {{
        if (quizBtn) quizBtn.classList.remove('active');
        if (writtenBtn) writtenBtn.classList.add('active');
        renderWrittenExam();
        switchScreen(writtenScreen);
      }} else {{
        if (writtenBtn) writtenBtn.classList.remove('active');
        if (quizBtn) quizBtn.classList.add('active');
        switchScreen(startScreen);
      }}
    }}

    function backToSubjectOverview() {{
      const quizBtn = document.getElementById('modeQuizBtn');
      const writtenBtn = document.getElementById('modeWrittenBtn');
      if (writtenBtn) writtenBtn.classList.remove('active');
      if (quizBtn) quizBtn.classList.add('active');
      switchScreen(startScreen);
    }}

    let allWrittenExpanded = false;
    function toggleAllWrittenAnswers() {{
      allWrittenExpanded = !allWrittenExpanded;
      const boxes = document.querySelectorAll('.written-answer-box');
      boxes.forEach(b => {{
        if (allWrittenExpanded) b.classList.add('active');
        else b.classList.remove('active');
      }});
      const btn = document.getElementById('toggleAllAnswersBtn');
      if (btn) btn.textContent = allWrittenExpanded ? '🙈 ซ่อนเฉลยทั้งหมด' : '👁️ เปิดดูเฉลยทั้งหมด';
    }}

    function toggleWrittenAnswer(qId) {{
      const box = document.getElementById('ansBox_' + qId);
      if (!box) return;
      box.classList.toggle('active');
    }}

    function renderWrittenExam() {{
      const subj = allSubjects[currentSubjectKey];
      if (!subj || !subj.written_exam) return;
      
      const container = document.getElementById('writtenQuestionsList');
      container.innerHTML = '';
      
      let currentPartName = '';

      subj.written_exam.forEach((q, idx) => {{
        if (q.part && q.part !== currentPartName) {{
          currentPartName = q.part;
          const partDiv = document.createElement('div');
          partDiv.className = 'written-part-divider';
          partDiv.innerHTML = `<span>📂 ${{currentPartName}}</span>`;
          container.appendChild(partDiv);
        }}

        const card = document.createElement('div');
        card.className = 'written-q-card';
        card.id = 'writtenCard_' + q.id;

        const codeBlock = q.code ? `
          <div class="ans-sec-title">💻 โค้ด Python สำหรับตรวจผลลัพธ์การคำนวณ (Automated Verification):</div>
          <pre class="ans-code-block"><code>${{escapeHtml(q.code)}}</code></pre>
        ` : '';

        card.innerHTML = `
          <div class="written-q-header">
            <span class="written-q-title">${{escapeHtml(q.title || 'ข้อที่ ' + q.id)}}</span>
            <div class="written-q-badges">
              <span class="badge-score">คะแนนเต็ม ${{q.score}} คะแนน</span>
              <span class="badge-type">${{escapeHtml(q.type || 'อัตนัย')}}</span>
            </div>
          </div>
          <div class="written-q-text">${{escapeHtml(q.question)}}</div>
          
          <div class="written-practice-box">
            <textarea placeholder="พื้นที่สำหรับนักศึกษาฝึกพิมพ์ตอบคำถามข้อนี้ (จำลองการทำข้อเขียน)..."></textarea>
          </div>

          <div style="display: flex; justify-content: flex-end;">
            <button class="btn-toggle-answer" onclick="toggleWrittenAnswer(${{q.id}})">
              <span>👁️ ดูแนวคำตอบ เฉลย และเกณฑ์การตรวจ</span>
            </button>
          </div>

          <div class="written-answer-box" id="ansBox_${{q.id}}">
            <div class="ans-sec-title">✅ คีย์ / แนวคำตอบมาตรฐาน:</div>
            <div class="ans-sec-content">${{escapeHtml(q.answer)}}</div>

            <div class="ans-sec-title">📊 เกณฑ์การให้คะแนน (Scoring Rubric):</div>
            <div class="ans-sec-content">${{escapeHtml(q.rubric)}}</div>

            <div class="ans-sec-title">📖 ข้อความอ้างอิงจากเอกสารสไลด์:</div>
            <div class="ans-sec-content"><strong>แหล่งอ้างอิง:</strong> ${{escapeHtml(q.reference)}}<br><br><strong>ข้อความตรง:</strong><br>${{escapeHtml(q.quote || '')}}</div>

            ${{codeBlock}}
          </div>
        `;

        container.appendChild(card);
      }});
    }}

    function escapeHtml(str) {{
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    // Update tags on Portal cards indicating in-progress quizzes
    window.updatePortalResumeTags = function() {{
      ['tourism', 'mobile', 'iot', 'bi'].forEach(key => {{
        const tag = document.getElementById('resumeTag_' + key);
        if (!tag) return;
        const saved = getSavedProgress(key);
        if (saved && !saved.isCompleted && saved.currentIndex > 0) {{
          tag.innerHTML = `<span>📌 ค้างข้อ ${{saved.currentIndex + 1}}/80</span>`;
          tag.style.display = 'flex';
        }} else {{
          tag.style.display = 'none';
        }}
      }});
    }};

    // Get progress from localStorage
    function getSavedProgress(subjKey) {{
      try {{
        const raw = localStorage.getItem('quiz_progress_' + subjKey);
        if (!raw) return null;
        return JSON.parse(raw);
      }} catch (e) {{
        return null;
      }}
    }}

    // Check and show resume banner in Start Screen
    window.checkAndShowResumeCard = function(subjKey) {{
      const saved = getSavedProgress(subjKey);
      if (saved && !saved.isCompleted && saved.currentIndex > 0) {{
        const dateStr = saved.lastUpdated 
          ? new Date(saved.lastUpdated).toLocaleTimeString('th-TH', {{ hour: '2-digit', minute: '2-digit' }}) 
          : 'ล่าสุด';
        resumeDescText.innerHTML = `คุณทำแบบทดสอบค้างไว้ถึงข้อที่ <strong>${{saved.currentIndex + 1}}</strong> (บันทึกไว้ ${{saved.currentIndex}} จาก ${{saved.totalQuestions || 80}} ข้อ) • บันทึกอัตโนมัติเมื่อ ${{dateStr}} น.`;
        resumeBtnText.textContent = `▶️ ทำต่อจากข้อ ${{saved.currentIndex + 1}}`;
        resumeCardBox.style.display = 'block';
      }} else {{
        resumeCardBox.style.display = 'none';
      }}
    }};

    function selectSubject(subjKey) {{
      currentSubjectKey = subjKey;
      window.currentSubjectKey = subjKey;
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

      // Guidelines modal check
      if (subj.guidelines && subj.guidelines.length > 0) {{
        guidelinesBanner.style.display = 'flex';
        guidelinesBtnContainer.style.display = 'block';

        const modalTitle = document.getElementById('guidelinesModalTitle');
        const viewBtn = document.getElementById('viewGuidelinesBtn');
        const bannerBtn = document.getElementById('bannerGuidelinesBtn');
        const bannerText = document.getElementById('guidelinesBannerText');

        if (subjKey === 'bi') {{
          if (modalTitle) modalTitle.textContent = '📋 แนวข้อสอบข้อเขียน 20 ข้อพร้อมเกณฑ์เฉลย วิชา ธุรกิจอัจฉริยะ (Business Intelligence)';
          if (viewBtn) viewBtn.textContent = '📋 ดูแนวข้อสอบข้อเขียน 20 ข้อพร้อมเกณฑ์เฉลยฉบับเต็ม';
          if (bannerBtn) bannerBtn.textContent = 'อ่านแนวข้อสอบ 20 ข้อ';
          if (bannerText) bannerText.textContent = '💡 ข้อสอบชุดนี้สร้างขึ้นตามพิมพ์เขียว Business Intelligence Blueprint พร้อมแนวข้อสอบข้อเขียน 20 ข้อและเกณฑ์เฉลย';
        }} else {{
          if (modalTitle) modalTitle.textContent = '📋 แนวทางข้อสอบปลายภาค วิชา อินเทอร์เน็ตของสรรพสิ่ง (8312404)';
          if (viewBtn) viewBtn.textContent = '📋 ดูแนวทางข้อสอบปลายภาค 25 ข้อฉบับเต็ม';
          if (bannerBtn) bannerBtn.textContent = 'อ่านแนวคำถาม 25 ข้อ';
          if (bannerText) bannerText.textContent = '💡 ข้อสอบชุดนี้สร้างขึ้นตามแนวทางข้อสอบปลายภาค 25 ข้อ โดยเน้นหลักการทำงาน การวิเคราะห์สถานการณ์ และการประยุกต์ใช้จริง';
        }}

        modalGuidelinesList.innerHTML = '';
        if (subjKey === 'bi') {{
          const bannerAction = document.createElement('div');
          bannerAction.style.cssText = 'margin-bottom: 16px; padding: 12px; background: #f3e8ff; border: 1px solid #d8b4fe; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;';
          bannerAction.innerHTML = `
            <span style="font-size: 0.9rem; font-weight: 700; color: #6b21a8;">💡 คุณสามารถเปิดทำข้อสอบข้อเขียนพร้อมกล่องพิมพ์ตอบได้</span>
            <button class="btn btn-primary" style="padding: 6px 14px; font-size: 0.85rem;" onclick="closeGuidelinesModal(); switchSubjectMode('written');">
              📝 เปิดโหมดข้อสอบข้อเขียนเต็มจอ
            </button>
          `;
          modalGuidelinesList.appendChild(bannerAction);
        }}

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

      // Toggle mode selector for subjects with written exam
      const modeBox = document.getElementById('subjectModeSelector');
      if (modeBox) {{
        if (subj.written_exam && subj.written_exam.length > 0) {{
          modeBox.style.display = 'flex';
          const quizBtn = document.getElementById('modeQuizBtn');
          const writtenBtn = document.getElementById('modeWrittenBtn');
          if (quizBtn) quizBtn.classList.add('active');
          if (writtenBtn) writtenBtn.classList.remove('active');
        }} else {{
          modeBox.style.display = 'none';
        }}
      }}

      // Check for saved progress
      window.checkAndShowResumeCard(subjKey);

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
      window.updatePortalResumeTags();
      switchScreen(portalScreen);
    }}

    function confirmExitToPortal() {{
      // Auto-save triggers automatically
      triggerAutosaveIndicator();
      if (confirm('ระบบได้บันทึกความคืบหน้าปัจจุบันไว้เรียบร้อยแล้ว คุณสามารถกลับมาทำต่อได้ตลอดเวลา\\n\\nต้องการกลับไปที่หน้าเลือกวิชาใช่หรือไม่?')) {{
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

    // ================= AUTO-SAVE CORE FUNCTIONS =================
    function triggerAutosaveIndicator() {{
      autosavePill.classList.add('show');
      setTimeout(() => {{
        autosavePill.classList.remove('show');
      }}, 2200);
    }}

    function autoSaveProgress() {{
      if (!currentSubjectKey) return;
      const progressData = {{
        subjectKey: currentSubjectKey,
        currentIndex: currentIndex,
        score: score,
        userAnswers: userAnswers,
        isShuffle: document.getElementById('shuffleToggle').checked,
        activeQuestions: activeQuestions,
        totalQuestions: activeQuestions.length,
        lastUpdated: Date.now(),
        isCompleted: false
      }};

      // 1. LocalStorage (instant, works offline/guest)
      try {{
        localStorage.setItem('quiz_progress_' + currentSubjectKey, JSON.stringify(progressData));
      }} catch (err) {{
        console.warn("LocalStorage save error:", err);
      }}

      // 2. Cloud Firestore (if logged in)
      if (window.saveToFirestore) {{
        window.saveToFirestore(currentSubjectKey, progressData);
      }}

      // 3. UI feedback
      triggerAutosaveIndicator();
    }}

    function clearSavedProgress(subjKey) {{
      try {{
        localStorage.removeItem('quiz_progress_' + subjKey);
      }} catch (e) {{}}
      if (window.deleteFromFirestore) {{
        window.deleteFromFirestore(subjKey);
      }}
    }}

    // ================= START QUIZ MODES =================
    // Mode A: Start Fresh
    function startFreshQuiz() {{
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

      // Reset stored progress
      clearSavedProgress(currentSubjectKey);
      autoSaveProgress();

      switchScreen(quizScreen);
      renderQuestion();
    }}

    // Discard saved and start fresh
    function discardSavedAndStartFresh() {{
      if (confirm('คุณแน่ใจหรือไม่ว่าต้องการล้างความคืบหน้าที่บันทึกไว้ และเริ่มทำใหม่ตั้งแต่ข้อที่ 1?')) {{
        clearSavedProgress(currentSubjectKey);
        window.checkAndShowResumeCard(currentSubjectKey);
        startFreshQuiz();
      }}
    }}

    // Mode B: Resume from Saved
    function resumeSavedQuiz() {{
      const saved = getSavedProgress(currentSubjectKey);
      if (!saved) {{
        startFreshQuiz();
        return;
      }}

      activeQuestions = saved.activeQuestions || allSubjects[currentSubjectKey].questions;
      currentIndex = saved.currentIndex || 0;
      score = saved.score || 0;
      userAnswers = saved.userAnswers || new Array(activeQuestions.length).fill(null);
      hasAnsweredCurrent = false;

      switchScreen(quizScreen);
      renderQuestion();
      triggerAutosaveIndicator();
    }}

    function escapeHtml(text) {{
      return String(text)
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

      // Code snippet box
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

      // Highlight choice buttons
      const choiceButtons = choicesGrid.querySelectorAll('.choice-btn');
      choiceButtons.forEach((btn, idx) => {{
        btn.disabled = true;
        if (idx === q.correctAnswer) {{
          btn.classList.add('correct');
        }} else if (idx === selectedIndex && !isCorrect) {{
          btn.classList.add('wrong');
        }}
      }});

      // Show explanation card
      explanationCard.className = 'explanation-card ' + (isCorrect ? 'is-correct' : 'is-wrong');
      explanationIcon.innerHTML = isCorrect
        ? '<svg width="22" height="22" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>'
        : '<svg width="22" height="22" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path></svg>';
      explanationTitle.textContent = isCorrect ? 'ตอบถูกต้อง!' : 'ตอบไม่ถูกต้อง';
      explanationBody.textContent = q.explanation;
      explanationCard.style.display = 'block';

      // AUTO-SAVE IMMEDIATELY!
      autoSaveProgress();

      // Show Next Button
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
        // Auto-save pointing to the new current question
        autoSaveProgress();
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
        if (!ans) return;
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

      // Quiz completed: clear active in-progress state so next time starts fresh
      clearSavedProgress(currentSubjectKey);
      window.updatePortalResumeTags();

      renderReview();
    }}

    function renderReview() {{
      const reviewContainer = document.getElementById('reviewContainer');
      reviewContainer.innerHTML = '';
      const letters = ['ก', 'ข', 'ค', 'ง'];

      userAnswers.forEach((ans, idx) => {{
        if (!ans) return;
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
      clearSavedProgress(currentSubjectKey);
      switchScreen(startScreen);
    }}

    // Initial check on load
    window.addEventListener('DOMContentLoaded', () => {{
      window.updatePortalResumeTags();
    }});
  </script>
</body>
</html>
"""

output_path = "/Users/wiwi/PKRU/webapp ติวข้อสอบ/index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated index.html with Firebase Auth & Auto-save successfully at: {output_path}")
