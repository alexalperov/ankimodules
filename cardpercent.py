     def cPctCorrect(c, n, t):
            responsesFunc =  mw.col.db.scalar(
                "select reps from cards where id = ?", c.id)

            lapsesFunc = mw.col.db.scalar(
                "select lapses from cards where id = ?", c.id)

            if responsesFunc > 0:
                percent = Decimal(lapsesFunc)/Decimal(responsesFunc)
            if responsesFunc:
                return str(percent)

        cc = advBrowser.newCustomColumn(
            type='cpct',
            name='Percent Correct',
            onData=cPctCorrect,
            onSort=lambda: "(select max(percent))"
        )
        self.customColumns.append(cc)
