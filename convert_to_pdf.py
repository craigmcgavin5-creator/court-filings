from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# Create PDF
pdf_file = "McGavin_Application.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle', parent=styles['Heading1'], fontSize=12, textColor='black', spaceAfter=6, alignment=TA_CENTER, fontName='Helvetica-Bold'
)
heading_style = ParagraphStyle(
    'CustomHeading', parent=styles['Heading2'], fontSize=11, textColor='black', spaceAfter=6, spaceBefore=6, fontName='Helvetica-Bold'
)
body_style = ParagraphStyle(
    'CustomBody', parent=styles['BodyText'], fontSize=10, textColor='black', spaceAfter=6, alignment=TA_LEFT, fontName='Helvetica'
)

# Add title
elements.append(Paragraph("SUPREME COURT OF WESTERN AUSTRALIA", title_style))
elements.append(Paragraph("CIV 1515 of 2024", title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("MCGAVIN v MCGAVIN", title_style))
elements.append(Spacer(1, 0.3*inch))

# Add recipient info
elements.append(Paragraph("To: Registrar Nelson (Case Manager)", body_style))
elements.append(Paragraph("c/- Associate to Registrar Nelson", body_style))
elements.append(Paragraph("Supreme Court of Western Australia", body_style))
elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("By: Electronic Case Management System (ECMS) filing", body_style))
elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("Cc (service): Rowe Bristol Lawyers (for the defendant)", body_style))
elements.append(Paragraph("Email: reception@rowebristol.com.au", body_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph("5 March 2026", body_style))
elements.append(Spacer(1, 0.2*inch))

# Application title
elements.append(Paragraph("APPLICATION BY LETTER (O 4A r 5A) – REQUEST TO AMEND CASE MANAGEMENT DIRECTION", heading_style))
elements.append(Paragraph("(EXTENSION OF TIME TO COMPLY WITH ORDER 4 MADE 5 NOVEMBER 2024)", body_style))
elements.append(Spacer(1, 0.2*inch))

# Introduction
intro_text = "I, Craig McGavin, the plaintiff (in person), request pursuant to Order 4A rule 5A of the Rules of the Supreme Court 1971 (WA) that the case management direction be amended by extending the time for me to comply with Order 4 made by Lundberg J on 5 November 2024."
elements.append(Paragraph(intro_text, body_style))
elements.append(Spacer(1, 0.2*inch))

# Section 1
elements.append(Paragraph("1. ORDERS SOUGHT", heading_style))
order_text = "I seek an order that the time for the plaintiff to comply with Order 4 made on 5 November 2024 be extended to 4.00pm on Friday, 17 April 2026 (being an extension of 441 days from 31 January 2025), and such further or other orders as the Registrar considers appropriate."
elements.append(Paragraph(order_text, body_style))
elements.append(Spacer(1, 0.2*inch))

# Section 2
elements.append(Paragraph("2. ORDER TO BE AMENDED", heading_style))
order_detail = "Order 4 made by Lundberg J on 5 November 2024 provides:<br/>\"The plaintiff is to file and serve an amended writ of summons and a further amended statement of claim by no later than 4.00pm on Friday, 31 January 2025.\""
elements.append(Paragraph(order_detail, body_style))
elements.append(Spacer(1, 0.2*inch))

# Section 3
elements.append(Paragraph("3. REASONS (SUMMARY)", heading_style))
reason_intro = "I did not comply by 31 January 2025 due to significant circumstances affecting my capacity, including:"
elements.append(Paragraph(reason_intro, body_style))
reasons = [
    "(a) significant medical and mental health issues (supported by medical documents);",
    "(b) homelessness from 18 September 2024 to 7 January 2026;",
    "(c) a criminal trial in the Rockingham Magistrates Court in which I pleaded not guilty and represented myself due to lack of funds (trial from 6 March 2025 to 18 August 2025);",
    "(d) being summonsed to attend as a Crown/prosecution witness in other proceedings, including a District Court trial commencing 16 September 2025 relating to a home invasion in which I was seriously assaulted; and a further listed attendance on 31 March 2026 in the Rockingham Magistrates Court; and",
    "(e) a final violence restraining order made on 2 February 2026 (duration stated as \"life\")."
]
for reason in reasons:
    elements.append(Paragraph(reason, body_style))
elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("I rely on my supporting affidavit affirmed 5 March 2026 and its exhibits.", body_style))
elements.append(Spacer(1, 0.2*inch))

# Section 4
elements.append(Paragraph("4. DOCUMENTS FILED/SERVED WITH THIS LETTER", heading_style))
docs = [
    "(a) Affidavit of Craig McGavin affirmed 5 March 2026;",
    "(b) Exhibit \"A\" – medical documents (including medical certificate);",
    "(c) Exhibit \"B\" – violence restraining order dated 2 February 2026; and",
    "(d) Exhibit \"C\" – criminal court/prosecution document."
]
for doc in docs:
    elements.append(Paragraph(doc, body_style))
elements.append(Spacer(1, 0.2*inch))

# Section 5
elements.append(Paragraph("5. SERVICE", heading_style))
service_text = "This application by letter and the supporting affidavit (with exhibits) have been served today on the defendant's solicitors, Rowe Bristol Lawyers, by email to reception@rowebristol.com.au."
elements.append(Paragraph(service_text, body_style))
elements.append(Spacer(1, 0.3*inch))

# Signature
elements.append(Paragraph("Yours faithfully", body_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("Craig McGavin", body_style))
elements.append(Paragraph("Plaintiff (in person)", body_style))
elements.append(Paragraph("6 Tanson Road, Parmelia WA 6167", body_style))
elements.append(Paragraph("Email: craigmcgavin5@gmail.com", body_style))
elements.append(Paragraph("Phone: [insert]", body_style))

# Build PDF
doc.build(elements)
print(f"PDF created successfully: {pdf_file}")
