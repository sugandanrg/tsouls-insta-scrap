from xopen import xopen
import glob


files = glob.glob("colorsinart_/2018*xz")
content = ""

for file in files:
    with xopen(file) as f:
        content = content + " \n " + str(f.read())

"""content = pd.read_json('colorsinart_/2018-10-13_22-41-41_UTC.json.xz', compression = 'xz')
"""
