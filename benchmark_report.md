# Benchmark Report
Environment: Python 3.12, standard library only. 26 measurements: exp and sigmoid at x = -6, -2, 0, 2, 6; softmax on vectors of 10, 100 and 1000 numbers.

## Speed (average ns per call)
- exp: exact 85.2, Taylor 335.9 (about 4x slower)
- sigmoid: exact 126.1, fast 89.5 (about 30% faster)
- softmax: exact 34,906.6, Taylor 138,415.6 (about 4x slower)

## Accuracy (maximum absolute error)
- exp Taylor: 158.83 (at x = 6); accurate only near 0
- sigmoid fast: 0.069
- softmax Taylor: 0.63 at size 10, shrinking as vectors grow

## Recommendation
In pure Python the exact math.exp is both faster and exact, because it runs as compiled code. Use the fast sigmoid only where an error up to 0.07 is acceptable. Never use the 6-term Taylor exp outside roughly -2 to 2.
