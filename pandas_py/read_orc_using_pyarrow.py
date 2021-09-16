import pyarrow.orc as orc
import pyarrow.parquet as parquet

filename = "/Users/manikandan.kk/hello_world_orc/part-00000-b6e99eb9-cf0c-4b0b-b627-d1dcddb42dfc-c000.snappy.orc"


orcFileReference = orc.ORCFile(filename)
print(type(orcFileReference))

dataTable = orcFileReference.read()
print (type(dataTable))

pandasdf = dataTable.to_pandas()
print(pandasdf)
