import pandas as pd

def sorting_process():
    # CSV 데이터 로드
    file_path = 'ELG_Busan_PoC_per_CA_site_0226_0407.csv'
    df = pd.read_csv(file_path)

    # Timestamp 열을 datetime 형식으로 변환
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # enbid_pci 기준으로 데이터프레임 정렬
    df_sorted = df.sort_values(by=['enbid_pci','timestamp'])

    # 정렬된 데이터를 새로운 CSV 파일로 저장
    sorted_file_path = 'enbid_pci_sorted_data.csv'
    df_sorted.to_csv(sorted_file_path, index=False)
    print(f"Sorting completed. Results saved in '{sorted_file_path}'")

if __name__ == "__main__":
    sorting_process()