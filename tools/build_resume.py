from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Ikteder_Akhand_Udoy_Resume.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

INK = colors.HexColor("#111827")
MUTED = colors.HexColor("#374151")
BLUE = colors.HexColor("#164e82")
LINE = colors.HexColor("#9ca3af")

styles = getSampleStyleSheet()
name_style = ParagraphStyle(
    "Name",
    parent=styles["Title"],
    fontName="Times-Bold",
    fontSize=24,
    leading=25,
    alignment=TA_CENTER,
    textColor=INK,
    spaceAfter=1,
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=11.5,
    leading=13,
    alignment=TA_CENTER,
    textColor=INK,
    spaceAfter=3,
)
link_style = ParagraphStyle(
    "Links",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.6,
    leading=9.4,
    alignment=TA_CENTER,
    textColor=BLUE,
    spaceAfter=2,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontName="Times-Bold",
    fontSize=12.2,
    leading=12.8,
    textColor=INK,
    spaceBefore=2.6,
    spaceAfter=0.4,
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontName="Times-Roman",
    fontSize=8.65,
    leading=10.25,
    textColor=INK,
    spaceAfter=0,
)
small_style = ParagraphStyle(
    "Small",
    parent=body_style,
    fontSize=8.15,
    leading=9.55,
    textColor=MUTED,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=12,
    firstLineIndent=-7,
    bulletIndent=3,
    spaceBefore=0.2,
)


def p(text, style=body_style):
    return Paragraph(text, style)


def section(title):
    return [p(title, section_style), HRFlowable(width="100%", thickness=0.6, color=INK, spaceBefore=0, spaceAfter=1.6)]


def two_col(title, date, subtitle=None):
    left = f"<b>{title}</b>"
    if subtitle:
        left += f"<br/><i>{subtitle}</i>"
    table = Table([[p(left), p(date)]], colWidths=[6.45 * inch, 1.05 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.7),
    ]))
    return table


def bullet(text):
    return p(f"• {text}", bullet_style)


story = [
    p("Ikteder Akhand Udoy", name_style),
    p("AI/ML and Software Engineering", role_style),
    p(
        'Primary: <link href="mailto:ikteder.akhand@gmail.com">ikteder.akhand@gmail.com</link>  |  '
        'Boise State: <link href="mailto:iktederakhandudo989@u.boisestate.edu">iktederakhandudo989@u.boisestate.edu</link><br/>'
        '<link href="https://www.linkedin.com/in/ikteder-akhand-udoy-680a4122a">LinkedIn</link>  |  '
        '<link href="https://github.com/Ikteder">GitHub</link>  |  '
        '<link href="https://ikteder.github.io/">Portfolio</link>  |  '
        '<link href="https://scholar.google.com/citations?hl=en&amp;user=7CEKc9wAAAAJ">Google Scholar</link>  |  '
        '<link href="https://www.boisestate.edu/coen-lpins/people/">LPiNS Profile</link>',
        link_style,
    ),
]

story += section("Summary")
story += [p(
    "PhD researcher and software engineer with experience in applied machine learning, forecasting, data analytics, and AI-driven automation. "
    "Strong in Python, SQL, pandas, NumPy, scikit-learn, PyTorch, and reproducible experimentation. Experienced building data pipelines, "
    "predictive models, validation workflows, and decision-support tools that turn complex data into reliable business and technical insights."
)]

story += section("Education")
story += [
    two_col("Boise State University", "Expected Dec 2027", "PhD in Computing, Data Science and Machine Learning"),
    two_col("American International University-Bangladesh", "2017-2021", "B.S. in Computer Science and Engineering"),
]

