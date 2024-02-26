from flask import render_template, request
from app import app
from app.classes.Posto import Posto
from app.classes.DataRead import DataRead

@app.route("/", methods = ['GET', 'POST'])
def index():
    cords = [ 
             Posto("-6.76","-38.96", 80),
             Posto("-3.67","-38.97", 133),
             Posto("-5.91","-39.26", 349) 
            ]
    if request.method == 'POST':
        ano = int(request.form['ano'])
        mes = int(request.form['mes'])
        postoId = request.form['postoId']
        
        mesPos = 1 if mes + 1 > 12 else mes+1
        anoPos = ano + 1 if mesPos == 1 else ano
        
        reader = DataRead(postoId)
        table = reader.getData()
        
        diario = table[(table["Data"] >= f'{ano}-{mes}-01') & (table["Data"] <  f'{anoPos}-{mesPos}-01')]
        mensal = table[(table["Data"] >= f'{ano}-01-01') & (table["Data"] < f'{ano + 1}-01-01')]
        anual = table[(table["Data"] <= f'{ano}-12-31') & (table["Data"] >= f'{ano-9}-01-01')]
        
        diarioPrecipitacao = []
        for value in diario['Precipitacao'].values:
            diarioPrecipitacao.append(value)
        mensalPrecipitacao = []
        anualPrecipitacao = []
        
        mesI = mes
        anoI = ano
        
        for i in range(1, 13):
            
            mesI = mesI + 1 if mesI + 1 <= 12 else 1
            anoI = anoI + 1 if mesI < mes else anoI
            mesPos = mesI + 1 if mesI + 1 < 12 else 1
            min = f'{ano}-{mesI}-01'
            max = f'{anoI}-{mesPos}-01'

            mesData = mensal[(mensal['Data'] >= min) & (mensal['Data'] < max)]
            precip = mesData['Precipitacao'].values
            value = float('{:.3f}'.format(precip.sum()))
            mensalPrecipitacao.append(value)
        
        for i in range(10):
            min = f'{(ano - i)}-01-01'
            max = f'{(ano - i)}-12-31'

            anoData = anual[(anual['Data'] >= min) & (anual['Data'] <= max)]
            precip = anoData['Precipitacao'].values
            value = float('{:.3f}'.format(precip.sum()))
            anualPrecipitacao.append(value)
            
        diarioLabel = []
        mensalLabel = []
        anualLabel = []
        
        for i in range(1, len(diarioPrecipitacao)+1):
            diarioLabel.append(i)
        for i in range(1,13):
            value = (mes + i) if (mes + i) <= 12 else mes + i - 12
            mensalLabel.append(value) 
            
        for i in range( len(anualPrecipitacao)):
            anualLabel.append(ano - i)
            
        
        
        return render_template("index.html", cords = cords, diario=[diarioLabel, diarioPrecipitacao], mensal=[mensalLabel, mensalPrecipitacao], anual=[anualLabel, anualPrecipitacao], post = request.method == 'POST')
        
    return render_template("index.html", cords = cords)