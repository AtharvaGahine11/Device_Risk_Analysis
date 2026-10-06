"""
Build all 7 Academic Documents in both DOCX and PDF formats:
1. BRD_Device_Risk_Analysis
2. SRS_Device_Risk_Analysis
3. SOW_Device_Risk_Analysis
4. WBS_Device_Risk_Analysis
5. Test_Cases_Device_Risk_Analysis
6. Project_Report_Device_Risk_Analysis
7. Presentation_Script_Device_Risk_Analysis
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

os.makedirs("docs", exist_ok=True)

# -----------------------------------------------------------------------------
# DOCX BASE UTILS
# -----------------------------------------------------------------------------
def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_docx(title, subtitle):
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        
    p_uni = doc.add_paragraph()
    p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = p_uni.add_run("ITM SKILLS UNIVERSITY\nSchool of Future Tech\nDepartment of Computer Science & Engineering\n")
    r_uni.font.name = 'Helvetica'
    r_uni.font.size = Pt(13)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_paragraph().paragraph_format.space_after = Pt(20)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run(title)
    r_title.font.name = 'Helvetica'
    r_title.font.size = Pt(22)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(37, 99, 235)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run(subtitle)
    r_sub.font.name = 'Helvetica'
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(71, 85, 105)

    doc.add_paragraph().paragraph_format.space_after = Pt(30)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = p_meta.add_run(
        "Student Name: Atharva Gahine\n"
        "Degree Program: B.Tech Computer Science & Engineering\n"
        "Semester: V | Batch: 2024–2028\n"
        "Academic Course: Machine Learning (Case Study No. 86)\n"
        "Submission Date: October 2026"
    )
    r_meta.font.name = 'Helvetica'
    r_meta.font.size = Pt(10.5)
    r_meta.font.color.rgb = RGBColor(51, 65, 85)

    doc.add_page_break()
    return doc

def d_h1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(16)
    h.paragraph_format.space_after = Pt(6)
    r = h.add_run(text)
    r.font.name = 'Helvetica'
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = RGBColor(15, 23, 42)

def d_h2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(11)
    h.paragraph_format.space_after = Pt(4)
    r = h.add_run(text)
    r.font.name = 'Helvetica'
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(37, 99, 235)

def d_p(doc, text, bold_pre=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    if bold_pre:
        r_pre = p.add_run(bold_pre)
        r_pre.font.name = 'Helvetica'
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(30, 41, 59)
    r = p.add_run(text)
    r.font.name = 'Helvetica'
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(51, 65, 85)

def d_b(doc, text, bold_pre=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_pre:
        r_pre = p.add_run(bold_pre)
        r_pre.font.name = 'Helvetica'
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(30, 41, 59)
    r = p.add_run(text)
    r.font.name = 'Helvetica'
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(51, 65, 85)

def d_table(doc, headers, data):
    tbl = doc.add_table(rows=len(data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        set_cell_background(hdr_cells[i], '1E293B')
        for p in hdr_cells[i].paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Helvetica'
                run.font.size = Pt(9.0)
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)

    for r_idx, row in enumerate(data):
        row_cells = tbl.rows[r_idx + 1].cells
        bg_col = 'F8FAFC' if r_idx % 2 == 0 else 'FFFFFF'
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_col)
            for p in row_cells[c_idx].paragraphs:
                for run in p.runs:
                    run.font.name = 'Helvetica'
                    run.font.size = Pt(8.5)
                    run.font.color.rgb = RGBColor(51, 65, 85)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

# -----------------------------------------------------------------------------
# REPORTLAB PDF UTILS
# -----------------------------------------------------------------------------
styles = getSampleStyleSheet()
p_title = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor('#1E3A8A'), alignment=TA_CENTER, spaceAfter=8)
p_sub = ParagraphStyle('S', fontName='Helvetica-Oblique', fontSize=11, leading=15, textColor=colors.HexColor('#475569'), alignment=TA_CENTER, spaceAfter=16)
p_meta = ParagraphStyle('M', fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#334155'), alignment=TA_CENTER, spaceAfter=22)
p_h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=12.5, leading=16, textColor=colors.HexColor('#0F172A'), spaceBefore=11, spaceAfter=5)
p_h2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=colors.HexColor('#2563EB'), spaceBefore=8, spaceAfter=3)
p_body = ParagraphStyle('B', fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#334155'), alignment=TA_JUSTIFY, spaceAfter=5)
p_bullet = ParagraphStyle('BL', fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#334155'), leftIndent=12, spaceAfter=2)
p_cell = ParagraphStyle('C', fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=colors.HexColor('#1E293B'))
p_hdr = ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER)

def create_pdf(filename, story):
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
    doc.build(story)

def make_pdf_tbl(headers, data, col_widths=None):
    table_data = [[Paragraph(h, p_hdr) for h in headers]]
    for row in data:
        table_data.append([Paragraph(str(val), p_cell) for val in row])
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E293B')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#F8FAFC'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    return t

print("Base setup ready.")
