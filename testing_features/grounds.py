import subprocess

# result = subprocess.run("psql -U jjigna23 -h hopper01.hpc.stlawu.edu -d uni_full -f dummy",
#                        shell=True, capture_output=True)

# print(result.returncode)

from region import region

print(region())