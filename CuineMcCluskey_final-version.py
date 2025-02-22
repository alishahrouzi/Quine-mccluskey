import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

def quine_mccluskey(minterms, num_bits):
    def count_ones(bits):
        return bits.count('1')

    def group_minterms(minterms, num_bits):
        groups = [[] for _ in range(num_bits + 1)]
        for minterm in minterms:
            bits = f'{minterm:0{num_bits}b}'
            groups[count_ones(bits)].append(bits)
        return groups

    def find_prime_implicants(groups):
        prime_implicants = set()
        while groups:
            new_groups = [[] for _ in range(len(groups) - 1)]
            used = set()
            for i in range(len(groups) - 1):
                for a in groups[i]:
                    for b in groups[i + 1]:
                        diff = [k for k in range(len(a)) if a[k] != b[k]]
                        if len(diff) == 1:
                            new_term = list(a)
                            new_term[diff[0]] = '-'
                            new_groups[i].append(''.join(new_term))
                            used.add(a)
                            used.add(b)
            for group in groups:
                for term in group:
                    if term not in used:
                        prime_implicants.add(term)
            groups = new_groups
        return prime_implicants

    def minimize_implicants(minterms, prime_implicants):
        prime_chart = {minterm: [] for minterm in minterms}
        for implicant in prime_implicants:
            for minterm in minterms:
                bit_minterm = f'{minterm:0{num_bits}b}'
                if all(x == y or x == '-' for x, y in zip(implicant, bit_minterm)):
                    prime_chart[minterm].append(implicant)
        
        essential_implicants = set()
        while prime_chart:
            for minterm, implicants in list(prime_chart.items()):
                if len(implicants) == 1:
                    essential_implicant = implicants[0]
                    essential_implicants.add(essential_implicant)
                    for covered_minterm in list(prime_chart.keys()):
                        if essential_implicant in prime_chart[covered_minterm]:
                            del prime_chart[covered_minterm]
            if not prime_chart:
                break
            max_cover = max(prime_chart, key=lambda k: len(prime_chart[k]))
            essential_implicant = prime_chart[max_cover][0]
            essential_implicants.add(essential_implicant)
            for covered_minterm in list(prime_chart.keys()):
                if essential_implicant in prime_chart[covered_minterm]:
                    del prime_chart[covered_minterm]

        return essential_implicants

    groups = group_minterms(minterms, num_bits)
    prime_implicants = find_prime_implicants(groups)
    essential_implicants = minimize_implicants(minterms, prime_implicants)
    return essential_implicants

class QuineMcCluskeyUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel('لطفا مینترم ها وارد کنید (با استفاده از "," جدا کنید):', self)
        layout.addWidget(self.label)
        
        self.mintermsInput = QLineEdit(self)
        layout.addWidget(self.mintermsInput)
        
        self.calcButton = QPushButton('محاسبه کن', self)
        layout.addWidget(self.calcButton)
        self.calcButton.clicked.connect(self.calculate)
        
        self.result = QTextEdit(self)
        self.result.setReadOnly(True)
        layout.addWidget(self.result)
        
        self.setLayout(layout)
        self.setWindowTitle(' محاسبه گر کویین مک کلاوسکی')
        self.show()
        
    def calculate(self):
        minterms_str = self.mintermsInput.text()
        minterms = [int(x.strip()) for x in minterms_str.split(',')]
        num_bits = max(minterms).bit_length()
        
        essential_implicants = quine_mccluskey(minterms, num_bits)
        result_str = ', '.join(essential_implicants)
        
        self.result.setText(result_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuineMcCluskeyUI()
    sys.exit(app.exec_())
