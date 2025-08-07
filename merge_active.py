from common import function_merge

# Gọi hàm merge_csv từ module function_merge
df = function_merge.merge_csv(file1 = 'active.csv', file2 = 'activelogin.csv', on = "MASTER_ACCOUNT", how = "left", output = "data_active.csv")