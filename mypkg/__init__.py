from importlib.resources import files
data_text = files('mypkg').joinpath('datafile.txt').read_text()
print(data_text)