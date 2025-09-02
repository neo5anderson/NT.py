from ntpy import fio, calc, __version__

# import timeit
# timeit.timeit('', number=100, globals=globals())


def main():
  print(f"Hello from {__package__}({__version__})! ")

  # data = {
  #     'Name': ['Alice', 'Bob', 'Charlie'],
  #     'Age': [25.2, 30, 35],
  #     'City': ['New York', 'Los Angeles', 'Chicago']
  # }

  # data = fio.getXlsx('ds/qs.xlsx')
  # fio.saveCSV(csv, "out.csv", colsInline=False)

  # h = data[0]
  # s = data[1]
  # v = data[2]

  # (_, _, eq) = calc.xn2y([h], v, degree=3)
  # rs = calc.solvePolyEq(eq)
  # print(rs)

  # c = calc.poly(h, v)
  # calc.fl2el(c)


if __name__ == "__main__":
  main()
