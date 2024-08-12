import pandas as pd
import numpy as np

def analyze_min_rb_per_cell_time_entropy_zero():
    # CSV 파일 로드
    df = pd.read_csv('entropy_results_all_combinations.csv')

    # 엔트로피가 0인 행만 필터링
    zero_entropy = df[df['entropy'] == 0]

    # 가용 가능한 RB 수 계산
    max_rb = {'RB_800': 50, 'RB_1800': 100, 'RB_2100': 75, 'RB_2600_10': 50, 'RB_2600_20': 100}
    
    def calculate_available_rb(row):
        available_rb = max_rb['RB_800'] + max_rb['RB_1800']  # 800MHz와 1800MHz는 항상 켜져 있음
        if row['Status_2100'] == 1:
            available_rb += max_rb['RB_2100']
        if row['Status_2600_10'] == 1:
            available_rb += max_rb['RB_2600_10']
        if row['Status_2600_20'] == 1:
            available_rb += max_rb['RB_2600_20']
        return available_rb

    zero_entropy['available_rb'] = zero_entropy.apply(calculate_available_rb, axis=1)

    # 각 셀(enbid_pci)별, 각 시간대별로 가용 가능한 RB 수가 최소인 행 찾기
    min_rb_rows = zero_entropy.loc[zero_entropy.groupby(['enbid_pci', 'time'])['available_rb'].idxmin()]

    # 결과를 CSV 파일로 저장
    output_file = 'min_rb_per_cell_time_entropy_zero_results.csv'
    min_rb_rows.to_csv(output_file, index=False)
    print(f"\n결과가 '{output_file}'에 저장되었습니다.")

if __name__ == "__main__":
    analyze_min_rb_per_cell_time_entropy_zero()