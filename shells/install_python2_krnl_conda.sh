conda create -n ipykernel_py2 python=2.7 anaconda
source activate ipykernel_py2    # On Windows, remove the word 'source'
python -m ipykernel install --user
