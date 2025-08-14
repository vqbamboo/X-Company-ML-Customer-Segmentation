from common.ultis import model

# Chạy model KMeans
model.model(
    original_data='data/data_inactive.csv', 
    input_data='data/fixed_data_inactive.csv', 
    model_path='model/kmeans_model.pkl', 
    output_path='data/data_with_cluster.csv', 
    summary_path='data/summary_inactive_5.csv',
    percentile_path='data/percentile_inactive_5.csv'
)