story += section("Research Experience")
story += [
    two_col("Graduate Research Assistant - Boise State University", "2023-Present", "Machine Learning, Data Pipelines, and AI Systems"),
    bullet("Build Python and PyTorch pipelines for data preprocessing, model training, evaluation, experiment orchestration, metric aggregation, and automated reporting."),
    bullet("Develop and compare machine-learning approaches across classification, vision, and language workloads using controlled experiments, ablations, multi-seed evaluations, and error analysis."),
    bullet("Analyze model and system performance using accuracy, precision, recall, F1, perplexity, latency, throughput, memory, and numerical-consistency metrics."),
    bullet("Create reusable workflows for data validation, structured logging, checkpoint analysis, model comparison, and automation to improve reproducibility and reliability."),
    Spacer(1, 0.7),
    two_col("Teaching Assistant - Boise State University", "2023-Present", "Algorithms, Data Structures, Digital Systems, and AI Hardware Systems"),
    bullet("Support students in programming, algorithms, debugging, data structures, machine-learning concepts, and problem solving."),
]

story += section("Industry Experience")
story += [
    two_col("Software Engineer I - Playense", "Jan 2022-Jun 2023", "Software and Application Development"),
    bullet("Developed, tested, and debugged application features using Python, C++, and Dart while translating requirements into software."),
    bullet("Implemented and integrated software components, investigated technical issues, and adapted solutions to evolving requirements."),
    bullet("Completed and delivered eight client projects through final handoff, meeting customer and project requirements."),
]

story += section("Selected Data Science and AI Projects")
story += [
    bullet("<b>Demand Forecasting and Inventory Decision Support</b> - Built a retail time-series forecasting pipeline using lag, rolling, promotion, holiday, and calendar features; compared baselines with RMSE, MAE, and MAPE and translated predictions into inventory-risk support."),
    bullet("<b>Customer Churn and Revenue Risk Analytics</b> - Developed a Python/SQL workflow for cleaning, feature engineering, churn prediction, segmentation, revenue-risk prioritization, model comparison, and dashboard-ready outputs."),
    bullet("<b>Dataset Quality and Leakage Detection Platform</b> - Built a reusable framework for detecting missingness, duplicates, split leakage, label conflicts, outliers, imbalance, and distribution drift across tabular, image, and time-series datasets."),
]

story += section("Technical Skills")
story += [
    bullet("<b>Programming / Data:</b> Python, SQL, C/C++, Bash, pandas, NumPy, Jupyter"),
    bullet("<b>Machine Learning:</b> scikit-learn, XGBoost, PyTorch, TensorFlow, regression, classification, predictive modeling, time-series forecasting, feature engineering"),
    bullet("<b>Analytics:</b> Data cleaning, data validation, statistical analysis, model evaluation, ETL-style workflows, structured reporting"),
    bullet("<b>Automation:</b> Hugging Face, LLM applications, retrieval workflows, agentic AI, automated experimentation"),
    bullet("<b>Engineering:</b> Git/GitHub, Linux, Docker, pytest, FastAPI, REST APIs, SQLite, Streamlit, debugging, automated testing"),
]

story += section("Selected Publications")
story += [
    bullet("<b>Multiplier-Free LLM Linear Layers via Weights-Only Power-of-Two QAT</b> - I. A. Udoy and O. Hassan, IEEE ICAD 2026."),
    bullet("<b>Lightweight Binarized Neural Network for Real-Time Sleep Apnea Detection on Edge Hardware</b> - I. A. Udoy, R. Sharmin, et al., IEEE MeMeA 2025."),
]

story += section("Involvement and Leadership")
story += [
    bullet("Mentored two undergraduate researchers at Boise State University, guiding experimentation, implementation, debugging, analysis, and research communication."),
    bullet("Presented research at IEEE ICAD 2026 and IEEE WMED 2026; IEEE TinyML Workshop Instructor, 2025."),
]

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=letter,
    rightMargin=0.44 * inch,
    leftMargin=0.44 * inch,
    topMargin=0.35 * inch,
    bottomMargin=0.34 * inch,
    title="Ikteder Akhand Udoy - AI/ML and Software Engineering Resume",
    author="Ikteder Akhand Udoy",
)
doc.build(story)
print(OUTPUT)
