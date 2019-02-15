import pandas as pd

if __name__ == "__main__":
  
  data = pd.read_csv("C:/Users/Deepesh K Rana/Documents/test.csv")
  print(data["Country Name"])