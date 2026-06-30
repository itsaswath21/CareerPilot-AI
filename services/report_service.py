from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def create_report(text, filename):

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            "<b>CareerPilot AI Report</b>",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(text.replace("\n", "<br/>"),
        styles["BodyText"])
    )

    pdf.build(story)