conda activate f2

for suffix in b c
do
    pyreverse -o png -p monte_carlo_$suffix monte_carlo_$suffix.py
    mv classes_monte_carlo_${suffix}.png ../img
done
