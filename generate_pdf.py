from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, ListFlowable, ListItem, KeepTogether
)
from reportlab.lib import colors
from datetime import datetime

OUTPUT_PATH = "/Users/rishi/Desktop/Learning/CabBooking/Driver_Booking_App_Plan.pdf"

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    rightMargin=50,
    leftMargin=50,
    topMargin=60,
    bottomMargin=50,
)

styles = getSampleStyleSheet()

# Custom colors
PRIMARY = HexColor("#1a73e8")
DARK = HexColor("#202124")
GRAY = HexColor("#5f6368")
LIGHT_BG = HexColor("#f8f9fa")
ACCENT = HexColor("#34a853")
WARNING = HexColor("#ea4335")
ORANGE = HexColor("#fa7b17")
TABLE_HEADER_BG = HexColor("#1a73e8")
TABLE_ALT_BG = HexColor("#e8f0fe")

# Styles
styles.add(ParagraphStyle(
    name='CoverTitle', fontSize=32, leading=40, alignment=TA_CENTER,
    textColor=PRIMARY, fontName='Helvetica-Bold', spaceAfter=10
))
styles.add(ParagraphStyle(
    name='CoverSubtitle', fontSize=14, leading=20, alignment=TA_CENTER,
    textColor=GRAY, fontName='Helvetica', spaceAfter=6
))
styles.add(ParagraphStyle(
    name='SectionTitle', fontSize=20, leading=26, textColor=PRIMARY,
    fontName='Helvetica-Bold', spaceBefore=24, spaceAfter=12
))
styles.add(ParagraphStyle(
    name='SubSection', fontSize=14, leading=18, textColor=DARK,
    fontName='Helvetica-Bold', spaceBefore=16, spaceAfter=8
))
styles.add(ParagraphStyle(
    name='SubSubSection', fontSize=12, leading=16, textColor=HexColor("#333333"),
    fontName='Helvetica-Bold', spaceBefore=12, spaceAfter=6
))
styles.add(ParagraphStyle(
    name='BodyText2', fontSize=10, leading=15, textColor=DARK,
    fontName='Helvetica', spaceAfter=6, alignment=TA_JUSTIFY
))
styles.add(ParagraphStyle(
    name='BulletItem', fontSize=10, leading=15, textColor=DARK,
    fontName='Helvetica', spaceAfter=4, leftIndent=20, bulletIndent=10
))
styles.add(ParagraphStyle(
    name='TableHeader', fontSize=9, leading=12, textColor=white,
    fontName='Helvetica-Bold', alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    name='TableCell', fontSize=9, leading=12, textColor=DARK,
    fontName='Helvetica'
))
styles.add(ParagraphStyle(
    name='TableCellCenter', fontSize=9, leading=12, textColor=DARK,
    fontName='Helvetica', alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    name='FooterNote', fontSize=8, leading=10, textColor=GRAY,
    fontName='Helvetica-Oblique', alignment=TA_CENTER
))

story = []

# ─── COVER PAGE ───
story.append(Spacer(1, 2 * inch))
story.append(Paragraph("Driver Booking App", styles['CoverTitle']))
story.append(Spacer(1, 8))
story.append(Paragraph("Comprehensive Project Plan", styles['CoverSubtitle']))
story.append(Spacer(1, 20))
story.append(HRFlowable(width="40%", thickness=2, color=PRIMARY, spaceAfter=20, hAlign='CENTER'))
story.append(Spacer(1, 12))
story.append(Paragraph("Consolidated from: Cab App Estimation, iDrive Test Cases & SetRite UI Flows", styles['CoverSubtitle']))
story.append(Spacer(1, 8))
story.append(Paragraph(f"Prepared on: {datetime.now().strftime('%B %d, %Y')}", styles['CoverSubtitle']))
story.append(PageBreak())

