conda activate f2

for suffix in a b c d e
do
    pyreverse -o png -p particle_system_$suffix particle_system_$suffix.py
    mv classes_particle_system_${suffix}.png ../img
done
