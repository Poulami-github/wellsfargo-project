from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels.api as sm


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to the page."}
  
@app.post("/upload", tags=["upload"])
async def upload_file() -> dict:
    return { result: true, msg: 'file uploaded' }
  
@app.delete("/delete", tags=["delete"])
async def delete_file() -> dict:
    return { result: true, msg: 'file deleted' }

@app.post("/scatterplot", tags=["scatterplot"])
async def draw_scatterplot(df: dict) -> dict:
    df = pd.read_csv(df[0])
    plt.scatter(df['x'], df['y'])
    plt.show()
    
@app.post("/linearregression", tags=["linearregression"])
async def linearregression(df: dict) -> dict:
    X_train, X_test, y_train, y_test = train_test_split(df['x'], df['y'], train_size = 0.7, 
                                                    test_size = 0.3, random_state = 100)
    X_train_sm = sm.add_constant(X_train)
    # Fitting the resgression line using 'OLS'
    lr = sm.OLS(y_train, X_train_sm).fit()
    plt.scatter(X_train, y_train)
    plt.plot(X_train, 2.106e+04 + 6449.4158*X_train, 'r')
    plt.show()
  
 