# ─── TABLE OF CONTENTS ───
story.append(Paragraph("Table of Contents", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=16))
toc_items = [
    ("1.", "Executive Summary"),
    ("2.", "Source Document Analysis"),
    ("3.", "App Architecture Overview"),
    ("4.", "App 1: Rider / Customer App"),
    ("5.", "App 2: Driver App"),
    ("6.", "App 3: Management / Admin App"),
    ("7.", "Effort Estimation"),
    ("8.", "Tech Stack Recommendation"),
    ("9.", "Test Coverage Summary"),
    ("10.", "Known Issues & Resolutions"),
    ("11.", "Implementation Roadmap"),
]
for num, title in toc_items:
    story.append(Paragraph(f"<b>{num}</b>  {title}", styles['BodyText2']))
story.append(PageBreak())

# ─── 1. EXECUTIVE SUMMARY ───
story.append(Paragraph("1. Executive Summary", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))
story.append(Paragraph(
    "This document consolidates insights from three source documents — a task estimation spreadsheet "
    "(Cab App), a comprehensive test case suite (iDrive), and a full UI/UX flow presentation (SetRite) "
    "— into a unified project plan for building a <b>Driver Booking App</b>. The app ecosystem consists of "
    "three interconnected applications: a <b>Rider App</b>, a <b>Driver App</b>, and a <b>Management/Admin App</b>, "
    "all built as a hybrid solution targeting both iOS and Android platforms.",
    styles['BodyText2']
))
story.append(Paragraph(
    "The plan covers feature specifications, effort estimates, technology recommendations, test coverage, "
    "known issues from prior implementations, and a phased implementation roadmap.",
    styles['BodyText2']
))
story.append(PageBreak())

# ─── 2. SOURCE DOCUMENT ANALYSIS ───
story.append(Paragraph("2. Source Document Analysis", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

src_data = [
    [Paragraph("<b>Document</b>", styles['TableHeader']),
     Paragraph("<b>Type</b>", styles['TableHeader']),
     Paragraph("<b>Key Contents</b>", styles['TableHeader'])],
    [Paragraph("Cab App.xlsx", styles['TableCell']),
     Paragraph("Estimation", styles['TableCellCenter']),
     Paragraph("Task-wise effort breakdown (in days) across UX design, technical design, coding, testing, integration, product review, and release for Driver App, User App, and Management App.", styles['TableCell'])],
    [Paragraph("Testcases for iDrive.xlsx", styles['TableCell']),
     Paragraph("QA/Testing", styles['TableCellCenter']),
     Paragraph("36 functional test cases covering app installation, booking flows (single/round trips, hours/days), OTP verification, status tracking, payments, and profile management. Includes 9 bug reports with resolutions.", styles['TableCell'])],
    [Paragraph("SetRite.pptx", styles['TableCell']),
     Paragraph("UI/UX Flow", styles['TableCellCenter']),
     Paragraph("33-slide UI mockup showing complete user journeys for Customer App, Service Person App, Office Help Desk Console, and Management Dashboard — including registration, request lifecycle, maps, payments, ratings, and feedback.", styles['TableCell'])],
]
src_table = Table(src_data, colWidths=[1.3*inch, 0.9*inch, 4.0*inch])
src_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    ('BACKGROUND', (0, 1), (-1, 1), white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ALT_BG),
    ('BACKGROUND', (0, 3), (-1, 3), white),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
]))
story.append(src_table)
story.append(PageBreak())

# ─── 3. APP ARCHITECTURE OVERVIEW ───
story.append(Paragraph("3. App Architecture Overview", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))
story.append(Paragraph(
    "The system is composed of three client applications communicating with a shared backend infrastructure:",
    styles['BodyText2']
))

