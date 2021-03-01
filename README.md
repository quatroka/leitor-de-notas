# Leitor de notas

## Install the package

    pip install leitor-de-notas

## Example

```python
from leitordenotas.nota_de_corretagem_reader import NotaDeCorretagemReader
filepath = 'path_to_file'
NotaDeCorretagemReader(filepath).read()

# you can specify the parser
from leitordenotas.builder.clear_reader_builder import ClearReaderBuilder
NotaDeCorretagemReader(filepath, parser=ClearReaderBuilder).read()
```

## Corretoras suportadas

- Easynvest
- Clear
- Banco Inter

### Important links:
[IRRF calc](https://www.investimentonabolsa.com/2014/10/entenda-irrf-nota-de-corretagem.html)
