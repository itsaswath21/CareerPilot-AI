from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def create_report(analysis, filename):

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            "CareerPilot AI Resume Report",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph("<br/><br/>", styles["BodyText"])
    )

    paragraphs = analysis.split("\n")

    for line in paragraphs:

        if line.strip():

            story.append(
                Paragraph(
                    line.replace("\n", "<br/>"),
                    styles["BodyText"]
                )
            )

    doc.build(story)