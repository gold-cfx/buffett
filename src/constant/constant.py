from src import project_dir
import os
ts_token = os.environ.get("ts_token")
data_dir = f"{project_dir}/data"
tools_dir = f"{project_dir}/src/all_tools"
require_key = "_require"

# file name
file_name = "{start_date}_{end_date}_{data_type}.{suffix}"
