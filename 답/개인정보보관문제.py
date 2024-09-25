from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    # 오늘 날짜를 datetime 형식으로 변환
    today_date = datetime.strptime(today, "%Y.%m.%d")

    # 약관을 딕셔너리로 변환
    term_dict = {}
    for term in terms:
        type_, months = term.split()
        term_dict[type_] = int(months)

    # 삭제할 인덱스를 담을 리스트
    result = []

    # 개인정보 수집 일자와 약관 종류를 분리하여 처리
    for i, privacy in enumerate(privacies):
        date_str, type_ = privacy.split()
        privacy_date = datetime.strptime(date_str, "%Y.%m.%d")

        # 약관에 따른 보관 기한을 더한 만료일 계산
        expiration_date = privacy_date + relativedelta(months=term_dict[type_])

        # 만료일이 오늘 날짜 이전이면 삭제 대상
        if expiration_date <= today_date:
            result.append(i + 1)  # 인덱스는 1부터 시작하므로 +1

    return result