-- metal bands
-- glam rock
SELECT band_name,
    (COALESCE(split, YEAR(NOW())) - formed) AS lifespan
FROM metal_bands
WhERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;