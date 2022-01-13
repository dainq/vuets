import requests

headers = {
    'authority': 'svr9.fireant.vn',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json, text/plain, */*',
    'requestverificationtoken': 'cbwp3YJKDo7_zm9U0WR-b9PbClDDdau-eZnuV6GA00UNz7hc5j4YnL3T0jpXVX-lCCj3KtFJjsIPj9MMKlzcJNh-pJY1:rmqykw69z2PW-9m529dJ_gT4RHmL7ppzJtGsZC6vXIKi1GXeiymfaI_nE1U47Cesh-R136cc7aUuSvDiwsDBAEU4-t7PhJ7SCLF__v5H4LGdqgZ84Mk_0-djKg3S0c1OQDoZHA2',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.fireant.vn',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.fireant.vn/',
    'accept-language': 'en,en-US;q=0.9,ja;q=0.8,vi;q=0.7,zh-TW;q=0.6,zh;q=0.5',
    'cookie': '_gid=GA1.2.818934979.1641861612; FireAnt.Authentication.v3=W0iskOi26UbAIR8hQ_zVnE-nBLkEWrjW80-1G7A58coDkoadsr70L-00rz2GtPEqB_pIWGj7wc6oA0p1ngasKVjT-MG10a-mgOJI1GWZfD0X_TOsR7GM5vfjoDrHG1BAIMc_UhuAGbtjblMlkJkAYgirHjjZeK-3PDioDz5WvQ2-uj2bjpkRtW9vBQQIQGMAEPpQ3hvrxpRQS7kRJSURdh5TsiKGa7HIMMQE49jN96SxZAjgeSyG5FhJGeS6Fu3Iohu1aKSUYL3wB_WmaQutKMCyzxF2aNi3w0-8w68M-JG-267KQmxtULMYikxyDhBpuVoH1WCv1AmwUd1Ym9RaNljFDZ8oqyvhhdmc7FH55g5hWBCpGBhqdOcw3mUh8ie3KZ4vVekePDEoCv_PkktFituEWdr3Kn4NjCzVxpOzxvs3DrynO5D5PaMTgv6jPdgT4CNCL921UIRl6eQSMuSbixv65IqE2-0wM_ddPQYAkWAMXzZcrzPgXPTZd9YNmTmI6Ra16F1SL7fItR7za-gXqjcQvtJv-otlRYFd2blCU-qPtLZIjn6Wa3gSmZVDlPseGXIwVXIcnjc5k76gEecOF0A2FinW90G_dmcTYVoGY9VrmDITzhzvepejcplR7XJK5f6Rmlt8lcxM8pYZhjEZdKr6ZWIyNoBocq4hjafukbfJ3bjR6Wuy1MLVMH4drfjcsPNcL1-WbbwEEuVJbmbwIjxFgHg8SwHkheVD9A_i41Z1M-db_8l8ncVy-qDk7xnBlOcgzatSlm06O60gUWbYbE5ED3-7N0acm0itb03Wspu9WGOCacpkJaxThtyF0QF3TRBLTPSUrAfK8GU41QAaPgkgMEi24_e4AwLC4A0lxiPm3xuNS_tgy9rM2CDsiJ5ZLcFdTLqq_flcSDKFibm9gTucpWYW7_SzwftHlT3cZjUyuWtize_VK_0nVEgNaU9JJv6zsjJhSrQTQNn_0eMYlP3IsJs7WiwcmH79YZtCb7xi0LKvstJ-QWwS9OXqlbnnZA2YF-BXSQVyaXOAc2RdT8wp9VPcEBFb_681-zX1pEGwlM4lgJBmaLIurXC56dTqLp0JFV7blDGFLK1CdKbNpKfRSX7hNJFqqs1g1tmkE6FwxNJvfaLH9X6Skih2UiMfOrVLOKBugVJLH8IYxxypLfG-zi_sv8hXyJdb7XuBd39L2soGYffbhxcYQ4FgtGrMPXpDaNYKWA7CcCLZGywGTITu1-xh-m6eOUe_gSbUNJ02QxdYqUU7531oHfesglY_PBt-TtTlACDa8piXvMIWgUtHAf38jBgB1VhvJ-OkPeRJVtlDQYUklgut7oIjKi-LJGbv3qM1Y2YjEOsJS-rOAV4agXHbTMjYdBY-b7s6RPd5RHpVqfM5i0R-DXxU1j-dK_L2OWgNIS9iNQx7magY8fONqtiQ4i6aq1cNA6b1UrEscf22w6e0hk5iHIgD7RbP7VcdcVgCfwErahpRNvR9SRTPKdZUBupw54WoDmDeoalRwt192dt1klEhrcqAtOCrWHRpaHeu35efIOSLud2WzTpv4Z3WBnfZeungiuMcngGh39ZKgw0Y-irDPQlbgQ6MstPfbF7xr6-JFX6srm2PA-Ml_-JMFQdXVfpGVrA5eC61Pv4vxKqPCQ7DP0sfwj9H-aax_CpWKCc-kLpIqRHuUdiDHh7b2TcXm1-ckaF6NxEdSa4_Hua05q4wPKDsIqWMHgwZXlx_djjHY0byaHis-aOXEmH4QiIx2hrFFYiEgkyQ5cHd98E5XPRXEkMNav-yPNXgVDHnfiprJ7YfC5LnEzF2sXQ2ojvlIStpFTrSoaLhKeWrZPe7r5YqXeAA2DDQyHX_TSdqngJmsitWcEnrjxi-4MK0g-YXCjiuYPgWIJVQ1fCz8Tm1mKu-e9PU9CmR7Kz2jZ6qE65br-3B_JktA5YDR0-u3Sn4RTWzDqD8lmkuGZgCklzOXmU3oFQYze2K-rrPkJkqRtGUuvWydLFHWyLAUNrp3zkCpue5xxtUl_nAyiW5R2NiSs4ciNQFwfR_tKniAEZVw4AuwaUgz2L4ZMOWv2QlrmBwiaEMnVoY1lkMtOvRcH8EMveXSyecjdev8Hlv91o2OECSsx7h23LJuM-Js8tnn3BBTfmXWnDViJHShi_W1KOs1_wUV_zz4GIwQ6Ef4WLwT6gMAeJl7afN_tV4j_WLY04zp6lb7jH8uL0lpZbEh_c3QMAvgddzOsTGhq2j7paAvnfKAfa3QCcoKcc1qhi1VGgiopsqix73fz4MLh9Ah8bmBekA8t7As7L0K_Ojy8bDIGWjkE65rpYhsrEhkb1K039DXDscya4KuqoT8BoPzLC3FLDyTI7PYOT5N7p466KNOQrNunBqyAMr6JIFuEKRLmXevOEy--Hnhriti1ZjrIMlUqypwRp2PW3Y6BF9iyYQIuR3sud5vbSNjSIKBNGQ5_miPwRfzrGAf9U5DA6WW0mVvhYu-Kqa1Ag_k0ln0SkEwjVArVHd2JBeYSKMTv2W9iNVFQqQxNP4xO1W09iBDZ8fiFcVOZNe-AxuarjIuEws9J98VTVvR_nBKyUGFd5EXKgmWmRF22vmMaSJuJ9V-gMcGZqnYkSTojHLUCqUo8g32FNWHhs8x52330NBGknzzi3UdgRIBJN3wlD6c-jCGMtPXv_lsGrFRNeb8fbyluGRd0z5RFM7I6rarGvVU8sQvxVc_9PqAxW_kG-NwHDPyyt-5c3PUwYkbGxignWAINLy_B8IH_TF6_O3LJ1-cIG_Hs76UKtr0vcCqUl43Es8YYDtxqwoHTkfMdqBiluTARcposA0hgIJUnDi-9l6XjtUn86bCXceuCRRlAq8jI9PaiemTZZWYOIg2cQ3OL93C4sh_LCjUCkRoEfo_X4EGTczQLdhHHFTnjlZO0xxrh-J8CPBYfEhEN6HFXTVTIuoNzXzsNHjsCZoK4WPoDWhrk0_OmMOkCy38izVpK6L61aenWcDQ25k-fWG5mYwIWHqWo44AhwRK_UXs8CNEStLY5KjugycsXyKXW9WYP82n4gb; ASP.NET_SessionId=zxsyveewk3euxi5vjkxrhjha; _ga_ZJ4G3SW582=GS1.1.1641896962.5.0.1641896962.0; _ga=GA1.2.1818055386.1641861612; _gat=1',
}

params = (
    ('symbol', 'VND'),
    ('resolution', 'D'),
    ('startDate', '2020-5-16'),
    ('endDate', '2020-7-2'),
)

response = requests.get('https://svr9.fireant.vn/api/Data/Markets/Bars', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://svr9.fireant.vn/api/Data/Markets/Bars?symbol=VND&resolution=D&startDate=2020-5-16&endDate=2020-7-2', headers=headers)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.options('https://svr8.fireant.vn/api/Data/Companies/TimescaleMarks?symbol=VND&startDate=2020-6-9&endDate=2020-8-19', headers=headers)
print(response.json())

print(pd.DataFrame(dct["Bars"]))
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://restv2.fireant.vn/posts?symbol=VIC&type=0&offset=0&limit=20', headers=headers)