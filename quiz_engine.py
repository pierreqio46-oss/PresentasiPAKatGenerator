class QuizGenerator:

    def __init__(self,client):

        self.client=client


    def create_quiz(self,text):

        prompt=f"""
        Buat 10 soal pilihan ganda
        dari materi:

        {text}
        """

        result=self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return result.choices[0].message.content