import pyupbit

access = "hII4kuPIoBlxvx1Tdg8xNO6sBnpcNk7PsWC0JWu8"          # 본인 값으로 변경
secret = "aLrS2AKQP8EerSjWKqQczkijOhdMfC10ZXTCsHGF"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회