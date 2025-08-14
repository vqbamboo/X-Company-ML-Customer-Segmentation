from common.ultis import preprocessing 

# Gọi hàm merge từ module preprocessing
preprocessing.merge(file1='data\\inactive_no_login.csv', file2='data\\inactive_login.csv', key="MASTER_ACCOUNT", method="left", output='D:\\Quân\\MBS\\5th_Project_Churn_Segmentation_Larger_Clusters\\inactive\\data\\data_inactive.csv')

