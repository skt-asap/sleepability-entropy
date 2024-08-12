import pandas as pd

def probability2_process():
    # CSV 파일 읽기
    df = pd.read_csv('sleep_possibilities_all_combinations.csv')

    # timestamp를 datetime 타입으로 변환
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # 시간(HH:MM) 추출
    df['time'] = df['timestamp'].dt.strftime('%H:%M')

    # enbid_pci, time, 그리고 주파수 대역 상태로 그룹화하고 평균 계산
    result = df.groupby(['enbid_pci', 'time', 'Status_2100', 'Status_2600_10', 'Status_2600_20'])['sleep_possible'].mean().reset_index()

    # 컬럼 이름 변경 (평균 값을 확률로 표시)
    result.rename(columns={'sleep_possible': 'sleep_probability'}, inplace=True)

    # 결과 출력
    print(result.head(20))

    # CSV 파일로 저장
    output_file = 'sleep_probabilities_result_all_combinations.csv'
    result.to_csv(output_file, index=False)
    print(f"Sleep probability calculation completed. Results saved in '{output_file}'.")

if __name__ == "__main__":
    probability2_process()