import streamlit as st
import requests
import pandas as pd
from geopy.geocoders import Nominatim

def get_radio_info(call_sign):
    api_url = "https://www.tele.soumu.go.jp/musen/list"  # 正確なエンドポイントを適宜設定
    params = {
        "ST": 1,  # 免許情報検索
        "DA": 1,  # 詳細情報取得
        "OW": "AT", # アマチュア局
        "OF": 2,  # JSON形式
        "DC": 1,  # 取得件数
        "SC": 1,  # スタートカウント
        "MA": call_sign,
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }

    response = requests.get(api_url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("無線局情報の取得に失敗しました。")
        return None

def extract_info(data):
    if "musen" not in data or len(data["musen"]) == 0:
        st.error("該当する無線局が見つかりませんでした。")
        return None

    records = []
    for item in data["musen"]:
        detail = item.get("detailInfo", {})
        record = {
            "コールサイン": detail.get("identificationSignals", ""),
            "無線局名": detail.get("name", ""),
            "住所": detail.get("radioEuipmentLocation", ""),
            "種別": detail.get("radioStationCategory", ""),
            "目的": detail.get("radioStationPurpose", ""),
            "許可日": detail.get("licenseDate", ""),
            "有効期限": detail.get("validTerms", ""),
            "移動範囲": detail.get("movementArea", ""),
            "通信事項": detail.get("commMatter", ""),
            "通信相手": detail.get("commPartner", ""),
        }
        records.append(record)

    return pd.DataFrame(records)

def get_coordinates(address):
    geolocator = Nominatim(user_agent="streamlit-radio-app")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None

def main():
    st.title("無線局情報検索アプリ")

    call_sign = st.text_input("コールサインを入力してください", "JS2IIU")

    if st.button("検索"):
        st.write("無線局情報を取得しています...")

        # APIから無線局情報を取得
        data = get_radio_info(call_sign)
        if data:
            df = extract_info(data)
            if df is not None:
                st.dataframe(df)

                # 住所を地図に表示
                for address in df["住所"].unique():
                    lat, lon = get_coordinates(address)
                    if lat and lon:
                        st.map(pd.DataFrame([{"lat": lat, "lon": lon}]))

if __name__ == "__main__":
    main()