arch_data = [
    [Paragraph("<b>Component</b>", styles['TableHeader']),
     Paragraph("<b>Users</b>", styles['TableHeader']),
     Paragraph("<b>Purpose</b>", styles['TableHeader'])],
    [Paragraph("Rider App", styles['TableCell']),
     Paragraph("Customers", styles['TableCellCenter']),
     Paragraph("Search drivers, book trips (single/round, hours/days), track status, make payments, rate drivers", styles['TableCell'])],
    [Paragraph("Driver App", styles['TableCell']),
     Paragraph("Drivers", styles['TableCellCenter']),
     Paragraph("Receive ride broadcasts, navigate to rider & destination, manage trips, track earnings", styles['TableCell'])],
    [Paragraph("Admin App", styles['TableCell']),
     Paragraph("Operators", styles['TableCellCenter']),
     Paragraph("Dashboard, driver management, trip monitoring, financials, reports, help desk console", styles['TableCell'])],
    [Paragraph("Backend API", styles['TableCell']),
     Paragraph("All Apps", styles['TableCellCenter']),
     Paragraph("REST APIs, WebSocket server, authentication, payment processing, push notifications", styles['TableCell'])],
]
arch_table = Table(arch_data, colWidths=[1.2*inch, 0.9*inch, 4.1*inch])
arch_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    ('BACKGROUND', (0, 1), (-1, 1), white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ALT_BG),
    ('BACKGROUND', (0, 3), (-1, 3), white),
    ('BACKGROUND', (0, 4), (-1, 4), TABLE_ALT_BG),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
]))
story.append(arch_table)
story.append(PageBreak())

