Este código cria uma **calculadora simples com interface gráfica** usando o módulo `tkinter` do Python. Aqui está um resumo conciso das suas funcionalidades:

### **Principais Características**:
1. **Interface Gráfica**:
   - Janela principal com título "Calculadora" (400x600 pixels, não redimensionável).
   - Visor (campo de entrada) para exibir números e resultados.
   - Botões numéricos (0-9) e operações básicas (+, -, *, /).

2. **Funcionalidades**:
   - **Inserir números/operações**: Ao clicar nos botões, o valor é exibido no visor.
   - **Calcular (`eval`)**: Processa a expressão matemática digitada e exibe o resultado.
   - **Limpar visor (C)**: Apaga todo o conteúdo do visor.
   - **Botão de sair**: Encerra o programa.

3. **Layout Organizado**:
   - Botões numéricos em formato de teclado (3x3 + 0 e ponto decimal).
   - Botões de operações à direita.
   - Botão `=` para calcular e `C` para limpar.

4. **Tratamento Básico de Erros**:
   - Se uma expressão inválida for digitada, mostra "Erro" no visor.

### **Como Funciona**:
- O usuário digita uma expressão (ex: `2 + 3 * 4`) usando os botões.
- Ao pressionar `=`, o código usa `eval()` para calcular o resultado.
- O botão `C` limpa o visor para uma nova operação.

### **Observações**:
- **Uso do `eval()`**: Embora prático, pode ser inseguro se usado em aplicações reais (pois executa qualquer código Python). Em um projeto mais robusto, seria melhor usar um parser matemático dedicado.
- **Design Simples**: Cores básicas e layout funcional, sem recursos avançados como histórico ou memória.

### **Exemplo de Uso**:
1. Clique em: `2`, `+`, `3`, `*`, `4`, `=`
2. Resultado no visor: `14` (pois `2 + (3 * 4) = 14`).

É uma calculadora básica, mas funcional, ideal para aprender `tkinter` e lógica de interfaces gráficas em Python.
