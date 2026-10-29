import math

def calculate_heat_loss(temp_in, temp_out, area, insulation_level):
    """
    기계공학 열역학 공식(열전달)을 이용하여 벽면을 통한 열손실량(Watt)을 계산합니다.
    공식: Q = U * A * dT
    - Q: 열손실량 (W)
    - U: 열관류율 (W/m²K)
    - A: 벽면 및 창문 면적 (m²)
    - dT: 실내외 온도차 (°C 또는 K)
    """
    # 단열 등급에 따른 열관류율(U값) 설정
    u_values = {
        "1": 0.3,  # 우수 (최신 단열재 및 3중창)
        "2": 0.6,  # 보통 (일반 이중창 및 일반 벽체)
        "3": 1.2   # 미흡 (단창 및 노후 건물)
    }
    u_val = u_values.get(insulation_level, 0.6)
    delta_t = abs(temp_in - temp_out)
    heat_loss = u_val * area * delta_t
    return heat_loss, u_val

def get_valid_float(prompt):
    """숫자가 아닌 값이 입력되었을 때 튕기지 않도록 하는 예외 처리 함수"""
    while True:
        try:
            val = float(input(prompt))
            return val
        except ValueError:
            print("[입력 오류] 정수 또는 실수(숫자)만 입력 가능합니다. 다시 입력해 주세요.\n")

def main():
    print("=" * 65)
    print(" 🌡️ [기계공학 융합] 열역학 기반 스마트 냉난방 절전 도우미")
    print("=" * 65)

    # 1. 환경 변수 입력
    print("\n[1] 현재 환경 정보 입력")
    temp_in = get_valid_float(" - 현재 실내 온도 (°C): ")
    temp_out = get_valid_float(" - 현재 실외 온도 (°C): ")
    humidity_in = get_valid_float(" - 현재 실내 습도 (%): ")

    # 2. 건물/공간 정보 입력 및 예외 처리
    print("\n[2] 공간 및 단열 정보 입력")
    room_area = get_valid_float(" - 방/거실의 벽면 및 창문 총 면적 (m² 예: 20): ")
    
    while True:
        print(" - 단열 등급 선택 (1: 우수[3중창], 2: 보통[이중창], 3: 미흡[단창/노후]): ")
        insulation = input("   선택 (1/2/3): ").strip()
        if insulation in ["1", "2", "3"]:
            break
        print("[입력 오류] 1, 2, 3 번호 중에서만 선택해 주세요.\n")

    # 3. 열역학 연산 수행
    heat_loss, u_val = calculate_heat_loss(temp_in, temp_out, room_area, insulation)

    # 4. 분석 결과 및 최적 제어 제안
    print("\n" + "=" * 65)
    print(" 📊 열역학 분석 및 최적 에너지 제어 리포트")
    print("=" * 65)
    print(f"• 실내외 온도차: {abs(temp_in - temp_out):.1f} °C")
    print(f"• 적용된 열관류율(U값): {u_val} W/m²K")
    print(f"• 추정 열손실(취득)량: {heat_loss:.2f} Watt (W)")
    print("-" * 65)

    # 계절 판별 (외기온도와 내기온도 비교)
    is_winter = temp_out < temp_in

    if is_winter:
        target_temp = 20.0  # 겨울철 권장 실내온도
        print(f"• 계절 구분: 겨울철 난방 모드")
        if temp_in > 22.0:
            print("⚠️ [경고] 현재 설정 온도가 권장 기준보다 높아 열손실이 큽니다.")
            saving = (temp_in - target_temp) * 7  # 1도 낮출 때마다 약 7% 절감
            print(f"💡 권장: 희망 온도를 {target_temp}°C로 낮추면 난방비를 약 {saving:.1f}% 절약할 수 있습니다.")
        else:
            print("✅ 적정 난방 온도를 유지하고 있습니다.")

        if humidity_in < 40:
            print("💧 [가습 제안] 습도가 낮아 체감 온도가 떨어집니다. 가습기를 가동하여 습도를 50%로 유지하면 난방 효율이 높아집니다.")
    else:
        target_temp = 26.0  # 여름철 권장 실내온도
        print(f"• 계절 구분: 여름철 냉방 모드")
        if temp_in < 24.0:
            print("⚠️ [경고] 현재 설정 온도가 너무 낮아 에어컨 과부하가 발생합니다.")
            saving = (target_temp - temp_in) * 6  # 1도 올릴 때마다 약 6% 절감
            print(f"💡 권장: 희망 온도를 {target_temp}°C로 올려 설정하면 전기세를 약 {saving:.1f}% 절약할 수 있습니다.")
        else:
            print("✅ 적정 냉방 온도를 유지하고 있습니다.")

    print("-" * 65)
    print("🔧 [기계공학적 단열 및 제어 개선 팁]")
    if insulation == "3":
        print("• 현재 창호 단열이 미흡합니다. 문풍지/뽁뽁이 설치 시 열관류율(U)이 감소하여 열손실을 최대 30% 줄일 수 있습니다.")
    else:
        print("• 단열 상태가 양호합니다. 환기 시스템 제어로 실내 공기질을 관리해 주세요.")
    print("=" * 65)

if __name__ == "__main__":
    main()
