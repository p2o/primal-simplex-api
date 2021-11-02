import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from app.primal_simplex import PrimalSimplex

my_app = FastAPI()


class Dados(BaseModel):
    A : list
    b : list
    c : list


@my_app.post("/primalsimplex")
def primalsimplex(dados : Dados):
    pl = PrimalSimplex(dados.A, dados.b, dados.c)
    pl.solve()
    if pl.solucao[0] == 1:
        x = pl.x
        fx = pl.fx
    else:
        x = -1
        fx = 0
    return {
        "status" : "SUCCESS",
        "solucao" : pl.solucao,
        "x" : x,
        "fx" : fx
    }


if __name__ == "__main__":
    uvicorn.run(my_app, host="0.0.0.0", port=80)