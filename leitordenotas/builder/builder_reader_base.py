class BuilderReaderBase:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.parsed_data = {}

    def parse_real(self, value: str, dc='C') -> int:
        value = abs(int(self.clean_string(value.replace(',', '').replace('.', ''))))
        return value if dc.strip() == 'C' else value * -1

    @staticmethod
    def clean_string(value: str) -> str:
        return value.strip().replace('\n', '')

    def build(self) -> dict:
        self.build_negociacoes()
        self.build_resumo_negocios()
        self.build_resumo_financeiro()
        self.build_info()
        self.irrf_retido_fonte()
        return self.parsed_data

    def build_negociacoes(self):
        pass

    def build_resumo_negocios(self):
        pass

    def build_resumo_financeiro(self):
        pass

    def build_info(self):
        pass

    def irrf_retido_fonte(self):  # TODO: need refactor
        irrf_retido = False
        total_cblc = self.parsed_data['resumo_financeiro']['clearing']['total_cblc']
        total_bolsa = self.parsed_data['resumo_financeiro']['bolsa']['total_bovespa']
        total_operacional = self.parsed_data['resumo_financeiro']['custos_operacionais'][
            'taxa_operacional']
        total_nota = self.parsed_data['total']
        if total_cblc + total_bolsa + total_operacional != total_nota:
            irrf_retido = True
        self.parsed_data['irrf_retido_fonte'] = irrf_retido