# ─── 4. RIDER APP ───
story.append(Paragraph("4. App 1: Rider / Customer App", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

rider_features = [
    ("4.1 Registration & Authentication", [
        "Sign up via phone number with OTP verification (SMS)",
        "Social login support (Facebook / Google)",
        "Name and phone number collection during registration",
        "OTP verification screen with submit and cancel options",
        "Session persistence across app restarts",
    ]),
    ("4.2 Home Screen", [
        "App logo with branding",
        "\"Hire Driver\" primary action button",
        "\"Other Services\" secondary option",
        "List of serviceable locations/cities",
        "Google Maps integration showing nearby available drivers",
    ]),
    ("4.3 Booking Flow", [
        "Search location with Google Maps autocomplete",
        "Location validation — popup for unsupported areas: \"We are sorry. Currently we don't provide service in searched location.\"",
        "Trip type selection: Single Trip or Round Trip",
        "Duration selection: Hours or Days",
        "Date picker: up to 3 days ahead (hours) or 5 days ahead (days)",
        "Time picker: minimum 30 minutes from current time",
        "Choose current location or pick from map",
    ]),
    ("4.4 Fare Estimation & Confirmation", [
        "Per-hour charge: Rs 99/hour",
        "Per-day charge: Rs 499/day",
        "Driver charges: Rs 3/km after reaching destination",
        "Extra hour charges: Rs 99/hr",
        "Total fare calculation displayed before confirmation",
        "Update button — navigate back to modify booking details",
        "Confirm Booking — generates booking reference number",
    ]),
    ("4.5 Status Tracking", [
        "Service Requested — date, time, request status as \"Driver Needed\", request number",
        "Request Received — driver search in progress, status updates",
        "Job Assigned — driver name, contact number, \"Call Service Person\" button",
        "Job Completed — payment charges, final summary",
        "Each status includes: Cancel, Update, Pay, and Book Another Request buttons",
    ]),
    ("4.6 Payments", [
        "Pay by Cash option",
        "Online Payment via payment gateway (Credit Card, Debit Card, Net Banking)",
        "Payment confirmation and receipt",
    ]),
    ("4.7 Profile & Account", [
        "View/edit profile: name, email, phone, address, profile picture",
        "Transaction history — past bookings with dates, service person details, amounts",
        "Notifications — real-time alerts for booking status changes",
    ]),
    ("4.8 Additional Features", [
        "Trip sharing — allow others to track the trip in real-time",
        "Feedback — write and submit feedback",
        "Rating — rate the driver/service after completion",
        "Recommend Us — share/recommend the service",
        "Logout functionality",
    ]),
]

for title, items in rider_features:
    story.append(Paragraph(title, styles['SubSection']))
    for item in items:
        story.append(Paragraph(f"•  {item}", styles['BulletItem']))

story.append(PageBreak())

# ─── 5. DRIVER APP ───
story.append(Paragraph("5. App 2: Driver App", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

driver_features = [
    ("5.1 Registration", [
        "Registration form: Name, Address, Phone, Email",
        "Professional details: Years of experience, Education, Certification",
        "Specialization and Languages known",
        "Registration subject to admin approval",
        "Confirmation with request number",
    ]),
    ("5.2 Receive & Accept Rides", [
        "Get broadcast of hire requests in real-time",
        "View requester details: name, phone, address, service time",
        "Confirm or Cancel incoming job requests",
        "After customer confirms, Call button is enabled for direct contact",
    ]),
    ("5.3 Navigation", [
        "Google Maps integration with preloaded source and destination",
        "Turn-by-turn navigation to rider's location",
        "Navigation to trip destination after pickup",
        "Time estimation for arrival",
    ]),
    ("5.4 Trip Management", [
        "Start trip — begin fare metering",
        "Calculate fare — based on distance, time, and rate",
        "End trip — stop metering, generate fare summary",
        "Collect fare — cash or mark online payment received",
    ]),
    ("5.5 History & Accounting", [
        "View completed and pending jobs with status",
        "Latest jobs shown at the top with notification badges",
        "Trip and settlement accounting",
        "Earnings summary and payout tracking",
    ]),
]

for title, items in driver_features:
    story.append(Paragraph(title, styles['SubSection']))
    for item in items:
        story.append(Paragraph(f"•  {item}", styles['BulletItem']))

story.append(PageBreak())

# ─── 6. MANAGEMENT APP ───
story.append(Paragraph("6. App 3: Management / Admin App", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

admin_features = [
    ("6.1 Dashboard", [
        "Total requests count",
        "Open requests count",
        "Pending requests count",
        "Payments summary",
        "Negative feedbacks alert",
        "Notification badge on new request arrival",
    ]),
    ("6.2 Request Management", [
        "View all requests — latest on top with status (Open/Pending/Done)",
        "Search by request ID, phone number, name, status, or service type",
        "Create new requests manually",
        "Edit existing requests",
        "Assign service persons/drivers to requests",
        "Provide cost estimation to customers",
    ]),
    ("6.3 Driver Management", [
        "Register and approve new drivers",
        "Issue device and app credentials",
        "View driver profiles and performance",
    ]),
    ("6.4 Trip Monitoring", [
        "Real-time trip tracking across all active rides",
        "Status progression monitoring",
        "Help desk request tracker console (desktop view)",
    ]),
    ("6.5 Financial Management", [
        "Generate accounting reports for drivers",
        "Receive collections from drivers",
        "Process payments to drivers",
        "View all payment history with amounts per request",
    ]),
    ("6.6 Reports & Analytics", [
        "Reports on drivers, trips, and payments",
        "Open requests report",
        "Completed jobs report",
        "Revenue and payment analytics",
    ]),
]

for title, items in admin_features:
    story.append(Paragraph(title, styles['SubSection']))
    for item in items:
        story.append(Paragraph(f"•  {item}", styles['BulletItem']))

story.append(PageBreak())

# ─── 7. EFFORT ESTIMATION ───
story.append(Paragraph("7. Effort Estimation", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))
story.append(Paragraph(
    "The following estimation is derived from the Cab App spreadsheet. All values are in <b>person-days</b>. "
    "Phases include: Architecture (5 days), Dev/Test Environment Setup (3 days), plus feature-level effort.",
    styles['BodyText2']
))

story.append(Paragraph("7.1 Driver App Features", styles['SubSection']))
est_header = [
    Paragraph("<b>Feature</b>", styles['TableHeader']),
    Paragraph("<b>UX</b>", styles['TableHeader']),
    Paragraph("<b>Design</b>", styles['TableHeader']),
    Paragraph("<b>Code</b>", styles['TableHeader']),
    Paragraph("<b>Test</b>", styles['TableHeader']),
    Paragraph("<b>Integ.</b>", styles['TableHeader']),
    Paragraph("<b>Review</b>", styles['TableHeader']),
    Paragraph("<b>Release</b>", styles['TableHeader']),
    Paragraph("<b>Total</b>", styles['TableHeader']),
]
driver_est = [
    est_header,
    ["Get broadcast of hire request", "1", "1", "3", "1", "0.5", "0.2", "0.2", "6.9"],
    ["Show hirer details & location", "1", "1", "2", "1", "0.5", "0.2", "0.2", "5.9"],
    ["Estimate time", "-", "1", "1", "1", "0.5", "0.2", "0.2", "3.9"],
    ["Guide to hirer's location", "1", "1", "2", "1", "0.5", "0.2", "0.2", "5.9"],
    ["Show navigation to destination", "1", "1", "3", "1", "0.5", "0.2", "0.2", "6.9"],
    ["Start trip", "1", "1", "1", "1", "0.5", "0.2", "0.2", "4.9"],
    ["Calculate fare", "1", "1", "2", "1", "0.5", "0.2", "0.2", "5.9"],
    ["End trip", "1", "1", "1", "1", "0.5", "0.2", "0.2", "4.9"],
    ["Collect fare", "1", "1", "2", "1", "0.5", "0.2", "0.2", "5.9"],
    ["Accounting & settlements", "1", "1", "5", "2", "0.5", "0.2", "0.2", "9.9"],
    ["Cancel trip", "1", "1", "2", "1", "0.5", "0.2", "0.2", "5.9"],
]
for i, row in enumerate(driver_est):
    if i == 0:
        continue
    driver_est[i] = [Paragraph(row[0], styles['TableCell'])] + [Paragraph(c, styles['TableCellCenter']) for c in row[1:]]

d_table = Table(driver_est, colWidths=[1.7*inch, 0.5*inch, 0.55*inch, 0.5*inch, 0.5*inch, 0.5*inch, 0.55*inch, 0.55*inch, 0.5*inch])
d_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    *[('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG if i % 2 == 0 else white) for i in range(1, len(driver_est))],
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
]))
story.append(d_table)
story.append(Spacer(1, 12))

story.append(Paragraph("7.2 Rider App Features", styles['SubSection']))
rider_est = [
    est_header,
    ["User registration", "1", "1", "3", "1", "0.5", "0.2", "0.2", "6.9"],
    ["View taxis near location", "2", "1", "5", "2", "0.5", "0.2", "0.2", "10.9"],
    ["Book a taxi", "2", "1", "3", "2", "0.5", "0.2", "0.2", "8.9"],
    ["Specify destination", "1", "1", "2", "1", "0.5", "0.2", "0.2", "5.9"],
    ["Specify location", "1", "1", "2", "1", "0.5", "0.2", "0.2", "5.9"],
    ["Get feedback for last trip", "1", "1", "1", "1", "0.5", "0.2", "0.2", "4.9"],
    ["Show fare for ended trip", "1", "2", "1", "1", "0.5", "0.2", "0.2", "5.9"],
    ["Build user profile", "1", "1", "1", "1", "0.5", "0.2", "0.2", "4.9"],
    ["Cancel trip", "1", "1", "1", "1", "0.5", "0.2", "0.2", "4.9"],
    ["Allow others to track trip", "2", "2", "1", "1", "0.5", "0.2", "0.2", "6.9"],
    ["Online payment (gateway)", "1", "3", "1", "1", "0.5", "0.2", "0.2", "6.9"],
]
for i, row in enumerate(rider_est):
    if i == 0:
        continue
    rider_est[i] = [Paragraph(row[0], styles['TableCell'])] + [Paragraph(c, styles['TableCellCenter']) for c in row[1:]]

r_table = Table(rider_est, colWidths=[1.7*inch, 0.5*inch, 0.55*inch, 0.5*inch, 0.5*inch, 0.5*inch, 0.55*inch, 0.55*inch, 0.5*inch])
r_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    *[('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG if i % 2 == 0 else white) for i in range(1, len(rider_est))],
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
]))
story.append(r_table)
story.append(Spacer(1, 12))

story.append(Paragraph("7.3 Management App Features", styles['SubSection']))
mgmt_est = [
    est_header,
    ["Register driver", "1", "4", "1", "1", "0.5", "0.2", "0.2", "7.9"],
    ["Issue device and app", "1", "3", "1", "1", "0.5", "0.2", "0.2", "6.9"],
    ["Monitor trips", "2", "2", "10", "3", "1", "1", "1", "20"],
    ["Generate accounting", "2", "2", "6", "2", "1", "1", "1", "15"],
    ["Receive collections", "2", "2", "6", "2", "1", "1", "1", "15"],
    ["Make payments to drivers", "2", "2", "4", "2", "1", "1", "1", "13"],
    ["Reports & analytics", "4", "4", "15", "5", "2", "2", "2", "34"],
]
for i, row in enumerate(mgmt_est):
    if i == 0:
        continue
    mgmt_est[i] = [Paragraph(row[0], styles['TableCell'])] + [Paragraph(c, styles['TableCellCenter']) for c in row[1:]]

m_table = Table(mgmt_est, colWidths=[1.7*inch, 0.5*inch, 0.55*inch, 0.5*inch, 0.5*inch, 0.5*inch, 0.55*inch, 0.55*inch, 0.5*inch])
m_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    *[('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG if i % 2 == 0 else white) for i in range(1, len(mgmt_est))],
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
]))
story.append(m_table)
story.append(Spacer(1, 12))

# Summary box
story.append(Paragraph("7.4 Total Effort Summary", styles['SubSection']))
summary_data = [
    [Paragraph("<b>Category</b>", styles['TableHeader']), Paragraph("<b>Effort (Days)</b>", styles['TableHeader'])],
    [Paragraph("Architecture", styles['TableCell']), Paragraph("5", styles['TableCellCenter'])],
    [Paragraph("Dev & Test Environment Setup", styles['TableCell']), Paragraph("3", styles['TableCellCenter'])],
    [Paragraph("Driver App Features", styles['TableCell']), Paragraph("~67", styles['TableCellCenter'])],
    [Paragraph("Rider App Features", styles['TableCell']), Paragraph("~73", styles['TableCellCenter'])],
    [Paragraph("Management App Features", styles['TableCell']), Paragraph("~112", styles['TableCellCenter'])],
    [Paragraph("<b>Grand Total</b>", styles['TableCell']), Paragraph("<b>~260 person-days</b>", styles['TableCellCenter'])],
]
s_table = Table(summary_data, colWidths=[3.5*inch, 2.0*inch])
s_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    ('BACKGROUND', (0, -1), (-1, -1), HexColor("#e6f4ea")),
    *[('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG if i % 2 == 0 else white) for i in range(1, len(summary_data)-1)],
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
]))
story.append(s_table)
story.append(PageBreak())

# ─── 8. TECH STACK ───
story.append(Paragraph("8. Tech Stack Recommendation", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

tech_data = [
    [Paragraph("<b>Layer</b>", styles['TableHeader']),
     Paragraph("<b>Technology</b>", styles['TableHeader']),
     Paragraph("<b>Rationale</b>", styles['TableHeader'])],
    ["Frontend (Mobile)", "React Native / Flutter", "Single codebase for iOS & Android; hybrid as per requirement"],
    ["Backend API", "Node.js (Express) or Spring Boot", "REST APIs with WebSocket support for real-time features"],
    ["Database", "PostgreSQL + Redis", "Relational data storage with Redis for caching & session management"],
    ["Maps & Location", "Google Maps SDK", "Autocomplete, navigation, geocoding, real-time tracking"],
    ["Real-time Comm.", "WebSockets (Socket.io)", "Live driver location broadcast, status updates, ride matching"],
    ["Authentication", "Firebase Auth", "OTP/SMS verification, social login (Google, Facebook)"],
    ["Payments", "Razorpay / Stripe", "Credit card, debit card, net banking payment gateway"],
    ["Push Notifications", "Firebase Cloud Messaging", "Real-time alerts for booking status, job assignment"],
    ["File Storage", "AWS S3 / Firebase Storage", "Profile pictures, documents, receipts"],
    ["CI/CD", "GitHub Actions / Fastlane", "Automated build, test, and deployment pipelines"],
]
for i, row in enumerate(tech_data):
    if i == 0:
        continue
    tech_data[i] = [Paragraph(row[0], styles['TableCell']), Paragraph(row[1], styles['TableCell']), Paragraph(row[2], styles['TableCell'])]

t_table = Table(tech_data, colWidths=[1.4*inch, 1.7*inch, 3.1*inch])
t_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    *[('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG if i % 2 == 0 else white) for i in range(1, len(tech_data))],
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(t_table)
story.append(PageBreak())

# ─── 9. TEST COVERAGE ───
story.append(Paragraph("9. Test Coverage Summary", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))
story.append(Paragraph(
    "Based on the iDrive test case suite, the following areas have been validated with <b>36 test cases</b>. "
    "Results: <b>30 Passed</b>, <b>2 Failed</b>, <b>4 Yet to Test</b>.",
    styles['BodyText2']
))

test_areas = [
    [Paragraph("<b>Area</b>", styles['TableHeader']),
     Paragraph("<b>Test Cases</b>", styles['TableHeader']),
     Paragraph("<b>Status</b>", styles['TableHeader'])],
    ["App Installation & Loading", "T001-T002, T009", "3 Passed / 2 Pending"],
    ["General App Behavior", "T003-T008", "4 Passed / 2 Pending"],
    ["Home & Login Screen", "T010, T016-T017", "3 Passed"],
    ["Booking Flow (Single/Round, Hours/Days)", "T011-T015, T020-T025", "11 Passed"],
    ["OTP & Verification", "T018-T019", "2 Passed"],
    ["Status Tracking", "T026-T032", "7 Passed"],
    ["Notifications", "T033", "1 Failed"],
    ["Transaction History", "T034", "1 Failed"],
    ["Profile & Logout", "T035-T036", "2 Passed"],
]
for i, row in enumerate(test_areas):
    if i == 0:
        continue
    color = styles['TableCell']
    test_areas[i] = [Paragraph(row[0], styles['TableCell']), Paragraph(row[1], styles['TableCellCenter']), Paragraph(row[2], styles['TableCell'])]

ta_table = Table(test_areas, colWidths=[2.5*inch, 1.7*inch, 2.0*inch])
ta_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    *[('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG if i % 2 == 0 else white) for i in range(1, len(test_areas))],
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(ta_table)
story.append(PageBreak())

# ─── 10. KNOWN ISSUES ───
story.append(Paragraph("10. Known Issues & Resolutions", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))
story.append(Paragraph(
    "The following bugs were identified in the iDrive implementation. Each must be addressed in the new build:",
    styles['BodyText2']
))

bugs = [
    [Paragraph("<b>ID</b>", styles['TableHeader']),
     Paragraph("<b>Issue</b>", styles['TableHeader']),
     Paragraph("<b>Description</b>", styles['TableHeader']),
     Paragraph("<b>Resolution</b>", styles['TableHeader'])],
    ["T01", "Splash Screen", "White screen appears after splash before home page loads", "Add proper loading state; preload assets during splash"],
    ["T02", "Update Button", "Pressing Update creates a duplicate service request instead of updating", "Fix API call to use PUT/PATCH instead of POST"],
    ["T03", "Time Picker", "Selected time resets to current time after pressing Update", "Persist user-selected time in state management"],
    ["T04", "OTP Verification", "Verification box disappears when user switches to SMS and returns", "Persist modal state across app lifecycle events"],
    ["T05", "Cancel Button", "No confirmation popup shown when canceling a request", "Add confirmation dialog before cancellation API call"],
    ["T06", "Notifications", "Cannot scroll notification page to view all notifications", "Fix scroll container; implement auto-scroll with manual override"],
    ["T07", "Transaction History", "Shows driver assignment details instead of actual transactions", "Query correct data source; display payment history"],
    ["T08", "Rating", "App rating is hardcoded to 1 star", "Implement dynamic star rating component"],
    ["T09", "Back Button", "Back button after booking allows navigation to previous screen", "Disable/intercept back navigation after booking confirmation"],
]
for i, row in enumerate(bugs):
    if i == 0:
        continue
    bugs[i] = [Paragraph(row[0], styles['TableCellCenter']), Paragraph(row[1], styles['TableCell']),
               Paragraph(row[2], styles['TableCell']), Paragraph(row[3], styles['TableCell'])]

b_table = Table(bugs, colWidths=[0.5*inch, 1.1*inch, 2.3*inch, 2.3*inch])
b_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
    *[('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG if i % 2 == 0 else white) for i in range(1, len(bugs))],
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dadce0")),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
]))
story.append(b_table)
story.append(PageBreak())

# ─── 11. IMPLEMENTATION ROADMAP ───
story.append(Paragraph("11. Implementation Roadmap", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=12))

phases = [
    ("Phase 1: Foundation (Weeks 1-3)", ACCENT, [
        "Architecture design and documentation",
        "Development and test environment setup",
        "Backend API scaffolding (auth, database, project structure)",
        "CI/CD pipeline setup",
        "Google Maps SDK and Firebase integration",
    ]),
    ("Phase 2: Core Rider App (Weeks 4-7)", PRIMARY, [
        "User registration with OTP verification",
        "Home screen with map and nearby drivers",
        "Booking flow: single/round trips, hours/days selection",
        "Fare estimation and booking confirmation",
        "Status tracking (4-stage lifecycle)",
        "User profile management",
    ]),
    ("Phase 3: Core Driver App (Weeks 8-10)", ORANGE, [
        "Driver registration and approval flow",
        "Ride broadcast and accept/reject mechanism",
        "Google Maps navigation integration",
        "Trip lifecycle: start, fare calculation, end, collect",
        "Job history and earnings view",
    ]),
    ("Phase 4: Payments & Communication (Weeks 11-12)", PRIMARY, [
        "Payment gateway integration (Razorpay/Stripe)",
        "Cash and online payment flows",
        "Push notifications for status changes",
        "Real-time WebSocket communication",
        "Trip sharing feature",
    ]),
    ("Phase 5: Admin App (Weeks 13-16)", HexColor("#7b1fa2"), [
        "Management dashboard with KPIs",
        "Request management console (create, edit, assign, search)",
        "Driver management (registration approval, monitoring)",
        "Financial management (accounting, collections, payouts)",
        "Reports and analytics",
    ]),
    ("Phase 6: Polish & Launch (Weeks 17-18)", WARNING, [
        "Address all known issues from iDrive bug report",
        "Comprehensive QA testing (36+ test cases)",
        "Performance optimization and load testing",
        "App store submission (iOS & Android)",
        "Post-launch monitoring and bug fixes",
    ]),
]

for phase_title, color, items in phases:
    story.append(Paragraph(phase_title, styles['SubSection']))
    for item in items:
        story.append(Paragraph(f"•  {item}", styles['BulletItem']))
    story.append(Spacer(1, 8))

story.append(Spacer(1, 20))
story.append(HRFlowable(width="100%", thickness=1, color=GRAY, spaceAfter=12))
story.append(Paragraph(
    "This document was auto-generated by consolidating: Cab App.xlsx, Testcases for iDrive.xlsx, and SetRite.pptx",
    styles['FooterNote']
))

# Build PDF
doc.build(story)
print(f"PDF generated: {OUTPUT_PATH}")
