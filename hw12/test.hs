expectation :: [(Double, Double)] -> Double
expectation = sum . map (uncurry (*))

variance :: [(Double, Double)] -> Double
variance xs = sum $ map (\(x, y) -> (x - mu) * (x - mu) * y) xs
    where mu = expectation xs
