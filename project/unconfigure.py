import os
print(os.path.abspath("."))
config = f"""
random_state=42
absPath = '..'

"""
src_config = open('src\\myConfig.py',"w")
src_config.write(config)
src_config.close()
notebooks_config = open('notebooks\\myConfig.py',"w")
notebooks_config.write(config)
notebooks_config.close()
print(config)
