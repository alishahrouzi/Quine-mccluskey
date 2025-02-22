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

    groups = group_minterms(minterms, num_bits)
    prime_implicants = find_prime_implicants(groups)
    return prime_implicants

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
        
        prime_implicants = quine_mccluskey(minterms, num_bits)
        result_str = ', '.join(prime_implicants)
        
        self.result.setText(result_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuineMcCluskeyUI()
    sys.exit(app.exec_())
