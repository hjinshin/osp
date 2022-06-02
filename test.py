
test = [{
        "Gubun": "\uc804\uacf5",        
        "SubjectName": "\uac00\uc871\ud559",
        "SubjectCode": "CHFA0231",
        "ClassCode": "CHFA0231-001",
        "ClassDivideNumber": "001",
        "EstablishedUniversity": "\uc0ac\ubc94\ub300\ud559",
        "EstablishedDepartment": "\uac00\uc815\uad50\uc721\uacfc",
        "ProfessorNames": "\uc774\ud6a8\ub9bc",
        "Season": "1\ud559\uae30",
        "ApplicantsMax": "19",
        "ApplicantsCurrent": "30",
        "IsUntact": "N",
        "Schedule": "\ubaa9 5A,5B,\ubaa9 6A,6B,\ubaa9 7A,7B",
        "Credit": "3",
        "Rate1": "20",
        "Rate2": "25",
        "Rate3": "20",
        "Rate4": "15",
        "Rate5": "20",
        "Rate6": "0",
        "Rate7": "0",
        "Rate8": "0",
        "Rate9": "0",
        "PriorSubject": "\uac00\uc815\uc0dd\ud65c\ubb38\ud654",
        "SubsequentSubject": "\uac00\uc815\uacbd\uc601"
}]

result = [{
            'Gubun' :  '',  # 전공, 교양, 첨성인**
            'SubjectName': '', # 과목 명
            'SubjectCode': '',  # 과목 코드
            'ClassCode': '',  # 과목 코드 (분반 포함)
            'ClassDivideNumber': '',  # 분반
            'EstablishedUniversity': '',  # 개설 대학
            'EstablishedDepartment': '',  # 개설 학과
            'ProfessorNames': '',  # 교수명 (배열 형식임)
            'Season': '',  # 개설 학기
            'ApplicantsMax': '',  # 수강 총원
            'ApplicantsCurrent': '',  # 수강 인원
            'IsUntact': '',  # 비대면 여부(Y or N)
            'Schedule': '',  # 시간표 (배열 형식임)
            'Credit': '',  # 학점
            'Rate1' : '',  # 출석 비중
            'Rate2' : '',  # 중간 시험
            'Rate3' : '',  # 기말 시험
            'Rate4' : '',  # 과제
            'Rate5' : '',  # 발표
            'Rate6' : '',  # 토론
            'Rate7' : '',  # 안전교육
            'Rate8': '',  # 기타
            'Rate9' : '',  # ?
            'PriorSubject' : '',         # 권장선수과목
            'SubsequentSubject' : '',  # 권장후수과             
}]
