from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import mm
from django.http import FileResponse
from xml.sax.saxutils import escape

def make_cv_pdf(profile):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        rightMargin=18*mm, leftMargin=18*mm,
        topMargin=15*mm, bottomMargin=15*mm
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle("Title2", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, leading=24)
    heading = ParagraphStyle("Heading2", parent=styles["Heading2"], fontSize=11, spaceBefore=9, spaceAfter=4)
    body = ParagraphStyle("Body2", parent=styles["BodyText"], fontSize=9.5, leading=13)

    story = [
        Paragraph(escape(profile.full_name), title),
        Paragraph(escape(profile.target_role), ParagraphStyle("Role", parent=body, alignment=TA_CENTER)),
        Spacer(1, 5),
        Paragraph(escape(" | ".join(x for x in [profile.email, profile.phone, profile.location] if x)), body),
        Spacer(1, 7),
        HRFlowable(width="100%"),
    ]

    sections = [
        ("PROFESSIONAL SUMMARY", profile.generated_summary or profile.bio),
        ("EXPERIENCE", profile.generated_experience or profile.experience),
        ("EDUCATION", profile.education),
        ("SKILLS", profile.skills),
        ("PROJECTS", profile.projects),
        ("CERTIFICATIONS", profile.certifications),
    ]

    for heading_text, content in sections:
        if content:
            story += [Paragraph(heading_text, heading), Paragraph(escape(content).replace("\n", "<br/>"), body)]

    links = " | ".join(x for x in [profile.linkedin, profile.github] if x)
    if links:
        story += [Paragraph("LINKS", heading), Paragraph(escape(links), body)]

    doc.build(story)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{profile.full_name.replace(' ', '_')}_CV.pdf")
