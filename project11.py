import streamlit as st

st.title("🍹 Đặt đồ uống Online")

with st.form('Order đồ uống'):

    drinks = (
        'Trà sữa truyền thống',
        'Trà sữa matcha',
        'Trà sữa trái cây',
        'Trà đào cam sả',
        'Hồng trà sữa',
        'Trà ô long sữa',
        'Sữa tươi trân châu đường đen',
        'Cà phê sữa',
        'Latte',
        'Trà xoài kem cheese'
    )
    option_drink = st.selectbox('Bạn muốn loại đồ uống gì?', drinks)

    sugars = (
        'Đường trắng',
        'Đường nâu',
        'Ít đường',
        'Không đường'
    )
    option_sugar = st.selectbox('Bạn thích thêm loại đường nào cho đồ uống của bạn?', sugars)

    jellys = (
        'Thạch rau câu',
        'Thạch nha đam',
        'Thạch phô mai',
        'Thạch dừa',
        'Không thêm thạch'
    )
    option_jelly = st.selectbox('Bạn thích thêm loại thạch nào cho đồ uống của bạn?', jellys)

    toppings = (
        'Trân châu đen',
        'Trân châu trắng',
        'Kem cheese',
        'Pudding trứng',
        'Không thêm topping'
    )
    option_topping = st.selectbox("Bạn muốn thêm topping gì?", toppings)

    nums = st.slider('Số lượng bạn muốn đặt:', 1, 10, 1)

    bill = {
        'Loại đồ uống:': option_drink,
        'Loại đường:': option_sugar,
        'Loại thạch:': option_jelly,
        'Topping thêm:': option_topping,
        'Số lượng:': nums
    }

    submitted = st.form_submit_button("Xác nhận")

if submitted:
    st.subheader('🧾 Thông tin đơn hàng:')
    for x, y in bill.items():
        st.write(x,y)

print_bill = st.checkbox('In hoá đơn')
if print_bill:
    ans = ""
    for x in bill:
        ans += f"{x} {bill[x]}\n"

    st.download_button(
        "Tải hóa đơn",
        ans,
        file_name="hoa_don.txt"
        )
