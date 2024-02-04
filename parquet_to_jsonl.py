

import pyarrow.parquet as pq

columns = ['instruction-turkish', 'text-turkish']  # list of columns to read

pds = pq.read_pandas('train-00000-of-00001.parquet',
                     columns).to_pandas()
# rename columns
pds.columns = ['Prompt', 'Completion']

# convert to jsonl
jsonl_str = pds.to_json(orient='records', lines=True,
                        force_ascii=False, index=False)

print
with open('./output.jsonl', 'w', encoding='utf-8') as f:
    f.write(jsonl_str)
