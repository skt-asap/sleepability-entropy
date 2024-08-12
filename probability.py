import pandas as pd
from itertools import product

def probability_process():
    # CSV 파일에서 데이터 로드
    df = pd.read_csv('enbid_pci_sorted_data.csv', parse_dates=['timestamp'])

    # timestamp 열을 datetime 형식으로 변환하고 time과 date 열 추가
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['time'] = df['timestamp'].dt.time
    df['date'] = df['timestamp'].dt.date

    # 주파수 대역 컬럼 리스트 정의
    RB_columns = ['RB_800', 'RB_1800', 'RB_2100', 'RB_2600_10', 'RB_2600_20']

    # 각 주파수 대역의 최대 가용 RB 수 정의 (실제 값으로 수정 필요)
    max_rb = {'RB_800': 50, 'RB_1800': 100, 'RB_2100': 75, 'RB_2600_10': 50, 'RB_2600_20': 100}

    def check_sleep_possibility(row, active_bands):
        total_rb_used = row['RBused']  # 기존의 RBused 값 사용
        total_rb_available = sum(max_rb[band] for band in active_bands)
        threshold = 0.6 * total_rb_available
        return int(total_rb_used <= threshold)

    # 2100MHz, 2600MHz 10MHz, 2600MHz 20MHz에 대한 조합 생성
    variable_bands = ['RB_2100', 'RB_2600_10', 'RB_2600_20']
    combinations = list(product([0, 1], repeat=3))  #0,1 두 개 가지고 가능한 모든 조합 만들기

    results = []

    for _, row in df.iterrows():
        for combo in combinations:
            active_bands = ['RB_800', 'RB_1800'] + [band for i, band in enumerate(variable_bands) if combo[i] == 1]
            sleep_possible = check_sleep_possibility(row, active_bands)

            results.append({
                'timestamp': row['timestamp'],
                'enbid_pci': row['enbid_pci'],
                'Status_800': 1,  # 항상 켜져 있음
                'Status_1800': 1,  # 항상 켜져 있음
                'Status_2100': combo[0],
                'Status_2600_10': combo[1],
                'Status_2600_20': combo[2],
                'sleep_possible': sleep_possible
            })

    # 결과를 DataFrame으로 변환
    result_df = pd.DataFrame(results)

    # 결과를 CSV 파일로 저장
    output_file = 'sleep_possibilities_all_combinations.csv'
    result_df.to_csv(output_file, index=False)

    print(f"Sleep possibility calculation completed. Results saved in '{output_file}'.")
    print(result_df.head())  # 결과 확인을 위해 상위 몇 개 행 출력

if __name__ == "__main__":
    probability_process()