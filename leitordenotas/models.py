from datetime import datetime
from typing import List

from pydantic import BaseModel


class Negocio(BaseModel):
    # tipo_operacao: str
    titulo: str
    # ticker: str
    obs: str
    qtd: int
    preco: int
    valor_operacao: int


class ResumoNegocio(BaseModel):
    debentures: int
    vendas_vista: int
    compras_vista: int
    opcoes_compras: int
    opcoes_vendas: int
    operacoes_termo: int
    valor_operacoes_titulos_publicos: int
    valor_operacoes: int


class Clearing(BaseModel):
    valor_liquido_operacoes: int
    taxa_liquidacao: int
    taxa_registro: int
    total_cblc: int


class Bolsa(BaseModel):
    taxa_termo_opcoes: int
    taxa_ana: int
    emolumentos: int
    total_bovespa: int


class CustosOperacionais(BaseModel):
    taxa_operacional: int
    # execucao: int
    # taxa_custodia: int
    impostos: int
    irrf: int
    outros: int
    # total_custos_despesas: int


class ResumoFinanceiro(BaseModel):
    clearing: Clearing
    bolsa: Bolsa
    custos_operacionais: CustosOperacionais


class NotaDeCorretagem(BaseModel):
    negocios: List[Negocio]
    resumo_negocios: ResumoNegocio
    resumo_financeiro: ResumoFinanceiro
    numero: str
    data_pregao: datetime
    total: int
    irrf_retido_fonte: bool
