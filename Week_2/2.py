sist = int(input())
diast = int(input())
age = int(input())
weight = int(input())
PD = sist - diast #40-60 норма
SAD = PD + diast #70-110
SistV = ((101 + 0.5 * PD) - (0.6 * diast) - 0.6 * age) #60-150
MOK = SistV * 70 #4000-6000 мл
Vcirk = 60 * weight #3000-5000 мл
print(PD, SAD, SistV, MOK, Vcirk)
