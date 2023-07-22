# Code Quantum complexity of a given circuit

import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram


# use oop to create a class for the circuit
# class QuantumComplexity:
#     def __init__(self, n):
#         self.n = n
#         self.q = QuantumRegister(n)
#         self.c = ClassicalRegister(n)
#         self.circuit = QuantumCircuit(self.q, self.c)
#         self.circuit.h(self.q)
#         self.circuit.measure(self.q, self.c)
#
#     def run(self):
#         backend = Aer.get_backend('qasm_simulator')
#         job = execute(self.circuit, backend, shots=1000)
#         job_monitor(job)
#         result = job.result()
#         counts = result.get_counts(self.circuit)
#         return counts
#
#     def plot(self, counts):
#         plot_histogram(counts)
#         plt.show()
#
#
# def main():
#     n = 5
#     qc = QuantumComplexity(n)
#     counts = qc.run()
#     qc.plot(counts)


# explanation of the code
# 1. create a class for the circuit
# 2. create a constructor for the class
# 3. create a method to run the circuit
# 4. create a method to plot the circuit
# 5. create a main function to run the code

# use oop to initialize a qubit and measure it plot state vector of the qubit
class QuantumComplexity:
    def __init__(self, n):
        self.n = n
        self.q = QuantumRegister(n)
        self.c = ClassicalRegister(n)
        self.circuit = QuantumCircuit(self.q, self.c)
        self.circuit.h(self.q)
        self.circuit.measure(self.q, self.c)

    def run(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def plot(self, counts):
        plot_histogram(counts)
        plt.show()


def main():
    n = 5
    qc = QuantumComplexity(n)
    counts = qc.run()
    qc.plot(counts)


if __name__ == '__main__':
    main()
