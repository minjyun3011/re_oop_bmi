# Pythonのクラス名はUpperCamelCaseが普通
# 例外として一般的に大文字で意味が通じる場合はOK 正式名称のBodyMassIndexだと一般的ではない(伝わらない)
class BMI:
    def __init__(self, height, weight):
    # そもそも今回やりたいことはBMIの計算のみなので、この2つのリンキングは不要
        # self.height = height
        # self.weight = weight
        self.value = weight / (height ** 2)

        if not (10 <= self.value <= 40):
            raise ValueError("BMIが正常値の範囲を超えています")

    # __str__メソッド
    def __str__(self):
        return f"あなたのBMIは{self.value:.2f}です"

# BMI = 体重 ÷ 身長の2乗(**)
    # def calculate_bmi(self):
    #     return self.weight / (self.height ** 2)

# BMIクラスのインスタンス化
tanaka_bmi = BMI(1.80, 67.0)
sasami_bmi = BMI(1.58, 80.0)
yabai_bmi = BMI(1.70, 7500.0)

print("tanaka")
# print(tanaka_bmi.height, tanaka_bmi.height)
print(tanaka_bmi)

print("sasami")
# print(sasami_bmi.height, sasami_bmi.height)
print(sasami_bmi)

print("error")
print(yabai_bmi)
