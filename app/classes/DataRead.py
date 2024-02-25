import pandas as pd
from pathlib import Path

class DataRead:
  def __init__(self, id: int) -> None:
    self.id = id
  
  def getData(self) -> pd.DataFrame:
    csvPath = Path(__file__).parent.parent / 'data' / f'{self.id}.csv'
    data = pd.read_csv(csvPath)
    data["Data"] = pd.to_datetime(data["Data"])
    
    return data
    