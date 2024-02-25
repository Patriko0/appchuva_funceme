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
        
        diarioPrecipitacao = diario['Precipitacao'].values
        mensalPrecipitacao = []
        anualPrecipitacao = []
        
        for i in range(1, 13):
            mesPos = i if i + 1 > 12 else i+1
            anoPos = ano + 1 if mesPos == i else ano
            min = f'{ano}-{i}-01'
            max = f'{anoPos}-{mesPos}-01'
            
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
                   
        return render_template("index.html", cords = cords, diario=diarioPrecipitacao, mensal=mensal, anual=anual)
        
    return render_template("index.html", cords = cords)