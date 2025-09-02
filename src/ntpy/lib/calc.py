import re
from typing import Iterable
import numpy as np

from sympy import symbols, Eq, solve

from sklearn.metrics import r2_score as r2
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def str2e(s) -> str:
  return s if len(s) < 5 else f'{float(s):.4e}'


def fl2el(fl) -> list[str]:
  return list(map(lambda f: str2e(str(f)), fl))


def poly(x, y, degree=3) -> Iterable:
  return np.polyfit(x, y, degree).tolist()


def polyResults(coef, x) -> Iterable:
  return np.poly1d(coef)(x).tolist()


def polyRoots(coef) -> Iterable:
  return np.roots(coef).tolist()


def xn2y(X, y, degree=2, output=False, foo='Xn2y'):
  poly = PolynomialFeatures(degree=degree, include_bias=False)
  x = np.array(X).T
  xp = poly.fit_transform(x)

  model = LinearRegression()
  model.fit(xp, y)
  # y1 = model.predict(xp)

  coef = model.coef_
  names = poly.get_feature_names_out().tolist()

  eq = f'{model.intercept_:.4e} + '

  for i in range(len(names)):
    ex = names[i].replace('^', '**').replace(' ', '*')
    eq += f"({coef[i]:.4e})*{ex} + "

  eq = re.sub(r'x(\d+)', r'x[\1]', eq[:-3])

  local = {}
  src = compile(f'def {foo}(x):\n\treturn {eq}', "<string>", "exec")
  exec(src, {}, local)
  func = local[foo]

  y2 = [func(x[i]) for i in range(len(x))]
  yr2 = r2(y, y2)

  if output:
    q = eq.replace(' + ', ' + \\\n\t') \
        .replace('*x', ' * x').replace('e+00', '')

    print(f'{foo}: degree = {degree}, R² = {yr2:.4%}\n  f(x) = {q}')

  return (func, yr2, eq)


def solvePolyEq(eq):
  (x0, _, y) = symbols('x:2,y', real=True)
  eq = re.sub(r'x\[(\d+)\]', r'x\1', eq)
  solution = solve(Eq(eval(eq), y), x0)

  reals = []
  for s in solution:
    sol = str(s)
    if 'I' in sol:
      continue

    reals.append(re.sub(r'([-]?\d*\.\d+)', lambda m: str2e(m.group(0)), sol))

  return reals
