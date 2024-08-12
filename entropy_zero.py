import pandas as pd
import numpy as np

def entropy_zero_process():
    # CSV 파일에서 데이터 로드
    df = pd.read_csv('sleep_probabilities_result_all_combinations.csv')

    # 엔트로피 계산 함수
    def calculate_entropy(p):
        p = np.clip(p, 1e-10, 1 - 1e-10)
        entropy = -p * np.log10(p) - (1-p) * np.log10(1-p)
        return 0 if entropy < 1e-6 else entropy

    # 각 조합에 대한 엔트로피 계산
    df['entropy'] = df['sleep_probability'].apply(calculate_entropy)

    # CSV 파일로 저장
    output_file = 'entropy_results_all_combinations.csv'
    df.to_csv(output_file, index=False)
    print(f"Entropy calculation completed. Results saved in '{output_file}'.")

if __name__ == "__main__":
    entropy_zero_process()