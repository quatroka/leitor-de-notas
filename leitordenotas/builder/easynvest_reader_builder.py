import re
from datetime import datetime

from leitordenotas.builder.builder_reader_base import BuilderReaderBase


class EasynvestReaderBuilder(BuilderReaderBase):
    NEGOCIACOES_PATTERN = '(BOVESPA[\n ])([CV]\s)(VIS\s|FRACIONARIO\s|D2S\s)([A-Z0-9 ]+)(\n \#\n|\n \n|\n|)*([0-9 ]+\n)([0-9.]+,[0-9]{2}\n)([0-9.]+,[0-9]{2}\n)([CD]\n)'
    RESUMO_NEGOCIOS_PATTERN = '([A-Za-z0-9 êàúíóçõã\(\)\-\.\,\/]+\n)([0-9.]+,[0-9]{2}\n)'
    RESUMO_FINANCEIRO_PATTERN = '([A-Za-z0-9 íóçõã\(\)\.\,\/\+]+\n)([0-9.-]+,[0-9]{2} )([CD])'
    NUMERO_NOTA_PATTERN = '(Nº Nota:\s)([0-9]+)'
    DATA_NOTA_PATTERN = '(Data pregão:\s)([0-9\/]+)'

    def build_negociacoes(self):
        self.parsed_data['negocios'] = []
        for negociacao in re.findall(self.NEGOCIACOES_PATTERN, self.raw_text):
            self.parsed_data['negocios'].append(
                {
                    'titulo': self.clean_string(negociacao[3]),
                    'qtd': self.parse_real(negociacao[5]),
                    'preco': self.parse_real(negociacao[6], dc=negociacao[8]),
                    'valor_operacao': self.parse_real(negociacao[7], dc=negociacao[8]),
                    'obs': self.clean_string(negociacao[4])
                }
            )

    def build_resumo_negocios(self):
        extracted = re.findall(self.RESUMO_NEGOCIOS_PATTERN, self.raw_text)
        values = extracted[-13:]
        self.parsed_data['resumo_negocios'] = {
            'debentures': self.parse_real(values[0][1], dc='D'),
            'vendas_vista': self.parse_real(values[1][1], dc='C'),
            'compras_vista': self.parse_real(values[2][1], dc='D'),
            'opcoes_compras': self.parse_real(values[3][1], dc='D'),
            'opcoes_vendas': self.parse_real(values[4][1], dc='C'),
            'operacoes_termo': self.parse_real(values[5][1], dc='D'),
            'valor_operacoes_titulos_publicos': self.parse_real(values[6][1], dc='D'),
            'valor_operacoes': self.parse_real(values[7][1], dc='D')
        }

    def build_resumo_financeiro(self):
        extracted = re.findall(self.RESUMO_FINANCEIRO_PATTERN, self.raw_text)[-13:]
        self.parsed_data['resumo_financeiro'] = {
            'clearing': {
                'valor_liquido_operacoes': self.parse_real(extracted[0][1],
                                                           dc=extracted[0][2]),
                'taxa_liquidacao': self.parse_real(extracted[1][1], dc=extracted[1][2]),
                'taxa_registro': self.parse_real(extracted[2][1], dc=extracted[2][2]),
                'total_cblc': self.parse_real(extracted[3][1], dc=extracted[3][2]),
            },
            'bolsa': {
                'taxa_termo_opcoes': self.parse_real(extracted[4][1], dc=extracted[4][2]),
                'taxa_ana': self.parse_real(extracted[5][1], dc=extracted[5][2]),
                'emolumentos': self.parse_real(extracted[6][1], dc=extracted[6][2]),
                'total_bovespa': self.parse_real(extracted[7][1], dc=extracted[7][2])
            },
            'custos_operacionais': {
                'taxa_operacional': self.parse_real(extracted[8][1], dc=extracted[8][2]),
                'impostos': self.parse_real(extracted[9][1], dc=extracted[9][2]),  # iss
                'irrf': self.parse_real(extracted[10][1], dc=extracted[10][2]),
                'outros': self.parse_real(extracted[11][1], dc=extracted[11][2]),
            }
        }
        self.parsed_data['total'] = self.parse_real(extracted[12][1], dc=extracted[12][2])

    def build_info(self):
        numero = re.search(self.NUMERO_NOTA_PATTERN, self.raw_text).group(2)
        self.parsed_data['numero'] = numero
        data_pregao = re.search(self.DATA_NOTA_PATTERN, self.raw_text).group(2)
        self.parsed_data['data_pregao'] = datetime.strptime(data_pregao, "%d/%m/%Y")
