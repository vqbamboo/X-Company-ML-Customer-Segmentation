from common.ultis import model

# Chạy model KMeans
model.model(
    original_data='data/data_active.csv', 
    input_data='data/fixed_data_active.csv', 
    model_path='model/kmeans_model.pkl', 
    output_path='data/data_with_cluster.csv', 
    summary_path='data/summary_active_3.csv',
    percentile_path='data/percentile_active_3.csv'
)

