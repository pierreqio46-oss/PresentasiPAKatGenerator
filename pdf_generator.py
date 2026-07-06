from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib import styles


class PDFGenerator:

    def create(self,text):

        output=(
            "output/materi.pdf"
        )

        doc=SimpleDocTemplate(
            output
        )

        style=(
            styles
            .getSampleStyleSheet()
        )

        data=[]

        for line in text.split("\n"):

            data.append(
                Paragraph(
                    line,
                    style["BodyText"]
                )
            )

            data.append(
                Spacer(1,6)
            )

        doc.build(data)

        return output